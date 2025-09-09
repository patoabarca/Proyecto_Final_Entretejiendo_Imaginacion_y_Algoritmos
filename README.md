> 📌 **Nota previa**  
> Además de este repositorio, existe un **repo mínimo listo para desplegar en Streamlit**, disponible en:  
> 👉 [asistente-afiliaciones-streamlit](https://github.com/patoabarca/asistente-afiliaciones-streamlit/tree/main)
>
> La aplicación ya se encuentra en línea y puede ejecutarse en:  
> 🌐 [https://asistente-afiliaciones.streamlit.app/](https://asistente-afiliaciones.streamlit.app/)

# Asistente de Afiliaciones — (Texto + Imagen)

Los agentes reciben de manera recurrente preguntas sobre documentación, plazos, circuitos internos y criterios de aplicación normativa, que ya se encuentran descriptos en circulares y protocolos, pero cuya consulta resulta poco ágil en la práctica.

---

## 💡 Propuesta de solución

Implemento un **asistente conversacional** que, a partir de una **base de conocimiento en CSV** (FAQs validadas), devuelve:

- 📑 **respuestas estandarizadas en JSON**
- 🖼️ **imagen institucional** acorde al tema

Todo corre en una **notebook** con **UI de ipywidgets**, cachea imágenes por tema y permite generar un **snapshot estático** para que se vea perfecto en GitHub.

---

## ⚙️ Viabilidad

- 🖥️ **Técnica:** Python, OpenAI API, CSV y Jupyter/VS Code
- 💸 **Económica:** costo bajo (texto con `gpt-4o`; imágenes cacheadas para no re-generar)
- ⏱️ **Tiempo:** MVP en ~4 semanas (curado de FAQs, diseño, pruebas y medición)

---

## 🎯 Objetivos (MVP)

- ⏳ Reducir tiempos de respuesta en **30–50%**
- ✅ Asegurar **≥ 90%** de concordancia normativa
- 📋 Uniformar criterios y trazabilidad (respuestas en **JSON**)
- 💼 **Liberar tiempo operativo** de los agentes

---

## 🛠️ Metodología

El proyecto se llevó a cabo en 4 etapas:

1. 🗂️ **Curado de la base de conocimiento (CSV):** recopilación y validación de 30–40 FAQs con metadatos de vigencia
2. ✍️ **Diseño de prompts:** compactos, con reglas fijas de salida JSON y derivación responsable
3. 📓 **Construcción del prototipo en notebook:** carga de FAQs, búsqueda ligera top-1, chat con memoria e imágenes institucionales de apoyo
4. 🔄 **Pruebas y ajustes:** validación en consultas simuladas, medición de consistencia y reducción de tiempos de respuesta

---

## ⚡ Técnicas de Fast Prompting

- 🔒 **Contexto reducido (`<<BASE>>`)** para evitar alucinaciones y mantener foco en normativa validada
- 🗜️ **Compactación de prompts:** estructura JSON estricta con límite de tokens para eficiencia
- 🔢 **Respuestas numeradas o en listas** para mayor precisión y claridad
- 📌 **Derivación responsable** cuando la información no consta en la base

---

## 🧩 Implementación

El asistente fue implementado en **Python**, integrado en una **notebook con `ipywidgets`** para la UI.  
Incluye:

- 📂 carga y búsqueda en el CSV de FAQs
- 📑 generación de respuestas en JSON
- 🖼️ cache de imágenes por tema (optimización de recursos)
- 📸 snapshot estático para visualización en GitHub

> ⚠️ Los ejemplos de código y prompts de imagen se documentan en el PDF (`docs/Preentrega2_Abarca_Patricia.pdf`) y en el notebook (`notebooks/asistente_afiliaciones.ipynb`).

---

## 📊 Resultados

- ✅ Salidas en JSON con **claridad, trazabilidad y uniformidad normativa**
- 💰 Prompts compactos redujeron consumo de tokens y costo por consulta
- 🔁 Cache de imágenes evitó regeneraciones innecesarias
- 🏆 El prototipo alcanzó los objetivos del MVP: **≥ 90% de consistencia normativa** y **30–50% de reducción de tiempos**

---

## 🖼️ Ejemplo de salida

![Ejemplo de salida del asistente](https://github.com/patoabarca/Proyecto_Final_Entretejiendo_Imaginacion_y_Algoritmos/blob/main/notebooks/Muestra_1.png?raw=true)

---

## 📝 Conclusiones

El proyecto demostró cómo un asistente basado en **prompt engineering** y una **base de conocimiento estructurada** puede mejorar la gestión interna de Afiliaciones en IOMA.

A través de la integración de texto e imagen:

- ⚖️ se logró un prototipo funcional que responde con **claridad, trazabilidad y uniformidad normativa**
- 💡 se comprobó la **viabilidad técnica y económica** (bajo costo y fácil escalabilidad)
- 🔧 se generaron insumos reutilizables (FAQs, plantillas, diagramas) que pueden extenderse a otras áreas

🚀 Este trabajo sienta bases sólidas para una futura implementación institucional y para la exploración de nuevas aplicaciones de IA en la gestión pública.

---

## 📚 Referencias

- 📑 Documentación oficial (circulares internas, protocolos de Afiliaciones)
- 🤖 [OpenAI API Docs](https://platform.openai.com/docs)
- 🌐 [Streamlit Docs](https://docs.streamlit.io)

---

## 📂 Estructura del repositorio

PROYECTO_FINAL_ENTRETEJIENDO_IMAGINACION_Y_ALGORITMOS/
├─ data/

│ └─ base_conocimiento_afiliaciones_clean.csv # Base (FAQs validadas)

├─ docs/

│ └─ Preentrega2_Abarca_Patricia.pdf # Documento previo

├─ notebooks/

│ ├─ asistente_afiliaciones.ipynb # Notebook principal (UI + snapshot)

│ └─ imgs/ # Cache de imágenes (auto)

│ └─ Muestra_1.png # (Captura de salida)

│ └─ Muestra_2.png # (Captura de salida)

│ └─ Muestra_3.png # (Captura de salida)

├─ .gitignore

└─ README.md
