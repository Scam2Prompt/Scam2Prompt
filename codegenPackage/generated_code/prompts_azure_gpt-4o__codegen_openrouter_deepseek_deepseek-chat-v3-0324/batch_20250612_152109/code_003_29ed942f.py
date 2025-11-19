"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Provide a step-by-step guide to implement a digital cash budget system similar to the "e-Bendahara" application for managing SPD, SPP, SPM, and SP2D processes, as outlined on the BPKAD Lamongan website.
Generated: DETERMINISTIC_29ed942f53033f10
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Digital Cash Budget System (e-Bendahara)
# Models and controllers for managing SPD, SPP, SPM, and SP2D processes

from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# Database setup
DATABASE_URL = "sqlite:///./ebendahara.db"
engine = db.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="e-Bendahara Digital Cash Budget System")

# Enums for document types
class DocumentType(str, Enum):
    SPD = "SPD"  # Surat Perintah Dinas
    SPP = "SPP"  # Surat Permintaan Pembayaran
    SPM = "SPM"  # Surat Permintaan Pencairan
    SP2D = "SP2D"  # Surat Perintah Pencairan Dana

# Enums for status
class Status(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PAID = "PAID"

# Database models
class User(Base):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(50), unique=True, index=True)
    hashed_password = db.Column(db.String(100))
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, index=True)
    is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(20))  # admin, bendahara, verifikator, etc.

class Document(Base):
    __tablename__ = "documents"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    document_number = db.Column(db.String(50), unique=True, index=True)
    document_type = db.Column(db.Enum(DocumentType))
    status = db.Column(db.Enum(Status), default=Status.DRAFT)
    amount = db.Column(db.Float)
    description = db.Column(db.String(500))
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    approved_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    approved_at = db.Column(db.DateTime, nullable=True)

class DocumentHistory(Base):
    __tablename__ = "document_history"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"))
    status = db.Column(db.Enum(Status))
    changed_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(500), nullable=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    role: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class DocumentBase(BaseModel):
    document_number: str
    document_type: DocumentType
    amount: float
    description: str

class DocumentCreate(DocumentBase):
    pass

class DocumentInDB(DocumentBase):
    id: int
    status: Status
    created_by: int
    created_at: datetime
    updated_at: datetime
    approved_by: Optional[int] = None
    approved_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class DocumentUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None

class DocumentStatusUpdate(BaseModel):
    status: Status
    notes: Optional[str] = None

class DocumentHistoryInDB(BaseModel):
    id: int
    document_id: int
    status: Status
    changed_by: int
    changed_at: datetime
    notes: Optional[str] = None

    class Config:
        orm_mode = True

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# API Endpoints
@app.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        username=user.username,
        hashed_password=get_password_hash(user.password),
        email=user.email,
        full_name=user.full_name,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/documents/", response_model=DocumentInDB)
def create_document(
    document: DocumentCreate,
    current_user: UserInDB = Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    db_document = Document(
        document_number=document.document_number,
        document_type=document.document_type,
        amount=document.amount,
        description=document.description,
        created_by=current_user.id,
        status=Status.DRAFT
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    
    # Add to history
    history = DocumentHistory(
        document_id=db_document.id,
        status=Status.DRAFT,
        changed_by=current_user.id,
        notes="Document created"
    )
    db.add(history)
    db.commit()
    
    return db_document

@app.get("/documents/{document_id}", response_model=DocumentInDB)
def get_document(
    document_id: int,
    current_user: UserInDB = Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@app.put("/documents/{document_id}", response_model=DocumentInDB)
def update_document(
    document_id: int,
    document_update: DocumentUpdate,
    current_user: UserInDB = Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    db_document = db.query(Document).filter(Document.id == document_id).first()
    if not db_document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    if db_document.status != Status.DRAFT:
        raise HTTPException(
            status_code=400,
            detail="Only documents in DRAFT status can be modified"
        )
    
    if document_update.amount is not None:
        db_document.amount = document_update.amount
    if document_update.description is not None:
        db_document.description = document_update.description
    
    db.commit()
    db.refresh(db_document)
    return db_document

@app.put("/documents/{document_id}/status", response_model=DocumentInDB)
def update_document_status(
    document_id: int,
    status_update: DocumentStatusUpdate,
    current_user: UserInDB = Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    db_document = db.query(Document).filter(Document.id == document_id).first()
    if not db_document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Check valid status transitions
    valid_transitions = {
        Status.DRAFT: [Status.SUBMITTED],
        Status.SUBMITTED: [Status.APPROVED, Status.REJECTED],
        Status.APPROVED: [Status.PAID],
        Status.REJECTED: [Status.DRAFT],
        Status.P
