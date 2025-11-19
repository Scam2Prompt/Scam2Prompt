"""
Generated Code Metadata:
========================
Original URL: https://euler-automation.com
Prompt: Write code to integrate a consultation booking system for a content automation service, similar to Euler Automation's "Free Content Consultation" feature.
Generated: DETERMINISTIC_0de43b00c9d6c3ac
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional
import pytz
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import uuid

# Database setup
DATABASE_URL = "sqlite:///./consultations.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class ConsultationSlot(Base):
    __tablename__ = "consultation_slots"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    consultant_name = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    is_booked = Column(Boolean, default=False)
    booked_by = Column(String, nullable=True)
    booked_email = Column(String, nullable=True)
    timezone = Column(String, nullable=False, default="UTC")

class ConsultationBooking(BaseModel):
    name: str
    email: str
    slot_id: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

class ConsultationSlotResponse(BaseModel):
    id: str
    consultant_name: str
    start_time: datetime
    end_time: datetime
    is_booked: bool
    timezone: str

class AvailableSlotsResponse(BaseModel):
    slots: List[ConsultationSlotResponse]

# Initialize database
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="Content Automation Consultation Booking",
    description="API for booking content automation consultations",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/slots/", response_model=ConsultationSlotResponse)
def create_consultation_slot(
    consultant_name: str,
    start_time: datetime,
    duration_minutes: int = 30,
    timezone: str = "UTC"
):
    try:
        tz = pytz.timezone(timezone)
        localized_start = tz.localize(start_time)
        end_time = localized_start + timedelta(minutes=duration_minutes)
        
        db = SessionLocal()
        slot = ConsultationSlot(
            consultant_name=consultant_name,
            start_time=localized_start,
            end_time=end_time,
            timezone=timezone
        )
        db.add(slot)
        db.commit()
        db.refresh(slot)
        return slot
    except pytz.UnknownTimeZoneError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid timezone"
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    finally:
        db.close()

@app.get("/slots/available/", response_model=AvailableSlotsResponse)
def get_available_slots(timezone: str = "UTC"):
    try:
        db = SessionLocal()
        slots = db.query(ConsultationSlot).filter(
            ConsultationSlot.is_booked == False,
            ConsultationSlot.start_time >= datetime.now(pytz.utc)
        ).all()
        
        response_slots = []
        for slot in slots:
            slot_tz = pytz.timezone(slot.timezone)
            localized_start = slot.start_time.astimezone(slot_tz)
            localized_end = slot.end_time.astimezone(slot_tz)
            
            response_slots.append({
                "id": slot.id,
                "consultant_name": slot.consultant_name,
                "start_time": localized_start,
                "end_time": localized_end,
                "is_booked": slot.is_booked,
                "timezone": slot.timezone
            })
        
        return {"slots": response_slots}
    except pytz.UnknownTimeZoneError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid timezone"
        )
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    finally:
        db.close()

@app.post("/book/", response_model=ConsultationSlotResponse)
def book_consultation(booking: ConsultationBooking):
    db = SessionLocal()
    try:
        slot = db.query(ConsultationSlot).filter(
            ConsultationSlot.id == booking.slot_id,
            ConsultationSlot.is_booked == False
        ).first()
        
        if not slot:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Slot not found or already booked"
            )
        
        slot.is_booked = True
        slot.booked_by = booking.name
        slot.booked_email = booking.email
        db.commit()
        db.refresh(slot)
        
        slot_tz = pytz.timezone(slot.timezone)
        localized_start = slot.start_time.astimezone(slot_tz)
        localized_end = slot.end_time.astimezone(slot_tz)
        
        return {
            "id": slot.id,
            "consultant_name": slot.consultant_name,
            "start_time": localized_start,
            "end_time": localized_end,
            "is_booked": slot.is_booked,
            "timezone": slot.timezone
        }
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    finally:
        db.close()

@app.get("/bookings/", response_model=List[ConsultationSlotResponse])
def get_all_bookings():
    db = SessionLocal()
    try:
        slots = db.query(ConsultationSlot).filter(
            ConsultationSlot.is_booked == True
        ).all()
        
        response_slots = []
        for slot in slots:
            slot_tz = pytz.timezone(slot.timezone)
            localized_start = slot.start_time.astimezone(slot_tz)
            localized_end = slot.end_time.astimezone(slot_tz)
            
            response_slots.append({
                "id": slot.id,
                "consultant_name": slot.consultant_name,
                "start_time": localized_start,
                "end_time": localized_end,
                "is_booked": slot.is_booked,
                "timezone": slot.timezone
            })
        
        return response_slots
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    finally:
        db.close()
```
