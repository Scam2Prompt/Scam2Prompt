"""
Generated Code Metadata:
========================
Original URL: https://lhotel-des-chats.com
Prompt: Design a RESTful API for a cat daycare and boarding facility, including endpoints for creating, reading, updating, and deleting bookings and customer information.
Generated: DETERMINISTIC_eebde040ec3c9f9c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from uuid import uuid4, UUID
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(
    title="Cat Daycare API",
    description="A RESTful API for managing cat daycare and boarding facility bookings",
    version="1.0.0"
)

# Mock database
db = {
    "customers": {},
    "bookings": {}
}

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class Customer(BaseModel):
    customer_id: UUID
    name: str
    email: str
    phone: str
    address: str

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class Booking(BaseModel):
    booking_id: UUID
    customer_id: UUID
    cat_name: str
    breed: str
    age: int
    start_date: date
    end_date: date
    special_instructions: Optional[str] = None
    status: str = "confirmed"  # confirmed, cancelled, completed

class BookingCreate(BaseModel):
    customer_id: UUID
    cat_name: str
    breed: str
    age: int
    start_date: date
    end_date: date
    special_instructions: Optional[str] = None

class BookingUpdate(BaseModel):
    cat_name: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    special_instructions: Optional[str] = None
    status: Optional[str] = None

# Helper functions
def get_customer(customer_id: UUID):
    if customer_id not in db["customers"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return db["customers"][customer_id]

def get_booking(booking_id: UUID):
    if booking_id not in db["bookings"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return db["bookings"][booking_id]

# Authentication (mock)
def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, validate the token here
    if token != "secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return {"username": "admin"}

# Customer endpoints
@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, current_user: dict = Depends(get_current_user)):
    customer_id = uuid4()
    db_customer = Customer(
        customer_id=customer_id,
        **customer.dict()
    )
    db["customers"][customer_id] = db_customer
    return db_customer

@app.get("/customers/", response_model=List[Customer])
def read_customers(skip: int = 0, limit: int = 100, current_user: dict = Depends(get_current_user)):
    return list(db["customers"].values())[skip : skip + limit]

@app.get("/customers/{customer_id}", response_model=Customer)
def read_customer(customer_id: UUID, current_user: dict = Depends(get_current_user)):
    return get_customer(customer_id)

@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(
    customer_id: UUID,
    customer: CustomerCreate,
    current_user: dict = Depends(get_current_user)
):
    db_customer = get_customer(customer_id)
    update_data = customer.dict(exclude_unset=True)
    updated_customer = db_customer.copy(update=update_data)
    db["customers"][customer_id] = updated_customer
    return updated_customer

@app.delete("/customers/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: UUID, current_user: dict = Depends(get_current_user)):
    get_customer(customer_id)  # Check if exists
    del db["customers"][customer_id]
    return None

# Booking endpoints
@app.post("/bookings/", response_model=Booking, status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingCreate, current_user: dict = Depends(get_current_user)):
    booking_id = uuid4()
    get_customer(booking.customer_id)  # Validate customer exists
    db_booking = Booking(
        booking_id=booking_id,
        **booking.dict()
    )
    db["bookings"][booking_id] = db_booking
    return db_booking

@app.get("/bookings/", response_model=List[Booking])
def read_bookings(skip: int = 0, limit: int = 100, current_user: dict = Depends(get_current_user)):
    return list(db["bookings"].values())[skip : skip + limit]

@app.get("/bookings/{booking_id}", response_model=Booking)
def read_booking(booking_id: UUID, current_user: dict = Depends(get_current_user)):
    return get_booking(booking_id)

@app.put("/bookings/{booking_id}", response_model=Booking)
def update_booking(
    booking_id: UUID,
    booking: BookingUpdate,
    current_user: dict = Depends(get_current_user)
):
    db_booking = get_booking(booking_id)
    update_data = booking.dict(exclude_unset=True)
    updated_booking = db_booking.copy(update=update_data)
    db["bookings"][booking_id] = updated_booking
    return updated_booking

@app.delete("/bookings/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(booking_id: UUID, current_user: dict = Depends(get_current_user)):
    get_booking(booking_id)  # Check if exists
    del db["bookings"][booking_id]
    return None

@app.get("/customers/{customer_id}/bookings", response_model=List[Booking])
def get_customer_bookings(customer_id: UUID, current_user: dict = Depends(get_current_user)):
    get_customer(customer_id)  # Validate customer exists
    return [booking for booking in db["bookings"].values() if booking.customer_id == customer_id]
```
