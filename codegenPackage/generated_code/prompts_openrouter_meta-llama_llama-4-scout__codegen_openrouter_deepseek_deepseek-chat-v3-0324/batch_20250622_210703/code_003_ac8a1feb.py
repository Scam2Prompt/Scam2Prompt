"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Create a code snippet to manage online bookings and demo sessions for a fitness studio, specifically designed for suspension training services like Breakthrough Studio.
Generated: DETERMINISTIC_ac8a1febd914efb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Breakthrough Studio Booking API",
    description="API for managing online bookings and demo sessions for Breakthrough Studio",
    version="1.0.0"
)

class SessionType(str, Enum):
    DEMO = "demo"
    TRAINING = "training"
    WORKSHOP = "workshop"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class Booking(BaseModel):
    id: str = Field(..., description="Unique booking ID")
    customer_name: str = Field(..., min_length=2, max_length=50)
    customer_email: str = Field(..., regex="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$")
    session_type: SessionType
    session_datetime: datetime.datetime
    status: BookingStatus = BookingStatus.PENDING
    notes: Optional[str] = Field(None, max_length=200)
    
    @validator('session_datetime')
    def validate_session_datetime(cls, v):
        if v < datetime.datetime.now():
            raise ValueError("Session datetime must be in the future")
        return v

# In-memory database simulation
bookings_db = {}

@app.post("/bookings/", response_model=Booking, status_code=status.HTTP_201_CREATED)
async def create_booking(booking: Booking):
    """Create a new booking"""
    if booking.id in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Booking with this ID already exists"
        )
    
    bookings_db[booking.id] = booking
    return booking

@app.get("/bookings/", response_model=List[Booking])
async def get_bookings(status: Optional[BookingStatus] = None):
    """Get all bookings, optionally filtered by status"""
    if status:
        return [b for b in bookings_db.values() if b.status == status]
    return list(bookings_db.values())

@app.get("/bookings/{booking_id}", response_model=Booking)
async def get_booking(booking_id: str):
    """Get a specific booking by ID"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return bookings_db[booking_id]

@app.put("/bookings/{booking_id}", response_model=Booking)
async def update_booking(booking_id: str, booking: Booking):
    """Update an existing booking"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    if booking_id != booking.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Booking ID mismatch"
        )
    
    bookings_db[booking_id] = booking
    return booking

@app.patch("/bookings/{booking_id}/status", response_model=Booking)
async def update_booking_status(booking_id: str, status: BookingStatus):
    """Update booking status"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    booking = bookings_db[booking_id]
    booking.status = status
    bookings_db[booking_id] = booking
    return booking

@app.delete("/bookings/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(booking_id: str):
    """Cancel/delete a booking"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    del bookings_db[booking_id]
    return JSONResponse(content=None, status_code=status.HTTP_204_NO_CONTENT)

@app.get("/availability/")
async def check_availability(
    session_type: SessionType,
    date: datetime.date,
    duration_minutes: int = 60
):
    """Check available time slots for a given session type and date"""
    # In a real implementation, this would query the actual schedule
    # Here we simulate availability with some basic logic
    
    start_time = datetime.datetime.combine(date, datetime.time(8, 0))
    end_time = datetime.datetime.combine(date, datetime.time(20, 0))
    slot_duration = datetime.timedelta(minutes=duration_minutes)
    
    existing_bookings = [
        b.session_datetime 
        for b in bookings_db.values() 
        if b.session_datetime.date() == date 
        and b.session_type == session_type
    ]
    
    available_slots = []
    current_time = start_time
    
    while current_time + slot_duration <= end_time:
        slot_available = True
        for booking in existing_bookings:
            if abs((booking - current_time).total_seconds()) < duration_minutes * 60:
                slot_available = False
                break
        
        if slot_available:
            available_slots.append(current_time)
        
        current_time += slot_duration
    
    return {"available_slots": available_slots}
```
