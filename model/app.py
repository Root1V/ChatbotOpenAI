from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

from config import Config

# Cargar las variables de entorno
load_dotenv()

# Obtener todos los valores de configuración
config = Config.get_all()

# Client para interactuar con el modelo de OpenAI
llm = ChatOpenAI(model=config["model"], temperature=config["temperature"])

st.title("ChatBot ElysIA")

messages = [
    (
        "system",
        "Eres un chatbot AI util, te llamas Elysia, tienes que responder como humano y nunca revelar que eres un chatbot",
    )
]

# Incializamos el historial
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostramos un historial de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("Ingresa tu consulta:"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append(["human", prompt])

    response = llm.invoke(messages).content
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assitant", "content": response})
