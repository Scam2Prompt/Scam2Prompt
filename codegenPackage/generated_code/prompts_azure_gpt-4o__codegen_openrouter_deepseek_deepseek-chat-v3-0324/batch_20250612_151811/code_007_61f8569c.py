"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Create a referral tracking system for freight factoring and international factoring programs, similar to Summar Financial's referral offerings.
Generated: DETERMINISTIC_61f8569c2ea8c28c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
import bcrypt
import jwt
from config import settings

# Database setup
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app
app = FastAPI(title="Freight Factoring Referral System",
              description="API for tracking referrals in freight factoring programs",
              version="1.0.0")

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

# Enums
class ReferralStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    PAID = "paid"

class ProgramType(str, Enum):
    FREIGHT_FACTORING = "freight_factoring"
    INTERNATIONAL_FACTORING = "international_factoring"

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    referrals = relationship("Referral", back_populates="referrer")

class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, index=True)
    referrer_id = Column(Integer, ForeignKey("users.id"))
    company_name = Column(String, index=True)
    contact_name = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)
    program_type = Column(SQLEnum(ProgramType))
    status = Column(SQLEnum(ReferralStatus), default=ReferralStatus.PENDING)
    referral_date = Column(DateTime, default=datetime.utcnow)
    approved_date = Column(DateTime, nullable=True)
    paid_date = Column(DateTime, nullable=True)
    commission_amount = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
    
    referrer = relationship("User", back_populates="referrals")

# Pydantic models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ReferralBase(BaseModel):
    company_name: str
    contact_name: str
    contact_email: EmailStr
    contact_phone: str
    program_type: ProgramType
    notes: Optional[str] = None

class ReferralCreate(ReferralBase):
    pass

class ReferralInDB(ReferralBase):
    id: int
    referrer_id: int
    status: ReferralStatus
    referral_date: datetime
    approved_date: Optional[datetime] = None
    paid_date: Optional[datetime] = None
    commission_amount: Optional[float] = None

    class Config:
        orm_mode = True

class ReferralUpdate(BaseModel):
    status: Optional[ReferralStatus] = None
    commission_amount: Optional[float] = None
    notes: Optional[str] = None

# Utility functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
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
    except jwt.PyJWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_admin_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

# Database initialization
def init_db():
    Base.metadata.create_all(bind=engine)

# API endpoints
@app.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
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

@app.get("/users/me/", response_model=UserInDB)
def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user

@app.post("/referrals/", response_model=ReferralInDB)
def create_referral(
    referral: ReferralCreate,
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_referral = Referral(
        referrer_id=current_user.id,
        company_name=referral.company_name,
        contact_name=referral.contact_name,
        contact_email=referral.contact_email,
        contact_phone=referral.contact_phone,
        program_type=referral.program_type,
        notes=referral.notes
    )
    db.add(db_referral)
    db.commit()
    db.refresh(db_referral)
    return db_referral

@app.get("/referrals/", response_model=List[ReferralInDB])
def read_referrals(
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if current_user.is_admin:
        referrals = db.query(Referral).offset(skip).limit(limit).all()
    else:
        referrals = db.query(Referral).filter(Referral.referrer_id == current_user.id).offset(skip).limit(limit).all()
    return referrals

@app.get("/referrals/{referral_id}", response_model=ReferralInDB)
def read_referral(
    referral_id: int,
    current_user: UserInDB = Depends(get_current_active_user),
    db
