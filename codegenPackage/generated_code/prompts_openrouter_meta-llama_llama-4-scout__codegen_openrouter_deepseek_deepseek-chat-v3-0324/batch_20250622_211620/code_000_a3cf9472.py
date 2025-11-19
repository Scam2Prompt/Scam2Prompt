"""
Generated Code Metadata:
========================
Original URL: https://jadobet.org
Prompt: Write a Python script to implement a simple casino game API, similar to BaxBet's offerings, with user registration, login, and deposit functionality.
Generated: DETERMINISTIC_a3cf9472d4ed2bc6
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import secrets
from typing import Dict, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError

# Configuration
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database simulation (in-memory for this example)
users_db: Dict[str, dict] = {}
games_db: Dict[str, dict] = {}

# FastAPI app initialization
app = FastAPI(title="Simple Casino API", description="A simple casino game API")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

class User(UserBase):
    balance: float
    is_active: bool

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class DepositRequest(BaseModel):
    amount: float

    @validator('amount')
    def amount_positive(cls, v):
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v

# Helper functions
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
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

def verify_password(plain_password: str, hashed_password: str):
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password

def get_current_user(token: str = Depends(oauth2_scheme)):
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
    except PyJWTError:
        raise credentials_exception
    user = get_user(users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/register", response_model=User)
async def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    user_dict = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "balance": 0.0,
        "is_active": True
    }
    users_db[user.username] = user_dict
    return User(**{k: v for k, v in user_dict.items() if k != "hashed_password"})

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users_db, form_data.username, form_data.password)
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

@app.post("/deposit", response_model=User)
async def deposit_funds(
    deposit: DepositRequest,
    current_user: User = Depends(get_current_active_user)
):
    users_db[current_user.username]["balance"] += deposit.amount
    return User(**{k: v for k, v in users_db[current_user.username].items() if k != "hashed_password"})

@app.get("/games")
async def list_games():
    return {"games": list(games_db.keys())}

# Sample game initialization
games_db["slots"] = {
    "name": "Slots",
    "description": "Classic slot machine game",
    "min_bet": 1.0,
    "max_bet": 100.0
}

games_db["blackjack"] = {
    "name": "Blackjack",
    "description": "Classic blackjack game",
    "min_bet": 5.0,
    "max_bet": 500.0
}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
