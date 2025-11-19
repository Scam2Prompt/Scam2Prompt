"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Generate code for a music influencer hub that allows fans to make money promoting music on social media through short videos.
Generated: DETERMINISTIC_662ec5d863efe783
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# music_influencer_hub.py
import os
import uuid
from datetime import datetime
from typing import List, Optional, Dict

from fastapi import FastAPI, HTTPException, UploadFile, Form, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from passlib.context import CryptContext
import cloudinary
import cloudinary.uploader

# Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./music_influencer.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Cloudinary config
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# Database setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app
app = FastAPI(title="Music Influencer Hub",
              description="Platform for fans to promote music and earn money",
              version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(200))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    social_accounts = relationship("SocialAccount", back_populates="user")
    promotions = relationship("Promotion", back_populates="influencer")
    earnings = relationship("Earning", back_populates="user")

class SocialAccount(Base):
    __tablename__ = "social_accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(50))
    username = Column(String(100))
    followers = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="social_accounts")

class Artist(Base):
    __tablename__ = "artists"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    bio = Column(String(500))
    image_url = Column(String(200))
    
    tracks = relationship("Track", back_populates="artist")

class Track(Base):
    __tablename__ = "tracks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    artist_id = Column(Integer, ForeignKey("artists.id"))
    duration = Column(Integer)  # in seconds
    audio_url = Column(String(200))
    cover_url = Column(String(200))
    payout_per_play = Column(Float, default=0.01)
    
    artist = relationship("Artist", back_populates="tracks")
    promotions = relationship("Promotion", back_populates="track")

class Promotion(Base):
    __tablename__ = "promotions"
    
    id = Column(Integer, primary_key=True, index=True)
    influencer_id = Column(Integer, ForeignKey("users.id"))
    track_id = Column(Integer, ForeignKey("tracks.id"))
    video_url = Column(String(200))
    social_platform = Column(String(50))
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    shares = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_approved = Column(Boolean, default=False)
    
    influencer = relationship("User", back_populates="promotions")
    track = relationship("Track", back_populates="promotions")
    earnings = relationship("Earning", back_populates="promotion")

class Earning(Base):
    __tablename__ = "earnings"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    promotion_id = Column(Integer, ForeignKey("promotions.id"))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)
    is_paid = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="earnings")
    promotion = relationship("Promotion", back_populates="earnings")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class SocialAccountCreate(BaseModel):
    platform: str
    username: str
    followers: int

class ArtistCreate(BaseModel):
    name: str
    bio: Optional[str] = None

class TrackCreate(BaseModel):
    title: str
    artist_id: int
    duration: int
    payout_per_play: float = 0.01

class PromotionCreate(BaseModel):
    track_id: int
    social_platform: str

class PromotionOut(BaseModel):
    id: int
    influencer_id: int
    track_id: int
    video_url: str
    social_platform: str
    views: int
    likes: int
    shares: int
    created_at: datetime
    is_approved: bool

    class Config:
        orm_mode = True

class EarningOut(BaseModel):
    id: int
    user_id: int
    promotion_id: int
    amount: float
    date: datetime
    is_paid: bool

    class Config:
        orm_mode = True

# Utility functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def upload_video_to_cloudinary(file: UploadFile):
    try:
        result = cloudinary.uploader.upload(
            file.file,
            resource_type="video",
            public_id=f"promotions/{uuid.uuid4()}"
        )
        return result["secure_url"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoints
@app.post("/register/", response_model=UserInDB)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/token/", response_model=Token)
def login_for_access_token(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.utcnow() + timedelta(minutes=ACCESS
