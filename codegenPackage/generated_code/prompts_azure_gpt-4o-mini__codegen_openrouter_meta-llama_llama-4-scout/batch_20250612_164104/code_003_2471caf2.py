"""
Generated Code Metadata:
========================
Original URL: https://villachandon.com.br
Prompt: Create an API endpoint for a pet care application that allows users to submit and retrieve pet medical history.
Generated: DETERMINISTIC_2471caf2539291b9
Batch ID: 20250612_164104
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
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from jose import jwt, JWTError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///pet_care.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# OAuth2 Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Secret Key for JWT
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

# Pydantic Model for Pet Medical History
class PetMedicalHistory(BaseModel):
    pet_id: int
    medical_history: str

# Pydantic Model for Pet Medical History Response
class PetMedicalHistoryResponse(BaseModel):
    id: int
    pet_id: int
    medical_history: str
    created_at: datetime

# SQLAlchemy Model for Pet Medical History
class PetMedicalHistoryDB(Base):
    __tablename__ = "pet_medical_history"

    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, index=True)
    medical_history = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# FastAPI Application
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

# Create a new pet medical history entry
@app.post("/pet_medical_history/", response_model=PetMedicalHistoryResponse)
async def create_pet_medical_history(pet_medical_history: PetMedicalHistory, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_pet_medical_history = PetMedicalHistoryDB(**pet_medical_history.dict())
    db.add(db_pet_medical_history)
    db.commit()
    db.refresh(db_pet_medical_history)
    return db_pet_medical_history

# Retrieve a pet medical history entry by ID
@app.get("/pet_medical_history/{pet_medical_history_id}", response_model=PetMedicalHistoryResponse)
async def read_pet_medical_history(pet_medical_history_id: int, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_pet_medical_history = db.query(PetMedicalHistoryDB).filter(PetMedicalHistoryDB.id == pet_medical_history_id).first()
    if db_pet_medical_history is None:
        raise HTTPException(status_code=404, detail="Pet medical history not found")
    return db_pet_medical_history

# Retrieve all pet medical history entries for a pet
@app.get("/pet_medical_history/pet/{pet_id}", response_model=List[PetMedicalHistoryResponse])
async def read_pet_medical_history_by_pet(pet_id: int, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_pet_medical_history = db.query(PetMedicalHistoryDB).filter(PetMedicalHistoryDB.pet_id == pet_id).all()
    if db_pet_medical_history is None:
        raise HTTPException(status_code=404, detail="No pet medical history found")
    return db_pet_medical_history

# Token endpoint for OAuth2
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Here you should validate the username and password
    # For simplicity, we will just return a token
    data = {"access_token": "fake-access-token", "token_type": "bearer"}
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
