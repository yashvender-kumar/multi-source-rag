import streamlit as st
from src.retrieval import ask, reload_index
from src.indexing import build_index
from src.ingestion import  load_all_docs, PDF_DIR, CSV_DIR, save_url
from pathlib import Path


st.set_page_config(page_title="Multi-Source RAG Assistant", layout="wide")
st.title("Rag Based Ai-ChatBot")

st.sidebar.header("Upload PDFs")

#PDF Uplaod
uploaded_pdfs = st.sidebar.file_uploader(
    "Upload PDF Files", type=["pdf"], accept_multiple_files=True
)

#CSV uplaod
uploaded_csvs = st.sidebar.file_uploader(
    "Upload CSVs", type= ["csv"], accept_multiple_files=True
)

#URL Input
url_input = st.sidebar.text_input("Add Web URL:")
if st.sidebar.button("Add URL"):
    if url_input:
        save_url(url_input)
        st.sidebar.success("URL Saved!")


#Process & Index Button
if st.sidebar.button("⚙️ Process & Build Index"):
    with st.spinner("Proccesing document & e-building index..."):
        # Save PDFs
        if uploaded_pdfs:
            PDF_DIR.mkdir(parents=True, exist_ok=True)
            for f in uploaded_pdfs:
                with open(PDF_DIR / f.name, "wb") as out:
                    out.write(f.getbuffer())


        # Save CSVs
        if uploaded_csvs:
            CSV_DIR.mkdir(parents=True, exist_ok=True)
            for f in uploaded_csvs:
                with open(CSV_DIR / f.name, "wb") as out:
                    out.write(f.getbuffer())

        # Build Index for all sources
        docs = load_all_docs()
        if docs:
            build_index(docs)
            reload_index()
            st.sidebar.success(f"Indexed {len(docs)} document successfully")
        else:
            st.sidebar.warning("No data found to index")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            with st.expander("View Sources"):
                for s in message["sources"]:
                    st.write("-", s)


query = st.chat_input("Ask Related to Document..")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    history_lines = []
    for msg in st.session_state.messages[-6:-1]:
        history_lines.append(f"{msg['role']}: {msg['content']}")
    history_str = "\n".join(history_lines)

    with st.spinner("Thinking..."):
        answer, sources = ask(query, chat_history=history_str)

    with st.chat_message("ai"):
        st.markdown(answer)
        if sources:
            with st.expander("View Sources"):
                for s in sources:
                    st.write("-", s)

    st.session_state.messages.append(
        {"role": "ai", "content": answer, "sources": sources}
    )


# For Execution -> python -m streamlit run app.py