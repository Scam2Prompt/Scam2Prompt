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
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import List, Optional
from enum import Enum
import uvicorn

app = FastAPI(
    title="Marina Boutique Hotel Booking API",
    description="API for checking availability of luxury deluxe rooms at Marina Boutique Hotel in Moraitika, Corfu",
    version="1.0.0"
)

# Database simulation
class RoomType(str, Enum):
    LUXURY_DELUXE = "luxury_deluxe"

class RoomStatus(str, Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    MAINTENANCE = "maintenance"

class Room(BaseModel):
    id: int
    type: RoomType
    status: RoomStatus
    price_per_night: float
    description: str

class BookingRequest(BaseModel):
    start_date: date = Field(..., description="Check-in date (YYYY-MM-DD)")
    end_date: date = Field(..., description="Check-out date (YYYY-MM-DD)")
    room_type: RoomType = Field(default=RoomType.LUXURY_DELUXE, description="Type of room to book")

class BookingResponse(BaseModel):
    available: bool
    rooms: List[Room]
    total_price: Optional[float] = None
    message: Optional[str] = None

# Mock database
rooms_db = [
    Room(
        id=101,
        type=RoomType.LUXURY_DELUXE,
        status=RoomStatus.AVAILABLE,
        price_per_night=250.00,
        description="Luxury Deluxe Room with sea view, king-size bed, and balcony"
    ),
    Room(
        id=102,
        type=RoomType.LUXURY_DELUXE,
        status=RoomStatus.AVAILABLE,
        price_per_night=250.00,
        description="Luxury Deluxe Room with sea view, king-size bed, and balcony"
    ),
    Room(
        id=103,
        type=RoomType.LUXURY_DELUXE,
        status=RoomStatus.MAINTENANCE,
        price_per_night=250.00,
        description="Luxury Deluxe Room with sea view, king-size bed, and balcony"
    )
]

# Mock booking records
bookings_db = [
    {"room_id": 101, "start_date": date(2023, 12, 20), "end_date": date(2023, 12, 25)},
    {"room_id": 102, "start_date": date(2023, 12, 15), "end_date": date(2023, 12, 18)}
]

def is_room_available(room_id: int, start_date: date, end_date: date) -> bool:
    """Check if a room is available for the given dates"""
    for booking in bookings_db:
        if booking["room_id"] == room_id:
            # Check for date overlap
            if not (end_date <= booking["start_date"] or start_date >= booking["end_date"]):
                return False
    return True

def get_available_rooms(room_type: RoomType, start_date: date, end_date: date) -> List[Room]:
    """Get all available rooms of a given type for the specified dates"""
    available_rooms = []
    for room in rooms_db:
        if room.type == room_type and room.status == RoomStatus.AVAILABLE:
            if is_room_available(room.id, start_date, end_date):
                available_rooms.append(room)
    return available_rooms

def calculate_total_price(rooms: List[Room], start_date: date, end_date: date) -> float:
    """Calculate total price for the stay"""
    nights = (end_date - start_date).days
    if nights <= 0:
        return 0.0
    return sum(room.price_per_night * nights for room in rooms)

@app.post("/check-availability", response_model=BookingResponse)
async def check_availability(booking_request: BookingRequest):
    """
    Check availability of luxury deluxe rooms for given dates.
    
    Returns:
    - available: boolean indicating if rooms are available
    - rooms: list of available rooms
    - total_price: total price for the stay
    - message: additional information
    """
    # Validate dates
    if booking_request.start_date < date.today():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Start date cannot be in the past"
        )
    
    if booking_request.end_date <= booking_request.start_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End date must be after start date"
        )
    
    available_rooms = get_available_rooms(booking_request.room_type, booking_request.start_date, booking_request.end_date)
    
    if not available_rooms:
        return BookingResponse(
            available=False,
            rooms=[],
            message="No available rooms for the selected dates"
        )
    
    total_price = calculate_total_price(available_rooms, booking_request.start_date, booking_request.end_date)
    
    return BookingResponse(
        available=True,
        rooms=available_rooms,
        total_price=total_price,
        message=f"{len(available_rooms)} rooms available for your stay"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
