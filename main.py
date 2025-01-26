# Arquivo principal do projeto

import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import torch
import transformers

CHAT_GROQ_JARVIS_API = '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'
os.environ ['API_KEY'] = CHAT_GROQ_JARVIS_API
chat = ChatGroq(model='llama-3.3-70b-versatile')

