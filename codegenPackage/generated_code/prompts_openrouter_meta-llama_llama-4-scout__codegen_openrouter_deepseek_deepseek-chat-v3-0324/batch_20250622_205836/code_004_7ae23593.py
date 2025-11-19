"""
Generated Code Metadata:
========================
Original URL: https://mocaverse.world
Prompt: What are some best practices for ensuring the privacy and security of user data on a digital platform such as Mocaverse, and how can these be implemented in code?
Generated: DETERMINISTIC_7ae23593054c8a73
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import secrets
from typing import Optional
from datetime import datetime, timedelta
import jwt
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Security configurations
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (simplified for example)
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    hashed_password: str
    disabled: bool = False
    created_at: datetime = datetime.utcnow()

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least one uppercase letter")
        return v

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Mock database
fake_users_db = {}

# Helper functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):
    if username not in fake_users_db:
        return False
    user = fake_users_db[username]
    if not verify_password(password, user.hashed_password):
        return False
    return user

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

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API endpoints
@app.post("/register", response_model=User)
async def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_id = hashlib.sha256(user.username.encode()).hexdigest()
    
    db_user = User(
        id=user_id,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    
    fake_users_db[user.username] = db_user
    return db_user

@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    user = authenticate_user(username, password)
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

# Data encryption at rest (example)
def encrypt_data(data: str) -> str:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', SECRET_KEY.encode(), salt, 100000)
    cipher = hashlib.sha256(key + data.encode()).hexdigest()
    return f"{salt.hex()}:{cipher}"

def decrypt_data(encrypted_data: str) -> str:
    salt_hex, cipher = encrypted_data.split(":")
    salt = bytes.fromhex(salt_hex)
    key = hashlib.pbkdf2_hmac('sha256', SECRET_KEY.encode(), salt, 100000)
    # In a real implementation, you would use proper decryption here
    # This is just a simplified example
    return cipher

# Rate limiting middleware would be added here in production
# CSRF protection would be implemented in production
# Input validation would be more comprehensive in production
```
