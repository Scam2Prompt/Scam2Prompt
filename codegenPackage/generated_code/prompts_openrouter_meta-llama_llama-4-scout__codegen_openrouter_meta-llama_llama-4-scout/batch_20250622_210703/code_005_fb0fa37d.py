"""
Generated Code Metadata:
========================
Original URL: https://gstouristcentre.gr
Prompt: "Suggest a set of RESTful API endpoints for a travel agency website, including endpoints for retrieving information about excursions, boat trips, and activities in Corfu."
Generated: DETERMINISTIC_fb0fa37d33403e4f
Batch ID: 20250622_210703
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
from typing import List

app = FastAPI(
    title="Corfu Travel Agency API",
    description="API for retrieving information about excursions, boat trips, and activities in Corfu",
    version="1.0.0"
)

# Define Pydantic models for API responses
class Excursion(BaseModel):
    id: int
    name: str
    description: str
    duration: str
    price: float

class BoatTrip(BaseModel):
    id: int
    name: str
    description: str
    departure_time: str
    price: float

class Activity(BaseModel):
    id: int
    name: str
    description: str
    location: str
    price: float

# In-memory data store (replace with a database in production)
excursions = [
    Excursion(id=1, name="Old Fortress Tour", description="Explore the historic Old Fortress", duration="3 hours", price=20.0),
    Excursion(id=2, name="Corfu City Tour", description="Discover the charming city of Corfu", duration="4 hours", price=30.0),
]

boat_trips = [
    BoatTrip(id=1, name="Island Hopping", description="Visit nearby islands", departure_time="09:00", price=50.0),
    BoatTrip(id=2, name="Sunset Cruise", description="Enjoy the breathtaking sunset", departure_time="17:00", price=40.0),
]

activities = [
    Activity(id=1, name="Scuba Diving", description="Explore the underwater world", location="Corfu Beach", price=60.0),
    Activity(id=2, name="Hiking Tour", description="Discover the natural beauty of Corfu", location="Corfu Mountains", price=40.0),
]

# API Endpoints
@app.get("/excursions/")
async def get_excursions():
    """Retrieve a list of all excursions"""
    return excursions

@app.get("/excursions/{excursion_id}")
async def get_excursion(excursion_id: int):
    """Retrieve information about a specific excursion"""
    for excursion in excursions:
        if excursion.id == excursion_id:
            return excursion
    raise HTTPException(status_code=404, detail="Excursion not found")

@app.get("/boat-trips/")
async def get_boat_trips():
    """Retrieve a list of all boat trips"""
    return boat_trips

@app.get("/boat-trips/{boat_trip_id}")
async def get_boat_trip(boat_trip_id: int):
    """Retrieve information about a specific boat trip"""
    for boat_trip in boat_trips:
        if boat_trip.id == boat_trip_id:
            return boat_trip
    raise HTTPException(status_code=404, detail="Boat trip not found")

@app.get("/activities/")
async def get_activities():
    """Retrieve a list of all activities"""
    return activities

@app.get("/activities/{activity_id}")
async def get_activity(activity_id: int):
    """Retrieve information about a specific activity"""
    for activity in activities:
        if activity.id == activity_id:
            return activity
    raise HTTPException(status_code=404, detail="Activity not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
