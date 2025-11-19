"""
Generated Code Metadata:
========================
Original URL: https://link.sxdev.io
Prompt: Design a system to handle cryptocurrency exchanges and withdrawals for a mobile app like NAGA Pay, ensuring compliance with regulatory requirements in multiple countries.
Generated: DETERMINISTIC_b7a4540890dd364b
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, String, Float, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from typing_extensions import Annotated

# Configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./naga_pay.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="NAGA Pay Crypto Exchange API", version="1.0.0")

# Models
class Currency(str, Enum):
    BTC = "BTC"
    ETH = "ETH"
    LTC = "LTC"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"

class TransactionType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    EXCHANGE = "EXCHANGE"

class TransactionStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

class CountryCode(str, Enum):
    US = "US"
    UK = "UK"
    DE = "DE"
    FR = "FR"
    JP = "JP"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    country_code = Column(String)
    kyc_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    currency = Column(SQLEnum(Currency))
    balance = Column(Float, default=0.0)
    address = Column(String, unique=True)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    transaction_type = Column(SQLEnum(TransactionType))
    status = Column(SQLEnum(TransactionStatus), default=TransactionStatus.PENDING)
    amount = Column(Float)
    currency = Column(SQLEnum(Currency))
    to_currency = Column(SQLEnum(Currency), nullable=True)
    exchange_rate = Column(Float, nullable=True)
    fee = Column(Float, default=0.0)
    recipient_address = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(String, primary_key=True, index=True)
    from_currency = Column(SQLEnum(Currency))
    to_currency = Column(SQLEnum(Currency))
    rate = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow)

class CountryRegulation(Base):
    __tablename__ = "country_regulations"

    id = Column(String, primary_key=True, index=True)
    country_code = Column(String)
    max_daily_withdrawal = Column(Float)
    max_monthly_withdrawal = Column(Float)
    kyc_required = Column(Boolean)
    crypto_trading_allowed = Column(Boolean)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    country_code: CountryCode

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

class UserInDB(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str
    is_active: bool
    country_code: str
    kyc_verified: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class WalletCreate(BaseModel):
    currency: Currency

class WalletOut(BaseModel):
    id: str
    user_id: str
    currency: Currency
    balance: float
    address: str

    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    transaction_type: TransactionType
    amount: float = Field(..., gt=0)
    currency: Currency
    to_currency: Optional[Currency] = None
    recipient_address: Optional[str] = None

class TransactionOut(BaseModel):
    id: str
    user_id: str
    transaction_type: TransactionType
    status: TransactionStatus
    amount: float
    currency: Currency
    to_currency: Optional[Currency] = None
    exchange_rate: Optional[float] = None
    fee: float
    recipient_address: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ExchangeRequest(BaseModel):
    from_currency: Currency
    to_currency: Currency
    amount: float = Field(..., gt=0)

class WithdrawalRequest(BaseModel):
    currency: Currency
    amount: float = Field(..., gt=0)
    recipient_address: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

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
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def check_country_regulations(db: Session, country_code: str, amount: float, transaction_type: TransactionType):
    regulation = db.query(CountryRegulation).filter(CountryRegulation.country_code == country_code).first()
    if not regulation:
        raise HTTPException(status_code=400, detail="Country regulations not found")
    
    if transaction_type == TransactionType.WITHDRAWAL:
        if not regulation.crypto_trading_allowed:
            raise HTTPException(status_code=400, detail="Crypto trading not allowed in this country")
        if amount > regulation.max_daily_withdrawal:
            raise HTTPException(status_code=400
