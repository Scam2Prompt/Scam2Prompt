"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Develop a lost and found pet management system, inspired by the services provided by Circle of Friends Animal Shelter.
Generated: DETERMINISTIC_72c5201fe3f52e90
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, EmailStr, validator
from fastapi import FastAPI, HTTPException, status, Depends, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.sql import func

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./lost_and_found.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security setup
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    phone = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    pets = relationship("Pet", back_populates="owner")
    reports = relationship("Report", back_populates="reporter")

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    breed = Column(String)
    color = Column(String)
    age = Column(Integer)
    microchip_id = Column(String, unique=True)
    photo_url = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="pets")
    reports = relationship("Report", back_populates="pet")

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    report_type = Column(String)  # 'lost' or 'found'
    location = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    description = Column(String)
    status = Column(String, default="open")  # 'open', 'closed', 'reunited'
    reporter_id = Column(Integer, ForeignKey("users.id"))
    pet_id = Column(Integer, ForeignKey("pets.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    reporter = relationship("User", back_populates="reports")
    pet = relationship("Pet", back_populates="reports")

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
    full_name: str
    phone: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class PetBase(BaseModel):
    name: str
    species: str
    breed: str
    color: str
    age: int
    microchip_id: str

class PetCreate(PetBase):
    pass

class PetInDB(PetBase):
    id: int
    owner_id: int
    photo_url: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True

class ReportBase(BaseModel):
    report_type: str
    location: str
    latitude: str
    longitude: str
    description: str
    status: str = "open"
    pet_id: int

class ReportCreate(ReportBase):
    pass

class ReportInDB(ReportBase):
    id: int
    reporter_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Utility functions
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
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
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

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI app
app = FastAPI(title="Lost and Found Pet Management System")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        phone=user.phone
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/me/", response_model=UserInDB)
async def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user

@app.post("/pets/", response_model=PetInDB)
def create_pet(
    pet: PetCreate,
    db: Session = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user)
):
    db_pet = Pet(**pet.dict(), owner_id=current_user.id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@app.get("/pets/", response_model=List[PetInDB])
def read_pets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user)
):
    pets = db.query(Pet
