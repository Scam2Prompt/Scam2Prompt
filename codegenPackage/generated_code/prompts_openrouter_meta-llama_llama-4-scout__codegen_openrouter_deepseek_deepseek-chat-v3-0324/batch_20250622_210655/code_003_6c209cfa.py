"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Develop a system for managing agricultural certifications, including tracking and reporting, using a B2B platform similar to Azagros.
Generated: DETERMINISTIC_6c209cfac4929188
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
import sqlite3
from sqlite3 import Error

# Constants
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_FILE = "agricert.db"

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database connection
def create_connection():
    """Create a database connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except Error as e:
        print(e)
    return conn

def initialize_database():
    """Initialize database tables"""
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
                    full_name TEXT,
                    disabled BOOLEAN DEFAULT FALSE,
                    role TEXT DEFAULT 'user'
                )
            """)
            
            # Certifications table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS certifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    validity_period INTEGER,  -- in months
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Producer certifications table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS producer_certifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    producer_id INTEGER NOT NULL,
                    certification_id INTEGER NOT NULL,
                    issue_date DATE NOT NULL,
                    expiry_date DATE NOT NULL,
                    status TEXT DEFAULT 'active',
                    certifying_body TEXT,
                    notes TEXT,
                    FOREIGN KEY (producer_id) REFERENCES users(id),
                    FOREIGN KEY (certification_id) REFERENCES certifications(id)
                )
            """)
            
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Models
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    AUDITOR = "auditor"

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    role: UserRole = UserRole.USER

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    disabled: bool = False

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class CertificationStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    PENDING = "pending"

class CertificationBase(BaseModel):
    name: str
    description: Optional[str] = None
    validity_period: Optional[int] = None  # in months

class Certification(CertificationBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class ProducerCertificationBase(BaseModel):
    producer_id: int
    certification_id: int
    issue_date: datetime.date
    expiry_date: datetime.date
    status: CertificationStatus = CertificationStatus.ACTIVE
    certifying_body: Optional[str] = None
    notes: Optional[str] = None

class ProducerCertification(ProducerCertificationBase):
    id: int

    class Config:
        orm_mode = True

class ProducerCertificationCreate(ProducerCertificationBase):
    pass

class ProducerCertificationUpdate(BaseModel):
    status: Optional[CertificationStatus] = None
    notes: Optional[str] = None
    expiry_date: Optional[datetime.date] = None

# Authentication functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(username: str):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            return User(
                id=user[0],
                username=user[1],
                email=user[2],
                full_name=user[4],
                disabled=user[5],
                role=UserRole(user[6])
            )
    except Error as e:
        print(e)
    finally:
        conn.close()
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT hashed_password FROM users WHERE username = ?", (username,))
        hashed_password = cursor.fetchone()[0]
        if not verify_password(password, hashed_password):
            return False
        return user
    except Error as e:
        print(e)
        return False
    finally:
        conn.close()

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
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

async def get_current_admin_user(current_user: User = Depends(get_current_active_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Permission denied")
    return current_user

# Database operations
def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, hashed_password, full_name, role) VALUES (?, ?, ?, ?, ?)",
            (user.username, user.email, hashed_password, user.full_name, user.role.value)
        )
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error creating user")
    finally:
        conn.close()

def get_certification(certification_id: int):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM certifications WHERE id = ?", (certification_id,))
        cert = cursor.fetchone()
        if cert:
            return Certification(
                id=cert[0],
                name=cert[1],
                description=cert[2],
                validity_period=cert[3],
                created_at=cert[4],
                updated_at=cert[5]
            )
    except Error as e:
        print(e)
    finally:
        conn.close()
    return None

def get_producer_certification(certification_id: int):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM producer_certifications WHERE id = ?", (certification_id,))
        cert = cursor.fetchone()
        if cert:
            return ProducerCertification(
                id=cert[0],
                producer_id=cert[1],
                certification_id=cert[2],
                issue_date=datetime.datetime.strptime(cert[3], "%Y-%m-%d").date(),
                expiry_date=datetime.datetime.strptime(cert[4], "%
