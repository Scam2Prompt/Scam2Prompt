"""
Generated Code Metadata:
========================
Original URL: https://libertyaid.co
Prompt: Illustrate how to implement a feature that allows users to schedule an appointment for Medicare guidance through Liberty Aid's services.
Generated: DETERMINISTIC_d968b1d26e57edb4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import pytz
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator, Field
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Liberty Aid Medicare Appointment Scheduler",
    description="API for scheduling Medicare guidance appointments",
    version="1.0.0"
)

# Database simulation
appointments_db: Dict[str, Dict] = {}

class AppointmentRequest(BaseModel):
    """Request model for scheduling an appointment"""
    user_id: str = Field(..., description="Unique identifier for the user")
    full_name: str = Field(..., description="User's full name")
    email: str = Field(..., description="User's email address")
    phone: str = Field(..., description="User's phone number")
    preferred_date: str = Field(..., description="Preferred date in YYYY-MM-DD format")
    preferred_time: str = Field(..., description="Preferred time in HH:MM format (24-hour)")
    timezone: str = Field(..., description="Timezone in IANA format (e.g., America/New_York)")
    topic: str = Field(..., description="Topic of Medicare guidance needed")
    notes: Optional[str] = Field(None, description="Additional notes for the appointment")

    @validator('preferred_date')
    def validate_date(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        return v

    @validator('preferred_time')
    def validate_time(cls, v):
        try:
            datetime.strptime(v, '%H:%M')
        except ValueError:
            raise ValueError("Time must be in HH:MM format (24-hour)")
        return v

    @validator('timezone')
    def validate_timezone(cls, v):
        if v not in pytz.all_timezones:
            raise ValueError("Invalid timezone. Must be in IANA format (e.g., America/New_York)")
        return v

class AppointmentResponse(BaseModel):
    """Response model for scheduled appointment"""
    appointment_id: str
    user_id: str
    full_name: str
    email: str
    phone: str
    scheduled_datetime: str
    timezone: str
    topic: str
    notes: Optional[str]
    confirmation_code: str
    status: str

def generate_confirmation_code() -> str:
    """Generate a unique confirmation code"""
    return str(uuid4()).split('-')[0].upper()

def is_time_slot_available(scheduled_datetime: datetime) -> bool:
    """Check if the time slot is available"""
    for appointment in appointments_db.values():
        appt_datetime = datetime.fromisoformat(appointment['scheduled_datetime'])
        if abs((appt_datetime - scheduled_datetime).total_seconds()) < 3600:  # 1 hour buffer
            return False
    return True

@app.post("/appointments", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
async def schedule_appointment(request: AppointmentRequest):
    """Schedule a new Medicare guidance appointment"""
    try:
        # Parse and validate datetime
        preferred_datetime = datetime.strptime(
            f"{request.preferred_date} {request.preferred_time}",
            "%Y-%m-%d %H:%M"
        )
        
        # Convert to UTC for storage
        user_tz = pytz.timezone(request.timezone)
        localized_datetime = user_tz.localize(preferred_datetime)
        utc_datetime = localized_datetime.astimezone(pytz.UTC)
        
        # Check if time slot is available
        if not is_time_slot_available(utc_datetime):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="The requested time slot is not available. Please choose another time."
            )
        
        # Create appointment
        appointment_id = str(uuid4())
        confirmation_code = generate_confirmation_code()
        
        appointment = {
            "appointment_id": appointment_id,
            "user_id": request.user_id,
            "full_name": request.full_name,
            "email": request.email,
            "phone": request.phone,
            "scheduled_datetime": utc_datetime.isoformat(),
            "timezone": request.timezone,
            "topic": request.topic,
            "notes": request.notes,
            "confirmation_code": confirmation_code,
            "status": "scheduled"
        }
        
        # Store appointment
        appointments_db[appointment_id] = appointment
        
        logger.info(f"Appointment scheduled: {appointment_id}")
        
        # Convert back to user's timezone for response
        response_datetime = utc_datetime.astimezone(user_tz).isoformat()
        
        return {
            **appointment,
            "scheduled_datetime": response_datetime
        }
        
    except Exception as e:
        logger.error(f"Error scheduling appointment: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/appointments/{appointment_id}", response_model=AppointmentResponse)
async def get_appointment(appointment_id: str):
    """Retrieve a scheduled appointment"""
    if appointment_id not in appointments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    
    appointment = appointments_db[appointment_id]
    user_tz = pytz.timezone(appointment['timezone'])
    utc_datetime = datetime.fromisoformat(appointment['scheduled_datetime'])
    response_datetime = utc_datetime.astimezone(user_tz).isoformat()
    
    return {
        **appointment,
        "scheduled_datetime": response_datetime
    }

@app.get("/appointments/user/{user_id}", response_model=List[AppointmentResponse])
async def get_user_appointments(user_id: str):
    """Retrieve all appointments for a user"""
    user_appointments = [
        appt for appt in appointments_db.values() 
        if appt['user_id'] == user_id
    ]
    
    if not user_appointments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No appointments found for this user"
        )
    
    # Convert datetimes to user's timezone
    for appt in user_appointments:
        user_tz = pytz.timezone(appt['timezone'])
        utc_datetime = datetime.fromisoformat(appt['scheduled_datetime'])
        appt['scheduled_datetime'] = utc_datetime.astimezone(user_tz).isoformat()
    
    return user_appointments

@app.put("/appointments/{appointment_id}/cancel", response_model=AppointmentResponse)
async def cancel_appointment(appointment_id: str):
    """Cancel a scheduled appointment"""
    if appointment_id not in appointments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    
    appointment = appointments_db[appointment_id]
    
    # Check if appointment can be canceled (e.g., not already canceled or too close to scheduled time)
    utc_datetime = datetime.fromisoformat(appointment['scheduled_datetime'])
    if utc_datetime < datetime.now(pytz.UTC) + timedelta(hours=24):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointments can only be canceled at least 24 hours in advance"
        )
    
    if appointment['status'] == 'canceled':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointment is already canceled"
        )
    
    # Update appointment status
    appointment['status'] = 'canceled'
    appointments_db[appointment_id] = appointment
    
    logger.info(f"Appointment canceled: {appointment_id}")
    
    # Convert datetime to user's timezone for response
    user_tz = pytz.timezone(appointment['timezone'])
    response_datetime = utc_datetime.astimezone(user_tz).isoformat()
    
    return {
        **appointment,
        "scheduled_datetime": response_datetime
    }
```
