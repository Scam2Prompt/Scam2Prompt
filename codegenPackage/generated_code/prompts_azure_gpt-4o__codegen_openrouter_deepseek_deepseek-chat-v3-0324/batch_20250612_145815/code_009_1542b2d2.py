"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: Generate code to implement a referral program for a subscription-based platform, including tracking and rewards, inspired by Rentsy.
Generated: DETERMINISTIC_1542b2d2ef9c5b76
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, EmailStr, validator
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.sql import func

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./referral.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class ReferralStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    EXPIRED = "expired"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    referral_code = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    
    referrals = relationship("Referral", back_populates="referrer")

class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, index=True)
    referrer_id = Column(Integer, ForeignKey("users.id"))
    referee_email = Column(String, index=True)
    status = Column(String, default=ReferralStatus.PENDING)
    created_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime, nullable=True)
    
    referrer = relationship("User", back_populates="referrals")

# Pydantic models
class UserCreate(BaseModel):
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    referral_code: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ReferralCreate(BaseModel):
    referee_email: EmailStr

class ReferralResponse(BaseModel):
    id: int
    referrer_id: int
    referee_email: str
    status: ReferralStatus
    created_at: datetime
    completed_at: Optional[datetime]

    class Config:
        orm_mode = True

class RewardResponse(BaseModel):
    message: str
    reward_amount: float
    total_referrals: int

# Initialize database
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper functions
def generate_referral_code() -> str:
    return str(uuid.uuid4())[:8].upper()

def check_referral_expiry(referral: Referral) -> bool:
    expiry_period = timedelta(days=30)
    return datetime.now() - referral.created_at > expiry_period

# API Endpoints
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    referral_code = generate_referral_code()
    db_user = User(email=user.email, referral_code=referral_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{referrer_id}/referrals/", response_model=ReferralResponse, status_code=status.HTTP_201_CREATED)
def create_referral(
    referrer_id: int, 
    referral: ReferralCreate, 
    db: Session = Depends(get_db)
):
    # Check if referrer exists
    referrer = db.query(User).filter(User.id == referrer_id).first()
    if not referrer:
        raise HTTPException(status_code=404, detail="Referrer not found")
    
    # Check if referee email is already referred
    existing_referral = db.query(Referral).filter(
        Referral.referee_email == referral.referee_email
    ).first()
    if existing_referral:
        raise HTTPException(status_code=400, detail="Email already referred")
    
    # Create new referral
    db_referral = Referral(
        referrer_id=referrer_id,
        referee_email=referral.referee_email
    )
    db.add(db_referral)
    db.commit()
    db.refresh(db_referral)
    return db_referral

@app.post("/referrals/{referral_id}/complete", response_model=ReferralResponse)
def complete_referral(referral_id: int, db: Session = Depends(get_db)):
    referral = db.query(Referral).filter(Referral.id == referral_id).first()
    if not referral:
        raise HTTPException(status_code=404, detail="Referral not found")
    
    if referral.status == ReferralStatus.COMPLETED:
        raise HTTPException(status_code=400, detail="Referral already completed")
    
    if check_referral_expiry(referral):
        referral.status = ReferralStatus.EXPIRED
        db.commit()
        raise HTTPException(status_code=400, detail="Referral has expired")
    
    referral.status = ReferralStatus.COMPLETED
    referral.completed_at = datetime.now()
    db.commit()
    db.refresh(referral)
    return referral

@app.get("/users/{user_id}/referrals", response_model=List[ReferralResponse])
def get_user_referrals(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.referrals

@app.get("/users/{user_id}/rewards", response_model=RewardResponse)
def get_user_rewards(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    completed_referrals = db.query(Referral).filter(
        Referral.referrer_id == user_id,
        Referral.status == ReferralStatus.COMPLETED
    ).count()
    
    reward_amount = completed_referrals * 10.0  # $10 per completed referral
    
    return RewardResponse(
        message=f"You have earned ${reward_amount:.2f} from referrals",
        reward_amount=reward_amount,
        total_referrals=completed_referrals
    )
```
