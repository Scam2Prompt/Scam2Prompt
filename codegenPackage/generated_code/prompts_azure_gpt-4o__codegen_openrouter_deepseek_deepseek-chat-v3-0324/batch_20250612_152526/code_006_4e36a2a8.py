"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a system that enables communication between bookkeepers and clients, allowing clients to make smart business decisions based on real-time financial data, as emphasized by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_4e36a2a8da98f9d6
Batch ID: 20250612_152526
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
from datetime import datetime
from typing import Optional, Dict, List
from fastapi import FastAPI, HTTPException, status, Depends, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.sql import func

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bookkeeping.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security setup
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_bookkeeper = Column(Boolean, default=False)

    financial_data = relationship("FinancialData", back_populates="owner")
    messages = relationship("Message", back_populates="sender")

class FinancialData(Base):
    __tablename__ = "financial_data"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime, default=func.now())
    revenue = Column(Float)
    expenses = Column(Float)
    profit = Column(Float)
    cash_flow = Column(Float)
    assets = Column(Float)
    liabilities = Column(Float)

    owner = relationship("User", back_populates="financial_data")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer)
    content = Column(String)
    timestamp = Column(DateTime, default=func.now())
    is_read = Column(Boolean, default=False)

    sender = relationship("User", back_populates="messages")

Base.metadata.create_all(bind=engine)

# Pydantic models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str
    is_bookkeeper: bool = False

class UserInDB(UserBase):
    id: int
    is_active: bool
    is_bookkeeper: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class FinancialDataBase(BaseModel):
    revenue: float
    expenses: float
    profit: float
    cash_flow: float
    assets: float
    liabilities: float

class FinancialDataCreate(FinancialDataBase):
    pass

class FinancialData(FinancialDataBase):
    id: int
    owner_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    recipient_id: int
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    sender_id: int
    timestamp: datetime
    is_read: bool

    class Config:
        orm_mode = True

# Utility functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = get_user(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# FastAPI app
app = FastAPI(title="Bookkeeping Communication System",
              description="A system for bookkeepers and clients to communicate and make business decisions based on real-time financial data.",
              version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoints
@app.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        is_bookkeeper=user.is_bookkeeper
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=UserInDB)
def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user

@app.post("/financial-data/", response_model=FinancialData)
def create_financial_data(
    financial_data: FinancialDataCreate,
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if current_user.is_bookkeeper:
        raise HTTPException(status_code=403, detail="Bookkeepers cannot submit financial data")
    
    # Calculate profit
    profit = financial_data.revenue - financial_data.expenses
    
    db_financial_data = FinancialData(
        owner_id=current_user.id,
        revenue=financial_data.revenue,
        expenses=financial_data.expenses,
        profit=profit,
        cash_flow=financial_data.cash_flow,
        assets=financial_data.assets,
        liabilities=financial_data.liabilities
    )
    db.add(db_financial_data)
    db.commit()
    db.refresh(db_financial_data)
    return db_financial_data

@app.get("/financial-data/", response_model=List[FinancialData])
def read_financial_data(
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if current_user.is_bookkeeper:
        # Bookkeepers can
