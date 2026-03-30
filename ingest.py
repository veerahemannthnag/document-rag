import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


DATA_DIR = "data"
DB_DIR = "chroma_db"


def load_documents(data_dir):
    docs = []

    for root, _, files in os.walk(data_dir):
        for file in files:
            file_path = os.path.join(root, file)
            ext = Path(file).suffix.lower()

            try:
                if ext == ".pdf":
                    loader = PyPDFLoader(file_path)
                    loaded_docs = loader.load()

                elif ext == ".txt":
                    loader = TextLoader(file_path, encoding="utf-8")
                    loaded_docs = loader.load()

                else:
                    print(f"Skipping unsupported file: {file_path}")
                    continue

                # Add metadata
                for doc in loaded_docs:
                    doc.metadata["source"] = file
                    doc.metadata["full_path"] = file_path
                    doc.metadata["category"] = Path(root).name
                    doc.metadata["file_type"] = ext

                docs.extend(loaded_docs)

            except Exception as e:
                print(f"Error loading {file_path}: {e}")

    return docs


def main():
    print("Loading documents...")
    documents = load_documents(DATA_DIR)

    if not documents:
        print("No supported documents found in 'data/' folder.")
        return

    print(f"Loaded {len(documents)} pages/sections")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    print("Creating embeddings... (this may take a few minutes first time)")
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print("Saving to ChromaDB...")
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=DB_DIR
    )

    db.persist()
    print("✅ Vector DB created successfully!")


if __name__ == "__main__":
    main()