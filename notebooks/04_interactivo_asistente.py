"""
04_interactivo_asistente.py
Demo interactiva · Asistente con base de conocimiento (CSV) + fast prompting.
Usa el endpoint chat.completions (como en clase) y selecciona la FAQ por palabras clave.
"""

import os, re
import pandas as pd
from textwrap import dedent
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Fuerza a cargar el .env de la RAÍZ del repo (sube un nivel desde /notebooks)
repo_root = Path(__file__).resolve().parents[1]
env_path = repo_root / ".env"
load_dotenv(dotenv_path=env_path if env_path.exists() else find_dotenv(), override=True)

print("Usando .env en:", env_path if env_path.exists() else find_dotenv())
val = os.getenv("OPENAI_API_KEY")
print("OPENAI_API_KEY cargada:", bool(val), "| longitud:", (len(val) if val else 0))

# --- API ---
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# --- Base de conocimiento ---
DF_PATH = "data/base_conocimiento_afiliaciones_clean.csv"
df = pd.read_csv(DF_PATH)

if "estado" in df.columns:
    df = df[df["estado"].str.lower().isin(["vigente", "en revisión"])].copy()

for col in ["id","titulo","contenido","respuesta_validada","palabras_clave"]:
    if col in df.columns:
        df[col] = df[col].fillna("").astype(str)

def tokens(txt):
    if isinstance(txt, (list, tuple, set)):
        txt = " ".join(map(str, txt))
    if txt is None:
        txt = ""
    try:
        txt = str(txt).lower()
    except Exception:
        txt = ""
    return [t for t in re.split(r"[^a-záéíóúñü0-9]+", txt) if t]

def score(consulta: str, fila) -> int:
    tq = set(tokens(consulta))
    st = set(tokens(fila.get("titulo", "")))
    sk = set(tokens(fila.get("palabras_clave", "")))
    sc = set(tokens(fila.get("contenido", "")))
    return 4*len(tq & st) + 3*len(tq & sk) + 1*len(tq & sc)

def buscar_faq(consulta: str):
    mejor_idx, mejor_s = None, 0
    for idx, fila in df.iterrows():
        s = score(consulta, fila)
        if s > mejor_s:
            mejor_s, mejor_idx = s, idx
    return df.loc[mejor_idx] if mejor_idx is not None else None


def construir_mensajes(fila, pregunta: str):
    base = (fila.get("respuesta_validada") or fila.get("contenido") or fila.get("titulo","")).strip()

    reglas_system = dedent("""
        Rol: Asistente de Afiliaciones de IOMA  
    Público: agentes en Delegaciones y App IOMA Digital  
    Tono: institucional, claro y preciso  

    Reglas:
    - Basate EXCLUSIVAMENTE en la BASE para pasos y requisitos.
    - Si falta un dato, colocá "No consta en la normativa adjunta" y derivá a Afiliaciones (SLA: 24 h).
    - Extensión total ≤ 350 palabras.

    Respuesta debe incluir:
    1. Checklist o pasos necesarios (listas o numeradas).
    2. Cierre: "Fuente: base de conocimiento vigente".
    3. Contexto ampliado con **dos subsecciones**:
       - **Términos clave**: al menos 3 viñetas con definiciones.
       - **Objetivo y buenas prácticas**: al menos 3 viñetas sobre propósito del trámite y recomendaciones.
    """)

    user_contenido = dedent(f"""
    Pregunta del agente: {pregunta}

    CONTEXTO – BASE (obligatorio):
    \"\"\"{base}\"\"\"
    """)

    return [
        {"role": "system", "content": reglas_system},
        {"role": "user",   "content": user_contenido},
    ]


# --- Loop interactivo ---
print("Asistente IOMA · escribí tu pregunta (o 'salir' para terminar)")
while True:
    consulta = input("\nTú: ").strip()
    if not consulta:
        continue
    if consulta.lower() in {"salir","exit","q"}:
        print("Asistente: ¡Listo! 👋")
        break

    fila = buscar_faq(consulta)
    if fila is None:
        print("Asistente: No se encontró una FAQ relevante. Derivar a Afiliaciones (SLA 24 h).")
        continue

    print(f"\nFAQ seleccionada: {fila.get('id','(sin id)')} — {fila.get('titulo','(sin título)')}")

    messages = construir_mensajes(fila, consulta)

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=400,
        )
        print("\nAsistente:\n", resp.choices[0].message.content)
    except Exception as e:
        print("Error al consultar el modelo:", e)
