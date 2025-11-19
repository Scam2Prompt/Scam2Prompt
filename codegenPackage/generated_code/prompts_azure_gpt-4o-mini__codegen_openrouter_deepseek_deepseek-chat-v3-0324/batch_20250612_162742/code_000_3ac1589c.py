"""
Generated Code Metadata:
========================
Original URL: https://loyal.credit
Prompt: What are the key features of the loyalty program offered by Loyal Credit, and how can I implement a similar API for managing customer rewards?
Generated: DETERMINISTIC_3ac1589cbbdc4ba7
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Loyalty Program API Implementation

```python
"""
Loyalty Program API for managing customer rewards
Key features:
- Points accrual based on purchases
- Tiered membership levels
- Reward redemption
- Expiration policies
- Account management
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, List
from enum import Enum
import uuid
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, validator
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./loyalty_program.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class MembershipTier(str, Enum):
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"

class CustomerDB(Base):
    __tablename__ = "customers"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    current_points = Column(Float, default=0.0)
    lifetime_points = Column(Float, default=0.0)
    tier = Column(SQLEnum(MembershipTier), default=MembershipTier.BRONZE)
    join_date = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)

class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)
    customer_id = Column(String, index=True)
    amount = Column(Float)
    points_earned = Column(Float)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    description = Column(String)

class RewardDB(Base):
    __tablename__ = "rewards"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    point_cost = Column(Float)
    description = Column(String)
    is_active = Column(Integer, default=1)

class RedemptionDB(Base):
    __tablename__ = "redemptions"

    id = Column(String, primary_key=True, index=True)
    customer_id = Column(String, index=True)
    reward_id = Column(String)
    redemption_date = Column(DateTime, default=datetime.utcnow)
    points_used = Column(Float)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerResponse(BaseModel):
    id: str
    name: str
    email: str
    current_points: float
    lifetime_points: float
    tier: MembershipTier
    join_date: datetime
    last_activity: datetime

class Transaction(BaseModel):
    customer_id: str
    amount: float
    description: Optional[str] = None

class Reward(BaseModel):
    name: str
    point_cost: float
    description: Optional[str] = None

class RedemptionRequest(BaseModel):
    customer_id: str
    reward_id: str

# App setup
app = FastAPI(title="Loyalty Program API", version="1.0.0")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper functions
def calculate_points(amount: float, tier: MembershipTier) -> float:
    """Calculate points earned based on purchase amount and membership tier"""
    multiplier = {
        MembershipTier.BRONZE: 1.0,
        MembershipTier.SILVER: 1.1,
        MembershipTier.GOLD: 1.25,
        MembershipTier.PLATINUM: 1.5
    }
    return amount * multiplier[tier]

def determine_tier(lifetime_points: float) -> MembershipTier:
    """Determine customer tier based on lifetime points"""
    if lifetime_points >= 10000:
        return MembershipTier.PLATINUM
    elif lifetime_points >= 5000:
        return MembershipTier.GOLD
    elif lifetime_points >= 1000:
        return MembershipTier.SILVER
    return MembershipTier.BRONZE

# API Endpoints
@app.post("/customers/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """Create a new customer account"""
    db_customer = CustomerDB(
        id=str(uuid.uuid4()),
        name=customer.name,
        email=customer.email
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    """Get customer details"""
    customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.post("/transactions/", status_code=status.HTTP_201_CREATED)
def record_transaction(transaction: Transaction, db: Session = Depends(get_db)):
    """Record a transaction and update customer points"""
    customer = db.query(CustomerDB).filter(CustomerDB.id == transaction.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    points_earned = calculate_points(transaction.amount, customer.tier)
    
    # Update customer points
    customer.current_points += points_earned
    customer.lifetime_points += points_earned
    customer.last_activity = datetime.utcnow()
    
    # Check for tier upgrade
    new_tier = determine_tier(customer.lifetime_points)
    if new_tier != customer.tier:
        customer.tier = new_tier
    
    # Record transaction
    db_transaction = TransactionDB(
        id=str(uuid.uuid4()),
        customer_id=transaction.customer_id,
        amount=transaction.amount,
        points_earned=points_earned,
        description=transaction.description
    )
    
    db.add(db_transaction)
    db.commit()
    
    return {"message": "Transaction recorded successfully", "points_earned": points_earned}

@app.post("/rewards/", status_code=status.HTTP_201_CREATED)
def create_reward(reward: Reward, db: Session = Depends(get_db)):
    """Create a new reward option"""
    db_reward = RewardDB(
        id=str(uuid.uuid4()),
        name=reward.name,
        point_cost=reward.point_cost,
        description=reward.description
    )
    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)
    return {"message": "Reward created successfully", "reward_id": db_reward.id}

@app.post("/redeem/", status_code=status.HTTP_200_OK)
def redeem_reward(redemption: RedemptionRequest, db: Session = Depends(get_db)):
    """Redeem a reward for a customer"""
    customer = db.query(CustomerDB).filter(CustomerDB.id == redemption.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    reward = db.query(RewardDB).filter(RewardDB.id == redemption.reward_id).first()
    if not reward or not reward.is_active:
        raise HTTPException(status_code=404, detail="Reward not available")
    
    if customer.current_points < reward.point_cost:
        raise HTTPException(
            status_code=400,
            detail="Not enough points to redeem this reward"
        )
    
    # Deduct points
    customer.current_points -= reward.point_cost
    customer.last_activity = datetime.utcnow()
    
    # Record redemption
    db_redemption = RedemptionDB(
        id=str(uuid.uuid4()),
        customer_id=redemption.customer_id,
        reward_id=redemption.reward_id,
        points_used=reward.point_cost
    )
    
    db.add(db_redemption)
    db.commit()
    
    return {
        "message": "Reward redeemed successfully",
        "remaining_points": customer.current_points
    }

@app.get("/rewards/", response_model=List[Dict])
def list_rewards(active_only: bool = True, db: Session = Depends(get_db)):
    """List available rewards"""
    query = db.query(RewardDB)
    if active_only:
        query = query.filter(RewardDB.is_active == 1)
    rewards = query.all()
    return [
        {
