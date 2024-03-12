# Q & A Chatbot
from langchain.llms import OpenAI 
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

## Function to,oad OpenAI model and get Responses
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response = llm(question)
    return response


## Initialize streamlit app
    
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")
input = st.text_input("Input: ",key="input")
response = get_openai_response(input)
submit = st.button("Ask the Question")

if submit:
    st.subheader("The Response is: ")
    st.write(response)
