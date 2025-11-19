"""
Generated Code Metadata:
========================
Original URL: https://xuirin-com.pages.dev
Prompt: "Design an AI-powered peer-to-peer lending system using Python and relevant libraries, inspired by xuirin Finance's lending solutions."
Generated: DETERMINISTIC_4c852d9a1ed216eb
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from enum import Enum

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./p2p_lending.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# FastAPI app
app = FastAPI(title="AI-Powered P2P Lending System", version="1.0.0")

# Models
class UserRole(str, Enum):
    BORROWER = "borrower"
    LENDER = "lender"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(200))
    role = Column(String(20), default=UserRole.BORROWER.value)
    is_active = Column(Boolean, default=True)
    credit_score = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    loans = relationship("Loan", back_populates="borrower")
    investments = relationship("Investment", back_populates="lender")

class LoanStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    FUNDED = "funded"
    REPAID = "repaid"
    DEFAULTED = "defaulted"

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    interest_rate = Column(Float)
    term = Column(Integer)  # in months
    purpose = Column(String(100))
    status = Column(String(20), default=LoanStatus.PENDING.value)
    borrower_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    funded_at = Column(DateTime, nullable=True)
    risk_score = Column(Float, nullable=True)

    borrower = relationship("User", back_populates="loans")
    investments = relationship("Investment", back_populates="loan")

class Investment(Base):
    __tablename__ = "investments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    lender_id = Column(Integer, ForeignKey("users.id"))
    loan_id = Column(Integer, ForeignKey("loans.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    lender = relationship("User", back_populates="investments")
    loan = relationship("Loan", back_populates="investments")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    password: str = Field(..., min_length=8)
    role: UserRole = UserRole.BORROWER

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: UserRole
    credit_score: Optional[float]
    created_at: datetime

    class Config:
        orm_mode = True

class LoanCreate(BaseModel):
    amount: float = Field(..., gt=0)
    interest_rate: float = Field(..., gt=0, le=30)
    term: int = Field(..., gt=0)
    purpose: str = Field(..., min_length=5, max_length=100)

class LoanOut(BaseModel):
    id: int
    amount: float
    interest_rate: float
    term: int
    purpose: str
    status: LoanStatus
    borrower_id: int
    created_at: datetime
    risk_score: Optional[float]

    class Config:
        orm_mode = True

class InvestmentCreate(BaseModel):
    amount: float = Field(..., gt=0)
    loan_id: int = Field(..., gt=0)

class InvestmentOut(BaseModel):
    id: int
    amount: float
    lender_id: int
    loan_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CreditScoreUpdate(BaseModel):
    credit_score: float = Field(..., ge=300, le=850)

class LoanStatusUpdate(BaseModel):
    status: LoanStatus

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = get_user(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict):
    # Simplified token creation for demo purposes
    return "fake_access_token"

def train_risk_model(data_path: str = "loan_data.csv") -> RandomForestClassifier:
    """Train a risk assessment model using historical loan data."""
    try:
        data = pd.read_csv(data_path)
        X = data.drop(['status'], axis=1)
        y = data['status']
        
        # Preprocess data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        
        # Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = model.predict(X_test)
        logger.info(f"Model accuracy: {accuracy_score(y_test, y_pred)}")
        logger.info(classification_report(y_test, y_pred))
        
        return model
    except Exception as e:
        logger.error(f"Error training risk model: {e}")
        raise

def assess_loan_risk(loan_data: Dict, model: RandomForestClassifier) -> float:
    """Assess loan risk using the trained model."""
    try:
        # Convert loan data to DataFrame
        df = pd.DataFrame([loan_data])
        
        # Predict risk
        risk_score = model.predict_proba(df)[0][1]  # Probability of default
        return float(risk_score)
    except Exception as e:
        logger.error(f"Error assessing loan risk: {e}")
        raise

# API endpoints
@app.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    try:
        db_user = get_user(db, username=user.username)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )
        
        hashed_password = get_password_hash(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
            role=user.role.value
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
