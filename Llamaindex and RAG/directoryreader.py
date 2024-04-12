import llama_index
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv

load_dotenv()

def main(url: str)-> None:
    document=SimpleDirectoryReader(url).load_data()
    index=VectorStoreIndex.from_documents(documents=document)
    query_engine=index.as_query_engine()
    response=query_engine.query("What did the artical saying please summarize it?")
    print(response)

if __name__ == "__main__":
    main(url=r"D:\\Programs\\GenAI\\LLamaindex\\data")