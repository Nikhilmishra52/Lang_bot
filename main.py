import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-3.5-turbo",
               openai_api_key=openai_api_key
                )
from langchain_core.messages import SystemMessage,HumanMessage


class request_data(BaseModel):
    message:str


app=FastAPI()

@app.post("/chat")
def chat(Request:request_data):
    query=Request.message
    messages = [
        SystemMessage(content="Translate the following from English into Italian"),
        HumanMessage(content=query),
    ]

    response=llm.invoke(messages)
    return response

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app)