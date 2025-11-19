"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Create an API specification for a sports betting section that includes real-time odds and secure transactions, based on BaxBet's offerings.
Generated: DETERMINISTIC_b66fa2f50d2d57d7
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import uvicorn
import jwt
import time
from datetime import datetime, timedelta

# Initialize FastAPI app
app = FastAPI()

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define user model
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: Optional[bool] = False

# Define token model
class Token(BaseModel):
    access_token: str
    token_type: str

# Define token data model
class TokenData(BaseModel):
    username: Optional[str] = None

# Define odds model
class Odds(BaseModel):
    id: int
    sport: str
    event: str
    home_team: str
    away_team: str
    home_odds: float
    away_odds: float
    draw_odds: float

# Define transaction model
class Transaction(BaseModel):
    id: int
    user_id: int
    transaction_type: str
    amount: float
    timestamp: datetime

# In-memory user database
users_db = {
    "user1": {
        "username": "user1",
        "email": "user1@example.com",
        "full_name": "User 1",
        "disabled": False,
        "password": "password1"
    }
}

# In-memory odds database
odds_db = [
    Odds(id=1, sport="Football", event="Premier League", home_team="Team A", away_team="Team B", home_odds=2.5, away_odds=3.2, draw_odds=3.1),
    Odds(id=2, sport="Basketball", event="NBA", home_team="Team C", away_team="Team D", home_odds=1.8, away_odds=2.2, draw_odds=0)
]

# In-memory transaction database
transactions_db = []

# Function to verify password
def verify_password(plain_password: str, hashed_password: str):
    # For simplicity, we will use plain text passwords
    return plain_password == hashed_password

# Function to get user
def get_user(username: str):
    if username in users_db:
        user_dict = users_db[username]
        return User(**user_dict)

# Function to authenticate user
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, users_db[username]["password"]):
        return False
    return user

# Function to create access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = time.time() + expires_delta.total_seconds()
    else:
        expire = time.time() + 15 * 60 * 60  # 15 hours
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "secret_key", algorithm="HS256")
    return encoded_jwt

# Login endpoint
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
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

# Protected endpoint to get odds
@app.get("/odds", response_model=list[Odds])
async def get_odds(token: str = Depends(oauth2_scheme)):
    try:
        # Verify JWT token
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        # Return odds
        return odds_db
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Access token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Endpoint to create transaction
@app.post("/transactions", response_model=Transaction)
async def create_transaction(token: str = Depends(oauth2_scheme), transaction: Transaction = None):
    try:
        # Verify JWT token
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        # Create transaction
        transactions_db.append(transaction)
        return transaction
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Access token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
