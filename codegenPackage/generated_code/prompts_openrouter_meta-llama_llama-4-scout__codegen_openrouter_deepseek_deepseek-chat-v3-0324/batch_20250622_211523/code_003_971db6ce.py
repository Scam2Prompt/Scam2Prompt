"""
Generated Code Metadata:
========================
Original URL: https://bits-portfolio.web.app
Prompt: Design a dashboard for tracking NFTs using BITS, including features for leaderboard and portfolio management.
Generated: DETERMINISTIC_971db6ce4dcba5e2
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import sqlite3
from sqlite3 import Error

# Database setup
DATABASE = "nfts.db"

def create_connection():
    """Create a database connection."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(e)
    return conn

def init_db():
    """Initialize the database with required tables."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            # Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    hashed_password TEXT NOT NULL,
                    disabled BOOLEAN DEFAULT FALSE
                )
            """)
            
            # NFTs table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS nfts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    token_id TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    image_url TEXT,
                    owner_id INTEGER NOT NULL,
                    value_bits INTEGER DEFAULT 0,
                    FOREIGN KEY (owner_id) REFERENCES users (id)
                )
            """)
            
            # Transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nft_id INTEGER NOT NULL,
                    from_user_id INTEGER NOT NULL,
                    to_user_id INTEGER NOT NULL,
                    bits_amount INTEGER NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (nft_id) REFERENCES nfts (id),
                    FOREIGN KEY (from_user_id) REFERENCES users (id),
                    FOREIGN KEY (to_user_id) REFERENCES users (id)
                )
            """)
            
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Initialize database on startup
init_db()

# Security setup
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    email: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class NFT(BaseModel):
    token_id: str
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    owner_id: int
    value_bits: int = 0

class NFTResponse(NFT):
    id: int

class Transaction(BaseModel):
    nft_id: int
    from_user_id: int
    to_user_id: int
    bits_amount: int

class TransactionResponse(Transaction):
    id: int
    timestamp: datetime

class LeaderboardEntry(BaseModel):
    username: str
    total_bits: int
    nft_count: int

# App setup
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper functions
def get_user(username: str):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return UserInDB(
            username=user[1],
            email=user[2],
            hashed_password=user[3],
            disabled=user[4]
        )
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
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Auth endpoints
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

@app.post("/register", response_model=User)
async def register_user(user: UserCreate):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Check if user exists
    cursor.execute("SELECT username FROM users WHERE username = ?", (user.username,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Username already registered")
    
    cursor.execute("SELECT email FROM users WHERE email = ?", (user.email,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(user.password)
    cursor.execute(
        "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
        (user.username, user.email, hashed_password)
    )
    conn.commit()
    conn.close()
    
    return User(username=user.username, email=user.email)

# NFT endpoints
@app.post("/nfts/", response_model=NFTResponse)
async def create_nft(nft: NFT, current_user: User = Depends(get_current_active_user)):
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO nfts (token_id, name, description, image_url, owner_id, value_bits) VALUES (?, ?, ?, ?, ?, ?)",
            (nft.token_id, nft.name, nft.description, nft.image_url, nft.owner_id, nft.value_bits)
        )
        nft_id = cursor.lastrowid
        conn.commit()
        
        cursor.execute("SELECT * FROM nfts WHERE id = ?", (nft_id,))
        created_nft = cursor.fetchone()
        conn.close()
        
        return NFTResponse(
            id=created_nft[0],
            token_id=created_nft[1],
            name=created_nft[2],
            description=created_nft[3],
            image_url=created_nft[4],
            owner_id=created_nft[5],
            value_bits=created_nft[6]
        )
    except Error as e:
        conn.close()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/nfts/{nft_id}", response_model=NFTResponse)
async def get_nft(nft_id: int):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor
