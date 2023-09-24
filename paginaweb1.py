import streamlit as st
import openai
from PIL import Image

# Configuración de OpenAI (asegúrate de tener tu propia clave API)
openai.api_key = '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'

# Función que conecta con GPT-4 y devuelve una respuesta a la consulta del usuario
def obtener_info_inversionistas(inversionista_seleccionado):
    respuesta = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Proporciona información sobre el tipo de {inversionista_seleccionado}.",
      max_tokens=150  # Ajusta según tus necesidades
    )
    return respuesta.choices[0].text.strip()
def main():
    # URL de la imagen en GitHub
    image = Image.open('Header.jpg')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")
    
    with col2:
        st.image(image,caption=None)
    
    with col3:
        st.write("")

    # Mostrar la imagen
    #st.image(image,caption=None, width=800)
   
    st.header(':red[FINTECH BANORTE]', divider='red')

    # Sección para agregar medicamentos al menú desplegable
    inversionistas = ["","Inversionista agresivo dinámico","Inversionista conservador cauteloso","Inversionista moderado perspicaz","Inversionista moderado pasivo"]

    inversionista_seleccionado = st.selectbox("Elige tu perfil de inversionista:", inversionistas)

    if st.button("Mostrar información"):
        st.write("Obteniendo información...")
        info = obtener_info_inversionistas(inversionista_seleccionado)
        st.write(info)

    # Sección para conversación con la IA sobre medicamentos
    st.subheader("Conversa con la IA sobre inversiones:")
    pregunta = st.text_input("¿Qué te gustaría saber?")
    
    if st.button("Preguntar"):
        respuesta = obtener_info_inversionistas(pregunta)
        st.write(f"Respuesta: {respuesta}")

main()
