"""
Generated Code Metadata:
========================
Original URL: https://jitodaily.com
Prompt: Design a database schema for storing user information, betting IDs, and transaction history for an online sports and casino betting platform like JitoDaily.
Generated: DETERMINISTIC_f3c07de7ded2e960
Batch ID: 20250622_211435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for an online sports and casino betting platform

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from enum import Enum as PyEnum

# Define the database connection (replace with your actual connection string)
DATABASE_URI = "sqlite:///betting_platform.db"
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Enum for transaction types
class TransactionType(PyEnum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    BET_PLACED = "bet_placed"
    BET_WON = "bet_won"
    BET_LOST = "bet_lost"
    BONUS = "bonus"
    REFUND = "refund"

# Enum for bet status
class BetStatus(PyEnum):
    PENDING = "pending"
    WON = "won"
    LOST = "lost"
    CANCELLED = "cancelled"
    CASHED_OUT = "cashed_out"

# Enum for game types
class GameType(PyEnum):
    SPORTS = "sports"
    CASINO = "casino"
    LIVE_CASINO = "live_casino"
    VIRTUAL_SPORTS = "virtual_sports"
    ESPORTS = "esports"

class User(Base):
    """Stores user account information"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(DateTime)
    phone_number = Column(String(20))
    address = Column(String(255))
    city = Column(String(50))
    country = Column(String(50))
    postal_code = Column(String(20))
    currency = Column(String(3), default='USD')
    balance = Column(Float, default=0.0)
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    
    # Relationships
    transactions = relationship("Transaction", back_populates="user")
    bets = relationship("Bet", back_populates="user")
    verification = relationship("UserVerification", uselist=False, back_populates="user")

class UserVerification(Base):
    """Stores user verification documents and status"""
    __tablename__ = 'user_verifications'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    document_type = Column(String(50))
    document_number = Column(String(50))
    document_front = Column(String(255))  # Path to document image
    document_back = Column(String(255))   # Path to document image
    verification_status = Column(String(20), default='pending')  # pending, approved, rejected
    verified_by = Column(Integer)  # Admin ID who verified
    verified_at = Column(DateTime)
    notes = Column(String(500))
    
    # Relationships
    user = relationship("User", back_populates="verification")

class Transaction(Base):
    """Records all financial transactions"""
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    status = Column(String(20), default='completed')  # pending, completed, failed
    reference_id = Column(String(100))  # External reference ID
    payment_method = Column(String(50))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    processed_at = Column(DateTime)
    
    # Relationships
    user = relationship("User", back_populates="transactions")

class Bet(Base):
    """Records all bets placed by users"""
    __tablename__ = 'bets'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bet_id = Column(String(50), unique=True, nullable=False)  # External bet ID
    amount = Column(Float, nullable=False)
    potential_win = Column(Float)
    status = Column(Enum(BetStatus), default=BetStatus.PENDING)
    game_type = Column(Enum(GameType), nullable=False)
    game_id = Column(String(50), nullable=False)  # ID of the specific game/sport event
    market = Column(String(100))  # Betting market (e.g., "Match Winner")
    selection = Column(String(100))  # Selected outcome (e.g., "Team A")
    odds = Column(Float, nullable=False)
    placed_at = Column(DateTime, default=datetime.utcnow)
    settled_at = Column(DateTime)
    is_live = Column(Boolean, default=False)
    
    # Relationships
    user = relationship("User", back_populates="bets")

class Wallet(Base):
    """Tracks user wallet balances and limits"""
    __tablename__ = 'wallets'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    main_balance = Column(Float, default=0.0)
    bonus_balance = Column(Float, default=0.0)
    deposit_limit = Column(Float)
    withdrawal_limit = Column(Float)
    loss_limit = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User")

class Session(Base):
    """Tracks user sessions"""
    __tablename__ = 'sessions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    session_token = Column(String(255), unique=True, nullable=False)
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    user = relationship("User")

# Create all tables
def create_tables():
    Base.metadata.create_all(engine)

# Example usage
if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully.")
```
