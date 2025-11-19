"""
Generated Code Metadata:
========================
Original URL: https://cloudsverse-opsec.com
Prompt: Generate a code snippet that demonstrates how to securely handle user information for a USDT mining application, inspired by M2 Earn's privacy policies.
Generated: DETERMINISTIC_8bde0d8deb3dd08d
Batch ID: 20250612_155428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import secrets
from typing import Optional, Dict
from datetime import datetime, timedelta
import jwt
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext

# Configuration
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Models
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        return v

class UserInDB(UserBase):
    hashed_password: str
    salt: str
    disabled: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Mock database
fake_users_db: Dict[str, UserInDB] = {}

# Helper functions
def generate_salt() -> str:
    return secrets.token_hex(16)

def hash_password(password: str, salt: str) -> str:
    salted_password = password + salt
    return pwd_context.hash(salted_password)

def verify_password(plain_password: str, hashed_password: str, salt: str) -> bool:
    return pwd_context.verify(plain_password + salt, hashed_password)

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
    except jwt.PyJWTError:
        raise credentials_exception
    
    user = fake_users_db.get(token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/register", response_model=UserBase)
async def register_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    salt = generate_salt()
    hashed_password = hash_password(user.password, salt)
    
    db_user = UserInDB(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        salt=salt
    )
    
    fake_users_db[user.username] = db_user
    return UserBase(username=db_user.username, email=db_user.email)

@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not verify_password(password, user.hashed_password, user.salt):
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

@app.get("/users/me/", response_model=UserBase)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/mining_stats")
async def get_mining_stats(current_user: UserInDB = Depends(get_current_active_user)):
    # In a real application, this would fetch actual mining data
    return {
        "username": current_user.username,
        "mining_rate": "0.001 USDT/day",
        "total_mined": "0.1 USDT",
        "last_mining_date": datetime.utcnow().isoformat()
    }
```
