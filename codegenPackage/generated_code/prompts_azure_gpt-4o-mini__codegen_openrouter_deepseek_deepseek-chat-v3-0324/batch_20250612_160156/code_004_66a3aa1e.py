"""
Generated Code Metadata:
========================
Original URL: https://supremeprofund.com
Prompt: Illustrate how to implement a referral program in a web application, inspired by the referral income model used by SupremeProFund.
Generated: DETERMINISTIC_66a3aa1e2801b52e
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py
import uuid
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from passlib.context import CryptContext

# Database setup
DATABASE_URL = "sqlite:///./referral_program.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    referral_code = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    referrals = relationship("Referral", back_populates="referrer")

class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, index=True)
    referrer_id = Column(Integer, ForeignKey("users.id"))
    referee_id = Column(Integer, unique=True)  # Would be FK to users.id in production
    referee_email = Column(String)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    referrer = relationship("User", back_populates="referrals")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    referral_code: Optional[str] = None

    @validator('password')
    def password_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    referral_code: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ReferralResponse(BaseModel):
    id: int
    referrer_id: int
    referee_email: str
    is_verified: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ReferralStatsResponse(BaseModel):
    total_referrals: int
    verified_referrals: int
    pending_referrals: int
    referral_income: float

# Helper functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    referral_code = str(uuid.uuid4())[:8]
    
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        referral_code=referral_code
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # If user was referred, create referral record
    if user.referral_code:
        referrer = db.query(User).filter(User.referral_code == user.referral_code).first()
        if referrer:
            create_referral(db, referrer.id, db_user.id, db_user.email)
    
    return db_user

def create_referral(db: Session, referrer_id: int, referee_id: int, referee_email: str):
    db_referral = Referral(
        referrer_id=referrer_id,
        referee_id=referee_id,
        referee_email=referee_email
    )
    db.add(db_referral)
    db.commit()
    db.refresh(db_referral)
    return db_referral

def verify_referral(db: Session, referral_id: int):
    referral = db.query(Referral).filter(Referral.id == referral_id).first()
    if not referral:
        return None
    
    referral.is_verified = True
    db.commit()
    db.refresh(referral)
    return referral

def get_referral_stats(db: Session, user_id: int):
    referrals = db.query(Referral).filter(Referral.referrer_id == user_id).all()
    
    total = len(referrals)
    verified = len([r for r in referrals if r.is_verified])
    pending = total - verified
    
    # Simple income calculation - $10 per verified referral
    income = verified * 10.0
    
    return {
        "total_referrals": total,
        "verified_referrals": verified,
        "pending_referrals": pending,
        "referral_income": income
    }

# FastAPI app
app = FastAPI()

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db, user=user)

@app.get("/users/{user_id}/referrals", response_model=List[ReferralResponse])
def get_user_referrals(user_id: int, db: Session = Depends(get_db)):
    referrals = db.query(Referral).filter(Referral.referrer_id == user_id).all()
    return referrals

@app.post("/referrals/{referral_id}/verify", response_model=ReferralResponse)
def verify_user_referral(referral_id: int, db: Session = Depends(get_db)):
    referral = verify_referral(db, referral_id)
    if not referral:
        raise HTTPException(status_code=404, detail="Referral not found")
    return referral

@app.get("/users/{user_id}/referral-stats", response_model=ReferralStatsResponse)
def get_user_referral_stats(user_id: int, db: Session = Depends(get_db)):
    stats = get_referral_stats(db, user_id)
    return stats

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```
