import os
from langchain_community.document_loaders import PyPDFLoader


DATA_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_all_pdfs():
    pdf_files = [
        os.path.join(DATA_FOLDER, f)
        for f in os.listdir(DATA_FOLDER)
        if f.lower().endswith('.pdf')
    ]
    all_documents = []
    for pdf_path in pdf_files:
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        all_documents.extend(docs)
    print(f"Loaded {len(all_documents)} pages from {len(pdf_files)} PDFs")
    return all_documents
