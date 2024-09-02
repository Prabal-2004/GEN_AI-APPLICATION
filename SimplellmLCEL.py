import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes
model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
# from langchain_core.messages import HumanMessage,SystemMessage
# messages=[
#     SystemMessage(content="Translate the following from English to French"),
#     HumanMessage(content="Hello How are you?")
# ]
# result=model.invoke(messages)

parser=StrOutputParser()
# parser.invoke(result)
# chain=model|parser
# chain.invoke(messages)

template="Translate the following into {language}: "
prompt=ChatPromptTemplate(
    [("system",template),("user","{text}")]
)
chain=prompt|model|parser
chain.invoke({"language":"French","text":"Hello"})
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A Simple API Server using Langchain runnable interfaces")
add_routes(
    app,
    chain,
    path="/chain"
)
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
