import streamlit as st
import os

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

st.set_page_config('preguntaDOC')
st.header("Pregunta a tu PDF")
OPENAI_API_KEY = st.text_input('OpenAI API Key', type='password')
pdf_obj = st.file_uploader("Carga tu documento", type="pdf", on_change=st.cache_resource.clear)

@st.cache_resource 
def create_embeddings(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        length_function=len
        )        
    chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    return knowledge_base

if pdf_obj:
    knowledge_base = create_embeddings(pdf_obj)
    user_question = st.text_input("Haz una pregunta sobre tu PDF:")

    if user_question:
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        docs = knowledge_base.similarity_search(user_question, 3)
        llm = ChatOpenAI(model_name='gpt-3.5-turbo')
        chain = load_qa_chain(llm, chain_type="stuff")
        respuesta = chain.run(input_documents=docs, question=user_question)

        st.write(respuesta)    