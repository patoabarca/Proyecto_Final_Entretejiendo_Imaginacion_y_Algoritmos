# fix_csv.py
import csv, re
from pathlib import Path

# Carpeta donde está este script
BASE = Path(__file__).resolve().parent

# Rutas (ajusta solo si tu CSV se llama distinto)
RUTA = BASE / "data" / "base_conocimiento_afiliaciones.csv"
SALIDA = BASE / "data" / "base_conocimiento_afiliaciones_clean.csv"

print("== Fix CSV IOMA ==")
print("Working dir del script:", BASE)
print("Entrada:", RUTA)
print("Salida :", SALIDA)

if not RUTA.exists():
    raise FileNotFoundError(f"No se encontró el archivo de entrada: {RUTA}")

total = 0
with open(RUTA, encoding="utf-8") as f_in, open(SALIDA, "w", encoding="utf-8", newline="") as f_out:
    lector = csv.reader(f_in)
    escritor = csv.writer(f_out, quoting=csv.QUOTE_ALL)  # entrecomilla todo

    for fila in lector:
        total += 1
        fila_limpia = []
        for celda in fila:
            celda = (celda or "").strip()
            # [texto](url) -> url
            celda = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\2', celda)
            fila_limpia.append(celda)
        escritor.writerow(fila_limpia)

print(f"✅ Listo. Filas procesadas: {total}")
print(f"➡️ Archivo limpio guardado en: {SALIDA}")