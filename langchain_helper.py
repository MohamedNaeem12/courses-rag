import os
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.llms import GooglePalm
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA    
from langchain.document_loaders import CSVLoader

load_dotenv()

llm = GooglePalm(google_api_key=os.getenv("GOOGLE_API_KEY"), temperature=0)

instructor_embeddings = HuggingFaceInstructEmbeddings()
vector_db_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path='coursesqa.csv', source_column='prompt')
    docs = loader.load()
    vectordb = FAISS.from_documents(documents = docs, embedding=instructor_embeddings)
    vectordb.save_local(vector_db_file_path)

def get_qa_chain():
    vectordb = FAISS.load_local(file_path=vector_db_file_path, embedding=instructor_embeddings)
    retriever = vectordb.as_retriever(threshold=0.7)
    
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    return chain



if __name__ == "__main__":
    create_vector_db()