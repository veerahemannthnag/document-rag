

# Document RAG

A Retrieval-Augmented Generation (RAG) system for querying and chatting with documents using LangChain, ChromaDB, and Streamlit.

## Features

- Document ingestion and vectorization
- Interactive chat interface for querying documents
- Document generation utilities
- Web-based UI with Streamlit

## Prerequisites

- Python 3.8+
- Ollama (for running the phi3:mini model)

## Installation

1. **Install Ollama**:
   - Download from [https://ollama.com/download](https://ollama.com/download)
   - Run the model: `ollama run phi3:mini`

2. **Set up the project**:
   ```bash
   cd document-rag
   mkdir chroma_db
   mkdir data
   python -m venv langchain_env
   langchain_env\Scripts\activate  # On Windows
   python -m pip install --upgrade pip
   pip install langchain chromadb pypdf sentence-transformers streamlit langchain-community reportlab
   ```

## Usage

1. **Generate sample documents** (optional):
   ```bash
   python generate_docs.py
   ```

2. **Ingest documents**:
   ```bash
   python ingest.py
   ```

3. **Run the chat interface** (command-line):
   ```bash
   python chat.py
   ```

4. **Run the web app**:
   ```bash
   streamlit run app.py
   ```

## Project Structure

- `app.py`: Streamlit web application
- `chat.py`: Command-line chat interface
- `generate_docs.py`: Document generation script
- `ingest.py`: Document ingestion and vectorization script

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.