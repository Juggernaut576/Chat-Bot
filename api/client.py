import requests
import streamlit as st

# def get_openai_response(input_text):
#     response = requests.post("http://localhost:8000/essay/invoke", json={"topic": input_text})
#
#     return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}}
    )

    data = response.json()
    return data["output"]

st.title("LangServe API Client")
input_text = st.text_input("Enter a topic for essay:")

if input_text:
    st.write(get_ollama_response(input_text))

# if input_text1:
#     st.write(get_openai_response(input_text1))

