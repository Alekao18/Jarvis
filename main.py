# Arquivo principal do projeto

import os
import speech_recognition as sr
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from gtts import gTTS
import playsound
import torch
import transformers
import pyaudio

jarvis_api = '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'
os.environ ['GROQ_API_KEY'] = jarvis_api
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Inicializa reconhecimento de voz
reconhecedor = sr.Recognizer()

def ouvir_jarvis():
    with sr.Microphone() as source:
        print('Jarvis ouvindo...')
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)
    try:
        comando = reconhecedor.recognize_amazon(audio)
        print('Você quis dizer {comando}')
        return comando
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro na API de reconhecimento de voz.")
        return ""

def falar(texto):
    tts = gTTS(text=texto, lang='pt-br')
    tts.save("resposta.mp3")
    playsound.playsound("resposta.mp3", True)

while True:
    comando = ouvir_jarvis()
    if comando == 'desligar':
        falar_respota = "Até mais!"
        break
    resposta = chat.invoke(str(comando)).content
    falar(resposta)
    print(f"Jarvis: {resposta}")
        

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