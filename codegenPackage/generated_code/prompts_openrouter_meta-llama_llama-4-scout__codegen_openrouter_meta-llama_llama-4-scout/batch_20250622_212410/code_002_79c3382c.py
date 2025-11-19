"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Generate a RESTful API for tracking youth participation in community programs, using the ICYD.org vision as a guiding framework.
Generated: DETERMINISTIC_79c3382c5207f31d
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**youth_participation_api.py**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# ICYD.org Vision: "Unlocking the potential of young people"
# API Description: Tracking youth participation in community programs

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///youth_participation.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define the YouthParticipation model
class YouthParticipation(Base):
    __tablename__ = "youth_participation"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    program_name = Column(String)
    participation_date = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# FastAPI Application
app = FastAPI()

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class YouthParticipationRequest(BaseModel):
    name: str
    program_name: str
    participation_date: str

class YouthParticipationResponse(BaseModel):
    id: int
    name: str
    program_name: str
    participation_date: str

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Authentication
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    # For demonstration purposes, assume the token is valid
    return token

# API Endpoints
@app.post("/youth_participation/")
async def create_youth_participation(
    youth_participation: YouthParticipationRequest,
    db: SessionLocal = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        new_participation = YouthParticipation(
            name=youth_participation.name,
            program_name=youth_participation.program_name,
            participation_date=youth_participation.participation_date
        )
        db.add(new_participation)
        db.commit()
        db.refresh(new_participation)
        return {"id": new_participation.id, **youth_participation.dict()}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/youth_participation/")
async def read_youth_participation(
    db: SessionLocal = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        participation = db.query(YouthParticipation).all()
        return [{"id": p.id, "name": p.name, "program_name": p.program_name, "participation_date": p.participation_date} for p in participation]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/youth_participation/{participation_id}")
async def read_youth_participation_by_id(
    participation_id: int,
    db: SessionLocal = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        participation = db.query(YouthParticipation).filter(YouthParticipation.id == participation_id).first()
        if participation is None:
            raise HTTPException(status_code=404, detail="Participation not found")
        return {"id": participation.id, "name": participation.name, "program_name": participation.program_name, "participation_date": participation.participation_date}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/youth_participation/{participation_id}")
async def update_youth_participation(
    participation_id: int,
    youth_participation: YouthParticipationRequest,
    db: SessionLocal = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        existing_participation = db.query(YouthParticipation).filter(YouthParticipation.id == participation_id).first()
        if existing_participation is None:
            raise HTTPException(status_code=404, detail="Participation not found")
        existing_participation.name = youth_participation.name
        existing_participation.program_name = youth_participation.program_name
        existing_participation.participation_date = youth_participation.participation_date
        db.commit()
        db.refresh(existing_participation)
        return {"id": existing_participation.id, **youth_participation.dict()}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/youth_participation/{participation_id}")
async def delete_youth_participation(
    participation_id: int,
    db: SessionLocal = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        participation = db.query(YouthParticipation).filter(YouthParticipation.id == participation_id).first()
        if participation is None:
            raise HTTPException(status_code=404, detail="Participation not found")
        db.delete(participation)
        db.commit()
        return {"message": "Participation deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# Token Endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    # For demonstration purposes, assume the credentials are valid
    return {"access_token": "example_token", "token_type": "bearer"}
```
**main.py**
```python
import uvicorn
from youth_participation_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
