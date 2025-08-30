
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


#Langsmith 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")    
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]= "Q&A Chatbot"

from langchain_openai import ChatOpenAI, OpenAI
import openai
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.llms import Ollama


prompt=PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Please answer the question: {question}"
)

def get_answer(question,api_key, llm,temperature,max_tokens):
    openai.api_key = api_key
    llm= ChatOpenAI(model=llm, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain= prompt | llm | output_parser
    response = chain.invoke({"question": question})
    return response

def get_answer_ollama(question,llm):
    llm= Ollama(model=llm)
    output_parser = StrOutputParser()
    chain= prompt | llm | output_parser
    response = chain.invoke({"question": question})
    return response



st.title("Enhanced Q&A Chatbot with LangChain and OpenAI / Open-source LLMs")

st.sidebar.header("Select LLM Type")
llm_type = st.sidebar.selectbox(
    "LLM Type",
    options=["OpenAI", "Ollama"],
    index=0,
    help="Select the type of LLM you want to use for generating responses."
)

if llm_type == "OpenAI":
    st.sidebar.header("Configuration")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")

    llm=st.sidebar.selectbox(
    "Select LLM",
    options=["gpt-3.5-turbo","gpt-3.5-turbo-16k", "gpt-4o"],
    index=0,
    help="Select the LLM you want to use for generating responses."
)
    temperature= st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, step=0.1)
    max_tokens = st.sidebar.slider("Max Tokens", 50, 2000, 500, step=50)

else:
    st.sidebar.header("Configuration")

    llm=st.sidebar.selectbox(
    "Select LLM",
    options=["llama3.2:1b","gemma3:1b"],
    index=0,
    help="Select the LLM you want to use for generating responses."
)





# Main input and output area
st.header("Ask a Question")
question = st.text_input("Enter your question here:")

if llm_type == "OpenAI":
    if question:
        response=get_answer(question, api_key, llm, temperature, max_tokens)
        st.write(response)
    else:
        st.write("Please enter a question to get an answer.")
else:
    if question:
        response=get_answer_ollama(question, llm)
        st.write(response)
    else:
        st.write("Please enter a question to get an answer.")



