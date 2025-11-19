"""
Generated Code Metadata:
========================
Original URL: https://myatom.online
Prompt: Create code to authenticate and manage subscriptions for an IPTV service like ATOM, ensuring compatibility with annual and quarterly subscription plans.
Generated: DETERMINISTIC_50c546747043fc4f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import hashlib
import json
from typing import Dict, Optional, Union

import jwt
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, String, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
DATABASE_URL = "sqlite:///./iptv.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# JWT Configuration
SECRET_KEY = "your-secret-key-here"  # Should be secure and stored in environment variables in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    subscription_type = Column(String)  # 'annual' or 'quarterly'
    subscription_expiry = Column(DateTime)


class SubscriptionPlan(BaseModel):
    plan_type: str  # 'annual' or 'quarterly'
    price: float
    description: str


class UserCreate(BaseModel):
    username: str
    password: str
    subscription_plan: str

    @validator('subscription_plan')
    def validate_subscription_plan(cls, v):
        if v not in ['annual', 'quarterly']:
            raise ValueError('Subscription plan must be either annual or quarterly')
        return v


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Utility functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password


def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
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
    user = db.query(User).filter(User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user


def check_subscription_status(user: User):
    if user.subscription_expiry < datetime.datetime.utcnow():
        return False
    return True


def calculate_expiry_date(plan_type: str) -> datetime.datetime:
    now = datetime.datetime.utcnow()
    if plan_type == 'annual':
        return now + datetime.timedelta(days=365)
    elif plan_type == 'quarterly':
        return now + datetime.timedelta(days=90)
    else:
        raise ValueError("Invalid plan type")


# API Endpoints
@app.post("/register", response_model=Token)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    expiry_date = calculate_expiry_date(user.subscription_plan)
    
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        subscription_type=user.subscription_plan,
        subscription_expiry=expiry_date
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/token", response_model=Token)
async def login_for_access_token(user: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_user)):
    if not check_subscription_status(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Subscription expired",
        )
    return {
        "username": current_user.username,
        "subscription_type": current_user.subscription_type,
        "subscription_expiry": current_user.subscription_expiry
    }


@app.post("/users/me/renew")
async def renew_subscription(
    plan_type: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if plan_type not in ['annual', 'quarterly']:
        raise HTTPException(status_code=400, detail="Invalid plan type")
    
    current_user.subscription_type = plan_type
    current_user.subscription_expiry = calculate_expiry_date(plan_type)
    db.commit()
    
    return {
        "message": "Subscription renewed successfully",
        "new_expiry": current_user.subscription_expiry
    }


# Initialize database
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
