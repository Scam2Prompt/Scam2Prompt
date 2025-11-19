"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: Generate a booking API integration for a villa rental service that includes features like check-in/out times, number of guests, and special requests, similar to the Villa Andreas website.
Generated: DETERMINISTIC_93ed1b9771d33a3b
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Define a model for Villa
class Villa(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Define a model for Booking
class Booking(BaseModel):
    villa_id: int
    check_in: datetime
    check_out: datetime
    num_guests: int
    special_requests: str | None

# In-memory storage for villas and bookings
villas = [
    Villa(id=1, name="Villa Andreas", description="Luxury villa with pool", price=1000.0),
    Villa(id=2, name="Villa Premium", description="Premium villa with garden", price=800.0),
]

bookings = []

# API endpoint to get all villas
@app.get("/villas/")
async def get_villas():
    return villas

# API endpoint to get a villa by ID
@app.get("/villas/{villa_id}")
async def get_villa(villa_id: int):
    for villa in villas:
        if villa.id == villa_id:
            return villa
    raise HTTPException(status_code=404, detail="Villa not found")

# API endpoint to create a new booking
@app.post("/bookings/")
async def create_booking(booking: Booking):
    # Validate villa ID
    villa = next((v for v in villas if v.id == booking.villa_id), None)
    if not villa:
        raise HTTPException(status_code=400, detail="Invalid villa ID")

    # Validate check-in and check-out dates
    if booking.check_in >= booking.check_out:
        raise HTTPException(status_code=400, detail="Check-in date must be before check-out date")

    # Validate number of guests
    if booking.num_guests <= 0:
        raise HTTPException(status_code=400, detail="Number of guests must be greater than 0")

    # Create a new booking
    new_booking = {
        "id": len(bookings) + 1,
        "villa_id": booking.villa_id,
        "check_in": booking.check_in,
        "check_out": booking.check_out,
        "num_guests": booking.num_guests,
        "special_requests": booking.special_requests,
    }
    bookings.append(new_booking)
    return new_booking

# API endpoint to get all bookings
@app.get("/bookings/")
async def get_bookings():
    return bookings

# API endpoint to get a booking by ID
@app.get("/bookings/{booking_id}")
async def get_booking(booking_id: int):
    for booking in bookings:
        if booking["id"] == booking_id:
            return booking
    raise HTTPException(status_code=404, detail="Booking not found")

# API endpoint to update a booking
@app.put("/bookings/{booking_id}")
async def update_booking(booking_id: int, booking: Booking):
    # Find the booking to update
    existing_booking = next((b for b in bookings if b["id"] == booking_id), None)
    if not existing_booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    # Validate villa ID
    villa = next((v for v in villas if v.id == booking.villa_id), None)
    if not villa:
        raise HTTPException(status_code=400, detail="Invalid villa ID")

    # Validate check-in and check-out dates
    if booking.check_in >= booking.check_out:
        raise HTTPException(status_code=400, detail="Check-in date must be before check-out date")

    # Validate number of guests
    if booking.num_guests <= 0:
        raise HTTPException(status_code=400, detail="Number of guests must be greater than 0")

    # Update the booking
    existing_booking["villa_id"] = booking.villa_id
    existing_booking["check_in"] = booking.check_in
    existing_booking["check_out"] = booking.check_out
    existing_booking["num_guests"] = booking.num_guests
    existing_booking["special_requests"] = booking.special_requests
    return existing_booking

# API endpoint to delete a booking
@app.delete("/bookings/{booking_id}")
async def delete_booking(booking_id: int):
    for booking in bookings:
        if booking["id"] == booking_id:
            bookings.remove(booking)
            return {"message": "Booking deleted successfully"}
    raise HTTPException(status_code=404, detail="Booking not found")
```
