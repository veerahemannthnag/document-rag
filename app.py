import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

DB_DIR = "chroma_db"

PROMPT_TEMPLATE = """
You are a helpful assistant answering questions ONLY from the provided document context.

Rules:
- Use only the provided context.
- If the answer is not in the context, say:
  "I couldn't find that in the documents."
- Do not make up facts.
- Keep answers concise and clear.

Context:
{context}

Question:
{question}

Answer:
"""

PROMPT = PromptTemplate(
    template=PROMPT_TEMPLATE,
    input_variables=["context", "question"]
)


@st.cache_resource
def load_qa_chain():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding
    )

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3, "fetch_k": 8}
    )

    llm = Ollama(model="phi3:mini")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    return qa


st.set_page_config(page_title="Document Chatbot", page_icon="📄")
st.title("📄 Document Chatbot")
st.write("Ask questions about your uploaded documents.")

qa = load_qa_chain()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask a question:")

if st.button("Ask") and query:
    with st.spinner("Searching documents and generating answer..."):
        result = qa({"query": query})

        answer = result["result"]
        sources = result["source_documents"]

        st.session_state.chat_history.append({
            "question": query,
            "answer": answer,
            "sources": sources
        })

# Show chat history
for chat in reversed(st.session_state.chat_history):
    st.markdown(f"### 🙋 You")
    st.write(chat["question"])

    st.markdown(f"### 🤖 Bot")
    st.write(chat["answer"])

    st.markdown("**Sources:**")
    seen = set()
    for doc in chat["sources"]:
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "N/A")
        key = (source, page)

        if key not in seen:
            st.write(f"- {source} (page: {page})")
            seen.add(key)

    st.markdown("---")