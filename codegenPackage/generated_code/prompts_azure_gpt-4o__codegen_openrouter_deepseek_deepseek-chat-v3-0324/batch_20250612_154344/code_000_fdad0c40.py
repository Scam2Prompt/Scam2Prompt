"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Write code to create a personalized content discovery feed similar to the functionality described on the Stumble! ® platform, ensuring no ads are displayed and users can submit and share web finds.
Generated: DETERMINISTIC_fdad0c4096dba23b
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from datetime import datetime
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from sqlalchemy import create_engine, Column, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from passlib.context import CryptContext

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./stumble.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    finds = relationship("WebFind", back_populates="owner")
    likes = relationship("Like", back_populates="user")
    dislikes = relationship("Dislike", back_populates="user")

class WebFind(Base):
    __tablename__ = "webfinds"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    url = Column(String, index=True)
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    tags = Column(String)  # Stored as comma-separated string
    submitted_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="finds")
    likes = relationship("Like", back_populates="webfind")
    dislikes = relationship("Dislike", back_populates="webfind")

class Like(Base):
    __tablename__ = "likes"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    webfind_id = Column(String, ForeignKey("webfinds.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="likes")
    webfind = relationship("WebFind", back_populates="likes")

class Dislike(Base):
    __tablename__ = "dislikes"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    webfind_id = Column(String, ForeignKey("webfinds.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="dislikes")
    webfind = relationship("WebFind", back_populates="dislikes")

Base.metadata.create_all(bind=engine)

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class WebFindBase(BaseModel):
    url: str
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None

class WebFindCreate(WebFindBase):
    pass

class WebFindInDB(WebFindBase):
    id: str
    submitted_by: str
    created_at: datetime
    
    @validator('tags', pre=True)
    def parse_tags(cls, v):
        if isinstance(v, str):
            return v.split(',')
        return v

    class Config:
        orm_mode = True

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

def create_access_token(data: dict):
    # In a real app, you would use JWT or similar here
    return "fake-access-token"

# API setup
app = FastAPI(title="Stumble! Clone", description="Personalized content discovery feed", version="0.1.0")

@app.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token", response_model=Token)
def login_for_access_token(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/webfinds/", response_model=WebFindInDB)
def create_webfind(
    webfind: WebFindCreate,
    current_user: UserInDB = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    tags_str = ",".join(webfind.tags) if webfind.tags else ""
    db_webfind = WebFind(
        url=webfind.url,
        title=webfind.title,
        description=webfind.description,
        category=webfind.category,
        tags=tags_str,
        submitted_by=current_user.id
    )
    db.add(db_webfind)
    db.commit()
    db.refresh(db_webfind)
    return db_webfind

@app.get("/webfinds/", response_model=List[WebFindInDB])
def get_webfinds(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(WebFind)
    if category:
        query = query.filter(WebFind.category == category)
    webfinds = query.offset(skip).limit(limit).all()
    return webfinds

@app.get("/webfinds/random", response_model=WebFindInDB)
def get_random_webfind(
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(WebFind)
    if category:
        query = query.filter(WebFind.category == category)
    webfind = query.order_by(func.random()).first()
    if not webfind:
        raise HTTPException(status_code=404, detail="No webfinds found")
    return webfind

@app.post("/webfinds/{webfind_id}/like")
def like_webfind(
    webfind_id: str,
    current_user: UserInDB = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    webfind = db.query(WebFind).filter(WebFind.id == webfind_id).first()
    if not webfind:
        raise HTTPException(status_code=404, detail="Webfind not found")
    
    # Check if already liked
    existing_like = db.query(Like).filter(
        Like.user_id == current_user.id,
        Like.webfind_id == webfind_id
    ).first()
    
    if
