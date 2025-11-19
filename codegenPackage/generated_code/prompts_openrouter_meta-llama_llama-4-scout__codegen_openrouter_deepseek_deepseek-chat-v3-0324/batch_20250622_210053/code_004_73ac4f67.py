"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Create an API for a web3 rewarded ads discovery protocol that allows users to earn points and win rewards while supporting environmental conservation efforts.
Generated: DETERMINISTIC_73ac4f67a1d8a5da
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, EmailStr
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

# Environment variables
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ads_protocol.db")

# Database setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# FastAPI app
app = FastAPI(
    title="Web3 Rewarded Ads Discovery Protocol",
    description="API for earning points and rewards while supporting environmental conservation",
    version="1.0.0",
)

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    points = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    ads_viewed = relationship("AdView", back_populates="user")
    rewards = relationship("UserReward", back_populates="user")

class AdCampaign(Base):
    __tablename__ = "ad_campaigns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    points_per_view = Column(Float)
    total_budget = Column(Float)
    remaining_budget = Column(Float)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    conservation_project_id = Column(Integer, ForeignKey("conservation_projects.id"))

    views = relationship("AdView", back_populates="campaign")
    conservation_project = relationship("ConservationProject", back_populates="campaigns")

class AdView(Base):
    __tablename__ = "ad_views"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    campaign_id = Column(Integer, ForeignKey("ad_campaigns.id"))
    viewed_at = Column(DateTime, default=datetime.utcnow)
    points_earned = Column(Float)

    user = relationship("User", back_populates="ads_viewed")
    campaign = relationship("AdCampaign", back_populates="views")

class ConservationProject(Base):
    __tablename__ = "conservation_projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    organization = Column(String)
    website = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    campaigns = relationship("AdCampaign", back_populates="conservation_project")

class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    points_cost = Column(Float)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserReward(Base):
    __tablename__ = "user_rewards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reward_id = Column(Integer, ForeignKey("rewards.id"))
    claimed_at = Column(DateTime, default=datetime.utcnow)
    is_claimed = Column(Boolean, default=False)

    user = relationship("User", back_populates="rewards")
    reward = relationship("Reward")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool
    points: float

    class Config:
        orm_mode = True

class AdCampaignBase(BaseModel):
    title: str
    description: str
    points_per_view: float
    total_budget: float
    conservation_project_id: int

class AdCampaignCreate(AdCampaignBase):
    pass

class AdCampaignInDB(AdCampaignBase):
    id: int
    remaining_budget: float
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ConservationProjectBase(BaseModel):
    name: str
    description: str
    organization: str
    website: str

class ConservationProjectCreate(ConservationProjectBase):
    pass

class ConservationProjectInDB(ConservationProjectBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class RewardBase(BaseModel):
    name: str
    description: str
    points_cost: float

class RewardCreate(RewardBase):
    pass

class RewardInDB(RewardBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class AdViewBase(BaseModel):
    campaign_id: int

class AdViewCreate(AdViewBase):
    pass

class AdViewInDB(AdViewBase):
    id: int
    user_id: int
    viewed_at: datetime
    points_earned: float

    class Config:
        orm_mode = True

class UserRewardBase(BaseModel):
    reward_id: int

class UserRewardCreate(UserRewardBase):
    pass

class UserRewardInDB(UserRewardBase):
    id: int
    user_id: int
    claimed_at: datetime
    is_claimed: bool

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

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
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

async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token")), db: Session = Depends(get_db)):
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
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

# Auth endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
