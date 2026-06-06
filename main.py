import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain
st.title("Courses QA 😊 ")

question = st.text_input("question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)
    
    st.header("Answer: ")
    st.write(response['result'])
    