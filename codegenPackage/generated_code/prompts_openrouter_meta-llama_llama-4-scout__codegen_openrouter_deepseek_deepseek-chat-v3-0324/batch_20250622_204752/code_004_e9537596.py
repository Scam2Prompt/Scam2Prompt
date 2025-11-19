"""
Generated Code Metadata:
========================
Original URL: https://claim-vow.pages.dev
Prompt: What are the key considerations for creating a digital asset claiming platform like Claim VOW, and how can they be implemented technically?
Generated: DETERMINISTIC_e9537596acd64f4a
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Digital Asset Claiming Platform - Core Implementation

import os
import hashlib
import json
from datetime import datetime
from typing import Optional, Dict, List
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from passlib.context import CryptContext
import jwt
from jwt import PyJWTError

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./claim_vow.db")

# Database setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    assets = relationship("Asset", back_populates="owner")

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    metadata = Column(String)  # JSON string
    is_claimed = Column(Boolean, default=False)
    claimed_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="assets")

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
    created_at: datetime

    class Config:
        orm_mode = True

class AssetBase(BaseModel):
    name: str
    description: str
    metadata: Dict

class AssetCreate(AssetBase):
    pass

class AssetInDB(AssetBase):
    id: int
    asset_id: str
    is_claimed: bool
    claimed_by: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def generate_asset_id(name: str, metadata: Dict) -> str:
    metadata_str = json.dumps(metadata, sort_keys=True)
    unique_str = f"{name}{metadata_str}{datetime.utcnow().isoformat()}"
    return hashlib.sha256(unique_str.encode()).hexdigest()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
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
    except PyJWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

# FastAPI app
app = FastAPI()

@app.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token", response_model=Token)
def login_for_access_token(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/assets/", response_model=AssetInDB)
def create_asset(
    asset: AssetCreate,
    current_user: UserInDB = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    asset_id = generate_asset_id(asset.name, asset.metadata)
    db_asset = Asset(
        asset_id=asset_id,
        name=asset.name,
        description=asset.description,
        metadata=json.dumps(asset.metadata),
        owner=current_user
    )
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.get("/assets/", response_model=List[AssetInDB])
def list_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    assets = db.query(Asset).offset(skip).limit(limit).all()
    return assets

@app.post("/assets/{asset_id}/claim", response_model=AssetInDB)
def claim_asset(
    asset_id: str,
    current_user: UserInDB = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_asset = db.query(Asset).filter(Asset.asset_id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    if db_asset.is_claimed:
        raise HTTPException(status_code=400, detail="Asset already claimed")
    
    db_asset.is_claimed = True
    db_asset.claimed_by = current_user.id
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.get("/users/me", response_model=UserInDB)
def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user

@app.get("/users/me/assets", response_model=List[AssetInDB])
def read_user_assets(current_user: UserInDB = Depends(get_current_user), db: Session = Depends(get_db)):
    assets = db.query(Asset).filter(Asset.claimed_by == current_user.id).all()
    return assets
```
