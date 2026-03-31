from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path

import streamlit as st
import os 
from dotenv import load_dotenv


# Get project root (New folder (2))
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env explicitly
load_dotenv(dotenv_path=BASE_DIR / ".env")


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
##Langsmith tracking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

##Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.Please respond to the user's queries."),
        ("user", "Question:{question}")
    ]
)

##streamlit framework

st.title("Langchain Demo with OpenAI")
input_text = st.text_input("Search the topic you want")

#Openai LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser() 
chain=prompt|llm|output_parser 

if input_text:
    st.write(chain.invoke({"question":input_text}))
