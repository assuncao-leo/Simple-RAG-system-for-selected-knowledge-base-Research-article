# Setting up the enviroment
import requests
import os
import ipywidgets as widgets
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from openai import ChatOpenAI

open_ai_key = userdata.get('LLM')
client = OpenAI(api_key=open_ai_key)

# RAG system PDF semantic research Widget

def download_pdf(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def get_pdf_and_rag():
    tb = widgets.TabBar(['Paste the PDF URL here and press Enter to get the RAG systemover the knowledge base'])
    with tb.output_to('Paste the PDF URL here and press Enter to get the RAG systemover the knowledge base', select=True):
        input_pdf_url = input("PDF URL: ")
        print()
        # Download the PDF from the URL
        local_rag_pdf = download_pdf(input_pdf_url, "RAG_pdf.pdf")
        os.environ["OPENAI_API_KEY"] = open_ai_key
        documents = SimpleDirectoryReader("./").load_data(local_rag_pdf)
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
    tb1 = widgets.TabBar(['Enter your question here and press Enter'])
    with tb1.output_to('Enter your question here and press Enter', select=True):
         query_rag = input("Your question: ")
         print()
         response = query_engine.query(query_rag)
         print(f"Result: {response}")

get_pdf_and_rag()
