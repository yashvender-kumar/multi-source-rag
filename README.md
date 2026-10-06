# Multi-Source RAG Chatbot

This is a RAG-based AI chatbot. You can upload PDF files, CSV files, or add website URLs, and then ask any question related to those documents. The chatbot reads the content and answers using only the information found in your files, and it also shows the source of every answer.

## Features
-> Multi-Source Ingestion: Ability to extract and process data from PDF documents, CSV datasets, and Web URLs.

-> Vector Embeddings & Semantic Search: Uses text chunking and HuggingFace embeddings for fast and accurate retrieval.

-> Conversational Memory: Session-state memory management to retain and remember past chat context.

-> Source Attribution: Displays the source file or URL for every answer.

-> Interactive UI: A clean and user-friendly chat interface built using Streamlit.

## Tech Stack
-> Framework: LangChain

-> LLM Provider: Groq (ya Gemini API)

->Embeddings: HuggingFace Embeddings / Google Generative AI Embeddings

->Vector Database: FAISS / ChromaDB

->Document Loaders: PyPDFLoader, CSVLoader, WebBaseLoader

->Frontend / UI: Streamlit

->Language & Utilities: Python 3.10+

## Setup
 `git clone -> ## Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/multi-source-rag.git](https://github.com/your-username/multi-source-rag.git)
   cd multi-source-rag

2. Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate

3. Install required dependencies:
    pip install -r requirements.txt

4. Set up environment variables:
    GROQ_API_KEY=your_groq_api_key_here

5. Run the Streamlit application:
    python -m streamlit run app.py

## Usage

1. **Launch the Application:** Run `python -m streamlit run app.py` in your terminal.
2. **Upload Data Sources:** Open the sidebar to upload PDF files, CSV datasets, or enter a Web URL.
3. **Build Vector Index:** Click the **"⚙️ Process & Build Index"** button to process and index the documents.
4. **Ask Questions:** Type your query in the chat input at the bottom to interact with the documents.
5. **View Sources:** Expand the **"View Sources"** section under any answer to check where the information came from.

## Roadmap

-> Multi-Source Data Ingestion: Process and clean data from PDFs, CSV files, and Web URLs.
-> Vector Storage & Chat Memory: Store embeddings with FAISS and track conversation history.
-> Source Tracking: Display exact document sources or URLs with every answer.
-> UI & UX Enhancements: Add an indexing progress bar and a clear chat history button.
-> Source Filtering: Allow users to filter search results by document type (e.g., PDF vs CSV).
-> Cloud Deployment: Host the Streamlit app live on Streamlit Community Cloud.
-> Hybrid Search Exploration: Combine BM25 keyword search with FAISS vector search for better accuracy.