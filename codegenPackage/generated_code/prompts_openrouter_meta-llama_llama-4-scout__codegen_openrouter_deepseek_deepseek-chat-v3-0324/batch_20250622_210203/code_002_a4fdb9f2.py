"""
Generated Code Metadata:
========================
Original URL: https://icrossingappxyz.com
Prompt: Generate a Python script to automate the process of registering users and verifying their identities through a QR code scan, as described in the "Identitas Kependudukan Digital" app.
Generated: DETERMINISTIC_a4fdb9f2c54355f8
Batch ID: 20250622_210203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
import qrcode
import json
import hashlib
from datetime import datetime
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, EmailStr, validator
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./digital_identity.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# FastAPI app
app = FastAPI(title="Digital Identity Registration API")

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    nik = Column(String(16), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    is_verified = Column(Boolean, default=False)
    verification_token = Column(String(36), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    nik: str = Field(..., min_length=16, max_length=16)
    password: str = Field(..., min_length=8)

    @validator('nik')
    def validate_nik(cls, v):
        if not v.isdigit():
            raise ValueError('NIK must contain only digits')
        return v

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    nik: str
    is_verified: bool
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class QRCodeData(BaseModel):
    verification_token: str

# Utility functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password: str) -> str:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + key.hex()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    salt = bytes.fromhex(hashed_password[:64])
    key = bytes.fromhex(hashed_password[64:])
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        plain_password.encode('utf-8'),
        salt,
        100000
    )
    return new_key == key

def generate_verification_token() -> str:
    return str(uuid.uuid4())

def generate_qr_code_data(token: str) -> bytes:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(token)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# API Endpoints
@app.post("/register/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Check if NIK already exists
    db_nik = db.query(User).filter(User.nik == user.nik).first()
    if db_nik:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NIK already registered"
        )
    
    # Create new user
    verification_token = generate_verification_token()
    hashed_password = hash_password(user.password)
    
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        nik=user.nik,
        hashed_password=hashed_password,
        verification_token=verification_token
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@app.get("/generate-qr/{user_id}", status_code=status.HTTP_200_OK)
def generate_qr_code(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if db_user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already verified"
        )
    
    qr_img = generate_qr_code_data(db_user.verification_token)
    return {"qr_code": qr_img}

@app.post("/verify/", status_code=status.HTTP_200_OK)
def verify_user(qr_data: QRCodeData, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.verification_token == qr_data.verification_token).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid verification token"
        )
    
    if db_user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already verified"
        )
    
    db_user.is_verified = True
    db.commit()
    
    return {"message": "User verified successfully"}

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

# Database initialization
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
