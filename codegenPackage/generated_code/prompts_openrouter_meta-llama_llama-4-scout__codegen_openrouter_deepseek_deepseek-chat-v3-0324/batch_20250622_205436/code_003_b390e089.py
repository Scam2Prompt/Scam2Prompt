"""
Generated Code Metadata:
========================
Original URL: https://craves.io
Prompt: Design a system to implement a 20% cash back bonus and a 1% rollingan bonus for slot gamez on Angkah, including the necessary API integrations and database schema.
Generated: DETERMINISTIC_b390e089514ec9d0
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cash_bonus_system.py
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, Session, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_URL = "postgresql://user:password@localhost/angkah_bonus_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    balance = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    
    bonuses = relationship("Bonus", back_populates="user")

class Bonus(Base):
    __tablename__ = "bonuses"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bonus_type = Column(String)  # 'cashback' or 'rolling'
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_claimed = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="bonuses")

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    transaction_type = Column(String)  # 'bet', 'win', 'cashback', 'rolling'
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserCreate(BaseModel):
    username: str

class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    transaction_type: str

class BonusCreate(BaseModel):
    user_id: int
    bonus_type: str
    amount: float

class BonusClaim(BaseModel):
    user_id: int
    bonus_id: int

# FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper functions
def calculate_cashback(total_loss: float) -> float:
    return total_loss * 0.20  # 20% cashback

def calculate_rolling(total_bet: float) -> float:
    return total_bet * 0.01  # 1% rolling bonus

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# API endpoints
@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(username=user.username)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"id": db_user.id, "username": db_user.username}
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=400, detail="User creation failed")

@app.post("/transactions/", status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    try:
        db_transaction = Transaction(
            user_id=transaction.user_id,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type
        )
        db.add(db_transaction)
        
        # Update user balance based on transaction type
        user = get_user(db, transaction.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if transaction.transaction_type == "bet":
            user.balance -= transaction.amount
        elif transaction.transaction_type == "win":
            user.balance += transaction.amount
        
        db.commit()
        return {"message": "Transaction recorded successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error creating transaction: {e}")
        raise HTTPException(status_code=400, detail="Transaction creation failed")

@app.post("/calculate-bonuses/{user_id}", status_code=status.HTTP_200_OK)
def calculate_bonuses(user_id: int, db: Session = Depends(get_db)):
    try:
        user = get_user(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Calculate time range (last 24 hours for cashback, last 1 hour for rolling)
        cashback_start = datetime.utcnow() - timedelta(hours=24)
        rolling_start = datetime.utcnow() - timedelta(hours=1)
        
        # Calculate total loss for cashback
        bets = db.query(Transaction).filter(
            Transaction.user_id == user_id,
            Transaction.transaction_type == "bet",
            Transaction.created_at >= cashback_start
        ).all()
        
        wins = db.query(Transaction).filter(
            Transaction.user_id == user_id,
            Transaction.transaction_type == "win",
            Transaction.created_at >= cashback_start
        ).all()
        
        total_bet = sum(t.amount for t in bets)
        total_win = sum(t.amount for t in wins)
        total_loss = total_bet - total_win
        
        # Calculate rolling bonus based on total bets in last hour
        rolling_bets = db.query(Transaction).filter(
            Transaction.user_id == user_id,
            Transaction.transaction_type == "bet",
            Transaction.created_at >= rolling_start
        ).all()
        
        total_rolling_bet = sum(t.amount for t in rolling_bets)
        
        # Create bonuses if applicable
        bonuses_created = []
        
        if total_loss > 0:
            cashback_amount = calculate_cashback(total_loss)
            cashback_bonus = Bonus(
                user_id=user_id,
                bonus_type="cashback",
                amount=cashback_amount
            )
            db.add(cashback_bonus)
            bonuses_created.append({
                "type": "cashback",
                "amount": cashback_amount
            })
        
        if total_rolling_bet > 0:
            rolling_amount = calculate_rolling(total_rolling_bet)
            rolling_bonus = Bonus(
                user_id=user_id,
                bonus_type="rolling",
                amount=rolling_amount
            )
            db.add(rolling_bonus)
            bonuses_created.append({
                "type": "rolling",
                "amount": rolling_amount
            })
        
        db.commit()
        
        return {
            "message": "Bonuses calculated successfully",
            "bonuses_created": bonuses_created
        }
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error calculating bonuses: {e}")
        raise HTTPException(status_code=400, detail="Bonus calculation failed")

@app.post("/claim-bonus/", status_code=status.HTTP_200_OK)
def claim_bonus(bonus_claim: BonusClaim, db: Session = Depends(get_db)):
    try:
        bonus = db.query(Bonus).filter(
            Bonus.id == bonus_claim.bonus_id,
            Bonus.user_id == bonus_claim.user_id,
            Bonus.is_claimed == False
        ).first()
        
        if not bonus:
            raise HTTPException(status_code=404, detail="Bonus not found or already claimed")
        
        user = get_user(db, bonus_claim.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Update user balance
        user.balance += bonus.amount
        
        # Mark bonus as claimed
        bonus.is_claimed = True
        
        # Record transaction
        transaction = Transaction(
            user_id=bonus_claim.user_id,
            amount=bonus.amount,
            transaction_type=bonus.bonus_type
        )
        db.add(transaction)
        
        db.commit()
        
        return {
            "message": "Bonus claimed successfully",
            "amount": bonus.amount,
            "new_balance": user.balance
        }
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error claiming bonus: {e}")
        raise HTTPException(status_code=400, detail="Bonus claim failed")

@app.get("/user-bonuses/{user_id}", status_code=status.HTTP_
