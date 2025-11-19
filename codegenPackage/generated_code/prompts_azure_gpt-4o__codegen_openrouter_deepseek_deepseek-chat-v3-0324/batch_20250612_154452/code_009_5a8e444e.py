"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Recommend software development practices for creating a scalable and secure electronic invoicing system, inspired by TICOM Software's emphasis on reliability and scalability.
Generated: DETERMINISTIC_5a8e444ea259f7fe
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electronic Invoicing System - Best Practices Implementation

This module demonstrates key software development practices for building a scalable
and secure electronic invoicing system, inspired by TICOM Software's principles.
"""

import logging
from typing import Optional, List
from abc import ABC, abstractmethod
import hashlib
import hmac
import os
from datetime import datetime
import json
from fastapi import FastAPI, HTTPException, status, Depends, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, validator, EmailStr
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/invoicing")
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# API Security
API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Constants
INVOICE_NUMBER_PREFIX = "INV"
HMAC_SECRET = os.getenv("HMAC_SECRET", "default-secret-key").encode()

class InvoiceItem(BaseModel):
    """Data model for invoice items with validation"""
    description: str
    quantity: int
    unit_price: float

    @validator('quantity')
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be positive')
        return v

    @validator('unit_price')
    def unit_price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Unit price must be positive')
        return v

class InvoiceCreate(BaseModel):
    """Data model for creating invoices"""
    customer_name: str
    customer_email: EmailStr
    items: List[InvoiceItem]
    due_date: datetime

    @validator('due_date')
    def due_date_must_be_future(cls, v):
        if v <= datetime.now():
            raise ValueError('Due date must be in the future')
        return v

class InvoiceDB(Base):
    """Database model for invoices"""
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True)
    customer_name = Column(String)
    customer_email = Column(String)
    items = Column(String)  # Stored as JSON
    amount_due = Column(Numeric(10, 2))
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")
    hmac_signature = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(api_key: str = Security(api_key_header)):
    """Verify API key"""
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key"
        )
    return api_key

def generate_hmac_signature(data: dict) -> str:
    """Generate HMAC signature for data integrity"""
    message = json.dumps(data, sort_keys=True).encode()
    return hmac.new(HMAC_SECRET, message, hashlib.sha256).hexdigest()

def verify_hmac_signature(data: dict, signature: str) -> bool:
    """Verify HMAC signature"""
    expected_signature = generate_hmac_signature(data)
    return hmac.compare_digest(expected_signature, signature)

class InvoiceNumberGenerator:
    """Invoice number generation service"""
    @staticmethod
    def generate_invoice_number(db: Session) -> str:
        """Generate unique invoice number"""
        last_invoice = db.query(InvoiceDB).order_by(InvoiceDB.id.desc()).first()
        last_id = last_invoice.id if last_invoice else 0
        return f"{INVOICE_NUMBER_PREFIX}-{datetime.now().year}-{last_id + 1:06d}"

class InvoiceRepository(ABC):
    """Abstract base class for invoice repository"""
    @abstractmethod
    def create_invoice(self, invoice_data: InvoiceCreate) -> InvoiceDB:
        pass

    @abstractmethod
    def get_invoice(self, invoice_number: str) -> Optional[InvoiceDB]:
        pass

class SQLInvoiceRepository(InvoiceRepository):
    """SQL implementation of invoice repository"""
    def __init__(self, db: Session):
        self.db = db

    def create_invoice(self, invoice_data: InvoiceCreate) -> InvoiceDB:
        """Create a new invoice"""
        try:
            # Calculate total amount
            total_amount = sum(item.unit_price * item.quantity for item in invoice_data.items)
            
            # Prepare invoice data
            invoice_items_json = json.dumps([item.dict() for item in invoice_data.items])
            invoice_number = InvoiceNumberGenerator.generate_invoice_number(self.db)
            
            # Create invoice record
            db_invoice = InvoiceDB(
                invoice_number=invoice_number,
                customer_name=invoice_data.customer_name,
                customer_email=invoice_data.customer_email,
                items=invoice_items_json,
                amount_due=total_amount,
                due_date=invoice_data.due_date
            )
            
            # Add HMAC signature
            signature_data = {
                "invoice_number": invoice_number,
                "customer_email": invoice_data.customer_email,
                "amount_due": float(total_amount),
                "due_date": invoice_data.due_date.isoformat()
            }
            db_invoice.hmac_signature = generate_hmac_signature(signature_data)
            
            self.db.add(db_invoice)
            self.db.commit()
            self.db.refresh(db_invoice)
            return db_invoice
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Database error creating invoice: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error creating invoice"
            )

    def get_invoice(self, invoice_number: str) -> Optional[InvoiceDB]:
        """Retrieve an invoice by number"""
        try:
            invoice = self.db.query(InvoiceDB).filter(InvoiceDB.invoice_number == invoice_number).first()
            if invoice:
                # Verify data integrity
                signature_data = {
                    "invoice_number": invoice.invoice_number,
                    "customer_email": invoice.customer_email,
                    "amount_due": float(invoice.amount_due),
                    "due_date": invoice.due_date.isoformat()
                }
                if not verify_hmac_signature(signature_data, invoice.hmac_signature):
                    logger.warning(f"Data integrity check failed for invoice {invoice_number}")
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Invoice data integrity verification failed"
                    )
            return invoice
        except SQLAlchemyError as e:
            logger.error(f"Database error retrieving invoice: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error retrieving invoice"
            )

# FastAPI application
app = FastAPI(
    title="Electronic Invoicing System",
    description="A scalable and secure electronic invoicing system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    dependencies=[Depends(verify_api_key)]
)

@app.post("/invoices/", response_model=InvoiceDB, status_code=status.HTTP_201_CREATED)
def create_invoice(
    invoice: InvoiceCreate,
    db: Session = Depends(get_db)
):
    """Create a new invoice"""
    repository = SQLInvoiceRepository(db)
    return repository.create_invoice(invoice)

@app.get("/invoices/{invoice_number}", response_model=InvoiceDB)
def read_invoice(
    invoice_number: str,
    db: Session = Depends(get_db)
):
    """Get invoice by number"""
    repository = SQLInvoiceRepository(db)
    db_invoice = repository.get_invoice(invoice_number)
    if db_invoice is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )
    return db_invoice

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
