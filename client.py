import requests
import streamlit as st

def get_ollama_respose_essay(input_text):
    response =requests.post("http://127.0.0.1:3535/essay/invoke",
                            json = {'input':{'topic': input_text}})
    
    
    
    return response.json()['output']


def get_ollama_respose_poem(input_text):
    response =requests.post("http://127.0.0.1:3535/poem/invoke",
                            json = {'input':{'topic': input_text}})
    
    
    return response.json()['output']


st.title('Api Setup using Langchain')
input_text = st.text_input("Write an essage on")
input_text1 = st.text_input("Write a poem on")


if input_text:
    st.write(get_ollama_respose_essay(input_text))
    
if input_text1:
    st.write(get_ollama_respose_poem(input_text1))

    