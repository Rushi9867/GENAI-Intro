import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain.llms import OpenAI 
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

## Function to load OpenAI model and get Responses

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],model_name='gpt-3.5-turbo-0125',temperature=0.6)
    
    industry_prompt = PromptTemplate(input_variables=['Industry'],
    template="When did started {Industry}")

    industry_chain = LLMChain(llm=llm,prompt=industry_prompt,output_key="Year")

    category_prompt = PromptTemplate(input_variables=['Industry'],
    template="What is the Category of this {Industry}")

    category_chain = LLMChain(llm=llm,prompt=category_prompt,output_key="Category")

    ceo_prompt = PromptTemplate(input_variables=['Industry'],
    template="Tell me the Name of Current CEO of this {Industry}")  

    ceo_chain = LLMChain(llm=llm,prompt=ceo_prompt,output_key="CEO")

    service_prompt = PromptTemplate(input_variables=['Industry'],
    template="Which Service provide this {Industry}")  

    service_chain = LLMChain(llm=llm,prompt=service_prompt,output_key="Service")

    model_prompt = PromptTemplate(input_variables=['Industry'],
    template="Tell me the Top Models in this {Industry}")  

    model_chain = LLMChain(llm=llm,prompt=model_prompt,output_key="Models")

    media_prompt = PromptTemplate(input_variables=['Industry'],
    template="Please provide the websites or instagram links of models {Industry}")  

    media_chain = LLMChain(llm=llm,prompt=media_prompt,output_key="links")

    chain = SequentialChain(chains=[industry_chain,category_chain,ceo_chain,service_chain,model_chain,media_chain],
    input_variables=['Industry'],
    output_variables=['Year','Category','CEO','Service','Models','links'])

    response = chain({"Industry":"question"})
    return response



## Initialize streamlit app
    
st.set_page_config(page_title="Industry Info")
st.header("Langchain Application")
input = st.text_input("Input Industry Name : ",key="input")
response = get_openai_response(input)
submit = st.button("Industry Submit")

if submit:
    st.subheader("The Response is: ")
    st.write(response)
