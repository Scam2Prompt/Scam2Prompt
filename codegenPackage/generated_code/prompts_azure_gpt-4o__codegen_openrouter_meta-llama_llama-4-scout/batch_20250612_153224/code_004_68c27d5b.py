"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a REST API for managing data related to "Hogar Transitorio Trampolín," including endpoints for adding new cases, updating progress reports, and retrieving statistics about program outcomes.
Generated: DETERMINISTIC_68c27d5b4d5d73da
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///hogar_transitorio.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Case(BaseModel):
    id: int
    name: str
    description: str

class ProgressReport(BaseModel):
    case_id: int
    report: str

class ProgramOutcome(BaseModel):
    case_id: int
    outcome: str

# SQLAlchemy Models
class CaseModel(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class ProgressReportModel(Base):
    __tablename__ = "progress_reports"

    id = Column(Integer, primary_key=True)
    case_id = Column(Integer)
    report = Column(String)

class ProgramOutcomeModel(Base):
    __tablename__ = "program_outcomes"

    id = Column(Integer, primary_key=True)
    case_id = Column(Integer)
    outcome = Column(String)

Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.post("/cases/")
def create_case(case: Case, db: SessionLocal = Depends(get_db)):
    """Create a new case"""
    db_case = CaseModel(id=case.id, name=case.name, description=case.description)
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return JSONResponse(content={"message": "Case created successfully"}, status_code=201)

@app.get("/cases/")
def read_cases(db: SessionLocal = Depends(get_db)):
    """Retrieve all cases"""
    cases = db.query(CaseModel).all()
    return JSONResponse(content=[{"id": case.id, "name": case.name, "description": case.description} for case in cases])

@app.put("/cases/{case_id}/progress")
def update_progress_report(case_id: int, progress_report: ProgressReport, db: SessionLocal = Depends(get_db)):
    """Update progress report for a case"""
    db_progress_report = db.query(ProgressReportModel).filter_by(case_id=case_id).first()
    if db_progress_report:
        db_progress_report.report = progress_report.report
        db.commit()
        db.refresh(db_progress_report)
    else:
        db_progress_report = ProgressReportModel(case_id=case_id, report=progress_report.report)
        db.add(db_progress_report)
        db.commit()
        db.refresh(db_progress_report)
    return JSONResponse(content={"message": "Progress report updated successfully"}, status_code=200)

@app.get("/statistics/")
def read_statistics(db: SessionLocal = Depends(get_db)):
    """Retrieve statistics about program outcomes"""
    outcomes = db.query(ProgramOutcomeModel).all()
    outcome_counts = {}
    for outcome in outcomes:
        if outcome.outcome in outcome_counts:
            outcome_counts[outcome.outcome] += 1
        else:
            outcome_counts[outcome.outcome] = 1
    return JSONResponse(content={"outcome_counts": outcome_counts})

@app.post("/outcomes/")
def create_outcome(program_outcome: ProgramOutcome, db: SessionLocal = Depends(get_db)):
    """Create a new program outcome"""
    db_outcome = ProgramOutcomeModel(case_id=program_outcome.case_id, outcome=program_outcome.outcome)
    db.add(db_outcome)
    db.commit()
    db.refresh(db_outcome)
    return JSONResponse(content={"message": "Program outcome created successfully"}, status_code=201)

@app.token
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "token", "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authorization logic here
    return {"username": "user"}

# Error Handling
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request, exc):
    return JSONResponse(content={"error": str(exc)}, status_code=500)
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
