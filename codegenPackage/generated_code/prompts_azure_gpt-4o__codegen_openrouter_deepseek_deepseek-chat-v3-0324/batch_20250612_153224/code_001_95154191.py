"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Recommend an API or library to create a product catalog for fishing reels, including features like "Old School Brass 1 & 2" and "Salmon Wide," as described on Emanuelson Reels.
Generated: DETERMINISTIC_951541910d4ba33c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Catalog API Implementation for Fishing Reels

This module provides a clean, production-ready implementation for managing a product catalog
of fishing reels with features like "Old School Brass 1 & 2" and "Salmon Wide".

Uses FastAPI for the REST API and SQLAlchemy for database operations.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./fishing_reels.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class ReelModel(Base):
    """SQLAlchemy model for fishing reel products"""
    __tablename__ = "reels"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    model = Column(String(50))
    description = Column(Text)
    price = Column(Float)
    features = Column(Text)  # JSON string of features
    in_stock = Column(Integer)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models for request/response
class ReelFeatures(BaseModel):
    """Features of a fishing reel"""
    material: str
    gear_ratio: Optional[str] = None
    ball_bearings: Optional[int] = None
    special_features: List[str] = []

class ReelCreate(BaseModel):
    """Request model for creating a reel"""
    name: str
    model: str
    description: Optional[str] = None
    price: float
    features: ReelFeatures
    in_stock: int

class ReelResponse(BaseModel):
    """Response model for reel data"""
    id: int
    name: str
    model: str
    description: Optional[str] = None
    price: float
    features: ReelFeatures
    in_stock: int

# FastAPI app
app = FastAPI(title="Fishing Reels Catalog API", version="1.0.0")

@app.post("/reels/", response_model=ReelResponse, status_code=status.HTTP_201_CREATED)
def create_reel(reel: ReelCreate):
    """Create a new fishing reel product"""
    db = SessionLocal()
    try:
        db_reel = ReelModel(
            name=reel.name,
            model=reel.model,
            description=reel.description,
            price=reel.price,
            features=reel.features.json(),
            in_stock=reel.in_stock
        )
        db.add(db_reel)
        db.commit()
        db.refresh(db_reel)
        return db_reel
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    finally:
        db.close()

@app.get("/reels/", response_model=List[ReelResponse])
def get_reels(skip: int = 0, limit: int = 100):
    """Get list of fishing reel products"""
    db = SessionLocal()
    try:
        reels = db.query(ReelModel).offset(skip).limit(limit).all()
        return reels
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    finally:
        db.close()

@app.get("/reels/{reel_id}", response_model=ReelResponse)
def get_reel(reel_id: int):
    """Get a specific fishing reel by ID"""
    db = SessionLocal()
    try:
        reel = db.query(ReelModel).filter
