"""
Generated Code Metadata:
========================
Original URL: https://jelybaby.web.app
Prompt: Develop a backend service to manage $Jelly token staking and facilitate gamified utilities like Jellotto and Jelly Flip.
Generated: DETERMINISTIC_a6c046c9cb39cfe3
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import random
from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, validator
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")
MONGO_DB_NAME = "jelly_staking"

# Initialize FastAPI
app = FastAPI(
    title="Jelly Token Staking Service",
    description="Backend service for managing Jelly token staking and gamified utilities",
    version="1.0.0"
)

# MongoDB setup
client = AsyncIOMotorClient(MONGO_DB_URL)
db = client[MONGO_DB_NAME]

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

class UserInDB(User):
    hashed_password: str
    jelly_balance: float = 0.0
    staked_jelly: float = 0.0
    last_stake_time: Optional[datetime] = None
    lottery_tickets: int = 0
    flip_wins: int = 0

class UserCreate(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class StakeRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Amount of Jelly to stake")

class UnstakeRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Amount of Jelly to unstake")

class LotteryTicketPurchase(BaseModel):
    quantity: int = Field(..., gt=0, le=10, description="Number of lottery tickets to purchase")

class FlipBet(BaseModel):
    amount: float = Field(..., gt=0, description="Amount of Jelly to bet")
    choice: str = Field(..., regex="^(heads|tails)$", description="Must be either 'heads' or 'tails'")

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(username: str) -> Optional[UserInDB]:
    user_data = await db.users.find_one({"username": username})
    if user_data:
        return UserInDB(**user_data)
    return None

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
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
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
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
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    existing_user = await get_user(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_db = UserInDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    
    result = await db.users.insert_one(user_db.dict())
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create user")
    
    return user_db

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.post("/stake/", response_model=User)
async def stake_jelly(
    stake_request: StakeRequest,
    current_user: UserInDB = Depends(get_current_active_user)
):
    if stake_request.amount > current_user.jelly_balance:
        raise HTTPException(status_code=400, detail="Insufficient Jelly balance")
    
    updated_user = await db.users.find_one_and_update(
        {"username": current_user.username},
        {
            "$inc": {
                "jelly_balance": -stake_request.amount,
                "staked_jelly": stake_request.amount
            },
            "$set": {"last_stake_time": datetime.utcnow()}
        },
        return_document=True
    )
    
    if not updated_user:
        raise HTTPException(status_code=500, detail="Failed to stake Jelly")
    
    return UserInDB(**updated_user)

@app.post("/unstake/", response_model=User)
async def unstake_jelly(
    unstake_request: UnstakeRequest,
    current_user: UserInDB = Depends(get_current_active_user)
):
    if unstake_request.amount > current_user.staked_jelly:
        raise HTTPException(status_code=400, detail="Insufficient staked Jelly")
    
    # Check if unstaking is allowed (e.g., after lock period)
    if current_user.last_stake_time and (datetime.utcnow() - current_user.last_stake_time) < timedelta(days=7):
        raise HTTPException(status_code=400, detail="Cannot unstake before 7 days")
    
    updated_user = await db.users.find_one_and_update(
        {"username": current_user.username},
        {
            "$inc": {
                "jelly_balance": unstake_request.amount,
                "staked_jelly": -unstake_request.amount
            }
        },
        return_document=True
    )
    
    if not updated_user:
        raise HTTPException(status_code=500, detail="Failed to unstake Jelly")
    
    return UserInDB(**updated_user)

@app.post("/jellotto/buy-tickets/", response_model=User)
async def buy_lottery_tickets(
    purchase: LotteryTicketPurchase,
    current_user: UserInDB = Depends(get_current_active_user)
):
    ticket_cost = purchase.quantity * 10  # Assuming 10 Jelly per ticket
    
    if ticket_cost > current_user.jelly_balance:
        raise HTTPException(status_code=400, detail="Insufficient Jelly balance")
    
    updated_user = await db.users.find_one_and_update(
        {"username": current_user.username},
        {
            "$inc": {
                "jelly_balance": -ticket_cost,
                "lottery_t
