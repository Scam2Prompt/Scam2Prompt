"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Design a database schema for storing user information, game data, and transaction records for a betting platform like VZ99.
Generated: DETERMINISTIC_b466daa8a6fbfde0
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database Schema for Betting Platform (VZ99-like)

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class UserStatus(PyEnum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    BANNED = "banned"

class TransactionType(PyEnum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    BET = "bet"
    WIN = "win"
    BONUS = "bonus"

class GameType(PyEnum):
    SLOT = "slot"
    SPORTS = "sports"
    LIVE_CASINO = "live_casino"
    LOTTERY = "lottery"

class User(Base):
    """User information table"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    salt = Column(String(50), nullable=False)
    balance = Column(Float, default=0.0, nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_login = Column(DateTime)
    verification_status = Column(Boolean, default=False, nullable=False)
    phone_number = Column(String(20))
    address = Column(String(255))

    transactions = relationship("Transaction", back_populates="user")
    bets = relationship("Bet", back_populates="user")

class Game(Base):
    """Game information table"""
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    game_type = Column(Enum(GameType), nullable=False)
    description = Column(String(500))
    min_bet = Column(Float, default=1.0, nullable=False)
    max_bet = Column(Float, default=1000.0, nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    bets = relationship("Bet", back_populates="game")

class Bet(Base):
    """Bet records table"""
    __tablename__ = 'bets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)
    amount = Column(Float, nullable=False)
    potential_win = Column(Float)
    outcome = Column(Float)  # Actual win amount (0 if lost)
    status = Column(String(20), default='pending', nullable=False)  # pending, won, lost, canceled
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    settled_at = Column(DateTime)
    details = Column(String(500))  # Additional bet details (e.g., team names, odds)

    user = relationship("User", back_populates="bets")
    game = relationship("Game", back_populates="bets")
    transaction = relationship("Transaction", uselist=False, back_populates="bet")

class Transaction(Base):
    """Financial transactions table"""
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    status = Column(String(20), default='pending', nullable=False)  # pending, completed, failed
    reference_id = Column(String(100), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime)
    bet_id = Column(Integer, ForeignKey('bets.id'))
    payment_method = Column(String(50))
    notes = Column(String(255))

    user = relationship("User", back_populates="transactions")
    bet = relationship("Bet", back_populates="transaction")

class SystemSettings(Base):
    """Platform configuration settings"""
    __tablename__ = 'system_settings'

    id = Column(Integer, primary_key=True)
    maintenance_mode = Column(Boolean, default=False, nullable=False)
    min_deposit = Column(Float, default=10.0, nullable=False)
    max_deposit = Column(Float, default=5000.0, nullable=False)
    min_withdrawal = Column(Float, default=20.0, nullable=False)
    max_withdrawal = Column(Float, default=10000.0, nullable=False)
    currency = Column(String(3), default='USD', nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class AuditLog(Base):
    """System audit log"""
    __tablename__ = 'audit_logs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String(100), nullable=False)
    description = Column(String(500))
    ip_address = Column(String(45))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    metadata = Column(String(1000))  # JSON data

# Example of how to initialize the database
def init_db(connection_string):
    """Initialize the database connection and create tables"""
    engine = db.create_engine(connection_string)
    Base.metadata.create_all(engine)
    return engine
```
