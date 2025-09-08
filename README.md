> **Nota previa**  
> Además de este repositorio, existe un **repo mínimo listo para desplegar en Streamlit**, disponible en:  
> 👉 [asistente-afiliaciones-streamlit](https://github.com/patoabarca/asistente-afiliaciones-streamlit/tree/main)
>
> La aplicación ya se encuentra en línea y puede ejecutarse en:  
> 🌐 [https://asistente-afiliaciones.streamlit.app/](https://asistente-afiliaciones.streamlit.app/)

# Asistente de Afiliaciones — v6 (Texto + Imagen)

Los agentes reciben gran volumen de consultas repetitivas, con normativa dispersa y respuestas poco uniformes. Esto genera demoras, dependencia de referentes y riesgo de inconsistencias.

## Propuesta de solución

Implemento un **asistente conversacional** que, a partir de una **base de conocimiento en CSV** (FAQs validadas), devuelve **respuestas estandarizadas en JSON** y una **imagen institucional** acorde al tema.  
Todo corre en una **notebook** con **UI de ipywidgets**, cachea imágenes por tema y permite generar un **snapshot estático** para que se vea perfecto en GitHub.

## Viabilidad

- **Técnica:** Python, OpenAI API, CSV y Jupyter/VS Code.
- **Económica:** costo bajo (texto con `gpt-4o-mini`; imágenes cacheadas para no re-generar).
- **Tiempo:** MVP en ~4 semanas (curado de FAQs, diseño v6, pruebas y medición).

## Objetivos (MVP)

- Reducir tiempos de respuesta en **30–50%**.
- Asegurar **≥ 90%** de concordancia normativa.
- Uniformar criterios y trazabilidad (respuestas en **JSON**).
- **Liberar tiempo operativo** de los agentes.

## Metodología

1. **Base de conocimiento (CSV):** normativa y respuestas validadas (`estado ∈ {vigente, en revisión}`).
2. **Prompt v6:** reglas fijas (JSON estricto) + contexto por turno con `<<BASE>>`.
3. **Búsqueda ligera:** ranking por tokens / título / palabras_clave (top-1).
4. **UI en notebook:** cuadro de texto + salida JSON + imagen 256×256.
5. **Cache de imágenes** por **tema** (genera 1024×1024 → mini 256×256, reutiliza si ya existe).
6. **Snapshot para GitHub:** banner + JSON + imagen (sin widgets).

## Tecnologías y herramientas

- **Python + OpenAI API**
  - Texto: `gpt-4o-mini` (cambiable por `gpt-4o`)
  - Imágenes: `dall-e-3` (fallback `gpt-image-1`)
- **ipywidgets** para la UI en la notebook
- **CSV** como fuente de FAQs validadas
- **GitHub** para versionado y visualización (con snapshot estático)
- (Opcional) **Diagrams.net/Excalidraw** para visualizaciones de proceso

## Implementación (resumen)

- Prompt principal **v6** implementado en Python.
- Notebook con:
  - carga de CSV y búsqueda de FAQ,
  - chat con memoria (historial),
  - generación/uso de imagen por tema con **cache** en `notebooks/imgs/`,
  - **UI** con banner y estilos IOMA,
  - celda `snapshot_github()` para exportar una **vista estática** (banner + JSON + imagen) antes de subir a GitHub.

## Conclusiones

El proyecto demostró cómo un asistente basado en **prompt engineering** y una **base de conocimiento estructurada** puede mejorar la gestión interna de Afiliaciones en IOMA.

A través de la integración de texto e imagen:

- se logró un prototipo funcional que responde con **claridad, trazabilidad y uniformidad normativa**,
- se comprobó la **viabilidad técnica y económica** (bajo costo y fácil escalabilidad),
- y se generaron insumos reutilizables (FAQs, plantillas, diagramas) que pueden extenderse a otras áreas.

Este trabajo sienta bases sólidas para una futura implementación institucional y para la exploración de nuevas aplicaciones de IA en la gestión pública.

## Estructura del repositorio

PROYECTO_FINAL_ENTRETEJIENDO_IMAGINACION_Y_ALGORITMOS/
├─ data/
│ └─ base_conocimiento_afiliaciones_clean.csv # Base (FAQs validadas)
├─ docs/
│ └─ Preentrega2_Abarca_Patricia.pdf # Documento previo
├─ notebooks/
│ ├─ asistente_afiliaciones.ipynb # Notebook principal (UI + snapshot)
│ └─ imgs/ # Cache de imágenes (auto)
├─ Muestra.png # Captura (opcional)
├─ .gitignore
└─ README.md
