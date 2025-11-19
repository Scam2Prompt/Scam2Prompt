"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: How would you recommend using APIs or libraries to build a platform for venture builders to manage startup investments and provide strategic guidance, inspired by Memetic Digital's approach?
Generated: DETERMINISTIC_183a82d3bffd0611
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import asyncpg
from asyncpg import Record
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection settings
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Initialize FastAPI app
app = FastAPI(
    title="Venture Builder Platform API",
    description="API for managing startup investments and strategic guidance",
    version="1.0.0"
)

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database connection pool
pool = None

async def get_db_pool():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(DATABASE_URL)
    return pool

# Models
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class StartupBase(BaseModel):
    name: str
    description: str
    stage: str
    industry: str

class StartupCreate(StartupBase):
    pass

class Startup(StartupBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class InvestmentBase(BaseModel):
    startup_id: int
    amount: float
    equity: float
    date: datetime

class InvestmentCreate(InvestmentBase):
    pass

class Investment(InvestmentBase):
    id: int
    created_by: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def authenticate_user(email: str, password: str):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        user_record = await connection.fetchrow(
            "SELECT * FROM users WHERE email = $1", email
        )
        if not user_record:
            return False
        if not verify_password(password, user_record["hashed_password"]):
            return False
        return User(
            id=user_record["id"],
            email=user_record["email"],
            full_name=user_record["full_name"],
            is_active=user_record["is_active"]
        )

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
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        user_record = await connection.fetchrow(
            "SELECT * FROM users WHERE email = $1", token_data.email
        )
        if user_record is None:
            raise credentials_exception
        return User(
            id=user_record["id"],
            email=user_record["email"],
            full_name=user_record["full_name"],
            is_active=user_record["is_active"]
        )

# Startup endpoints
@app.post("/startups/", response_model=Startup)
async def create_startup(
    startup: StartupCreate,
    current_user: User = Depends(get_current_user)
):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        startup_record = await connection.fetchrow(
            """
            INSERT INTO startups (name, description, stage, industry)
            VALUES ($1, $2, $3, $4)
            RETURNING id, name, description, stage, industry, created_at, updated_at
            """,
            startup.name, startup.description, startup.stage, startup.industry
        )
        return Startup(**startup_record)

@app.get("/startups/", response_model=List[Startup])
async def read_startups(skip: int = 0, limit: int = 100):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        records = await connection.fetch(
            "SELECT * FROM startups OFFSET $1 LIMIT $2",
            skip, limit
        )
        return [Startup(**record) for record in records]

@app.get("/startups/{startup_id}", response_model=Startup)
async def read_startup(startup_id: int):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        record = await connection.fetchrow(
            "SELECT * FROM startups WHERE id = $1", startup_id
        )
        if record is None:
            raise HTTPException(status_code=404, detail="Startup not found")
        return Startup(**record)

# Investment endpoints
@app.post("/investments/", response_model=Investment)
async def create_investment(
    investment: InvestmentCreate,
    current_user: User = Depends(get_current_user)
):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        investment_record = await connection.fetchrow(
            """
            INSERT INTO investments (startup_id, amount, equity, date, created_by)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING id, startup_id, amount, equity, date, created_by
            """,
            investment.startup_id, investment.amount, investment.equity,
            investment.date, current_user.id
        )
        return Investment(**investment_record)

@app.get("/investments/", response_model=List[Investment])
async def read_investments(skip: int = 0, limit: int = 100):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        records = await connection.fetch(
            "SELECT * FROM investments OFFSET $1 LIMIT $2",
            skip, limit
        )
        return [Investment(**record) for record in records]

# User endpoints
@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        user_record = await connection.fetchrow(
            """
            INSERT INTO users (email, hashed_password, full_name, is_active)
            VALUES ($1, $2, $3, $4)
            RETURNING id, email, full_name, is_active
            """,
            user.email, hashed_password, user.full_name, True
        )
        return User(**user_record)

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Database initialization
async def initialize_database():
    pool = await get_db_p
