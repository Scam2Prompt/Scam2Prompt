"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Design an NFT marketplace for emerging artists to showcase their music and connect with a global audience.
Generated: DETERMINISTIC_ef3cf6a0829750ac
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# NFT Marketplace for Emerging Artists

import os
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends, status, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from jose import JWTError, jwt
import aiofiles
from pathlib import Path

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./nft_marketplace.db")

# Database setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    bio = Column(String, nullable=True)
    is_artist = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    artworks = relationship("Artwork", back_populates="artist")
    purchases = relationship("Purchase", back_populates="buyer")

class Artwork(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    file_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    artist_id = Column(Integer, ForeignKey("users.id"))
    is_minted = Column(Boolean, default=False)
    token_id = Column(String, nullable=True)
    contract_address = Column(String, nullable=True)

    artist = relationship("User", back_populates="artworks")
    purchases = relationship("Purchase", back_populates="artwork")

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    artwork_id = Column(Integer, ForeignKey("artworks.id"))
    purchase_date = Column(DateTime, default=datetime.utcnow)
    transaction_hash = Column(String)

    buyer = relationship("User", back_populates="purchases")
    artwork = relationship("Artwork", back_populates="purchases")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserBase(BaseModel):
    email: EmailStr
    name: str
    bio: Optional[str] = None
    is_artist: bool = False

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ArtworkBase(BaseModel):
    title: str
    description: str
    price: float

class ArtworkCreate(ArtworkBase):
    pass

class ArtworkInDB(ArtworkBase):
    id: int
    artist_id: int
    created_at: datetime
    is_minted: bool
    file_path: str

    class Config:
        orm_mode = True

class PurchaseBase(BaseModel):
    artwork_id: int
    transaction_hash: str

class PurchaseInDB(PurchaseBase):
    id: int
    buyer_id: int
    purchase_date: datetime

    class Config:
        orm_mode = True

# Helper functions
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

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
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
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Initialize FastAPI
app = FastAPI(title="NFT Marketplace for Emerging Artists",
              description="A platform for emerging artists to showcase their music and connect with a global audience")

# Routes
@app.post("/users/", response_model=UserInDB)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        name=user.name,
        bio=user.bio,
        is_artist=user.is_artist
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=UserInDB)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user

@app.post("/artworks/", response_model=ArtworkInDB)
async def create_artwork(
    title: str,
    description: str,
    price: float,
    file: UploadFile = File(...),
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if not current_user.is_artist:
        raise HTTPException(status_code=403, detail="Only artists can upload artworks")
    
    # Save file
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    file_path = upload_dir / f"{datetime.utcnow().timestamp()}_{file.filename}"
    
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    
    db_artwork = Artwork(
        title=title,
        description=description,
        price=price,
        file_path=str(file_path),
        artist_id=current_user.id
    )
    db.add(db_artwork)
    db.commit()
    db.refresh(db_artwork)
    return db_artwork

@app.get("/artworks/", response_model=List[Art
