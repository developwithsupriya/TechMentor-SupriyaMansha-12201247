# ingest_documents.py
"""
Batch ingestion script to populate ChromaDB with PDF documents.
Uses the service modules from app/services/ for consistency.
"""

from app.services.document_loader import load_all_pdfs
from app.services.chunker import chunk_text
from app.services.embedder import embed_chunks
from app.services.vectordb import store_embeddings

def main():
    print("🚀 Starting PDF ingestion pipeline...")
    print("=" * 60)
    
    # Step 1: Load all PDF documents
    print("\n📄 Step 1: Loading PDFs from app/data/ directory...")
    try:
        documents = load_all_pdfs()
        print(f"✅ Loaded {len(documents)} pages from PDFs")
    except Exception as e:
        print(f"❌ Error loading PDFs: {e}")
        return
    
    # Step 2: Chunk the documents into smaller pieces
    print("\n✂️  Step 2: Chunking documents...")
    all_chunks = []
    try:
        for i, doc in enumerate(documents):
            chunks = chunk_text(doc.page_content, chunk_size=1000, chunk_overlap=150)
            all_chunks.extend(chunks)
            if (i + 1) % 100 == 0:
                print(f"   Processed {i + 1}/{len(documents)} pages...")
        print(f"✅ Created {len(all_chunks)} text chunks")
    except Exception as e:
        print(f"❌ Error chunking documents: {e}")
        return
    
    # Step 3: Generate embeddings for all chunks
    print("\n🧠 Step 3: Generating embeddings...")
    print("   (This may take a few minutes...)")
    try:
        embeddings = embed_chunks(all_chunks)
        print(f"✅ Generated {len(embeddings)} embeddings")
    except Exception as e:
        print(f"❌ Error generating embeddings: {e}")
        return
    
    # Step 4: Store chunks and embeddings in ChromaDB
    print("\n💾 Step 4: Storing in vector database...")
    try:
        store_embeddings(all_chunks, embeddings)
        print(f"✅ Successfully stored all data in ChromaDB!")
    except Exception as e:
        print(f"❌ Error storing in database: {e}")
        return
    
    # Summary
    print("\n" + "=" * 60)
    print("🎉 Ingestion pipeline completed successfully!")
    print(f"📊 Summary:")
    print(f"   • Total pages processed: {len(documents)}")
    print(f"   • Total chunks created: {len(all_chunks)}")
    print(f"   • Total embeddings stored: {len(embeddings)}")
    print(f"   • Database path: ./chroma_db/")
    print("=" * 60)
    print("\n✨ You can now start the FastAPI server:")
    print("   uvicorn app.main:app --reload")
    print("\n📚 Access API docs at: http://localhost:8000/docs")

if __name__ == "__main__":
    main()
