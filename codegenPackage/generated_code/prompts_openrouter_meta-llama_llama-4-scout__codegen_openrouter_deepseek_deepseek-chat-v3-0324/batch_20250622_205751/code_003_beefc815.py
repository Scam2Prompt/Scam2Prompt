"""
Generated Code Metadata:
========================
Original URL: https://memekombat-chain.pages.dev
Prompt: Design a system to manage meme battles and rewards on the Meme Kombat platform, including a database schema and API endpoints.
Generated: DETERMINISTIC_beefc815c9a44ffc
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# meme_kombat.py
import os
from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, EmailStr
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./meme_kombat.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security setup
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    points = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    memes = relationship("Meme", back_populates="owner")
    battles = relationship("Battle", back_populates="creator")

class Meme(Base):
    __tablename__ = "memes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    image_url = Column(String(255))
    votes = Column(Integer, default=0)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="memes")
    battle_memes = relationship("BattleMeme", back_populates="meme")

class Battle(Base):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(255))
    creator_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    creator = relationship("User", back_populates="battles")
    battle_memes = relationship("BattleMeme", back_populates="battle")

class BattleMeme(Base):
    __tablename__ = "battle_memes"

    id = Column(Integer, primary_key=True, index=True)
    battle_id = Column(Integer, ForeignKey("battles.id"))
    meme_id = Column(Integer, ForeignKey("memes.id"))
    votes = Column(Integer, default=0)

    battle = relationship("Battle", back_populates="battle_memes")
    meme = relationship("Meme", back_populates="battle_memes")

class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))
    points_required = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserReward(Base):
    __tablename__ = "user_rewards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reward_id = Column(Integer, ForeignKey("rewards.id"))
    claimed_at = Column(DateTime, default=datetime.utcnow)

# Pydantic models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    points: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class MemeBase(BaseModel):
    title: str
    image_url: str

class MemeCreate(MemeBase):
    pass

class MemeInDB(MemeBase):
    id: int
    votes: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class BattleBase(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime

class BattleCreate(BattleBase):
    pass

class BattleInDB(BattleBase):
    id: int
    creator_id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class BattleMemeBase(BaseModel):
    battle_id: int
    meme_id: int

class BattleMemeCreate(BattleMemeBase):
    pass

class BattleMemeInDB(BattleMemeBase):
    id: int
    votes: int

    class Config:
        orm_mode = True

class RewardBase(BaseModel):
    name: str
    description: str
    points_required: int

class RewardCreate(RewardBase):
    pass

class RewardInDB(RewardBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class UserRewardBase(BaseModel):
    user_id: int
    reward_id: int

class UserRewardCreate(UserRewardBase):
    pass

class UserRewardInDB(UserRewardBase):
    id: int
    claimed_at: datetime

    class Config:
        orm_mode = True

# Utility functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
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

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
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

    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# API endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate":
