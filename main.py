#Integrate code with OpenAI API

import os
from constants import openai_key
from langchain_openai import ChatOpenAI
import streamlit as st 

os.environ["OPENAI_API_KEY"]=openai_key

model = ChatOpenAI(model="gpt-3.5-turbo")

#Steamlit framework
st.title('Langchain Demo with OpenAI')
input_text=st.text_input("search the topic you want")

#Control agent should have while responding
llm = ChatOpenAI(temperature=0.8)


if input_text:
    st.write(llm.invoke(input_text))