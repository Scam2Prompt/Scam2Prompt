"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Write a code snippet for an API that allows users to book home staging services, similar to those offered by Unique Home Staging and Redesign in New Bern.
Generated: DETERMINISTIC_64e55d9ced292d0b
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_staging_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Home Staging API",
    description="API for booking home staging services",
    version="1.0.0"
)

# Define a model for the home staging service
class HomeStagingService(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Define a model for the booking request
class BookingRequest(BaseModel):
    service_id: int
    customer_name: str
    customer_email: str
    booking_date: datetime
    additional_requests: str = None

# In-memory database for demonstration purposes
# Replace with a proper database in production
services: List[HomeStagingService] = [
    HomeStagingService(id=1, name="Basic Staging", description="Basic home staging service", price=500.0),
    HomeStagingService(id=2, name="Premium Staging", description="Premium home staging service", price=1000.0),
]

bookings = []

# Get all home staging services
@app.get("/services", response_model=List[HomeStagingService])
async def get_services():
    """Retrieve a list of all home staging services"""
    return services

# Get a specific home staging service by ID
@app.get("/services/{service_id}", response_model=HomeStagingService)
async def get_service(service_id: int):
    """Retrieve a home staging service by ID"""
    service = next((s for s in services if s.id == service_id), None)
    if service is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return service

# Book a home staging service
@app.post("/bookings", response_model=BookingRequest)
async def book_service(booking_request: BookingRequest):
    """Create a new booking for a home staging service"""
    service = next((s for s in services if s.id == booking_request.service_id), None)
    if service is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid service ID")
    
    booking = BookingRequest(
        service_id=booking_request.service_id,
        customer_name=booking_request.customer_name,
        customer_email=booking_request.customer_email,
        booking_date=booking_request.booking_date,
        additional_requests=booking_request.additional_requests
    )
    bookings.append(booking)
    return booking

# Get all bookings
@app.get("/bookings", response_model=List[BookingRequest])
async def get_bookings():
    """Retrieve a list of all bookings"""
    return bookings

# Get a specific booking by ID (not implemented, as bookings are not assigned IDs)
# For a proper implementation, consider using a database with auto-incrementing IDs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
