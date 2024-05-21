from fastapi import FastAPI
import openai
from langchain.prompts import ChatPromptTemplate
#from langchain.chat_models import ChatOpenAI
#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
#from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
#OPENAI_API_KEY=openai.api_key=os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()
prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("{topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"

)

add_routes(
    app,
    prompt1|model,
    path="/poem"

)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)