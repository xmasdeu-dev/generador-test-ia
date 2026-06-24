import streamlit as st
import os
from openai import OpenAI
from pypdf import PdfReader
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Asistente de Estudio IA", page_icon="📚")
st.title("📚 Generador de Tests con IA")
st.write("Sube un documento PDF y la IA extraerá conceptos y creará preguntas de repaso.")

# 2. INICIALIZACIÓN DEL CLIENTE IA
# Ahora la clave se obtiene de manera segura del archivo .env
CLAVE_API = os.getenv("GROQ_API_KEY")

if not CLAVE_API:
    st.error("No se encontró la clave API. Asegúrate de tener el archivo .env configurado.")
else:
    client = OpenAI(
        api_key=CLAVE_API,
        base_url="https://api.groq.com/openai/v1" 
    )

    # 3. INTERFAZ DE SUBIDA DE ARCHIVOS
    archivo_subido = st.file_uploader("Sube tus apuntes en formato PDF", type="pdf")

    if archivo_subido is not None:
        if st.button("Generar Resumen y Preguntas"):
            with st.spinner('Extrayendo texto y analizando con IA...'):
                try:
                    # Extraer texto del PDF
                    lector = PdfReader(archivo_subido)
                    texto_pdf = ""
                    for pagina in lector.pages:
                        texto_pdf += pagina.extract_text() + "\n"
                    
                    # Definir el prompt
                    prompt_instrucciones = f"""
                    Actúa como un profesor universitario experto. Analiza el siguiente texto de apuntes y genera:
                    1. Un bloque llamado "RESUMEN REAL" con una síntesis estructurada.
                    2. Un bloque llamado "CONCEPTOS CLAVE" con una lista de términos y su definición.
                    3. Un bloque llamado "PREGUNTAS DE REPASO" con 3 preguntas de examen.
                    
                    Texto de los apuntes:
                    {texto_pdf}
                    """
                    
                    # Llamada a la IA
                    respuesta = client.chat.completions.create(
                        model="llama-3.1-8b-instant", 
                        messages=[{"role": "user", "content": prompt_instrucciones}]
                    )
                    
                    resultado_final = respuesta.choices[0].message.content
                    
                    # Mostrar resultados
                    st.success("¡Análisis completado!")
                    st.markdown(resultado_final)
                    
                except Exception as error:
                    st.error(f"Error al procesar: {error}")