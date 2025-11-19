"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Generate a REST API design for booking a hair transplant consultation online, incorporating features like free follow-up for 5 months and session duration details as described by Auqual Hair Services.
Generated: DETERMINISTIC_e2ef3b41a850e1ca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timedelta
from uuid import uuid4
from enum import Enum

app = FastAPI(
    title="Auqual Hair Services Booking API",
    description="API for booking hair transplant consultations with Auqual Hair Services",
    version="1.0.0"
)

# Database mock (in production, use a real database)
bookings_db = {}

# Models
class SessionType(str, Enum):
    standard = "standard"
    premium = "premium"
    executive = "executive"

class BookingStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    completed = "completed"
    cancelled = "cancelled"

class BookingRequest(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: str = Field(..., min_length=10, max_length=15)
    session_type: SessionType
    preferred_date: datetime
    notes: Optional[str] = Field(None, max_length=500)

class BookingResponse(BaseModel):
    booking_id: str
    customer_name: str
    email: str
    phone: str
    session_type: SessionType
    session_duration: str
    includes_follow_up: bool
    follow_up_months: int
    preferred_date: datetime
    booking_date: datetime
    status: BookingStatus
    notes: Optional[str]

class BookingUpdate(BaseModel):
    preferred_date: Optional[datetime]
    status: Optional[BookingStatus]
    notes: Optional[str] = Field(None, max_length=500)

# Helper functions
def get_session_duration(session_type: SessionType) -> str:
    durations = {
        SessionType.standard: "4 hours",
        SessionType.premium: "6 hours",
        SessionType.executive: "8 hours"
    }
    return durations[session_type]

def generate_follow_up_dates(booking_date: datetime) -> List[datetime]:
    return [booking_date + timedelta(days=30 * i) for i in range(1, 6)]

# API Endpoints
@app.post("/bookings", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(booking_request: BookingRequest):
    """Create a new hair transplant consultation booking"""
    booking_id = str(uuid4())
    
    booking_data = {
        "booking_id": booking_id,
        "customer_name": booking_request.customer_name,
        "email": booking_request.email,
        "phone": booking_request.phone,
        "session_type": booking_request.session_type,
        "session_duration": get_session_duration(booking_request.session_type),
        "includes_follow_up": True,
        "follow_up_months": 5,
        "preferred_date": booking_request.preferred_date,
        "booking_date": datetime.now(),
        "status": BookingStatus.pending,
        "notes": booking_request.notes,
        "follow_up_dates": generate_follow_up_dates(datetime.now())
    }
    
    bookings_db[booking_id] = booking_data
    return booking_data

@app.get("/bookings/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: str):
    """Retrieve a specific booking by ID"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return bookings_db[booking_id]

@app.put("/bookings/{booking_id}", response_model=BookingResponse)
async def update_booking(booking_id: str, booking_update: BookingUpdate):
    """Update an existing booking"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    booking = bookings_db[booking_id]
    
    if booking_update.preferred_date:
        booking["preferred_date"] = booking_update.preferred_date
    if booking_update.status:
        booking["status"] = booking_update.status
    if booking_update.notes is not None:
        booking["notes"] = booking_update.notes
    
    bookings_db[booking_id] = booking
    return booking

@app.get("/bookings", response_model=List[BookingResponse])
async def list_bookings(status: Optional[BookingStatus] = None):
    """List all bookings, optionally filtered by status"""
    if status:
        return [b for b in bookings_db.values() if b["status"] == status]
    return list(bookings_db.values())

@app.get("/bookings/{booking_id}/follow-ups", response_model=List[datetime])
async def get_follow_up_dates(booking_id: str):
    """Get follow-up dates for a booking"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return bookings_db[booking_id]["follow_up_dates"]

@app.delete("/bookings/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_booking(booking_id: str):
    """Cancel a booking"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    booking = bookings_db[booking_id]
    booking["status"] = BookingStatus.cancelled
    bookings_db[booking_id] = booking
    return None
```
