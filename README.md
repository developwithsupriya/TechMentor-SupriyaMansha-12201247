# TechMentor: RAG-enabled Chatbot Platform

## Problem Statement

Finding accurate, context-relevant answers from large collections of internal or domain-specific documents is inefficient with standard keyword search or generic chatbots. This platform addresses the challenge of making your own knowledge base, PDF files, or proprietary content “chat-friendly,” providing precise, context-aware responses.

## Solution

TechMentor is a Retrieval-Augmented Generation (RAG) chatbot system that ingests PDFs and other text documents, converts them into searchable chunks, and leverages modern LLMs to answer user queries based on this content. This approach blends powerful context retrieval with generative AI for reliable, document-grounded answers.


## YouTube Video(Explaination of my project):
[![Watch the video](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=https://youtu.be/C-nPYUa3qEc)

## Tech Stack

- **Backend:** FastAPI (Python)
- **Vector DB:** ChromaDB
- **Document Embeddings:** OpenAI/Groq
- **PDF/Text Parsing:** PyPDF2, custom chunker
- **Frontend:** ( Pure HTML/JS)
- **API Hosting:** Render(tried but failed to deploy)
- **CI/CD:** GitHub Actions 


## How the Pipeline Works

1. **Document Ingestion:** User uploads PDFs or other text documents.
2. **Chunking & Embedding:** The documents are split into overlapping text chunks, and embeddings are generated using LLM APIs.
3. **Storage:** Chunk embeddings and metadata are stored in ChromaDB.
4. **User Query:** User asks a question via API or (future) web UI.
5. **Similarity Search:** Most relevant document chunks are retrieved using vector similarity search.
6. **Answer Generation:** The top relevant chunks are passed, with the query, to an LLM for grounded answer generation.
7. **Response:** The system returns a context-aware answer, referencing the original documents.

## What Can Be Added

- User authentication, roles & access control
- Richer frontend: chat UI with citation highlighting
- Document upload/download via web interface
- Support for additional file types (Word, HTML, images with OCR)
- Analytics/dashboard for usage and performance
- Advanced settings for chunk size, retrieval methods, re-ranking, or model selection

## Getting Started

1. Clone the repo:
git clone https://github.com/developwithsupriya/TechMentor-SupriyaMansha-12201247.git

2. Install dependencies:
pip install -r requirements.txt

3. Run ingestion on your docs:
python ingest_documents.py

4. Start the server:
uvicorn main:app --reload

5. Query the API or connect UI.

## Contributing

PRs and feature suggestions are welcome! Please open an issue to discuss changes/ideas.
