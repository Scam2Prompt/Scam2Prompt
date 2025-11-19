"""
Generated Code Metadata:
========================
Original URL: https://atozdestinos.com.br
Prompt: "Design an API for a travel booking platform that integrates with multiple payment gateways and provides real-time itinerary updates for customers."
Generated: DETERMINISTIC_22bdbcb3a28f9f04
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Travel Booking Platform API

This module provides an API for a travel booking platform that integrates with
multiple payment gateways and provides real-time itinerary updates.
"""

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Travel Booking Platform API",
    description="API for travel bookings with payment gateway integration and real-time updates",
    version="1.0.0"
)

# OAuth2 security scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (simplified for example)
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    password_hash: str
    is_active: bool = True

class Booking(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    trip_details: dict
    status: str = "confirmed"
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Payment(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    booking_id: str
    amount: float
    currency: str = "USD"
    gateway: str
    status: str = "pending"
    transaction_id: Optional[str] = None

class ItineraryUpdate(BaseModel):
    booking_id: str
    update_type: str
    message: str
    timestamp: datetime = Field(default_factory=datetime.now)

# Mock database
db = {
    "users": {},
    "bookings": {},
    "payments": {},
    "itinerary_updates": {}
}

# Payment gateways
class PaymentGateway:
    @staticmethod
    def process_payment(booking_id: str, amount: float, currency: str, gateway: str) -> dict:
        """Process payment with the specified gateway"""
        # In a real implementation, this would interface with actual payment APIs
        transaction_id = f"txn_{str(uuid.uuid4())[:8]}"
        return {
            "transaction_id": transaction_id,
            "status": "completed",
            "gateway": gateway
        }

# Authentication
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Mock authentication function"""
    user = db["users"].get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# API Endpoints
@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(email: EmailStr, password: str):
    """Create a new user account"""
    user_id = str(uuid.uuid4())
    user = User(
        id=user_id,
        email=email,
        password_hash=password  # In production, hash the password properly
    )
    db["users"][user_id] = user.dict()
    return {"user_id": user_id}

@app.post("/bookings/", status_code=status.HTTP_201_CREATED)
async def create_booking(
    trip_details: dict,
    current_user: User = Depends(get_current_user)
):
    """Create a new booking"""
    booking = Booking(
        user_id=current_user.id,
        trip_details=trip_details
    )
    db["bookings"][booking.id] = booking.dict()
    return {"booking_id": booking.id}

@app.post("/bookings/{booking_id}/payments/", status_code=status.HTTP_201_CREATED)
async def process_payment(
    booking_id: str,
    amount: float,
    currency: str,
    gateway: str,
    current_user: User = Depends(get_current_user)
):
    """Process payment for a booking"""
    if booking_id not in db["bookings"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    if db["bookings"][booking_id]["user_id"] != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this booking"
        )
    
    payment_result = PaymentGateway.process_payment(
        booking_id, amount, currency, gateway
    )
    
    payment = Payment(
        booking_id=booking_id,
        amount=amount,
        currency=currency,
        gateway=gateway,
        status=payment_result["status"],
        transaction_id=payment_result["transaction_id"]
    )
    
    db["payments"][payment.id] = payment.dict()
    
    # Update booking status
    db["bookings"][booking_id]["status"] = "paid"
    db["bookings"][booking_id]["updated_at"] = datetime.now()
    
    return {"payment_id": payment.id, "status": payment.status}

@app.get("/bookings/{booking_id}/itinerary-updates/")
async def get_itinerary_updates(
    booking_id: str,
    current_user: User = Depends(get_current_user)
):
    """Get itinerary updates for a booking"""
    if booking_id not in db["bookings"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    if db["bookings"][booking_id]["user_id"] != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this booking"
        )
    
    updates = [
        update for update in db["itinerary_updates"].values()
        if update["booking_id"] == booking_id
    ]
    return {"updates": updates}

@app.post("/itinerary-updates/", status_code=status.HTTP_201_CREATED)
async def create_itinerary_update(
    booking_id: str,
    update_type: str,
    message: str,
    # In production, this would be protected with admin authentication
):
    """Create an itinerary update (admin only)"""
    if booking_id not in db["bookings"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    update = ItineraryUpdate(
        booking_id=booking_id,
        update_type=update_type,
        message=message
    )
    
    db["itinerary_updates"][str(uuid.uuid4())] = update.dict()
    
    # In production, this would trigger real-time notifications
    logger.info(f"New itinerary update for booking {booking_id}: {message}")
    
    return {"update_id": update.timestamp}

@app.get("/bookings/{booking_id}/status")
async def get_booking_status(
    booking_id: str,
    current_user: User = Depends(get_current_user)
):
    """Get the status of a booking"""
    if booking_id not in db["bookings"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    
    if db["bookings"][booking_id]["user_id"] != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this booking"
        )
    
    return {
        "status": db["bookings"][booking_id]["status"],
        "last_updated": db["bookings"][booking_id]["updated_at"]
    }

# WebSocket endpoint for real-time updates would be added here in production
```
