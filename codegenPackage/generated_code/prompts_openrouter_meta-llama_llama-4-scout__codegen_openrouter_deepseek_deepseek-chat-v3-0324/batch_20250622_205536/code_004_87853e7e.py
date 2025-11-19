"""
Generated Code Metadata:
========================
Original URL: https://sand.claims
Prompt: Design a basic database schema for storing information about claims, including fields for claimant details, claim status, and dates, which could be managed through a site like sand.claims.
Generated: DETERMINISTIC_87853e7ea4b38553
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for a claims management system

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Claimant(Base):
    """Stores claimant personal information"""
    __tablename__ = 'claimants'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(200))
    city = Column(String(50))
    state = Column(String(50))
    postal_code = Column(String(20))
    country = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    claims = relationship("Claim", back_populates="claimant")

class Claim(Base):
    """Stores claim information"""
    __tablename__ = 'claims'
    
    id = Column(Integer, primary_key=True)
    claimant_id = Column(Integer, ForeignKey('claimants.id'), nullable=False)
    claim_number = Column(String(50), unique=True, nullable=False)
    description = Column(String(500), nullable=False)
    status = Column(Enum('draft', 'submitted', 'in_review', 'approved', 'rejected', 
                         'paid', 'closed', name='claim_status'), 
                    default='draft', nullable=False)
    amount_claimed = Column(db.Numeric(10, 2))
    amount_approved = Column(db.Numeric(10, 2))
    incident_date = Column(DateTime)
    submission_date = Column(DateTime)
    review_date = Column(DateTime)
    decision_date = Column(DateTime)
    payment_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    claimant = relationship("Claimant", back_populates="claims")
    documents = relationship("Document", back_populates="claim")

class Document(Base):
    """Stores documents related to claims"""
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'), nullable=False)
    document_type = Column(String(50), nullable=False)
    file_name = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    file_size = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    claim = relationship("Claim", back_populates="documents")

def create_database(engine):
    """Create all tables in the database"""
    Base.metadata.create_all(engine)
```
