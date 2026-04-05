from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

DB_DIR = "chroma_db"


PROMPT_TEMPLATE = """
You are a helpful assistant answering questions ONLY from the provided document context.

Rules:
- Use only the context below.
- If the answer is not found in the context, say:
  "I couldn't find that in the documents."
- Do not make up facts.
- If possible, answer clearly and briefly.

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


def main():
    print("Loading vector database...")
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding
    )

    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10}
    )

    print("Connecting to Ollama...")
    llm = Ollama(model="phi3:mini")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    print("\n✅ Chatbot is ready!")
    print("Type your question. Type 'exit' to quit.\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        result = qa.invoke({"query": query})

        print("\nBot:")
        print(result["result"])

        print("\nSources:")
        seen = set()
        for doc in result["source_documents"]:
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")

            key = (source, page)
            if key not in seen:
                print(f"- {source} (page: {page})")
                seen.add(key)

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()