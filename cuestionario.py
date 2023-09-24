import streamlit as st
import openai
from PIL import Image

# Configuración de OpenAI (asegúrate de tener tu propia clave API)
openai.api_key = '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'

def main():
    genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")
main()
