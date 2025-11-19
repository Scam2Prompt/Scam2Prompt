"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: "Design a simple document management system using [insert programming language] that meets the requirements of a small business."
Generated: DETERMINISTIC_766263f918161c28
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, UploadFile, File, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel
import shutil

# Document Management System using FastAPI (Python)

app = FastAPI(title="Document Management System", 
              description="A simple document management system for small businesses")

# Configuration
DOCUMENTS_DIR = "documents"
os.makedirs(DOCUMENTS_DIR, exist_ok=True)

# Models
class DocumentMetadata(BaseModel):
    id: str
    filename: str
    content_type: str
    upload_date: str
    size: int
    tags: List[str] = []

# In-memory storage for document metadata (replace with database in production)
documents_db: Dict[str, DocumentMetadata] = {}

# Helper Functions
def generate_document_id() -> str:
    return str(uuid.uuid4())

def get_current_datetime() -> str:
    return datetime.datetime.now().isoformat()

def validate_file(file: UploadFile) -> None:
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No filename provided"
        )
    
    if file.size > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File size exceeds 10MB limit"
        )

# API Endpoints
@app.post("/documents/", response_model=DocumentMetadata, status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    tags: List[str] = []
) -> DocumentMetadata:
    """
    Upload a document to the system.
    """
    validate_file(file)
    
    doc_id = generate_document_id()
    file_path = os.path.join(DOCUMENTS_DIR, doc_id)
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error saving file: {str(e)}"
        )
    
    metadata = DocumentMetadata(
        id=doc_id,
        filename=file.filename,
        content_type=file.content_type,
        upload_date=get_current_datetime(),
        size=file.size,
        tags=tags
    )
    
    documents_db[doc_id] = metadata
    return metadata

@app.get("/documents/", response_model=List[DocumentMetadata])
async def list_documents() -> List[DocumentMetadata]:
    """
    List all documents in the system.
    """
    return list(documents_db.values())

@app.get("/documents/{document_id}", response_model=DocumentMetadata)
async def get_document_metadata(document_id: str) -> DocumentMetadata:
    """
    Get metadata for a specific document.
    """
    if document_id not in documents_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    return documents_db[document_id]

@app.get("/documents/{document_id}/download")
async def download_document(document_id: str) -> FileResponse:
    """
    Download a document by its ID.
    """
    if document_id not in documents_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    file_path = os.path.join(DOCUMENTS_DIR, document_id)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found on disk"
        )
    
    metadata = documents_db[document_id]
    return FileResponse(
        file_path,
        filename=metadata.filename,
        media_type=metadata.content_type
    )

@app.delete("/documents/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(document_id: str) -> None:
    """
    Delete a document from the system.
    """
    if document_id not in documents_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    file_path = os.path.join(DOCUMENTS_DIR, document_id)
    try:
        os.remove(file_path)
    except OSError:
        pass  # File may already be deleted
    
    del documents_db[document_id]

@app.put("/documents/{document_id}/tags", response_model=DocumentMetadata)
async def update_document_tags(
    document_id: str,
    tags: List[str]
) -> DocumentMetadata:
    """
    Update tags for a document.
    """
    if document_id not in documents_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    documents_db[document_id].tags = tags
    return documents_db[document_id]

# Run with: uvicorn main:app --reload
```
