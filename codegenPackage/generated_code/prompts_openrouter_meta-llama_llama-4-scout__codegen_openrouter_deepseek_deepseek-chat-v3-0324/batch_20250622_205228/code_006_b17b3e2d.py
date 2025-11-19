"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Design a system to monitor resellers and manage damage with e-commerce partners, including tracking seller performance and detecting potential issues.
Generated: DETERMINISTIC_b17b3e2db9211587
Batch ID: 20250622_205228
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
from typing import List, Dict, Optional
from enum import Enum
import requests
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_URL = "sqlite:///./reseller_monitoring.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Enums
class IssueSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class ResellerStatus(str, Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"

# Database Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Reseller(Base):
    __tablename__ = "resellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_email = Column(String, unique=True, index=True)
    status = Column(SQLEnum(ResellerStatus), default=ResellerStatus.ACTIVE)
    registration_date = Column(DateTime, default=datetime.utcnow)
    performance_score = Column(Float, default=0.0)
    issues = relationship("ResellerIssue", back_populates="reseller")

class ResellerIssue(Base):
    __tablename__ = "reseller_issues"

    id = Column(Integer, primary_key=True, index=True)
    reseller_id = Column(Integer, ForeignKey("resellers.id"))
    description = Column(String)
    severity = Column(SQLEnum(IssueSeverity))
    detected_at = Column(DateTime, default=datetime.utcnow)
    resolved = Column(Boolean, default=False)
    resolved_at = Column(DateTime, nullable=True)
    reseller = relationship("Reseller", back_populates="issues")

# Pydantic Models
class UserCreate(BaseModel):
    username: str
    password: str

class UserInDB(BaseModel):
    username: str
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ResellerCreate(BaseModel):
    name: str
    contact_email: str

class ResellerResponse(BaseModel):
    id: int
    name: str
    contact_email: str
    status: ResellerStatus
    registration_date: datetime
    performance_score: float

    class Config:
        orm_mode = True

class ResellerIssueCreate(BaseModel):
    description: str
    severity: IssueSeverity

class ResellerIssueResponse(BaseModel):
    id: int
    reseller_id: int
    description: str
    severity: IssueSeverity
    detected_at: datetime
    resolved: bool
    resolved_at: Optional[datetime]

    class Config:
        orm_mode = True

class PerformanceMetrics(BaseModel):
    reseller_id: int
    order_fulfillment_rate: float
    return_rate: float
    average_shipping_time: float
    customer_rating: float

    @validator('order_fulfillment_rate', 'return_rate', 'customer_rating')
    def validate_percentage(cls, v):
        if not 0 <= v <= 1:
            raise ValueError('must be between 0 and 1')
        return v

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Simplified for example - implement proper token verification in production
    user = db.query(User).filter(User.username == token).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def calculate_performance_score(metrics: PerformanceMetrics) -> float:
    weights = {
        'order_fulfillment_rate': 0.3,
        'return_rate': -0.2,  # Negative because higher return rate is bad
        'average_shipping_time': -0.1,  # Negative because longer shipping is bad
        'customer_rating': 0.4
    }
    
    score = (
        metrics.order_fulfillment_rate * weights['order_fulfillment_rate'] +
        (1 - metrics.return_rate) * weights['return_rate'] +
        (1 / (1 + metrics.average_shipping_time)) * weights['average_shipping_time'] +
        metrics.customer_rating * weights['customer_rating']
    )
    return max(0, min(1, score))  # Ensure score is between 0 and 1

# API Endpoints
@app.post("/users/", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token", response_model=Token)
def login_for_access_token(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": db_user.username, "token_type": "bearer"}

@app.post("/resellers/", response_model=ResellerResponse)
def create_reseller(
    reseller: ResellerCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_reseller = Reseller(**reseller.dict())
    db.add(db_reseller)
    db.commit()
    db.refresh(db_reseller)
    return db_reseller

@app.get("/resellers/", response_model=List[ResellerResponse])
def read_resellers(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    resellers = db.query(Reseller).offset(skip).limit(limit).all()
    return resellers

@app.get("/resellers/{reseller_id}", response_model=ResellerResponse)
def read_reseller(
    reseller_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    reseller = db.query(Reseller).filter(Reseller.id == reseller_id).first()
    if not reseller:
        raise HTTPException(status_code=404, detail="Reseller not found")
    return reseller

@app.post("/resellers/{reseller_id}/issues/", response_model=ResellerIssueResponse)
def create_reseller_issue(
    reseller_id: int,
    issue: ResellerIssueCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    reseller = db.query(Reseller).filter(Reseller.id == reseller_id).first()
    if not reseller:
        raise HTTPException(status_code=404, detail="Reseller not found")
    
    db_issue = ResellerIssue(reseller_id=reseller_id, **issue.dict())
    db.add(db_issue)
    db.commit
