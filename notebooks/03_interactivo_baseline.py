"""
03_interactivo_baseline.py
Demo interactiva · Baseline (sin base de conocimiento)
Usa el endpoint chat.completions como en el ejemplo de clase.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Baseline interactivo · escribí tu pregunta (o 'salir' para terminar)")

while True:
    consulta = input("\nTú: ").strip()
    if not consulta:
        continue
    if consulta.lower() in {"salir", "exit", "q"}:
        print("Baseline: ¡Listo! 👋")
        break

    messages = [
        {"role": "system", "content": "Respondé en tono institucional, en un solo párrafo breve (≤120 palabras)."},
        {"role": "user", "content": consulta},
    ]

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0,
            max_tokens=300,
        )
        print("\nBaseline:\n", resp.choices[0].message.content)
    except Exception as e:
        print("Error al consultar el modelo:", e)
