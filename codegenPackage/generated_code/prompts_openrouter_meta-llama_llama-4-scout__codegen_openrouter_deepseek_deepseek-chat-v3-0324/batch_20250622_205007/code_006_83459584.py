"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: What are the advantages and disadvantages of using a Bitcoin exchange script like Paxful's, and how can I customize it for my business needs?
Generated: DETERMINISTIC_83459584343a4612
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bitcoin Exchange Script Customization
This script demonstrates how to customize a Bitcoin exchange platform similar to Paxful.
It includes core functionalities and customization points for business needs.
"""

import json
from typing import Dict, Optional, List
from datetime import datetime
import hashlib
import hmac
import requests
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./bitcoin_exchange.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app
app = FastAPI(title="Bitcoin Exchange API", description="Customizable Bitcoin Exchange Platform")

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, index=True)
    seller_id = Column(Integer, index=True)
    amount_btc = Column(Float)
    amount_fiat = Column(Float)
    currency = Column(String, default="USD")
    status = Column(String, default="pending")  # pending, completed, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

class Wallet(Base):
    __tablename__ = "wallets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    btc_balance = Column(Float, default=0.0)
    fiat_balance = Column(Float, default=0.0)
    currency = Column(String, default="USD")

# Pydantic models for request/response validation
class UserCreate(BaseModel):
    username: str
    password: str
    email: str

    @validator('password')
    def password_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class TradeCreate(BaseModel):
    buyer_id: int
    seller_id: int
    amount_btc: float
    amount_fiat: float
    currency: str = "USD"

class WalletUpdate(BaseModel):
    user_id: int
    btc_balance: Optional[float] = None
    fiat_balance: Optional[float] = None

# Utility functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hmac.compare_digest(
        hashed_password.encode(),
        hashlib.sha256(plain_password.encode()).hexdigest().encode()
    )

def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Core exchange functionality
@app.post("/users/", response_model=Dict)
def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    """Create a new user account"""
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Create wallet for new user
    wallet = Wallet(user_id=db_user.id)
    db.add(wallet)
    db.commit()
    
    return {"message": "User created successfully", "user_id": db_user.id}

@app.post("/trades/", response_model=Dict)
def create_trade(trade: TradeCreate, db: SessionLocal = Depends(get_db)):
    """Create a new trade between users"""
    # Verify both users exist
    buyer = db.query(User).filter(User.id == trade.buyer_id).first()
    seller = db.query(User).filter(User.id == trade.seller_id).first()
    
    if not buyer or not seller:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verify seller has enough BTC
    seller_wallet = db.query(Wallet).filter(Wallet.user_id == trade.seller_id).first()
    if seller_wallet.btc_balance < trade.amount_btc:
        raise HTTPException(status_code=400, detail="Seller doesn't have enough BTC")
    
    # Create trade
    db_trade = Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    
    return {"message": "Trade created successfully", "trade_id": db_trade.id}

@app.post("/trades/{trade_id}/complete", response_model=Dict)
def complete_trade(trade_id: int, db: SessionLocal = Depends(get_db)):
    """Complete a trade by transferring funds"""
    trade = db.query(Trade).filter(Trade.id == trade_id).first()
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    
    if trade.status != "pending":
        raise HTTPException(status_code=400, detail="Trade is not pending")
    
    # Get wallets
    buyer_wallet = db.query(Wallet).filter(Wallet.user_id == trade.buyer_id).first()
    seller_wallet = db.query(Wallet).filter(Wallet.user_id == trade.seller_id).first()
    
    # Verify buyer has enough fiat
    if buyer_wallet.fiat_balance < trade.amount_fiat:
        raise HTTPException(status_code=400, detail="Buyer doesn't have enough fiat")
    
    # Transfer funds
    seller_wallet.fiat_balance += trade.amount_fiat
    seller_wallet.btc_balance -= trade.amount_btc
    
    buyer_wallet.fiat_balance -= trade.amount_fiat
    buyer_wallet.btc_balance += trade.amount_btc
    
    # Update trade status
    trade.status = "completed"
    trade.completed_at = datetime.utcnow()
    
    db.commit()
    
    return {"message": "Trade completed successfully"}

@app.get("/wallets/{user_id}", response_model=Dict)
def get_wallet(user_id: int, db: SessionLocal = Depends(get_db)):
    """Get user wallet information"""
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    
    return {
        "btc_balance": wallet.btc_balance,
        "fiat_balance": wallet.fiat_balance,
        "currency": wallet.currency
    }

# Customization points
class CustomFeeStructure(BaseModel):
    maker_fee: float = 0.001  # 0.1%
    taker_fee: float = 0.002  # 0.2%
    withdrawal_fee_btc: float = 0.0005  # BTC

@app.post("/admin/set_fees", response_model=Dict)
def set_fees(fees: CustomFeeStructure, token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_db)):
    """Admin endpoint to customize fee structure"""
    # In production, verify admin privileges here
    # For demo, we'll just accept the changes
    
    # Save fees to database or config file
    # This is a placeholder - implement your persistence logic
    with open("fee_config.json", "w") as f:
        json.dump(fees.dict(), f)
    
    return {"message": "Fee structure updated successfully"}

class CustomLimits(BaseModel):
    min_trade_btc: float = 0.001  # Minimum BTC trade amount
    max_trade_btc: float = 10.0   # Maximum BTC trade amount
    daily_withdrawal_limit: float = 2.0  # BTC

@app.post("/admin/set_limits", response_model=Dict)
def set_limits(limits: CustomLimits, token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_db)):
    """Admin endpoint to customize platform limits"""
    # Save limits to database or
