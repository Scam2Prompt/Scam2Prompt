"""
Generated Code Metadata:
========================
Original URL: https://ezi-trade.com
Prompt: "Design an API for Ezi-Trade's investment plans, including endpoints for deposit, withdrawal, and checking account balance, with proper error handling and security measures."
Generated: DETERMINISTIC_c4f8e746a9fec7a1
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import jwt
from datetime import datetime, timedelta

# Configuration
SECRET_KEY = "secret_key_here"
ALGORITHM = "HS256"

# Initialize FastAPI app
app = FastAPI()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User model
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool = False

# Investment plan model
class InvestmentPlan(BaseModel):
    plan_name: str
    balance: float

# Token model
class Token(BaseModel):
    access_token: str
    token_type: str

# Token data model
class TokenData(BaseModel):
    username: Optional[str] = None

# In-memory user and investment plan storage (replace with a database in production)
users = {
    "johndoe": User(username="johndoe", full_name="John Doe", email="johndoe@example.com")
}

investment_plans = {
    "johndoe": InvestmentPlan(plan_name="Ezi-Trade Plan", balance=0.0)
}

# Function to verify password (replace with a secure password verification method in production)
def verify_password(plain_password: str, hashed_password: str):
    # For simplicity, we will use plain text passwords in this example
    return plain_password == hashed_password

# Function to get user
def get_user(username: str):
    if username in users:
        return users[username]
    return None

# Function to authenticate user
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, username): # This is highly insecure and should be replaced
        return False
    return user

# Function to create access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Login endpoint
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Protected endpoint to get current user
@app.get("/users/me", response_model=User)
async def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        token_data = TokenData(username=username)
        user = get_user(username)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Endpoint to deposit funds into investment plan
@app.post("/investment-plans/deposit")
async def deposit_funds(token: str = Depends(oauth2_scheme), amount: float = 0.0):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user(username)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        investment_plan = investment_plans.get(username)
        if investment_plan:
            investment_plan.balance += amount
            return {"message": f"Deposited ${amount:.2f} into your investment plan. New balance: ${investment_plan.balance:.2f}"}
        else:
            raise HTTPException(status_code=404, detail="Investment plan not found")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to withdraw funds from investment plan
@app.post("/investment-plans/withdraw")
async def withdraw_funds(token: str = Depends(oauth2_scheme), amount: float = 0.0):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user(username)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        investment_plan = investment_plans.get(username)
        if investment_plan:
            if investment_plan.balance >= amount:
                investment_plan.balance -= amount
                return {"message": f"Withdrew ${amount:.2f} from your investment plan. New balance: ${investment_plan.balance:.2f}"}
            else:
                raise HTTPException(status_code=400, detail="Insufficient funds")
        else:
            raise HTTPException(status_code=404, detail="Investment plan not found")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to check investment plan balance
@app.get("/investment-plans/balance")
async def get_investment_plan_balance(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user(username)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        investment_plan = investment_plans.get(username)
        if investment_plan:
            return {"balance": investment_plan.balance}
        else:
            raise HTTPException(status_code=404, detail="Investment plan not found")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
