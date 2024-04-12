import llama_index
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv

load_dotenv()

def main(url: str)-> None:
    document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index=VectorStoreIndex.from_documents(documents=document)
    query_engine=index.as_query_engine()
    response=query_engine.query("What is Generative AI?")
    print(response)

if __name__ == "__main__":
    main(url="https://medium.com/@sunil.dangi/what-is-generative-ai-and-what-are-the-best-tools-and-resources-to-learn-it-b13bfa11eaaf")