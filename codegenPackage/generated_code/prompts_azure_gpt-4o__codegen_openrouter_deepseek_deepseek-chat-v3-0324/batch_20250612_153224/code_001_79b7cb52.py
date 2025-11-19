"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Recommend libraries or frameworks for implementing a therapy scheduling system that supports multidisciplinary services like psychology, logopedia, and physiotherapy, as described on Centro Abakadabra's webpage.
Generated: DETERMINISTIC_79b7cb52d1b586c5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports for a therapy scheduling system
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum
import uuid

# Database ORM (Object-Relational Mapping)
from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Web framework for API endpoints
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, validator

# Authentication and authorization
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt

# Configuration management
from pydantic_settings import BaseSettings

# --------------------------
# Configuration
# --------------------------
class Settings(BaseSettings):
    database_url: str = "sqlite:///./therapy_scheduling.db"
    secret_key: str = "your-secret-key-here"  # Should be environment variable in production
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()

# --------------------------
# Database Models
# --------------------------
Base = declarative_base()

class TherapyDiscipline(Enum):
    PSYCHOLOGY = "psychology"
    LOGOPEDIA = "logopedia"
    PHYSIOTHERAPY = "physiotherapy"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    disabled = Column(Integer, default=0)

    appointments = relationship("Appointment", back_populates="patient")

class Therapist(Base):
    __tablename__ = "therapists"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    discipline = Column(SQLEnum(TherapyDiscipline), nullable=False)
    bio = Column(String)
    available_hours = Column(String)  # Could be JSON or separate table in production

    appointments = relationship("Appointment", back_populates="therapist")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = Column(String, ForeignKey("users.id"))
    therapist_id = Column(String, ForeignKey("therapists.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    notes = Column(String)
    status = Column(String, default="scheduled")  # scheduled, completed, canceled

    patient = relationship("User", back_populates="appointments")
    therapist = relationship("Therapist", back_populates="appointments")

# --------------------------
# Pydantic Models
# --------------------------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None

class UserInDB(UserCreate):
    hashed_password: str

class TherapistCreate(BaseModel):
    name: str
    discipline: TherapyDiscipline
    bio: Optional[str] = None
    available_hours: Optional[str] = None

class AppointmentCreate(BaseModel):
    therapist_id: str
    start_time: datetime
    end_time: datetime
    notes: Optional[str] = None

    @validator('end_time')
    def validate_times(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError("End time must be after start time")
        return v

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# --------------------------
# Authentication
# --------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

# --------------------------
# Database Setup
# --------------------------
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------------
# FastAPI Application
# --------------------------
app = FastAPI()

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/therapists/", response_model=TherapistCreate)
async def create_therapist(therapist: TherapistCreate, db: SessionLocal = Depends(get_db)):
    db_therapist = Therapist(
        name=therapist.name,
        discipline=therapist.discipline,
        bio=therapist.bio,
        available_hours=therapist.available_hours
    )
    db.add(db_therapist)
    db.commit()
    db.refresh(db_therapist)
    return db_therapist

@app.post("/appointments/", response_model=AppointmentCreate)
async def create_appointment(
    appointment: AppointmentCreate,
    current_user: User = Depends(oauth2_scheme),
    db: SessionLocal = Depends(get_db)
):
    # Check therapist availability
    therapist = db.query(Therapist).filter(Therapist.id == appointment.therapist_id).first()
    if not therapist:
        raise HTTPException(status_code=404, detail="Therapist not found")
    
    # Check for overlapping appointments
    overlapping = db.query(Appointment).filter(
        Appointment.therapist_id == appointment.therapist_id,
        Appointment.start_time < appointment.end_time,
        Appointment.end_time > appointment.start_time
    ).first()
    
    if overlapping:
        raise HTTPException(status_code=400, detail="Therapist already has an appointment at this time")
    
    db_appointment = Appointment(
        patient_id=current_user.id,
        therapist_id=appointment.therapist_id,
        start_time=appointment.start_time,
        end_time=appointment.end_time,
        notes=appointment.notes
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# --------------------------
# Initialization
# --------------------------
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
