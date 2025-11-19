"""
Generated Code Metadata:
========================
Original URL: https://memeskombat.pages.dev
Prompt: Design a simple betting system API for a meme battle platform, inspired by Meme Kombat's battle and staking features, with endpoints for user registration, token staking, and reward distribution.
Generated: DETERMINISTIC_34c617d74f3d7fae
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime, timedelta
import secrets
import hashlib
import uuid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from enum import Enum

# Configuration
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (in-memory for simplicity)
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    hashed_password: str
    balance: float = 0.0
    disabled: bool = False

class BattleOutcome(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"

class Battle(BaseModel):
    id: str
    meme1_id: str
    meme2_id: str
    start_time: datetime
    end_time: datetime
    total_pool: float = 0.0

class Bet(BaseModel):
    id: str
    user_id: str
    battle_id: str
    amount: float
    chosen_meme_id: str
    created_at: datetime
    outcome: Optional[BattleOutcome] = None
    reward: Optional[float] = None

# In-memory "database"
db_users = {}
db_battles = {}
db_bets = {}

# Auth setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Helper functions
def get_user(username: str):
    if username in db_users:
        return db_users[username]
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
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
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Models for requests/responses
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class BetCreate(BaseModel):
    battle_id: str
    amount: float
    chosen_meme_id: str

    @validator('amount')
    def amount_positive(cls, v):
        if v <= 0:
            raise ValueError('Bet amount must be positive')
        return v

class BattleCreate(BaseModel):
    meme1_id: str
    meme2_id: str
    duration_minutes: int

    @validator('duration_minutes')
    def duration_positive(cls, v):
        if v <= 0:
            raise ValueError('Duration must be positive')
        return v

class BattleResult(BaseModel):
    winner_meme_id: Optional[str] = None  # None for draw

# API Endpoints
@app.post("/register", response_model=User)
async def register_user(user: UserCreate):
    if user.username in db_users:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = pwd_context.hash(user.password)
    user_id = str(uuid.uuid4())
    db_user = User(
        id=user_id,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db_users[user.username] = db_user
    return db_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
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

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.post("/battles", response_model=Battle)
async def create_battle(
    battle: BattleCreate,
    current_user: User = Depends(get_current_active_user)
):
    battle_id = str(uuid.uuid4())
    now = datetime.utcnow()
    end_time = now + timedelta(minutes=battle.duration_minutes)
    
    db_battle = Battle(
        id=battle_id,
        meme1_id=battle.meme1_id,
        meme2_id=battle.meme2_id,
        start_time=now,
        end_time=end_time
    )
    db_battles[battle_id] = db_battle
    return db_battle

@app.get("/battles/{battle_id}", response_model=Battle)
async def get_battle(battle_id: str):
    if battle_id not in db_battles:
        raise HTTPException(status_code=404, detail="Battle not found")
    return db_battles[battle_id]

@app.post("/bets", response_model=Bet)
async def place_bet(
    bet: BetCreate,
    current_user: User = Depends(get_current_active_user)
):
    # Check battle exists and is ongoing
    if bet.battle_id not in db_battles:
        raise HTTPException(status_code=404, detail="Battle not found")
    
    battle = db_battles[bet.battle_id]
    if datetime.utcnow() > battle.end_time:
        raise HTTPException(status_code=400, detail="Battle has already ended")
    
    # Check user has enough balance
    if current_user.balance < bet.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    # Check chosen meme is valid
    if bet.chosen_meme_id not in [battle.meme1_id, battle.meme2_id]:
        raise HTTPException(status_code=400, detail="Invalid meme choice")
    
    # Create bet
    bet_id = str(uuid.uuid4())
    db_bet = Bet(
        id=bet_id,
        user_id=current_user.id,
        battle_id=bet.battle_id,
        amount=bet.amount,
        chosen_meme_id=bet.chosen_meme_id,
        created_at=datetime.utcnow()
    )
    db_bets[bet_id] = db_bet
    
    # Update user balance and battle pool
    current_user.balance -= bet.amount
    battle.total_pool += bet.amount
    
    return db_bet

@app.post("/battles/{battle_id}/resolve", response_model=Battle)
async def resolve_battle(
    battle_id: str,
    result: BattleResult,
    current_user: User = Depends(get_current_active_user)
):
    # Check battle exists and is over
    if battle_id not in db_battles:
        raise HTTPException(status_code=404, detail="Battle not found")
    
    battle =
