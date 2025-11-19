"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Generate a code snippet for a web application that allows users to book online therapy sessions, incorporating features for individual therapy and webinars as described on Melika Taheri's website.
Generated: DETERMINISTIC_39ca9c47f8aa7d52
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code snippet for an online therapy session booking system:

```python
from datetime import datetime, timedelta
from enum import Enum
import logging
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, validator, Field
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./therapy.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums
class SessionType(str, Enum):
    INDIVIDUAL = "individual"
    WEBINAR = "webinar"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

# Database models
class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class DBSession(Base):
    __tablename__ = "therapy_sessions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    session_type = Column(SQLEnum(SessionType))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    max_participants = Column(Integer)
    therapist_id = Column(Integer)
    is_bookable = Column(Boolean, default=True)

class DBBooking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    session_id = Column(Integer)
    booking_time = Column(DateTime, default=datetime.utcnow)
    status = Column(SQLEnum(BookingStatus), default=BookingStatus.PENDING)

Base.metadata.create_all(bind=engine)

# Pydantic models
class SessionBase(BaseModel):
    title: str
    description: Optional[str] = None
    session_type: SessionType
    start_time: datetime
    end_time: datetime
    max_participants: int = Field(gt=0)
    therapist_id: int = Field(gt=0)

    @validator('end_time')
    def validate_end_time(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError('End time must be after start time')
        if (v - values['start_time']) > timedelta(hours=3):
            raise ValueError('Session cannot exceed 3 hours')
        return v

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    session_id: int
    user_id: int

class BookingResponse(BaseModel):
    id: int
    session_id: int
    user_id: int
    booking_time: datetime
    status: BookingStatus

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/sessions/", status_code=status.HTTP_201_CREATED)
async def create_session(session: SessionBase, db: Session = Depends(get_db)):
    """
    Create a new therapy session (individual or webinar)
    """
    try:
        db_session = DBSession(**session.dict())
        db.add(db_session)
        db.commit()
        db.refresh(db_session)
        logger.info(f"Created new session: {db_session.title}")
        return db_session
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating session: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/sessions/", response_model=list[SessionBase])
async def list_sessions(session_type: Optional[SessionType] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List all available therapy sessions with optional filtering by type
    """
    try:
        query = db.query(DBSession).filter(DBSession.is_bookable == True)
        if session_type:
            query = query.filter(DBSession.session_type == session_type)
        sessions = query.offset(skip).limit(limit).all()
        return sessions
    except Exception as e:
        logger.error(f"Error listing sessions: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving sessions")

@app.post("/bookings/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    """
    Book a therapy session or webinar
    """
    try:
        # Check if session exists and is bookable
        session = db.query(DBSession).filter(DBSession.id == booking.session_id, DBSession.is_bookable == True).first()
        if not session:
            raise HTTPException(status_code=404, detail="Session not found or not bookable")

        # Check if session is full (for webinars)
        if session.session_type == SessionType.WEBINAR:
            current_bookings = db.query(DBBooking).filter(
                DBBooking.session_id == booking.session_id,
                DBBooking.status == BookingStatus.CONFIRMED
            ).count()
            if current_bookings >= session.max_participants:
                raise HTTPException(status_code=400, detail="This webinar is fully booked")

        # Check if user already booked this session
        existing_booking = db.query(DBBooking).filter(
            DBBooking.user_id == booking.user_id,
            DBBooking.session_id == booking.session_id
        ).first()
        if existing_booking:
            raise HTTPException(status_code=400, detail="You have already booked this session")

        # Create the booking
        db_booking = DBBooking(
            user_id=booking.user_id,
            session_id=booking.session_id,
            status=BookingStatus.CONFIRMED
        )
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)

        logger.info(f"New booking created: {db_booking.id}")
        return db_booking

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating booking: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating booking")

@app.get("/bookings/user/{user_id}", response_model=list[BookingResponse])
async def get_user_bookings(user_id: int, db: Session = Depends(get_db)):
    """
    Get all bookings for a specific user
    """
    try:
        bookings = db.query(DBBooking).filter(DBBooking.user_id == user_id).all()
        return bookings
    except Exception as e:
        logger.error(f"Error retrieving user bookings: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving bookings")

@app.put("/bookings/{booking_id}/cancel", response_model=BookingResponse)
async def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    """
    Cancel a booking
    """
    try:
        booking = db.query(DBBooking).filter(DBBooking.id == booking_id).first()
        if not booking:
            raise HTTPException(status_code=404, detail="Booking not found")
        
        if booking.status == BookingStatus.CANCELLED:
            raise HTTPException(status_code=400, detail="Booking already cancelled")
        
        booking.status = BookingStatus.CANCELLED
        db.commit()
        db.refresh(booking)
        
        logger.info(f"Cancelled booking: {booking_id}")
        return booking
    
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error cancelling booking: {str(e)}")
        raise HTTPException(status_code=500, detail="Error cancelling booking")
```
