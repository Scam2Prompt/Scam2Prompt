"""
Generated Code Metadata:
========================
Original URL: https://yawnsworld-io.web.app
Prompt: "Develop a basic AI-powered sleep app concept that utilizes $YAWN tokens for optimizing sleep patterns, including potential features and a revenue model."
Generated: DETERMINISTIC_7a1a76415716e599
Batch ID: 20250622_205006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import requests
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, validator
from jose import JWTError, jwt
from passlib.context import CryptContext
import uvicorn

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
YAWN_TOKEN_EXCHANGE_RATE = 0.1  # 1 YAWN token = 0.1 USD

# Database models (in-memory for demo purposes)
fake_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "User One",
        "email": "user1@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGgaXNlK",  # password = "secret"
        "disabled": False,
        "yawn_tokens": 100,
        "sleep_data": []
    }
}

# Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    yawn_tokens: Optional[int] = None

class UserInDB(User):
    hashed_password: str
    sleep_data: List[Dict] = []

class SleepData(BaseModel):
    start_time: datetime
    end_time: datetime
    quality_score: float = Field(..., ge=0, le=100)
    interruptions: int = Field(..., ge=0)
    deep_sleep_minutes: int = Field(..., ge=0)
    rem_sleep_minutes: int = Field(..., ge=0)

class SleepRecommendation(BaseModel):
    recommendation: str
    confidence_score: float = Field(..., ge=0, le=1)
    cost_in_yawn_tokens: int = Field(..., ge=0)

class PurchaseTokens(BaseModel):
    amount_usd: float = Field(..., gt=0)
    
class SleepAnalysisRequest(BaseModel):
    days_to_analyze: int = Field(..., gt=0)

# Auth setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="YAWN Sleep App",
              description="AI-powered sleep optimization using YAWN tokens",
              version="0.1.0")

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

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
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def analyze_sleep_patterns(sleep_data: List[Dict], days_to_analyze: int) -> SleepRecommendation:
    """AI-powered sleep analysis (mock implementation)"""
    # In a real app, this would connect to an ML model
    avg_sleep = sum((d['end_time'] - d['start_time']).total_seconds() / 3600 
                    for d in sleep_data[-days_to_analyze:]) / days_to_analyze
    
    if avg_sleep < 7:
        return SleepRecommendation(
            recommendation="Increase sleep duration by 1-2 hours",
            confidence_score=0.85,
            cost_in_yawn_tokens=10
        )
    else:
        return SleepRecommendation(
            recommendation="Maintain current sleep schedule, focus on sleep quality",
            confidence_score=0.72,
            cost_in_yawn_tokens=5
        )

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
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

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.post("/sleep/record/")
async def record_sleep_data(
    sleep_data: SleepData,
    current_user: User = Depends(get_current_active_user)
):
    """Record a sleep session"""
    user_data = fake_users_db[current_user.username]
    user_data["sleep_data"].append(sleep_data.dict())
    return {"message": "Sleep data recorded successfully"}

@app.get("/sleep/history/", response_model=List[SleepData])
async def get_sleep_history(
    current_user: User = Depends(get_current_active_user)
):
    """Get user's sleep history"""
    return fake_users_db[current_user.username]["sleep_data"]

@app.post("/sleep/analyze/", response_model=SleepRecommendation)
async def analyze_sleep(
    analysis_request: SleepAnalysisRequest,
    current_user: User = Depends(get_current_active_user)
):
    """Get AI-powered sleep recommendations"""
    user_data = fake_users_db[current_user.username]
    if len(user_data["sleep_data"]) < analysis_request.days_to_analyze:
        raise HTTPException(
            status_code=400,
            detail=f"Not enough sleep data (need {analysis_request.days_to_analyze} days)"
        )
    
    if user_data["yawn_tokens"] < 5:  # Minimum cost for any analysis
        raise HTTPException(
            status_code=402,
            detail="Insufficient YAWN tokens for analysis"
        )
    
    recommendation = analyze_sleep_patterns(
        user_data["sleep_data"],
        analysis_request.days_to_analyze
    )
    
    # Deduct tokens
    user_data["yawn_tokens"] -= recommendation.cost_in_yawn_tokens
    
    return recommendation

@app.post("/tokens/purchase/")
async def purchase_yawn_tokens(
    purchase: PurchaseTokens,
    current_user: User = Depends(get_current_active_user)
):
    """Purchase YAWN tokens with real currency"""
    tokens_to_add = int(purchase.amount_usd / YAWN_TOKEN_EXCHANGE_RATE)
    fake_users_db[current_user.username]["yawn_tokens"] += tokens_to_add
    return {
        "message": f"Purchased {tokens_to_add} YAWN tokens",
        "new_balance": fake_users_db[current_user.username]["yawn_tokens"]
    }

@app.get("/tokens/balance/")
async def get_token_balance(
    current_user: User = Dep
