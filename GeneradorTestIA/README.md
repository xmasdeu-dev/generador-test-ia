# 📚 Generador de Tests con IA

Proyecto desarrollado como herramienta de estudio para optimizar el aprendizaje mediante inteligencia artificial. Esta aplicación permite procesar documentos PDF, extraer conceptos fundamentales y generar cuestionarios de repaso de forma automática.

## 🚀 Características
- **Procesamiento de PDF:** Lectura dinámica de apuntes de cualquier asignatura.
- **Resumen Estructurado:** Sintetiza el contenido en resúmenes claros.
- **Generador de Preguntas:** Crea automáticamente preguntas de examen basadas en el texto analizado.
- **Interfaz Web:** Desarrollada con Streamlit para una experiencia de usuario fluida.

## 🛠 Tecnologías Utilizadas
- **Python:** Lenguaje principal de desarrollo.
- **Streamlit:** Framework para la interfaz web.
- **Groq API:** Motor de IA (Llama 3.1) para el procesamiento de lenguaje.
- **PyPDF:** Librería para la extracción de texto.

## 📋 Cómo utilizarlo
1. Clona este repositorio: `git clone https://github.com/xmasdeu-dev/generador-test-ia.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Configura tu clave API en un archivo `.env`: `GROQ_API_KEY=tu_clave_aqui`
4. Ejecuta la aplicación: `streamlit run generador_test.py`

---
*Desarrollado por Xavier Masdeu | Estudiante de Ingeniería en Sistemas Audiovisuales*