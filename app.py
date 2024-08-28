from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="Langchain Api Calls",
    version = "1.0",
    description="My Api Server"
)

add_routes(
    app,
    Ollama(),
    path= "/ollama"
)

model=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write an detailed guide on {topic} with 1000 words")
prompt2= ChatPromptTemplate.from_template("Write a poem on {topic} with 200 words for a 5 year old child")

add_routes(
    app,
    prompt1 | model,
    path = "/essay"
)

add_routes(
    app,prompt2 | model,
    path = "/poem"
)

if __name__== "__main__":
    uvicorn.run(app,host = "localhost" , port = 3535)