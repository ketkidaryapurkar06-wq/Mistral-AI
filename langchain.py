from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = ChatPromptTemplate.from_messages([
    ("system", "you are a calculator that responds with math only"),
    ("human", "answer this math question: what is two plus two?"),
    ("ai", "2+2=4"),
    ("human", "answer this math question: {question}?")
])