"""
Generated Code Metadata:
========================
Original URL: https://treasury.casino
Prompt: Design a system for secure deposits and withdrawals on an online casino platform, considering multiple payment options, encryption technologies, and regulatory compliance, as seen on Treasury Brisbane Casino.
Generated: DETERMINISTIC_bfbd80eb238e7c06
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import json
import os
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, List

import bcrypt
import requests
from cryptography.fernet import Fernet
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", Fernet.generate_key().decode())
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./casino.db")

# Payment processor API keys (should be in environment variables in production)
PAYMENT_PROCESSORS = {
    "stripe": os.getenv("STRIPE_API_KEY"),
    "paypal": os.getenv("PAYPAL_API_KEY"),
    "bank_transfer": None  # Handled internally
}

# Initialize FastAPI
app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)

# Database setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
fernet = Fernet(SECRET_KEY.encode())

# Models
class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    BANK_TRANSFER = "bank_transfer"
    PAYPAL = "paypal"
    CRYPTO = "crypto"

class TransactionStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)
    balance = Column(Float, default=0.0)
    kyc_verified = Column(Boolean, default=False)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    amount = Column(Float)
    currency = Column(String, default="USD")
    payment_method = Column(SQLEnum(PaymentMethod))
    status = Column(SQLEnum(TransactionStatus), default=TransactionStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    reference = Column(String, unique=True, index=True)
    metadata = Column(String, nullable=True)  # Encrypted JSON

class PaymentProcessorConfig(BaseModel):
    name: str
    api_key: str
    is_active: bool = True

class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0)
    payment_method: PaymentMethod
    currency: str = "USD"
    metadata: Optional[Dict] = None

    @validator('amount')
    def validate_amount(cls, v):
        if v <= 0:
            raise ValueError("Amount must be positive")
        return round(v, 2)

class TransactionOut(BaseModel):
    id: int
    amount: float
    currency: str
    payment_method: PaymentMethod
    status: TransactionStatus
    created_at: datetime
    reference: str

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    full_name: str

class UserOut(BaseModel):
    username: str
    email: str
    full_name: str
    balance: float
    kyc_verified: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Utils
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

def create_access_token(data: dict, expires_delta: Optional[int] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def encrypt_data(data: dict) -> str:
    json_data = json.dumps(data).encode()
    return fernet.encrypt(json_data).decode()

def decrypt_data(encrypted_data: str) -> dict:
    decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()
    return json.loads(decrypted_data)

def generate_reference(user_id: int) -> str:
    timestamp = int(datetime.utcnow().timestamp())
    unique_str = f"{user_id}-{timestamp}"
    return hashlib.sha256(unique_str.encode()).hexdigest()[:20]

def process_payment(payment_method: PaymentMethod, amount: float, currency: str, user_data: dict):
    if payment_method == PaymentMethod.BANK_TRANSFER:
        return True, "bank_reference_123"
    elif payment_method == PaymentMethod.PAYPAL:
        # In production, this would call PayPal API
        return True, "paypal_transaction_123"
    elif payment_method == PaymentMethod.CREDIT_CARD:
        # In production, this would call Stripe API
        return True, "stripe_charge_123"
    elif payment_method == PaymentMethod.CRYPTO:
        # In production, this would call crypto payment processor
        return True, "crypto_tx_123"
    return False, "Payment method not supported"

# Auth
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        email=user.email,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token
