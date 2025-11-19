"""
Generated Code Metadata:
========================
Original URL: https://gavasilva.adv.br
Prompt: Generate a code snippet for a web application that allows users to schedule legal consultations with Gava & Silva Advogados, incorporating features for both in-person and online appointments.
Generated: DETERMINISTIC_b487595849c8b6fc
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Optional, List
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, validator, EmailStr
from enum import Enum
import uuid
import pytz

app = FastAPI(
    title="Gava & Silva Advogados Consultation Scheduler",
    description="API for scheduling legal consultations with Gava & Silva Advogados",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
consultations_db = []
users_db = []

class ConsultationType(str, Enum):
    IN_PERSON = "in_person"
    ONLINE = "online"

class ConsultationStatus(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class ConsultationBase(BaseModel):
    client_name: str
    client_email: EmailStr
    consultation_type: ConsultationType
    scheduled_time: datetime
    duration_minutes: int = 60
    notes: Optional[str] = None
    status: ConsultationStatus = ConsultationStatus.SCHEDULED

    @validator('scheduled_time')
    def validate_scheduled_time(cls, v):
        if v < datetime.now(pytz.utc) + timedelta(hours=24):
            raise ValueError("Consultations must be scheduled at least 24 hours in advance")
        if v.hour < 9 or v.hour >= 18:
            raise ValueError("Consultations must be between 9 AM and 6 PM")
        return v

    @validator('duration_minutes')
    def validate_duration(cls, v):
        if v not in [30, 60, 90]:
            raise ValueError("Duration must be 30, 60, or 90 minutes")
        return v

class ConsultationCreate(ConsultationBase):
    pass

class Consultation(ConsultationBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

def get_db():
    """Mock database session dependency"""
    try:
        yield
    finally:
        pass

@app.post("/consultations/", response_model=Consultation, status_code=status.HTTP_201_CREATED)
async def create_consultation(consultation: ConsultationCreate, db: None = Depends(get_db)):
    """
    Schedule a new consultation with Gava & Silva Advogados.
    """
    # Check for time conflicts
    for existing in consultations_db:
        existing_end = existing.scheduled_time + timedelta(minutes=existing.duration_minutes)
        new_end = consultation.scheduled_time + timedelta(minutes=consultation.duration_minutes)
        
        if (consultation.scheduled_time < existing_end and 
            new_end > existing.scheduled_time):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Time slot already booked"
            )

    # Create consultation
    consultation_data = consultation.dict()
    consultation_data["id"] = str(uuid.uuid4())
    consultation_data["created_at"] = datetime.now(pytz.utc)
    consultation_data["updated_at"] = datetime.now(pytz.utc)
    
    consultations_db.append(consultation_data)
    return consultation_data

@app.get("/consultations/", response_model=List[Consultation])
async def list_consultations(
    skip: int = 0, 
    limit: int = 100,
    status: Optional[ConsultationStatus] = None,
    db: None = Depends(get_db)
):
    """
    List all scheduled consultations, with optional filtering by status.
    """
    if status:
        return [c for c in consultations_db if c["status"] == status][skip:skip+limit]
    return consultations_db[skip:skip+limit]

@app.get("/consultations/{consultation_id}", response_model=Consultation)
async def get_consultation(consultation_id: str, db: None = Depends(get_db)):
    """
    Get details of a specific consultation.
    """
    for consultation in consultations_db:
        if consultation["id"] == consultation_id:
            return consultation
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Consultation not found"
    )

@app.put("/consultations/{consultation_id}", response_model=Consultation)
async def update_consultation(
    consultation_id: str, 
    consultation_update: ConsultationCreate,
    db: None = Depends(get_db)
):
    """
    Update an existing consultation.
    """
    for idx, consultation in enumerate(consultations_db):
        if consultation["id"] == consultation_id:
            # Check for time conflicts (excluding self)
            for existing in consultations_db:
                if existing["id"] == consultation_id:
                    continue
                    
                existing_end = existing["scheduled_time"] + timedelta(minutes=existing["duration_minutes"])
                new_end = consultation_update.scheduled_time + timedelta(minutes=consultation_update.duration_minutes)
                
                if (consultation_update.scheduled_time < existing_end and 
                    new_end > existing["scheduled_time"]):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Time slot already booked"
                    )

            updated_data = consultation_update.dict()
            updated_data["id"] = consultation_id
            updated_data["created_at"] = consultation["created_at"]
            updated_data["updated_at"] = datetime.now(pytz.utc)
            
            consultations_db[idx] = updated_data
            return updated_data
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Consultation not found"
    )

@app.delete("/consultations/{consultation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_consultation(consultation_id: str, db: None = Depends(get_db)):
    """
    Cancel a scheduled consultation.
    """
    for idx, consultation in enumerate(consultations_db):
        if consultation["id"] == consultation_id:
            if consultation["status"] == ConsultationStatus.CANCELLED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Consultation already cancelled"
                )
                
            if datetime.now(pytz.utc) > consultation["scheduled_time"] - timedelta(hours=24):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Cannot cancel within 24 hours of appointment"
                )
                
            consultations_db[idx]["status"] = ConsultationStatus.CANCELLED
            consultations_db[idx]["updated_at"] = datetime.now(pytz.utc)
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Consultation not found"
    )

@app.get("/consultations/availability/")
async def check_availability(
    start_time: datetime,
    end_time: datetime,
    db: None = Depends(get_db)
):
    """
    Check available time slots between start_time and end_time.
    """
    if start_time >= end_time:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End time must be after start time"
        )

    available_slots = []
    current_time = start_time
    
    while current_time + timedelta(minutes=30) <= end_time:
        slot_end = current_time + timedelta(minutes=30)
        is_available = True
        
        for consultation in consultations_db:
            if consultation["status"] == ConsultationStatus.CANCELLED:
                continue
                
            existing_start = consultation["scheduled_time"]
            existing_end = existing_start + timedelta(minutes=consultation["duration_minutes"])
            
            if (current_time < existing_end and slot_end > existing_start):
                is_available = False
                break
        
        if is_available:
            available_slots.append({
                "start_time": current_time,
                "end_time": slot_end
            })
        
        current_time += timedelta(minutes=30)
    
    return {"available_slots": available_slots}
```
