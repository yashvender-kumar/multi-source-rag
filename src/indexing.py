from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from pathlib import Path
from src.ingestion import load_all_docs

STORAGE_DIR = "storage"
EMBED_MODEL = "all-MiniLM-L6-v2"

embedding = HuggingFaceEmbeddings(model_name = EMBED_MODEL)

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 250)

def build_index(docs):
    chunks = splitter.split_documents(docs)
    print("Total Chunks:", len(chunks))

    index = FAISS.from_documents(chunks, embedding)

    index.save_local(STORAGE_DIR)

    return index


def load_index():
<<<<<<< HEAD
    try:
        return FAISS.load_local(STORAGE_DIR, embedding, allow_dangerous_deserialization=True)
    except Exception as e:
        print(f"Index file nahi mili: {e}")
        return None
=======
    return FAISS.load_local(STORAGE_DIR, embedding, allow_dangerous_deserialization=True)
>>>>>>> 2c6e4f6e67570f40a11ba8d6cc3aac254f1ff82f

if __name__ == "__main__":
    docs = load_all_docs()
    build_index(docs)
    index = load_index()

    result = index.similarity_search("What is the Ocean ?", k =2)
    print("Metadata", result[0].metadata)
    print("Text", result[0].page_content[:200])


# For Testing =>  python -m src.indexing   