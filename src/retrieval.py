from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from pathlib import Path
from src.indexing import load_index


GROQ_MODEL = "openai/gpt-oss-120b"

llm = ChatGroq(model=GROQ_MODEL, temperature=0)
index = load_index()


PROMPT_TEMPLATE = """
You are a helpful assistant. Answer the question using ONLY the context given below.
Use the chat history only to understand follow-up questions.
If the answer is not present in the context, say: "I could not find this information in the provided sources."

Chat History:
{chat_history}

Context:
{context}

Question:
{question}

Answer:
"""

def ask(question, chat_history= ""):
    docs = index.similarity_search(question, k=4)
    context = ""
    for doc in docs:
        context += doc.page_content + "\n\n"

    prompt = PROMPT_TEMPLATE.format(context=context, question=question, chat_history=chat_history)
    response = llm.invoke(prompt)
    answer = response.content

    sources = []
    for doc in docs:
        source_path = doc.metadata.get("source", "Unknown")

        #PDF Handling
        if "page" in doc.metadata:
            file_name = Path(source_path).name
            page = doc.metadata['page'] + 1
            text =f"PDF: {file_name}, page {page}"

        #CSV Handling
        elif "row" in doc.metadata:
            file_name = Path(source_path).name
            row = doc.metadata['row']
            text = f"CSV: {file_name}, row {row}"

        #Website URL Handling
        else:
            text = f"web: {source_path}"

        if text not in sources:
            sources.append(text)

    return answer, sources

def reload_index():
    global index
    index = load_index()


if __name__ == "__main__":
    while True:
        query = input("User: ")

        if query.lower() in ["exit", "quit", "bye"]:
            print("Good Bye")
            break

        answer, sources = ask(query)

        print("\nAi:", answer)
        print("\nSources:")
        for s in sources:
            print("-",s)
        print("-"*50)



# for Execution => python -m src.retrieval