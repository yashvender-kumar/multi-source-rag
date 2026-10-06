from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, WebBaseLoader

PDF_DIR = Path("data/pdfs")
CSV_DIR = Path("data/csvs")
URL_FILE = Path("data/urls.txt")


# CSVs Load Karein
def load_csvs():
    if not CSV_DIR.exists():
        return []

    csv_files = list(CSV_DIR.glob("*.csv"))
    if not csv_files:
        return []

    all_docs = []
    for csv in csv_files:
        loader = CSVLoader(str(csv))
        docs = loader.load()
        all_docs.extend(docs)

    return all_docs


# Web URLs Load Karein
def load_urls(urls):
    if not urls:
        return []

    loader = WebBaseLoader(urls)
    docs = loader.load()

    for doc in docs:
        lines = doc.page_content.splitlines()
        cleaned = [line.strip() for line in lines if line.strip()]
        doc.page_content = "\n".join(cleaned)

    return docs

def read_urls():
    if not URL_FILE.exists():
        return []
    with open(URL_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_url(url):
    URL_FILE.parent.mkdir(parents=True, exist_ok=True)
    urls = read_urls()
    if url not in urls:
        with open(URL_FILE, "a", encoding="utf-8") as f:  # Fixed 'a' mode
            f.write(url + "\n")


# PDFs Load Karein
def load_pdfs():
    if not PDF_DIR.exists():
        return []

    pdf_files = list(PDF_DIR.glob("*.pdf"))
    if not pdf_files:
        return []

    all_docs = []
    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        docs = loader.load()
        all_docs.extend(docs)

    return all_docs


# Unified Loader Function (PDF + CSV + URLs sabke liye)
def load_all_docs():
    docs = []
    
    # 1. PDFs
    try:
        pdf_docs = load_pdfs()
        docs.extend(pdf_docs)
    except Exception as e:
        print(f"Error loading PDFs: {e}")

    # 2. CSVs
    try:
        csv_docs = load_csvs()
        docs.extend(csv_docs)
    except Exception as e:
        print(f"Error loading CSVs: {e}")

    # 3. URLs
    urls = read_urls()
    if urls:
        try:
            url_docs = load_urls(urls)
            docs.extend(url_docs)
        except Exception as e:
            print(f"Error loading URLs: {e}")

    return docs


if __name__ == "__main__":
    all_docs = load_all_docs()
    print("Total documents loaded across all sources:", len(all_docs))