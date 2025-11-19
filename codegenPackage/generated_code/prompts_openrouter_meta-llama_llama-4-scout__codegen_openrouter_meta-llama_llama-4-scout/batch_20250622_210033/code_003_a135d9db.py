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
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Restaurant Reservation API",
    description="Manage restaurant reservations",
    version="1.0.0"
)

class Reservation(BaseModel):
    """Reservation model"""
    name: str
    email: str
    phone_number: str
    date: str
    time: str
    party_size: int

class ReservationRequest(BaseModel):
    """Reservation request model"""
    reservation: Reservation

class ReservationResponse(BaseModel):
    """Reservation response model"""
    id: int
    name: str
    email: str
    phone_number: str
    date: str
    time: str
    party_size: int

# In-memory reservation storage (replace with a database in production)
reservations: List[ReservationResponse] = []
next_id: int = 1

@app.post("/reservations/", status_code=status.HTTP_201_CREATED)
async def create_reservation(reservation_request: ReservationRequest):
    """Create a new reservation"""
    global next_id
    try:
        reservation = reservation_request.reservation
        if not reservation:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Reservation data is required")

        # Basic validation
        if len(reservation.name) < 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name is required")
        if not reservation.email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is required")
        if not reservation.phone_number:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone number is required")
        if not reservation.date:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Date is required")
        if not reservation.time:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Time is required")
        if reservation.party_size < 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Party size must be at least 1")

        new_reservation = ReservationResponse(
            id=next_id,
            name=reservation.name,
            email=reservation.email,
            phone_number=reservation.phone_number,
            date=reservation.date,
            time=reservation.time,
            party_size=reservation.party_size
        )
        reservations.append(new_reservation)
        next_id += 1
        return new_reservation
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/reservations/", status_code=status.HTTP_200_OK)
async def get_reservations():
    """Get all reservations"""
    return reservations

@app.get("/reservations/{reservation_id}", status_code=status.HTTP_200_OK)
async def get_reservation(reservation_id: int):
    """Get a reservation by ID"""
    for reservation in reservations:
        if reservation.id == reservation_id:
            return reservation
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")

@app.put("/reservations/{reservation_id}", status_code=status.HTTP_200_OK)
async def update_reservation(reservation_id: int, reservation_request: ReservationRequest):
    """Update a reservation"""
    for i, reservation in enumerate(reservations):
        if reservation.id == reservation_id:
            try:
                updated_reservation = reservation_request.reservation
                if not updated_reservation:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Reservation data is required")

                # Basic validation
                if len(updated_reservation.name) < 1:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name is required")
                if not updated_reservation.email:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is required")
                if not updated_reservation.phone_number:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone number is required")
                if not updated_reservation.date:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Date is required")
                if not updated_reservation.time:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Time is required")
                if updated_reservation.party_size < 1:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Party size must be at least 1")

                reservations[i] = ReservationResponse(
                    id=reservation_id,
                    name=updated_reservation.name,
                    email=updated_reservation.email,
                    phone_number=updated_reservation.phone_number,
                    date=updated_reservation.date,
                    time=updated_reservation.time,
                    party_size=updated_reservation.party_size
                )
                return reservations[i]
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")

@app.delete("/reservations/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reservation(reservation_id: int):
    """Delete a reservation"""
    for i, reservation in enumerate(reservations):
        if reservation.id == reservation_id:
            del reservations[i]
            return {"message": f"Reservation {reservation_id} deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")
```

```python
# main.py

from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
