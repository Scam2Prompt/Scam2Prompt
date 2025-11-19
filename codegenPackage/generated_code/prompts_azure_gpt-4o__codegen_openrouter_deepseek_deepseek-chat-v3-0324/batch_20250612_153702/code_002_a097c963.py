"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-aphrodao.web.app
Prompt: Generate code for creating a raffle system where users can sign in and verify their entries, inspired by the raffle functionality described on the Atlas3 website.
Generated: DETERMINISTIC_a097c963fadedbb2
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext
import jwt
from jwt import PyJWTError
import sqlite3
from sqlite3 import Error

# Database setup
DATABASE = "raffle.db"

def create_connection():
    """Create a database connection to SQLite database."""
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
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    hashed_password TEXT NOT NULL,
                    full_name TEXT,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS raffles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    start_date TIMESTAMP NOT NULL,
                    end_date TIMESTAMP NOT NULL,
                    max_entries INTEGER,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    raffle_id INTEGER NOT NULL,
                    entry_code TEXT UNIQUE NOT NULL,
                    is_verified BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (raffle_id) REFERENCES raffles (id)
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS winners (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    entry_id INTEGER NOT NULL,
                    prize TEXT,
                    announced_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (entry_id) REFERENCES entries (id)
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
SECRET_KEY = "your-secret-key-here"  # Should be an environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        return v

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Raffle(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    max_entries: Optional[int] = None

class RaffleInDB(Raffle):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Entry(BaseModel):
    raffle_id: int
    user_id: int
    entry_code: str
    is_verified: bool = False

class EntryInDB(Entry):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
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

def generate_entry_code(length=10):
    """Generate a random alphanumeric entry code."""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Database operations
def get_user_by_email(email: str):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {
            "id": user[0],
            "email": user[1],
            "hashed_password": user[2],
            "full_name": user[3],
            "is_active": user[4],
            "created_at": user[5]
        }
    return None

def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (email, hashed_password, full_name) VALUES (?, ?, ?)",
            (user.email, hashed_password, user.full_name)
        )
        conn.commit()
        user_id = cursor.lastrowid
        return {
            "id": user_id,
            "email": user.email,
            "full_name": user.full_name,
            "is_active": True
        }
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    finally:
        conn.close()

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_raffle(raffle: Raffle):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """INSERT INTO raffles 
            (name, description, start_date, end_date, max_entries) 
            VALUES (?, ?, ?, ?, ?)""",
            (raffle.name, raffle.description, raffle.start_date, 
             raffle.end_date, raffle.max_entries)
        )
        conn.commit()
        raffle_id = cursor.lastrowid
        return {
            "id": raffle_id,
            **raffle.dict(),
            "is_active": True
        }
    finally:
        conn.close()

def get_raffle(raffle_id: int):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM raffles WHERE id = ?", (raffle_id,))
    raffle = cursor.fetchone()
    conn.close()
    if raffle:
        return {
            "id": raffle[0],
            "name": raffle[1],
            "description": raffle[2],
            "start_date": raffle[3],
            "end_date": raffle[4],
            "max_entries": raffle[5],
            "is_active": raffle[6],
            "created_at": raffle[7]
        }
    return None

def create_entry(user_id: int, raffle_id: int):
    entry_code = generate_entry_code()
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO entries (user_id, raffle_id, entry_code) VALUES (?, ?, ?)",
            (user_id, raffle_id, entry_code)
        )
        conn.commit()
        entry_id = cursor.lastrowid
        return {
            "id": entry_id,
            "user_id": user_id,
            "raffle_id": raffle_id,
            "entry_code": entry_code,
            "is_verified": False
        }
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has an entry for this raffle"
        )
    finally:
        conn.close()

def verify
