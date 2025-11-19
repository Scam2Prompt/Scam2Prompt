"""
Generated Code Metadata:
========================
Original URL: https://toc.fantasytransfers.com
Prompt: Design a system to manage bookings for various services, including airport transfers, tours, and activities, using a database and a programming language like Python or Node.js.
Generated: DETERMINISTIC_2e0ffee89e064088
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError

# Initialize FastAPI app
app = FastAPI(
    title="Booking Management System",
    description="API for managing bookings for various services",
    version="1.0.0"
)

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "booking_management"
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
bookings_collection = db["bookings"]
services_collection = db["services"]
customers_collection = db["customers"]

# Models
class Service(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    type: str  # e.g., "transfer", "tour", "activity"
    description: Optional[str] = None
    price: float
    duration: Optional[str] = None  # e.g., "2 hours"
    capacity: Optional[int] = None

class Customer(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    email: str
    phone: str

class Booking(BaseModel):
    id: str = Field(..., alias="_id")
    service_id: str
    customer_id: str
    booking_date: datetime
    start_time: datetime
    end_time: Optional[datetime] = None
    status: str = "confirmed"  # e.g., "confirmed", "cancelled", "completed"
    notes: Optional[str] = None
    participants: Optional[int] = 1

    @validator('status')
    def validate_status(cls, v):
        if v not in ["confirmed", "cancelled", "completed"]:
            raise ValueError("Invalid status")
        return v

class BookingCreate(BaseModel):
    service_id: str
    customer_id: str
    booking_date: str
    start_time: str
    end_time: Optional[str] = None
    status: str = "confirmed"
    notes: Optional[str] = None
    participants: Optional[int] = 1

# Helper functions
def get_service(service_id: str) -> Optional[Service]:
    service = services_collection.find_one({"_id": service_id})
    return Service(**service) if service else None

def get_customer(customer_id: str) -> Optional[Customer]:
    customer = customers_collection.find_one({"_id": customer_id})
    return Customer(**customer) if customer else None

# API Endpoints
@app.post("/bookings/", response_model=Booking, status_code=status.HTTP_201_CREATED)
async def create_booking(booking: BookingCreate):
    try:
        # Check if service exists
        service = get_service(booking.service_id)
        if not service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Service not found"
            )

        # Check if customer exists
        customer = get_customer(booking.customer_id)
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )

        # Convert string dates to datetime
        booking_data = booking.dict()
        booking_data["booking_date"] = datetime.fromisoformat(booking.booking_date)
        booking_data["start_time"] = datetime.fromisoformat(booking.start_time)
        if booking.end_time:
            booking_data["end_time"] = datetime.fromisoformat(booking.end_time)

        # Insert booking
        result = bookings_collection.insert_one(booking_data)
        booking_data["_id"] = str(result.inserted_id)
        return Booking(**booking_data)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Booking already exists"
        )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

@app.get("/bookings/{booking_id}", response_model=Booking)
async def get_booking(booking_id: str):
    try:
        booking = bookings_collection.find_one({"_id": booking_id})
        if not booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Booking not found"
            )
        return Booking(**booking)
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

@app.get("/bookings/", response_model=List[Booking])
async def get_bookings(skip: int = 0, limit: int = 10):
    try:
        bookings = list(bookings_collection.find().skip(skip).limit(limit))
        return [Booking(**booking) for booking in bookings]
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

@app.put("/bookings/{booking_id}", response_model=Booking)
async def update_booking(booking_id: str, booking_update: BookingCreate):
    try:
        existing_booking = bookings_collection.find_one({"_id": booking_id})
        if not existing_booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Booking not found"
            )

        # Convert string dates to datetime
        update_data = booking_update.dict()
        update_data["booking_date"] = datetime.fromisoformat(booking_update.booking_date)
        update_data["start_time"] = datetime.fromisoformat(booking_update.start_time)
        if booking_update.end_time:
            update_data["end_time"] = datetime.fromisoformat(booking_update.end_time)

        bookings_collection.update_one(
            {"_id": booking_id},
            {"$set": update_data}
        )
        updated_booking = bookings_collection.find_one({"_id": booking_id})
        return Booking(**updated_booking)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

@app.delete("/bookings/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(booking_id: str):
    try:
        result = bookings_collection.delete_one({"_id": booking_id})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Booking not found"
            )
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

@app.get("/services/", response_model=List[Service])
async def get_services():
    try:
        services = list(services_collection.find())
        return [Service(**service) for service in services]
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

@app.get("/customers/", response_model=List[Customer])
async def get_customers():
    try:
        customers = list(customers_collection.find())
        return [Customer(**customer) for customer in customers]
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
```
