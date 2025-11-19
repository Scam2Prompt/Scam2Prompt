"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Illustrate how to implement a booking system for residential power washing services, based on the service structure of Klean-Pro Utah.
Generated: DETERMINISTIC_c30e226f3a732adc
Batch ID: 20250612_155128
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
from typing import Optional, List, Dict
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Klean-Pro Utah Power Washing Booking System",
    description="API for residential power washing service bookings",
    version="1.0.0"
)

# Database simulation
bookings_db = []
customers_db = []
services_db = []

class ServiceType(str, Enum):
    HOUSE_WASH = "House Wash"
    DRIVEWAY_CLEANING = "Driveway Cleaning"
    DECK_CLEANING = "Deck Cleaning"
    ROOF_CLEANING = "Roof Cleaning"
    FULL_PACKAGE = "Full Package"

class Service(BaseModel):
    id: str
    name: ServiceType
    description: str
    base_price: float
    estimated_duration: int  # in minutes

class Customer(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    address: str
    notes: Optional[str] = None

    @validator('email')
    def email_must_contain_at(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

class BookingStatus(str, Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Booking(BaseModel):
    id: str
    customer_id: str
    service_id: str
    scheduled_date: datetime.date
    scheduled_time: str
    status: BookingStatus = BookingStatus.PENDING
    notes: Optional[str] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @validator('scheduled_date')
    def scheduled_date_must_be_future(cls, v):
        if v < datetime.date.today():
            raise ValueError('Scheduled date must be in the future')
        return v

@app.on_event("startup")
async def startup_event():
    """Initialize sample data"""
    services_db.extend([
        Service(
            id="srv1",
            name=ServiceType.HOUSE_WASH,
            description="Complete exterior house wash",
            base_price=299.99,
            estimated_duration=120
        ),
        Service(
            id="srv2",
            name=ServiceType.DRIVEWAY_CLEANING,
            description="Driveway pressure washing",
            base_price=149.99,
            estimated_duration=60
        ),
        Service(
            id="srv3",
            name=ServiceType.FULL_PACKAGE,
            description="Complete exterior cleaning package",
            base_price=499.99,
            estimated_duration=240
        )
    ])

@app.get("/services", response_model=List[Service])
async def get_available_services():
    """Get all available services"""
    return services_db

@app.get("/services/{service_id}", response_model=Service)
async def get_service(service_id: str):
    """Get a specific service by ID"""
    service = next((s for s in services_db if s.id == service_id), None)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    return service

@app.post("/customers", response_model=Customer)
async def create_customer(customer: Customer):
    """Create a new customer"""
    if any(c.id == customer.id for c in customers_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer ID already exists"
        )
    customers_db.append(customer)
    return customer

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: str):
    """Get customer by ID"""
    customer = next((c for c in customers_db if c.id == customer_id), None)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer

@app.post("/bookings", response_model=Booking)
async def create_booking(booking: Booking):
    """Create a new booking"""
    # Validate customer exists
    if not any(c.id == booking.customer_id for c in customers_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer does not exist"
        )
    
    # Validate service exists
    if not any(s.id == booking.service_id for s in services_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Service does not exist"
        )
    
    # Check for booking conflicts (simplified)
    conflicting_bookings = [
        b for b in bookings_db
        if b.scheduled_date == booking.scheduled_date
        and b.scheduled_time == booking.scheduled_time
    ]
    
    if conflicting_bookings:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Time slot already booked"
        )
    
    bookings_db.append(booking)
    return booking

@app.get("/bookings", response_model=List[Booking])
async def get_bookings(
    status: Optional[BookingStatus] = None,
    date: Optional[datetime.date] = None
):
    """Get all bookings with optional filters"""
    result = bookings_db
    
    if status:
        result = [b for b in result if b.status == status]
    
    if date:
        result = [b for b in result if b.scheduled_date == date]
    
    return result

@app.get("/bookings/{booking_id}", response_model=Booking)
async def get_booking(booking_id: str):
    """Get a specific booking by ID"""
    booking = next((b for b in bookings_db if b.id == booking_id), None)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return booking

@app.put("/bookings/{booking_id}/status", response_model=Booking)
async def update_booking_status(booking_id: str, new_status: BookingStatus):
    """Update booking status"""
    booking = next((b for b in bookings_db if b.id == booking_id), None)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    booking.status = new_status
    return booking

@app.get("/availability/{date}")
async def check_availability(date: datetime.date):
    """Check available time slots for a given date"""
    if date < datetime.date.today():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Date must be in the future"
        )
    
    # Sample time slots
    all_slots = [
        "08:00 AM", "10:00 AM", "12:00 PM", 
        "02:00 PM", "04:00 PM"
    ]
    
    # Get booked slots for the date
    booked_slots = [
        b.scheduled_time for b in bookings_db
        if b.scheduled_date == date
    ]
    
    available_slots = [slot for slot in all_slots if slot not in booked_slots]
    
    return {
        "date": date,
        "available_slots": available_slots
    }
```
