"""
Generated Code Metadata:
========================
Original URL: https://casaamalfitana.com
Prompt: Design a simple API to manage restaurant reservations, including endpoints for sending and receiving reservation requests, using Casa Amalfitana's reservation form as a reference.
Generated: DETERMINISTIC_a135d9db9e0cd7cc
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Restaurant Reservation API for Casa Amalfitana
This API handles creating, retrieving, and managing restaurant reservations.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional
import uuid

app = FastAPI(
    title="Casa Amalfitana Reservation API",
    description="API for managing restaurant reservations",
    version="1.0.0"
)

# In-memory database for demonstration (replace with actual database in production)
reservations_db = {}

class Reservation(BaseModel):
    """Model representing a restaurant reservation"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    customer_name: str = Field(..., min_length=1, max_length=100)
    customer_email: EmailStr
    phone_number: str = Field(..., regex=r'^\+?[0-9]{8,15}$')
    party_size: int = Field(..., gt=0, le=20)
    reservation_date: datetime
    special_requests: Optional[str] = Field(None, max_length=500)
    
    @validator('reservation_date')
    def validate_reservation_date(cls, value):
        """Ensure reservation date is in the future"""
        if value < datetime.now():
            raise ValueError("Reservation date must be in the future")
        return value

class ReservationResponse(BaseModel):
    """Response model for reservation operations"""
    id: str
    customer_name: str
    reservation_date: datetime
    party_size: int
    status: str = "confirmed"

@app.post("/reservations/", response_model=ReservationResponse, status_code=status.HTTP_201_CREATED)
async def create_reservation(reservation: Reservation):
    """
    Create a new reservation
    
    Args:
        reservation: Reservation details
        
    Returns:
        Confirmation with reservation details
    """
    if reservation.id in reservations_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Reservation ID already exists"
        )
    
    reservations_db[reservation.id] = reservation.dict()
    return ReservationResponse(
        id=reservation.id,
        customer_name=reservation.customer_name,
        reservation_date=reservation.reservation_date,
        party_size=reservation.party_size
    )

@app.get("/reservations/{reservation_id}", response_model=Reservation)
async def get_reservation(reservation_id: str):
    """
    Retrieve a reservation by ID
    
    Args:
        reservation_id: UUID of the reservation
        
    Returns:
        Full reservation details
    """
    if reservation_id not in reservations_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reservation not found"
        )
    return reservations_db[reservation_id]

@app.get("/reservations/", response_model=list[ReservationResponse])
async def list_reservations():
    """
    List all reservations
    
    Returns:
        List of all reservations with basic info
    """
    return [
        ReservationResponse(
            id=reservation['id'],
            customer_name=reservation['customer_name'],
            reservation_date=reservation['reservation_date'],
            party_size=reservation['party_size']
        )
        for reservation in reservations_db.values()
    ]

@app.delete("/reservations/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_reservation(reservation_id: str):
    """
    Cancel a reservation by ID
    
    Args:
        reservation_id: UUID of the reservation to cancel
    """
    if reservation_id not in reservations_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reservation not found"
        )
    del reservations_db[reservation_id]
    return None
```
