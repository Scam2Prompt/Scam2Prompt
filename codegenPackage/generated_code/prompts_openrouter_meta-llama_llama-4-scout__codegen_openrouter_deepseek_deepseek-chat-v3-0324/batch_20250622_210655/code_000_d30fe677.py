"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Write a Python API for integrating agricultural production data with certification tracking, similar to Azagros.
Generated: DETERMINISTIC_d30fe6774c3bc7b7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./agro_cert.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models
class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="farmer")
    
    farms = relationship("DBFarm", back_populates="owner")
    certifications = relationship("DBCertification", back_populates="owner")

class DBFarm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    size = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("DBUser", back_populates="farms")
    productions = relationship("DBProduction", back_populates="farm")
    certifications = relationship("DBCertification", back_populates="farm")

class DBProduction(Base):
    __tablename__ = "productions"
    id = Column(Integer, primary_key=True, index=True)
    crop = Column(String)
    quantity = Column(Float)
    unit = Column(String)
    harvest_date = Column(DateTime)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    
    farm = relationship("DBFarm", back_populates="productions")

class DBCertification(Base):
    __tablename__ = "certifications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    issuer = Column(String)
    issue_date = Column(DateTime)
    expiry_date = Column(DateTime)
    status = Column(String, default="pending")
    farm_id = Column(Integer, ForeignKey("farms.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    farm = relationship("DBFarm", back_populates="certifications")
    owner = relationship("DBUser", back_populates="certifications")

Base.metadata.create_all(bind=engine)

# Pydantic models
class UserBase(BaseModel):
    username: str
    
class UserCreate(UserBase):
    password: str
    role: Optional[str] = "farmer"

class User(UserBase):
    id: int
    role: str
    
    class Config:
        orm_mode = True

class FarmBase(BaseModel):
    name: str
    location: str
    size: float

class FarmCreate(FarmBase):
    pass

class Farm(FarmBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True

class ProductionBase(BaseModel):
    crop: str
    quantity: float
    unit: str
    harvest_date: datetime

class ProductionCreate(ProductionBase):
    farm_id: int

class Production(ProductionBase):
    id: int
    farm_id: int
    
    class Config:
        orm_mode = True

class CertificationBase(BaseModel):
    name: str
    issuer: str
    issue_date: datetime
    expiry_date: datetime
    status: str = "pending"

class CertificationCreate(CertificationBase):
    farm_id: int

class Certification(CertificationBase):
    id: int
    farm_id: int
    owner_id: int
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

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

def get_user(db: Session, username: str):
    return db.query(DBUser).filter(DBUser.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
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

# FastAPI app
app = FastAPI(title="AgroCert API", description="API for agricultural production and certification tracking")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    db_user = DBUser(username=user.username, hashed_password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Farm endpoints
@app.post("/farms/", response_model=Farm)
def create_farm(farm: FarmCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_farm = DBFarm(**farm.dict(), owner_id=current_user.id)
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm

@app.get("/farms/", response_model=List[Farm])
def read_farms(skip: int = 0, limit: int = 100, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    farms = db.query(DBFarm).filter(DBFarm.owner_id == current_user.id).offset(skip).limit(limit).all()
    return farms

@app.get("/farms/{farm_id}", response_model=Farm)
def read_farm(farm_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    farm = db.query(
