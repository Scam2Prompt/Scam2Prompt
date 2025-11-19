"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: "Design a RESTful API for managing bloc services, including administration, maintenance, and cleaning, with endpoints for client access and feedback, as seen on BlocPrest."
Generated: DETERMINISTIC_5d8511522ef61e8d
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
from enum import Enum

app = FastAPI(
    title="Bloc Services API",
    description="RESTful API for managing bloc services including administration, maintenance, and cleaning.",
    version="1.0.0"
)

# Database mock (in production, use a real database)
db = {
    "services": [],
    "bookings": [],
    "feedbacks": [],
    "users": []
}

# Models
class ServiceType(str, Enum):
    ADMINISTRATION = "administration"
    MAINTENANCE = "maintenance"
    CLEANING = "cleaning"

class Service(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    type: ServiceType
    description: str
    price: float
    duration_minutes: int
    is_active: bool = True

class Booking(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    service_id: str
    user_id: str
    booking_date: datetime
    notes: Optional[str] = None
    status: str = "confirmed"  # confirmed, cancelled, completed

class Feedback(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    booking_id: str
    user_id: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    email: str
    phone: str
    is_admin: bool = False

# Helper functions
def get_service(service_id: str):
    for service in db["services"]:
        if service["id"] == service_id:
            return service
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Service not found"
    )

def get_booking(booking_id: str):
    for booking in db["bookings"]:
        if booking["id"] == booking_id:
            return booking
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Booking not found"
    )

def get_user(user_id: str):
    for user in db["users"]:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

# Service Endpoints
@app.post("/services/", response_model=Service, status_code=status.HTTP_201_CREATED)
def create_service(service: Service):
    """Create a new service"""
    service_dict = service.dict()
    db["services"].append(service_dict)
    return service_dict

@app.get("/services/", response_model=List[Service])
def list_services(service_type: Optional[ServiceType] = None):
    """List all services, optionally filtered by type"""
    if service_type:
        return [s for s in db["services"] if s["type"] == service_type]
    return db["services"]

@app.get("/services/{service_id}", response_model=Service)
def get_service_by_id(service_id: str):
    """Get a specific service by ID"""
    return get_service(service_id)

@app.put("/services/{service_id}", response_model=Service)
def update_service(service_id: str, updated_service: Service):
    """Update a service"""
    service = get_service(service_id)
    service.update(updated_service.dict())
    return service

@app.delete("/services/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(service_id: str):
    """Delete a service"""
    service = get_service(service_id)
    db["services"].remove(service)

# Booking Endpoints
@app.post("/bookings/", response_model=Booking, status_code=status.HTTP_201_CREATED)
def create_booking(booking: Booking):
    """Create a new booking"""
    # Validate service exists
    get_service(booking.service_id)
    # Validate user exists
    get_user(booking.user_id)
    
    booking_dict = booking.dict()
    db["bookings"].append(booking_dict)
    return booking_dict

@app.get("/bookings/", response_model=List[Booking])
def list_bookings(user_id: Optional[str] = None):
    """List all bookings, optionally filtered by user"""
    if user_id:
        return [b for b in db["bookings"] if b["user_id"] == user_id]
    return db["bookings"]

@app.get("/bookings/{booking_id}", response_model=Booking)
def get_booking_by_id(booking_id: str):
    """Get a specific booking by ID"""
    return get_booking(booking_id)

@app.put("/bookings/{booking_id}/cancel", response_model=Booking)
def cancel_booking(booking_id: str):
    """Cancel a booking"""
    booking = get_booking(booking_id)
    booking["status"] = "cancelled"
    return booking

# Feedback Endpoints
@app.post("/feedbacks/", response_model=Feedback, status_code=status.HTTP_201_CREATED)
def create_feedback(feedback: Feedback):
    """Create feedback for a booking"""
    # Validate booking exists
    booking = get_booking(feedback.booking_id)
    # Validate booking is completed
    if booking["status"] != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot leave feedback for incomplete booking"
        )
    # Validate user exists
    get_user(feedback.user_id)
    
    feedback_dict = feedback.dict()
    db["feedbacks"].append(feedback_dict)
    return feedback_dict

@app.get("/feedbacks/", response_model=List[Feedback])
def list_feedbacks(service_id: Optional[str] = None):
    """List all feedbacks, optionally filtered by service"""
    if service_id:
        # Get all bookings for this service
        service_bookings = [b["id"] for b in db["bookings"] if b["service_id"] == service_id]
        return [f for f in db["feedbacks"] if f["booking_id"] in service_bookings]
    return db["feedbacks"]

# User Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    """Create a new user"""
    # Check if email already exists
    if any(u["email"] == user.email for u in db["users"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    user_dict = user.dict()
    db["users"].append(user_dict)
    return user_dict

@app.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: str):
    """Get a specific user by ID"""
    return get_user(user_id)
```
