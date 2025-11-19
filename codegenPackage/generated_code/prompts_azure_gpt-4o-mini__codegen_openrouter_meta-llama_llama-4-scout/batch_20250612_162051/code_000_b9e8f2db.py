"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Generate a reservation system API for a hotel like Saman Eventos that handles bookings for business and leisure stays.
Generated: DETERMINISTIC_b9e8f2db6eafd811
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# reservation_system.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Hotel Reservation System API",
    description="API for managing hotel reservations",
    version="1.0.0"
)

# Define a model for Room
class Room(BaseModel):
    id: int
    room_type: str
    capacity: int
    rate: float

# Define a model for Reservation
class Reservation(BaseModel):
    id: int
    room_id: int
    guest_name: str
    arrival_date: datetime
    departure_date: datetime
    status: str

# In-memory data store for demonstration purposes
rooms: List[Room] = [
    Room(id=1, room_type="Single", capacity=1, rate=100.0),
    Room(id=2, room_type="Double", capacity=2, rate=150.0),
    Room(id=3, room_type="Suite", capacity=4, rate=300.0)
]

reservations: List[Reservation] = []

# API endpoint to get all rooms
@app.get("/rooms", response_model=List[Room])
def get_rooms():
    return rooms

# API endpoint to get a room by ID
@app.get("/rooms/{room_id}", response_model=Room)
def get_room(room_id: int):
    room = next((r for r in rooms if r.id == room_id), None)
    if room is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    return room

# API endpoint to create a new reservation
@app.post("/reservations", response_model=Reservation)
def create_reservation(reservation: Reservation):
    existing_reservation = next((r for r in reservations if r.id == reservation.id), None)
    if existing_reservation:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Reservation already exists")
    reservations.append(reservation)
    return reservation

# API endpoint to get all reservations
@app.get("/reservations", response_model=List[Reservation])
def get_reservations():
    return reservations

# API endpoint to get a reservation by ID
@app.get("/reservations/{reservation_id}", response_model=Reservation)
def get_reservation(reservation_id: int):
    reservation = next((r for r in reservations if r.id == reservation_id), None)
    if reservation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")
    return reservation

# API endpoint to update a reservation
@app.put("/reservations/{reservation_id}", response_model=Reservation)
def update_reservation(reservation_id: int, reservation: Reservation):
    existing_reservation = next((r for r in reservations if r.id == reservation_id), None)
    if existing_reservation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")
    existing_reservation.room_id = reservation.room_id
    existing_reservation.guest_name = reservation.guest_name
    existing_reservation.arrival_date = reservation.arrival_date
    existing_reservation.departure_date = reservation.departure_date
    existing_reservation.status = reservation.status
    return existing_reservation

# API endpoint to cancel a reservation
@app.delete("/reservations/{reservation_id}")
def cancel_reservation(reservation_id: int):
    reservation = next((r for r in reservations if r.id == reservation_id), None)
    if reservation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")
    reservations.remove(reservation)
    return {"message": "Reservation cancelled successfully"}

# API endpoint to check room availability
@app.get("/rooms/availability", response_model=List[Room])
def check_room_availability(arrival_date: datetime, departure_date: datetime):
    available_rooms = []
    for room in rooms:
        is_available = True
        for reservation in reservations:
            if reservation.room_id == room.id and \
               (arrival_date < reservation.departure_date and departure_date > reservation.arrival_date):
                is_available = False
                break
        if is_available:
            available_rooms.append(room)
    return available_rooms
```

```python
# main.py
import uvicorn
from reservation_system import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
