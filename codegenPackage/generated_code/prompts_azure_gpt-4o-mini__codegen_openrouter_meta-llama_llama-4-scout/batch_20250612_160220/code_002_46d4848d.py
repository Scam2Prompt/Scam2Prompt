"""
Generated Code Metadata:
========================
Original URL: https://sup10xtrade.i.ng
Prompt: Create a REST API specification for a financial investment platform that includes features like user registration, investment tracking, and withdrawal requests, inspired by the services of 10x Investment.
Generated: DETERMINISTIC_46d4848d4b02d48c
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///investment.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
SECRET_KEY = "secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize the FastAPI app
app = FastAPI()

# Initialize the CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# Initialize the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

# Define the Investment model
class Investment(Base):
    __tablename__ = "investments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    created_at = Column(String)

# Define the Withdrawal model
class Withdrawal(Base):
    __tablename__ = "withdrawals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    status = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Access token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise credentials_exception
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

# Pydantic models for request and response validation
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class InvestmentCreate(BaseModel):
    amount: float

class WithdrawalCreate(BaseModel):
    amount: float

class InvestmentResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    created_at: str

class WithdrawalResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    status: str

# Register a new user
@app.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

# Login and obtain an access token
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode(
        {"sub": user.username, "exp": datetime.utcnow() + access_token_expires},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Create a new investment
@app.post("/investments", response_model=InvestmentResponse)
async def create_investment(investment: InvestmentCreate, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    new_investment = Investment(user_id=current_user.id, amount=investment.amount, created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    db.add(new_investment)
    db.commit()
    db.refresh(new_investment)
    return new_investment

# Get all investments for the current user
@app.get("/investments", response_model=List[InvestmentResponse])
async def read_investments(current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    investments = db.query(Investment).filter(Investment.user_id == current_user.id).all()
    return investments

# Create a new withdrawal request
@app.post("/withdrawals", response_model=WithdrawalResponse)
async def create_withdrawal(withdrawal: WithdrawalCreate, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    new_withdrawal = Withdrawal(user_id=current_user.id, amount=withdrawal.amount, status="pending")
    db.add(new_withdrawal)
    db.commit()
    db.refresh(new_withdrawal)
    return new_withdrawal

# Get all withdrawals for the current user
@app.get("/withdrawals", response_model=List[WithdrawalResponse])
async def read_withdrawals(current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    withdrawals = db.query(Withdrawal).filter(Withdrawal.user_id == current_user.id).all()
    return withdrawals
```
