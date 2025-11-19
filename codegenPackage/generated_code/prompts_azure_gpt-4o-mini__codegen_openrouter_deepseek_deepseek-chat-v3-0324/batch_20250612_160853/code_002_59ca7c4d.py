"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Describe how to implement a consultation scheduling API for a clinic specializing in obesity and metabolic surgery, including features for multiple languages like Turkish and English.
Generated: DETERMINISTIC_59ca7c4d12ee95ce
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consultation_scheduling_api.py
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum
from fastapi import FastAPI, HTTPException, status, Query, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
import pytz
import logging
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./clinic.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# App initialization
app = FastAPI(
    title="Clinic Consultation Scheduling API",
    description="API for scheduling consultations in an obesity and metabolic surgery clinic",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enums
class Language(str, Enum):
    ENGLISH = "en"
    TURKISH = "tr"

class ConsultationType(str, Enum):
    INITIAL = "initial"
    FOLLOW_UP = "follow_up"
    PRE_OP = "pre_op"
    POST_OP = "post_op"

class UserRole(str, Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    PATIENT = "patient"
    STAFF = "staff"

# Database models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(SQLEnum(UserRole))
    preferred_language = Column(SQLEnum(Language), default=Language.ENGLISH)
    is_active = Column(Boolean, default=True)

    consultations = relationship("Consultation", back_populates="patient")

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    specialty = Column(String)
    bio = Column(String)
    available_days = Column(String)  # Comma-separated days (e.g., "Monday,Wednesday,Friday")

    consultations = relationship("Consultation", back_populates="doctor")

class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    scheduled_time = Column(DateTime)
    duration_minutes = Column(Integer, default=30)
    type = Column(SQLEnum(ConsultationType))
    notes = Column(String, nullable=True)
    is_confirmed = Column(Boolean, default=False)
    language_preference = Column(SQLEnum(Language), default=Language.ENGLISH)

    patient = relationship("User", back_populates="consultations")
    doctor = relationship("Doctor", back_populates="consultations")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserBase(BaseModel):
    email: str
    full_name: str
    preferred_language: Language = Language.ENGLISH

class UserCreate(UserBase):
    password: str
    role: UserRole

class UserOut(UserBase):
    id: int
    role: UserRole
    is_active: bool

    class Config:
        orm_mode = True

class DoctorBase(BaseModel):
    specialty: str
    bio: str
    available_days: str

class DoctorCreate(DoctorBase):
    user_id: int

class DoctorOut(DoctorBase):
    id: int
    user: UserOut

    class Config:
        orm_mode = True

class ConsultationBase(BaseModel):
    doctor_id: int
    scheduled_time: datetime
    duration_minutes: int = 30
    type: ConsultationType
    notes: Optional[str] = None
    language_preference: Language = Language.ENGLISH

    @validator('scheduled_time')
    def validate_scheduled_time(cls, v):
        if v < datetime.now(pytz.utc):
            raise ValueError("Scheduled time must be in the future")
        return v

class ConsultationCreate(ConsultationBase):
    pass

class ConsultationOut(ConsultationBase):
    id: int
    patient_id: int
    is_confirmed: bool
    patient: UserOut
    doctor: DoctorOut

    class Config:
        orm_mode = True

class TimeSlot(BaseModel):
    start_time: datetime
    end_time: datetime
    doctor_id: int

class Message(BaseModel):
    message: str
    language: Language = Language.ENGLISH

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utility functions
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def verify_token(token: str = Depends(oauth2_scheme)):
    # In a real implementation, verify the JWT token
    # This is a simplified version
    return {"sub": "user@example.com"}

# API endpoints
@app.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=f"hashed_{user.password}",  # In real app, use proper hashing
        role=user.role,
        preferred_language=user.preferred_language
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/doctors/", response_model=DoctorOut, status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = Doctor(
        user_id=doctor.user_id,
        specialty=doctor.specialty,
        bio=doctor.bio,
        available_days=doctor.available_days
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

@app.get("/doctors/", response_model=List[DoctorOut])
def list_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doctors = db.query(Doctor).offset(skip).limit(limit).all()
    return doctors

@app.get("/doctors/{doctor_id}/availability", response_model=List[TimeSlot])
def get_doctor_availability(
    doctor_id: int,
    start_date: datetime = Query(default_factory=datetime.now),
    end_date: datetime = Query(default_factory=lambda: datetime.now() + timedelta(days=7)),
    db: Session = Depends(get_db)
):
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    # Simplified availability calculation
    # In a real app, this would consider doctor's schedule, holidays, etc.
    available_slots = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.strftime("%A") in doctor.available_days:
            for hour in range(9, 17):  # 9 AM to 5 PM
                slot_start = current_date.replace(hour=hour, minute=0, second=0, microsecond=0)
                slot_end = slot_start + timedelta(minutes=30)
                available_slots.append(TimeSlot(
                    start_time=slot_start,
                    end_time=slot_end,
                    doctor_id=doctor_id
                ))
        current_date += timedelta(days=1)
    
    return available_slots

@app.post("/consultations/", response_model=ConsultationOut, status_code=status.HTTP_201_CREATED)
def create_consultation(
    consultation: ConsultationCreate,
    current_user: dict = Depends(verify_token),
    db: Session = Depends(get_db)
):
