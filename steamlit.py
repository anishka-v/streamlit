import streamlit as st
from meta_ai_api import MetaAI

st.title("Meta Bot")

client = MetaAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

#displaying chat history 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.prompt(message = prompt)
        st.markdown(response["message"])

    st.session_state.messages.append({"role": "assistant", "content": response["message"]})




