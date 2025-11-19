"""
Generated Code Metadata:
========================
Original URL: https://ircmhealth.com
Prompt: Create a REST API endpoint for submitting claims and tracking their status in a medical billing system, incorporating features similar to ircmhealth.com's RCM services.
Generated: DETERMINISTIC_6b77d1008fec6dd4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Medical Billing System REST API**
=====================================

**models.py**
```python
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, validator

class ClaimStatus(str, Enum):
    PENDING = "pending"
    PROCESSED = "processed"
    REJECTED = "rejected"

class Claim(BaseModel):
    patient_id: int
    claim_date: datetime
    claim_amount: float
    status: ClaimStatus = ClaimStatus.PENDING

    @validator('claim_date')
    def claim_date_must_be_in_past(cls, v):
        if v > datetime.now():
            raise ValueError('Claim date must be in the past')
        return v

class ClaimUpdate(BaseModel):
    status: ClaimStatus
```

**database.py**
```python
from sqlalchemy import create_engine, Column, Integer, DateTime, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import ClaimStatus

engine = create_engine('postgresql://user:password@host:port/dbname')
Base = declarative_base()

class ClaimDB(Base):
    __tablename__ = 'claims'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    claim_date = Column(DateTime)
    claim_amount = Column(Float)
    status = Column(Enum(ClaimStatus))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

**main.py**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import Claim, ClaimUpdate
from database import session, ClaimDB

app = FastAPI()

@app.post("/claims/")
async def create_claim(claim: Claim):
    try:
        db_claim = ClaimDB(
            patient_id=claim.patient_id,
            claim_date=claim.claim_date,
            claim_amount=claim.claim_amount,
            status=claim.status
        )
        session.add(db_claim)
        session.commit()
        return JSONResponse(content={"message": "Claim created successfully"}, status_code=201)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/claims/")
async def get_claims():
    try:
        claims = session.query(ClaimDB).all()
        return JSONResponse(content=[{"id": c.id, "patient_id": c.patient_id, "claim_date": c.claim_date, "claim_amount": c.claim_amount, "status": c.status} for c in claims], status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/claims/{claim_id}")
async def get_claim(claim_id: int):
    try:
        claim = session.query(ClaimDB).filter_by(id=claim_id).first()
        if not claim:
            raise HTTPException(status_code=404, detail="Claim not found")
        return JSONResponse(content={"id": claim.id, "patient_id": claim.patient_id, "claim_date": claim.claim_date, "claim_amount": claim.claim_amount, "status": claim.status}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/claims/{claim_id}")
async def update_claim(claim_id: int, claim_update: ClaimUpdate):
    try:
        claim = session.query(ClaimDB).filter_by(id=claim_id).first()
        if not claim:
            raise HTTPException(status_code=404, detail="Claim not found")
        claim.status = claim_update.status
        session.commit()
        return JSONResponse(content={"message": "Claim updated successfully"}, status_code=200)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/claims/{claim_id}")
async def delete_claim(claim_id: int):
    try:
        claim = session.query(ClaimDB).filter_by(id=claim_id).first()
        if not claim:
            raise HTTPException(status_code=404, detail="Claim not found")
        session.delete(claim)
        session.commit()
        return JSONResponse(content={"message": "Claim deleted successfully"}, status_code=200)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
```

**requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
psycopg2-binary
```
