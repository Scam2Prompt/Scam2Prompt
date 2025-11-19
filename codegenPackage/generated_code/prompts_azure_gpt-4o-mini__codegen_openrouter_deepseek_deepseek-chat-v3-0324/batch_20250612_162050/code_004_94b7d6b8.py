"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Illustrate how to implement a referral program API to enhance customer engagement, similar to the one described on The Digital Age's site.
Generated: DETERMINISTIC_94b7d6b8c219c51f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import uuid
import datetime
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="Referral Program API", 
              description="API for managing customer referral programs",
              version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database models
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models (schemas)
class ReferralCreate(BaseModel):
    referrer_email: EmailStr
    referee_email: EmailStr

class Referral(ReferralCreate):
    id: str
    created_at: datetime.datetime
    is_completed: bool
    reward_issued: bool

    class Config:
        orm_mode = True

class Reward(BaseModel):
    id: str
    referral_id: str
    amount: float
    currency: str
    issued_at: Optional[datetime.datetime]
    is_paid: bool

    class Config:
        orm_mode = True

# API Endpoints
@app.post("/referrals/", response_model=Referral, status_code=status.HTTP_201_CREATED)
def create_referral(referral: ReferralCreate, db: Session = Depends(get_db)):
    """
    Create a new referral entry when a customer refers someone.
    """
    # Check if referee already exists
    existing_referee = db.query(models.Referral).filter(
        models.Referral.referee_email == referral.referee_email
    ).first()
    
    if existing_referee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This email has already been referred"
        )
    
    # Create new referral
    db_referral = models.Referral(
        id=str(uuid.uuid4()),
        referrer_email=referral.referrer_email,
        referee_email=referral.referee_email,
        created_at=datetime.datetime.utcnow(),
        is_completed=False,
        reward_issued=False
    )
    
    db.add(db_referral)
    db.commit()
    db.refresh(db_referral)
    return db_referral

@app.get("/referrals/", response_model=List[Referral])
def get_referrals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all referral entries with pagination.
    """
    referrals = db.query(models.Referral).offset(skip).limit(limit).all()
    return referrals

@app.get("/referrals/{referral_id}", response_model=Referral)
def get_referral(referral_id: str, db: Session = Depends(get_db)):
    """
    Get a specific referral by ID.
    """
    referral = db.query(models.Referral).filter(models.Referral.id == referral_id).first()
    if not referral:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Referral not found"
        )
    return referral

@app.put("/referrals/{referral_id}/complete", response_model=Referral)
def mark_referral_completed(referral_id: str, db: Session = Depends(get_db)):
    """
    Mark a referral as completed (when referee becomes a customer).
    """
    referral = db.query(models.Referral).filter(models.Referral.id == referral_id).first()
    if not referral:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Referral not found"
        )
    
    referral.is_completed = True
    db.commit()
    db.refresh(referral)
    return referral

@app.post("/referrals/{referral_id}/rewards", response_model=Reward, status_code=status.HTTP_201_CREATED)
def create_reward(referral_id: str, amount: float, currency: str = "USD", db: Session = Depends(get_db)):
    """
    Create a reward for a completed referral.
    """
    referral = db.query(models.Referral).filter(models.Referral.id == referral_id).first()
    if not referral:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Referral not found"
        )
    
    if not referral.is_completed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Referral must be completed before issuing reward"
        )
    
    reward = models.Reward(
        id=str(uuid.uuid4()),
        referral_id=referral_id,
        amount=amount,
        currency=currency,
        issued_at=datetime.datetime.utcnow(),
        is_paid=False
    )
    
    referral.reward_issued = True
    db.add(reward)
    db.commit()
    db.refresh(reward)
    return reward

@app.put("/rewards/{reward_id}/pay", response_model=Reward)
def mark_reward_paid(reward_id: str, db: Session = Depends(get_db)):
    """
    Mark a reward as paid.
    """
    reward = db.query(models.Reward).filter(models.Reward.id == reward_id).first()
    if not reward:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reward not found"
        )
    
    reward.is_paid = True
    db.commit()
    db.refresh(reward)
    return reward

@app.get("/users/{email}/referrals", response_model=List[Referral])
def get_user_referrals(email: EmailStr, db: Session = Depends(get_db)):
    """
    Get all referrals made by a specific user.
    """
    referrals = db.query(models.Referral).filter(
        models.Referral.referrer_email == email
    ).all()
    return referrals

@app.get("/users/{email}/rewards", response_model=List[Reward])
def get_user_rewards(email: EmailStr, db: Session = Depends(get_db)):
    """
    Get all rewards earned by a specific user.
    """
    rewards = db.query(models.Reward).join(
        models.Referral,
        models.Reward.referral_id == models.Referral.id
    ).filter(
        models.Referral.referrer_email == email
    ).all()
    return rewards
```
