# Arquivo principal do projeto

import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import torch
import transformers
import pyaudio

jarvis_api = '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'
os.environ ['GROQ_API_KEY'] = jarvis_api
chat = ChatGroq(model='llama-3.3-70b-versatile')

def jarvis(pergunta):
    try:
        prompt = ChatPromptTemplate.from_template("{pergunta}")
        reponse = chat.invoke(prompt.format(pergunta=pergunta)) # Invoca o modelo de linguagem com o prompt formatado
        return reponse.content
    except Exception as e:
        return f"Erro ao processar a pergunta: {e}" # Erro caso haja alguma falha no processamento da pergunta
    
if __name__  == "__main__": #Construtor do código principal
    while True:
        pergunta_usuario = input('Você: ')
        if pergunta_usuario.lower() in ['sair', 'exit']:
            break
        resposta = jarvis(pergunta_usuario)
        print(f"Jarvis: {resposta}")