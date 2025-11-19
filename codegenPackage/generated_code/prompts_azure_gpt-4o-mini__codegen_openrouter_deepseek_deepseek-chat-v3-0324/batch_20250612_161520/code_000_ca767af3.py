"""
Generated Code Metadata:
========================
Original URL: https://tubalife.me
Prompt: Generate a booking system API for a spa that allows users to schedule services like Moroccan baths and massages at TUBA SPA in Riyadh.
Generated: DETERMINISTIC_ca767af39037dfd4
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field, validator
from datetime import datetime, time
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(
    title="TUBA SPA Booking API",
    description="API for booking spa services at TUBA SPA in Riyadh",
    version="1.0.0"
)

# Database simulation
class Database:
    def __init__(self):
        self.bookings = []
        self.services = [
            {"id": "1", "name": "Moroccan Bath", "duration": 90, "price": 300},
            {"id": "2", "name": "Swedish Massage", "duration": 60, "price": 250},
            {"id": "3", "name": "Hot Stone Massage", "duration": 75, "price": 350},
            {"id": "4", "name": "Aromatherapy", "duration": 45, "price": 200}
        ]
    
    def get_service_by_id(self, service_id: str):
        for service in self.services:
            if service["id"] == service_id:
                return service
        return None
    
    def add_booking(self, booking):
        self.bookings.append(booking)
        return booking
    
    def get_bookings(self):
        return self.bookings
    
    def get_booking_by_id(self, booking_id: UUID):
        for booking in self.bookings:
            if booking["id"] == booking_id:
                return booking
        return None
    
    def delete_booking(self, booking_id: UUID):
        for i, booking in enumerate(self.bookings):
            if booking["id"] == booking_id:
                return self.bookings.pop(i)
        return None

db = Database()

# Models
class ServiceType(str, Enum):
    MOROCCAN_BATH = "Moroccan Bath"
    SWEDISH_MASSAGE = "Swedish Massage"
    HOT_STONE_MASSAGE = "Hot Stone Massage"
    AROMATHERAPY = "Aromatherapy"

class Service(BaseModel):
    id: str
    name: str
    duration: int  # in minutes
    price: float

class BookingCreate(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=50)
    customer_phone: str = Field(..., regex=r"^\+?[0-9]{10,15}$")
    service_id: str
    booking_date: str
    booking_time: str
    notes: Optional[str] = Field(None, max_length=200)
    
    @validator('booking_date')
    def validate_booking_date(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        return v
    
    @validator('booking_time')
    def validate_booking_time(cls, v):
        try:
            time.fromisoformat(v)
        except ValueError:
            raise ValueError("Time must be in HH:MM format")
        return v

class Booking(BaseModel):
    id: UUID
    customer_name: str
    customer_phone: str
    service: Service
    booking_datetime: datetime
    notes: Optional[str]
    created_at: datetime

# API Endpoints
@app.get("/services", response_model=List[Service], tags=["Services"])
def get_available_services():
    """Get all available spa services"""
    return db.services

@app.get("/services/{service_id}", response_model=Service, tags=["Services"])
def get_service(service_id: str):
    """Get details of a specific service"""
    service = db.get_service_by_id(service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    return service

@app.post("/bookings", response_model=Booking, status_code=status.HTTP_201_CREATED, tags=["Bookings"])
def create_booking(booking_data: BookingCreate):
    """Create a new booking"""
    service = db.get_service_by_id(booking_data.service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    
    try:
        booking_datetime = datetime.strptime(
            f"{booking_data.booking_date} {booking_data.booking_time}",
            "%Y-%m-%d %H:%M"
        )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid date or time format"
        )
    
    # Check if booking is in the future
    if booking_datetime < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Booking must be in the future"
        )
    
    # Check for overlapping bookings (simplified)
    for existing_booking in db.get_bookings():
        existing_end = existing_booking["booking_datetime"] + timedelta(minutes=existing_booking["service"]["duration"])
        new_end = booking_datetime + timedelta(minutes=service["duration"])
        
        if (booking_datetime < existing_end and new_end > existing_booking["booking_datetime"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Time slot already booked"
            )
    
    booking = {
        "id": uuid4(),
        "customer_name": booking_data.customer_name,
        "customer_phone": booking_data.customer_phone,
        "service": service,
        "booking_datetime": booking_datetime,
        "notes": booking_data.notes,
        "created_at": datetime.now()
    }
    
    db.add_booking(booking)
    return booking

@app.get("/bookings", response_model=List[Booking], tags=["Bookings"])
def get_all_bookings():
    """Get all bookings"""
    return db.get_bookings()

@app.get("/bookings/{booking_id}", response_model=Booking, tags=["Bookings"])
def get_booking(booking_id: UUID):
    """Get details of a specific booking"""
    booking = db.get_booking_by_id(booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return booking

@app.delete("/bookings/{booking_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Bookings"])
def cancel_booking(booking_id: UUID):
    """Cancel a booking"""
    booking = db.delete_booking(booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return None
```
