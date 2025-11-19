"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Develop an API for managing grants programs, including endpoints for creating, reading, updating, and deleting program data."
Generated: DETERMINISTIC_1c55584910473610
Batch ID: 20250622_212142
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
from fastapi.requests import Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Security
security = HTTPBasic()

# Database Connection
SQLALCHEMY_DATABASE_URL = "sqlite:///grants.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class GrantProgram(BaseModel):
    id: int | None
    name: str
    description: str
    start_date: str
    end_date: str

# SQLAlchemy Models
class GrantProgramDB(Base):
    __tablename__ = "grant_programs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    start_date = Column(String)
    end_date = Column(String)

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

# Authentication
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return credentials.username

# Endpoints
@app.post("/grant_programs/", response_model=GrantProgram)
async def create_grant_program(grant_program: GrantProgram, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        db_grant_program = GrantProgramDB(**grant_program.dict())
        db.add(db_grant_program)
        db.commit()
        db.refresh(db_grant_program)
        return db_grant_program
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/grant_programs/", response_model=List[GrantProgram])
async def read_grant_programs(db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        grant_programs = db.query(GrantProgramDB).all()
        return [GrantProgram(id=gp.id, name=gp.name, description=gp.description, start_date=gp.start_date, end_date=gp.end_date) for gp in grant_programs]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/grant_programs/{grant_program_id}", response_model=GrantProgram)
async def read_grant_program(grant_program_id: int, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        grant_program = db.query(GrantProgramDB).filter(GrantProgramDB.id == grant_program_id).first()
        if grant_program is None:
            raise HTTPException(status_code=404, detail="Grant program not found")
        return GrantProgram(id=grant_program.id, name=grant_program.name, description=grant_program.description, start_date=grant_program.start_date, end_date=grant_program.end_date)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/grant_programs/{grant_program_id}", response_model=GrantProgram)
async def update_grant_program(grant_program_id: int, grant_program: GrantProgram, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        db_grant_program = db.query(GrantProgramDB).filter(GrantProgramDB.id == grant_program_id).first()
        if db_grant_program is None:
            raise HTTPException(status_code=404, detail="Grant program not found")
        grant_program_dict = grant_program.dict(exclude_unset=True)
        for key, value in grant_program_dict.items():
            setattr(db_grant_program, key, value)
        db.commit()
        db.refresh(db_grant_program)
        return db_grant_program
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/grant_programs/{grant_program_id}")
async def delete_grant_program(grant_program_id: int, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        grant_program = db.query(GrantProgramDB).filter(GrantProgramDB.id == grant_program_id).first()
        if grant_program is None:
            raise HTTPException(status_code=404, detail="Grant program not found")
        db.delete(grant_program)
        db.commit()
        return JSONResponse(content={"message": "Grant program deleted successfully"}, status_code=200)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
```
