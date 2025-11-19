"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Suggest tools or frameworks for implementing a scheduling system for medical examinations, including tests for confined spaces and working at heights, as offered by Medicid IPS.
Generated: DETERMINISTIC_7e7c441fc0f546d6
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import uuid
from enum import Enum
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from sqlalchemy import create_engine, Column, String, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./medicid.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums for examination types
class ExaminationType(str, Enum):
    GENERAL = "general"
    CONFINED_SPACES = "confined_spaces"
    WORKING_AT_HEIGHTS = "working_at_heights"

# Database models
class Examination(Base):
    __tablename__ = "examinations"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = Column(String, nullable=False)
    examination_type = Column(SQLEnum(ExaminationType), nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    duration_minutes = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    notes = Column(String, nullable=True)

# Pydantic models
class ExaminationCreate(BaseModel):
    patient_id: str = Field(..., min_length=1)
    examination_type: ExaminationType
    scheduled_time: datetime
    duration_minutes: int = Field(..., gt=0)
    notes: Optional[str] = None

    @validator('scheduled_time')
    def validate_scheduled_time(cls, v):
        if v < datetime.now():
            raise ValueError("Scheduled time must be in the future")
        return v

class ExaminationResponse(ExaminationCreate):
    id: str
    completed: bool

# FastAPI app
app = FastAPI(title="Medicid IPS Scheduling System")

# Create tables
Base.metadata.create_all(bind=engine)

# Helper function to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints
@app.post("/examinations/", response_model=ExaminationResponse, status_code=status.HTTP_201_CREATED)
def create_examination(examination: ExaminationCreate, db: SessionLocal = Depends(get_db)):
    """
    Schedule a new medical examination.
    """
    db_examination = Examination(**examination.dict())
    db.add(db_examination)
    db.commit()
    db.refresh(db_examination)
    return db_examination

@app.get("/examinations/", response_model=List[ExaminationResponse])
def list_examinations(limit: int = 100, db: SessionLocal = Depends(get_db)):
    """
    List all scheduled examinations.
    """
    return db.query(Examination).limit(limit).all()

@app.get("/examinations/{examination_id}", response_model=ExaminationResponse)
def get_examination(examination_id: str, db: SessionLocal = Depends(get_db)):
    """
    Get details of a specific examination.
    """
    examination = db.query(Examination).filter(Examination.id == examination_id).first()
    if not examination:
        raise HTTPException(status_code=404, detail="Examination not found")
    return examination

@app.put("/examinations/{examination_id}/complete", response_model=ExaminationResponse)
def mark_completed(examination_id: str, db: SessionLocal = Depends(get_db)):
    """
    Mark an examination as completed.
    """
    examination = db.query(Examination).filter(Examination.id == examination_id).first()
    if not examination:
        raise HTTPException(status_code=404, detail="Examination not found")
    examination.completed = True
    db.commit()
    db.refresh(examination)
    return examination

@app.get("/examinations/type/{examination_type}", response_model=List[ExaminationResponse])
def get_examinations_by_type(examination_type: ExaminationType, db: SessionLocal = Depends(get_db)):
    """
    Get examinations filtered by type.
    """
    return db.query(Examination).filter(Examination.examination_type == examination_type).all()

# Additional suggested tools/frameworks would be integrated here:
# - Celery for background tasks
# - Redis for caching
# - React/Vue for frontend
# - Docker for containerization
# - pytest for testing
```
