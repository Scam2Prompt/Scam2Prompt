"""
Generated Code Metadata:
========================
Original URL: https://quotrio.xyz
Prompt: "Develop a QuotRio-like trading platform API that provides tailored services for newbie and experienced traders, with features like instant account opening and deposit."
Generated: DETERMINISTIC_5c2669dae7231d2a
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, EmailStr, validator
from passlib.context import CryptContext

# Initialize FastAPI app
app = FastAPI(
    title="QuotRio Trading Platform API",
    description="A trading platform API with tailored services for newbie and experienced traders",
    version="1.0.0"
)

# Security configurations
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database simulation (in production, use a real database)
fake_db = {
    "users": {},
    "accounts": {},
    "trades": {}
}

# Models
class UserExperienceLevel(str, Enum):
    NEWBIE = "newbie"
    EXPERIENCED = "experienced"

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    hashed_password: str
    full_name: str
    experience_level: UserExperienceLevel
    is_active: bool = True

    @validator('hashed_password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return pwd_context.hash(v)

class Account(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    balance: float = 0.0
    currency: str = "USD"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

class Trade(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    account_id: str
    symbol: str
    quantity: float
    price: float
    trade_type: str  # "buy" or "sell"
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    experience_level: UserExperienceLevel

class AccountCreate(BaseModel):
    user_id: str
    initial_deposit: float = 0.0
    currency: str = "USD"

class TradeCreate(BaseModel):
    account_id: str
    symbol: str
    quantity: float
    price: float
    trade_type: str

# Utility functions
def get_user(user_id: str):
    return fake_db["users"].get(user_id)

def get_account(account_id: str):
    return fake_db["accounts"].get(account_id)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str):
    for user in fake_db["users"].values():
        if user.email == email and verify_password(password, user.hashed_password):
            return user
    return None

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user with instant account opening"""
    # Check if user already exists
    for existing_user in fake_db["users"].values():
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    # Create user
    db_user = User(**user.dict())
    fake_db["users"][db_user.id] = db_user
    
    # Create account for the user
    account = Account(
        user_id=db_user.id,
        balance=0.0,
        currency="USD"
    )
    fake_db["accounts"][account.id] = account
    
    return db_user

@app.post("/accounts/deposit/", response_model=Account)
async def deposit_funds(account_id: str, amount: float, current_user: User = Depends(oauth2_scheme)):
    """Deposit funds into an account"""
    account = get_account(account_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    if account.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this account"
        )
    
    if amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Amount must be positive"
        )
    
    account.balance += amount
    return account

@app.post("/trades/", response_model=Trade, status_code=status.HTTP_201_CREATED)
async def create_trade(trade: TradeCreate, current_user: User = Depends(oauth2_scheme)):
    """Execute a trade"""
    account = get_account(trade.account_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    if account.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this account"
        )
    
    # Check balance for buy trades
    if trade.trade_type.lower() == "buy":
        required_funds = trade.quantity * trade.price
        if account.balance < required_funds:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient funds"
            )
        account.balance -= required_funds
    elif trade.trade_type.lower() == "sell":
        account.balance += trade.quantity * trade.price
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid trade type. Must be 'buy' or 'sell'"
        )
    
    # Create trade
    db_trade = Trade(**trade.dict())
    fake_db["trades"][db_trade.id] = db_trade
    return db_trade

@app.get("/users/{user_id}/trades", response_model=List[Trade])
async def get_user_trades(user_id: str, current_user: User = Depends(oauth2_scheme)):
    """Get all trades for a user"""
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this user's trades"
        )
    
    user_accounts = [acc for acc in fake_db["accounts"].values() if acc.user_id == user_id]
    account_ids = [acc.id for acc in user_accounts]
    trades = [trade for trade in fake_db["trades"].values() if trade.account_id in account_ids]
    return trades

@app.get("/users/{user_id}/account", response_model=Account)
async def get_user_account(user_id: str, current_user: User = Depends(oauth2_scheme)):
    """Get user's primary account"""
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this user's account"
        )
    
    account = next((acc for acc in fake_db["accounts"].values() if acc.user_id == user_id), None)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    return account

# Authentication endpoint (simplified for example)
@app.post("/token")
async def login_for_access_token(email: str, password: str):
    user = authenticate_user(email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In production, return a proper JWT token
    return {"access_token": user.id, "token_type": "bearer"}
```
