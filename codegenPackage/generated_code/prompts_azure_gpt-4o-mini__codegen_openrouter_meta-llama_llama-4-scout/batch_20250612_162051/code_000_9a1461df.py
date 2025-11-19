"""
Generated Code Metadata:
========================
Original URL: https://marinahotelcorfu.com
Prompt: Generate a booking system API that allows users to check availability for luxury deluxe rooms at Marina Boutique Hotel in Moraitika, Corfu.
Generated: DETERMINISTIC_9a1461df7229e7a3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_system_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List

app = FastAPI(
    title="Marina Boutique Hotel Booking System API",
    description="API for booking luxury deluxe rooms at Marina Boutique Hotel in Moraitika, Corfu",
    version="1.0.0"
)

# Define the Room model
class Room(BaseModel):
    room_number: int
    room_type: str
    is_available: bool

# Define the Booking model
class Booking(BaseModel):
    room_number: int
    check_in: datetime
    check_out: datetime

# In-memory data store for demonstration purposes
# Replace with a database in a production environment
rooms: List[Room] = [
    Room(room_number=101, room_type="Luxury Deluxe", is_available=True),
    Room(room_number=102, room_type="Luxury Deluxe", is_available=True),
    Room(room_number=103, room_type="Luxury Deluxe", is_available=True),
]

bookings: List[Booking] = []

# API endpoint to check availability
@app.get("/availability")
async def check_availability(check_in: datetime, check_out: datetime):
    """
    Check availability for luxury deluxe rooms.

    Args:
    - check_in (datetime): Check-in date and time
    - check_out (datetime): Check-out date and time

    Returns:
    - A list of available rooms
    """
    available_rooms = []
    for room in rooms:
        is_room_available = True
        for booking in bookings:
            if room.room_number == booking.room_number:
                if (check_in >= booking.check_in and check_in < booking.check_out) or \
                   (check_out > booking.check_in and check_out <= booking.check_out) or \
                   (check_in <= booking.check_in and check_out >= booking.check_out):
                    is_room_available = False
                    break
        if is_room_available:
            available_rooms.append(room)
    return available_rooms

# API endpoint to book a room
@app.post("/book")
async def book_room(booking: Booking):
    """
    Book a luxury deluxe room.

    Args:
    - booking (Booking): Booking details

    Returns:
    - A success message
    """
    room = next((room for room in rooms if room.room_number == booking.room_number), None)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    if not room.is_available:
        raise HTTPException(status_code=400, detail="Room is not available")
    for existing_booking in bookings:
        if room.room_number == existing_booking.room_number:
            if (booking.check_in >= existing_booking.check_in and booking.check_in < existing_booking.check_out) or \
               (booking.check_out > existing_booking.check_in and booking.check_out <= existing_booking.check_out) or \
               (booking.check_in <= existing_booking.check_in and booking.check_out >= existing_booking.check_out):
                raise HTTPException(status_code=400, detail="Room is not available during this period")
    bookings.append(booking)
    room.is_available = False
    return {"message": "Room booked successfully"}

# API endpoint to cancel a booking
@app.delete("/cancel")
async def cancel_booking(room_number: int, check_in: datetime):
    """
    Cancel a booking.

    Args:
    - room_number (int): Room number
    - check_in (datetime): Check-in date and time

    Returns:
    - A success message
    """
    booking = next((booking for booking in bookings if booking.room_number == room_number and booking.check_in == check_in), None)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    bookings.remove(booking)
    room = next((room for room in rooms if room.room_number == room_number), None)
    room.is_available = True
    return {"message": "Booking cancelled successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
