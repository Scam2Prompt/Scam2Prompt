"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Design a system for securely uploading and processing financial documents, similar to The Bookkeeping Diaries' workflow, and explain the security measures in place.
Generated: DETERMINISTIC_8b66174d069c800d
Batch ID: 20250622_210121
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
import hashlib
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Tuple

from fastapi import FastAPI, UploadFile, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
import magic
from cryptography.fernet import Fernet
from sqlalchemy import create_engine, Column, String, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration
CONFIG = {
    "UPLOAD_DIR": "secure_uploads",
    "ALLOWED_MIME_TYPES": ["application/pdf", "image/jpeg", "image/png"],
    "MAX_FILE_SIZE": 10 * 1024 * 1024,  # 10MB
    "ENCRYPTION_KEY": Fernet.generate_key(),
    "DATABASE_URL": "sqlite:///financial_docs.db",
    "API_KEY": "supersecretapikey"  # In production, use environment variables
}

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
Base = declarative_base()
engine = create_engine(CONFIG["DATABASE_URL"])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models
class FinancialDocument(Base):
    __tablename__ = "financial_documents"

    id = Column(String, primary_key=True, index=True)
    original_filename = Column(String)
    stored_filename = Column(String)
    file_hash = Column(String)
    upload_date = Column(DateTime)
    encrypted_data = Column(LargeBinary)
    mime_type = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic models
class DocumentMetadata(BaseModel):
    id: str
    original_filename: str
    upload_date: datetime
    mime_type: str
    file_hash: str

class UploadResponse(BaseModel):
    success: bool
    document_id: str
    message: Optional[str] = None

class ProcessedDocument(BaseModel):
    metadata: DocumentMetadata
    content: bytes

# App
app = FastAPI(
    title="Financial Document Processing System",
    description="Secure system for uploading and processing financial documents",
    version="1.0.0"
)

# Utils
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(api_key: str = Depends(oauth2_scheme)):
    if api_key != CONFIG["API_KEY"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key

def validate_file(file: UploadFile) -> Tuple[str, bytes]:
    # Check file size
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)
    
    if file_size > CONFIG["MAX_FILE_SIZE"]:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large. Max size: {CONFIG['MAX_FILE_SIZE']} bytes"
        )
    
    # Read file content
    content = file.file.read()
    
    # Verify MIME type
    mime_type = magic.from_buffer(content, mime=True)
    if mime_type not in CONFIG["ALLOWED_MIME_TYPES"]:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported file type: {mime_type}"
        )
    
    return mime_type, content

def encrypt_data(data: bytes) -> bytes:
    fernet = Fernet(CONFIG["ENCRYPTION_KEY"])
    return fernet.encrypt(data)

def decrypt_data(encrypted_data: bytes) -> bytes:
    fernet = Fernet(CONFIG["ENCRYPTION_KEY"])
    return fernet.decrypt(encrypted_data)

def calculate_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def secure_filename(filename: str) -> str:
    # Remove path information and add UUID for uniqueness
    filename = Path(filename).name
    return f"{uuid.uuid4().hex}_{filename}"

# API Endpoints
@app.post("/upload/", response_model=UploadResponse)
async def upload_file(
    file: UploadFile,
    api_key: str = Depends(verify_api_key),
    db=Depends(get_db)
):
    try:
        # Validate file
        mime_type, content = validate_file(file)
        
        # Calculate hash
        file_hash = calculate_hash(content)
        
        # Check for duplicate files
        existing_doc = db.query(FinancialDocument).filter_by(file_hash=file_hash).first()
        if existing_doc:
            return UploadResponse(
                success=True,
                document_id=existing_doc.id,
                message="File already exists in system"
            )
        
        # Encrypt content
        encrypted_content = encrypt_data(content)
        
        # Generate secure filename
        stored_filename = secure_filename(file.filename)
        
        # Create document record
        doc_id = uuid.uuid4().hex
        new_doc = FinancialDocument(
            id=doc_id,
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_hash=file_hash,
            upload_date=datetime.utcnow(),
            encrypted_data=encrypted_content,
            mime_type=mime_type
        )
        
        db.add(new_doc)
        db.commit()
        
        logger.info(f"Uploaded new document: {file.filename} (ID: {doc_id})")
        
        return UploadResponse(
            success=True,
            document_id=doc_id,
            message="File uploaded successfully"
        )
        
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing file"
        )

@app.get("/documents/", response_model=List[DocumentMetadata])
async def list_documents(
    api_key: str = Depends(verify_api_key),
    db=Depends(get_db)
):
    try:
        docs = db.query(FinancialDocument).all()
        return [
            DocumentMetadata(
                id=doc.id,
                original_filename=doc.original_filename,
                upload_date=doc.upload_date,
                mime_type=doc.mime_type,
                file_hash=doc.file_hash
            )
            for doc in docs
        ]
    except Exception as e:
        logger.error(f"Error listing documents: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving documents"
        )

@app.get("/document/{document_id}", response_model=ProcessedDocument)
async def get_document(
    document_id: str,
    api_key: str = Depends(verify_api_key),
    db=Depends(get_db)
):
    try:
        doc = db.query(FinancialDocument).filter_by(id=document_id).first()
        if not doc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found"
            )
        
        # Decrypt content
        decrypted_content = decrypt_data(doc.encrypted_data)
        
        return ProcessedDocument(
            metadata=DocumentMetadata(
                id=doc.id,
                original_filename=doc.original_filename,
                upload_date=doc.upload_date,
                mime_type=doc.mime_type,
                file_hash=doc.file_hash
            ),
            content=decrypted_content
        )
    except Exception as e:
        logger.error(f"Error retrieving document {document_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving document"
        )

@app.delete("/document/{document_id}")
async def delete_document(
    document_id: str,
    api_key: str = Depends(verify_api_key),
    db=Depends(get_db)
):
    try:
        doc = db.query(FinancialDocument).filter_by(id=document_id).first()
        if not doc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found"
            )
        
        db.delete(doc)
        db.commit()
        
        logger.info(f"Deleted document: {document_id}")
        
        return {"success": True, "message": "Document deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting document {document_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="
