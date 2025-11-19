"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Create a sample API endpoint for a home services company that includes functionalities for booking water tank cleaning and thermal insulation services, reflecting the services provided by شركة انجاز.
Generated: DETERMINISTIC_98eb94bd342ff7ef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI(
    title="Home Services API",
    description="API for booking home services",
    version="1.0.0"
)

# Define services
class ServiceType(str, Enum):
    water_tank_cleaning = "water_tank_cleaning"
    thermal_insulation = "thermal_insulation"

# Request model for booking service
class BookServiceRequest(BaseModel):
    service_type: ServiceType
    customer_name: str
    customer_phone: str
    customer_address: str
    service_date: str
    service_time: str

# Response model for booking service
class BookServiceResponse(BaseModel):
    booking_id: int
    message: str

# In-memory storage for bookings (replace with database in production)
bookings = []
next_booking_id = 1

# API endpoint for booking services
@app.post("/book-service", response_model=BookServiceResponse)
async def book_service(request: BookServiceRequest):
    global next_booking_id
    try:
        # Validate request
        if not request.service_type:
            raise HTTPException(status_code=400, detail="Service type is required")
        
        # Create new booking
        booking = {
            "booking_id": next_booking_id,
            "service_type": request.service_type,
            "customer_name": request.customer_name,
            "customer_phone": request.customer_phone,
            "customer_address": request.customer_address,
            "service_date": request.service_date,
            "service_time": request.service_time
        }
        
        # Store booking
        bookings.append(booking)
        next_booking_id += 1
        
        # Return booking response
        return BookServiceResponse(booking_id=booking["booking_id"], message="Service booked successfully")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint for listing bookings
@app.get("/list-bookings")
async def list_bookings():
    try:
        return bookings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint for getting booking by ID
@app.get("/get-booking/{booking_id}")
async def get_booking(booking_id: int):
    try:
        for booking in bookings:
            if booking["booking_id"] == booking_id:
                return booking
        raise HTTPException(status_code=404, detail="Booking not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint for cancelling booking
@app.delete("/cancel-booking/{booking_id}")
async def cancel_booking(booking_id: int):
    try:
        for i, booking in enumerate(bookings):
            if booking["booking_id"] == booking_id:
                del bookings[i]
                return {"message": "Booking cancelled successfully"}
        raise HTTPException(status_code=404, detail="Booking not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
