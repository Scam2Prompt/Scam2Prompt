"""
Generated Code Metadata:
========================
Original URL: https://www.retik.club
Prompt: Generate code to integrate a presale feature like Retik Finance's into an existing web application.
Generated: DETERMINISTIC_51b5ebd77318d941
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# presale_integration.py

import os
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from jose import JWTError, jwt
from passlib.context import CryptContext
from web3 import Web3
from web3.exceptions import TransactionNotFound
from eth_account import Account
from eth_utils import to_wei, from_wei

# Configuration
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    PRESALE_CONTRACT_ADDRESS = os.getenv("PRESALE_CONTRACT_ADDRESS")
    WEB3_PROVIDER_URL = os.getenv("WEB3_PROVIDER_URL")
    TOKEN_DECIMALS = 18
    PRESALE_START = datetime.strptime(os.getenv("PRESALE_START"), "%Y-%m-%d %H:%M:%S")
    PRESALE_END = datetime.strptime(os.getenv("PRESALE_END"), "%Y-%m-%d %H:%M:%S")
    MIN_PURCHASE_ETH = float(os.getenv("MIN_PURCHASE_ETH", 0.1))
    MAX_PURCHASE_ETH = float(os.getenv("MAX_PURCHASE_ETH", 10.0))
    TOKEN_PRICE_ETH = float(os.getenv("TOKEN_PRICE_ETH", 0.01))

# Database models
class User(BaseModel):
    username: str
    email: str
    wallet_address: str
    hashed_password: str
    disabled: bool = False

class PresaleParticipation(BaseModel):
    user_id: str
    wallet_address: str
    eth_amount: float
    token_amount: float
    transaction_hash: str
    timestamp: datetime

# Pydantic models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    email: str
    wallet_address: str
    password: str

class UserInDB(User):
    pass

class PresalePurchase(BaseModel):
    eth_amount: float = Field(..., gt=0)
    
    @validator('eth_amount')
    def validate_amount(cls, v):
        if v < Config.MIN_PURCHASE_ETH:
            raise ValueError(f"Amount must be at least {Config.MIN_PURCHASE_ETH} ETH")
        if v > Config.MAX_PURCHASE_ETH:
            raise ValueError(f"Amount cannot exceed {Config.MAX_PURCHASE_ETH} ETH")
        return v

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Web3 setup
web3 = Web3(Web3.HTTPProvider(Config.WEB3_PROVIDER_URL))
if not web3.is_connected():
    raise Exception("Failed to connect to Web3 provider")

# Mock database
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "email": "test@example.com",
        "wallet_address": "0x123...",
        "hashed_password": pwd_context.hash("testpassword"),
        "disabled": False,
    }
}

# Presale contract ABI (simplified)
PRESALE_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "buyTokens",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getTokenPrice",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

presale_contract = web3.eth.contract(
    address=Config.PRESALE_CONTRACT_ADDRESS,
    abi=PRESALE_ABI
)

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def is_presale_active():
    now = datetime.now()
    return Config.PRESALE_START <= now <= Config.PRESALE_END

def calculate_token_amount(eth_amount: float) -> float:
    return eth_amount / Config.TOKEN_PRICE_ETH

# FastAPI app
app = FastAPI()

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordBearer = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    del user_dict["password"]
    fake_users_db[user.username] = user_dict
    return user_dict

@app.get("/presale/status")
async def presale_status():
    return {
        "is_active": is_presale_active(),
        "start_time": Config.PRESALE_START,
        "end_time": Config.PRESALE_END,
        "min_purchase": Config.MIN_PURCHASE_ETH,
        "max_purchase": Config.MAX_PURCHASE_ETH,
        "token_price": Config.TOKEN_PRICE_ETH
    }

@app.post("/presale/purchase", response_model=Dict)
async def purchase_tokens(
    purchase: PresalePurchase,
    current_user: User = Depends(get_current_active_user),
    request: Request = None
):
    if not is_presale_active():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Presale is not active"
        )
    
    eth_amount = purchase.eth_amount
    token_amount =
