"""
Generated Code Metadata:
========================
Original URL: https://inkasluxury.com
Prompt: Generate a code snippet for a travel booking API that allows users to customize their itineraries for tours in Peru, similar to the personalized experiences offered by Inkas Luxury.
Generated: DETERMINISTIC_d02c8518d6584ab9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_booking_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Peru Tour Itinerary API",
    description="API for customizing tour itineraries in Peru",
    version="1.0.0"
)

class Tour(BaseModel):
    """Tour model"""
    id: int
    name: str
    description: str
    price: float
    duration: int  # in days

class Itinerary(BaseModel):
    """Itinerary model"""
    id: int
    tour_id: int
    day: int
    activities: List[str]

class UserRequest(BaseModel):
    """User request model"""
    tour_id: int
    num_days: int
    preferred_activities: List[str]

class ItineraryResponse(BaseModel):
    """Itinerary response model"""
    itinerary: List[Itinerary]

# In-memory data store for demonstration purposes
tours = [
    Tour(id=1, name="Machu Picchu Tour", description="Explore Machu Picchu", price=1000.0, duration=5),
    Tour(id=2, name="Lima to Cusco Tour", description="Discover Lima and Cusco", price=800.0, duration=4)
]

itineraries = [
    Itinerary(id=1, tour_id=1, day=1, activities=["Check-in to hotel", "Visit Plaza de Armas"]),
    Itinerary(id=2, tour_id=1, day=2, activities=["Machu Picchu guided tour", "Sun Gate visit"]),
    Itinerary(id=3, tour_id=2, day=1, activities=["Lima city tour", "Visit Miraflores district"]),
    Itinerary(id=4, tour_id=2, day=2, activities=["Cusco city tour", "Visit Sacsayhuaman fortress"])
]

@app.get("/tours/")
def get_tours():
    """Get all tours"""
    return tours

@app.get("/tours/{tour_id}")
def get_tour(tour_id: int):
    """Get a tour by ID"""
    tour = next((t for t in tours if t.id == tour_id), None)
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    return tour

@app.post("/itineraries/")
def create_itinerary(user_request: UserRequest):
    """Create a customized itinerary"""
    tour = next((t for t in tours if t.id == user_request.tour_id), None)
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")

    itinerary = []
    for day in range(1, user_request.num_days + 1):
        activities = [a for a in [i.activities for i in itineraries if i.tour_id == user_request.tour_id and i.day == day] if a]
        filtered_activities = [a for a in activities[0] if a in user_request.preferred_activities]
        itinerary.append(Itinerary(id=len(itineraries) + 1, tour_id=user_request.tour_id, day=day, activities=filtered_activities))

    return ItineraryResponse(itinerary=itinerary)

@app.get("/itineraries/")
def get_itineraries():
    """Get all itineraries"""
    return itineraries

@app.get("/itineraries/{itinerary_id}")
def get_itinerary(itinerary_id: int):
    """Get an itinerary by ID"""
    itinerary = next((i for i in itineraries if i.id == itinerary_id), None)
    if itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary
```

```python
# main.py
import uvicorn
from travel_booking_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
