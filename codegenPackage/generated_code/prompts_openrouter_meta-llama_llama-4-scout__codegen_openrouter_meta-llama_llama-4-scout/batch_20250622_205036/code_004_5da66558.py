"""
Generated Code Metadata:
========================
Original URL: https://worldiscoveryperu.com
Prompt: "Design an API for a travel booking system that integrates information about various Peruvian destinations, such as Lima, Cusco, and Puerto Maldonado, and offers recommendations for accommodations and activities."
Generated: DETERMINISTIC_5da665583f22f3fe
Batch ID: 20250622_205036
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
    title="Peruvian Destinations Travel Booking API",
    description="API for booking travel to Peruvian destinations",
    version="1.0.0"
)

# Define a model for Destination
class Destination(BaseModel):
    id: int
    name: str
    description: str

# Define a model for Accommodation
class Accommodation(BaseModel):
    id: int
    name: str
    destination_id: int
    price: float

# Define a model for Activity
class Activity(BaseModel):
    id: int
    name: str
    destination_id: int
    price: float

# In-memory data store for destinations, accommodations, and activities
destinations = [
    Destination(id=1, name="Lima", description="Capital city of Peru"),
    Destination(id=2, name="Cusco", description="City in southeastern Peru"),
    Destination(id=3, name="Puerto Maldonado", description="City in southeastern Peru")
]

accommodations = [
    Accommodation(id=1, name="Hotel Lima", destination_id=1, price=100.0),
    Accommodation(id=2, name="Hotel Cusco", destination_id=2, price=80.0),
    Accommodation(id=3, name="Hotel Puerto Maldonado", destination_id=3, price=60.0)
]

activities = [
    Activity(id=1, name="Visit Machu Picchu", destination_id=2, price=50.0),
    Activity(id=2, name="Explore Lima's historic center", destination_id=1, price=20.0),
    Activity(id=3, name="Amazon rainforest tour", destination_id=3, price=80.0)
]

# API endpoint to get all destinations
@app.get("/destinations/", response_model=List[Destination])
def get_destinations():
    return destinations

# API endpoint to get a destination by ID
@app.get("/destinations/{destination_id}", response_model=Destination)
def get_destination(destination_id: int):
    for destination in destinations:
        if destination.id == destination_id:
            return destination
    raise HTTPException(status_code=404, detail="Destination not found")

# API endpoint to get accommodations for a destination
@app.get("/destinations/{destination_id}/accommodations/", response_model=List[Accommodation])
def get_accommodations(destination_id: int):
    return [accommodation for accommodation in accommodations if accommodation.destination_id == destination_id]

# API endpoint to get activities for a destination
@app.get("/destinations/{destination_id}/activities/", response_model=List[Activity])
def get_activities(destination_id: int):
    return [activity for activity in activities if activity.destination_id == destination_id]

# API endpoint to book a travel package (accommodation and activity)
class TravelPackage(BaseModel):
    destination_id: int
    accommodation_id: int
    activity_id: int

@app.post("/book-travel-package/")
def book_travel_package(travel_package: TravelPackage):
    destination = next((d for d in destinations if d.id == travel_package.destination_id), None)
    accommodation = next((a for a in accommodations if a.id == travel_package.accommodation_id), None)
    activity = next((a for a in activities if a.id == travel_package.activity_id), None)

    if not all([destination, accommodation, activity]):
        raise HTTPException(status_code=400, detail="Invalid travel package")

    if accommodation.destination_id != destination.id or activity.destination_id != destination.id:
        raise HTTPException(status_code=400, detail="Invalid travel package")

    # Here you would implement the actual booking logic (e.g., save to database, send confirmation email)
    return {"message": "Travel package booked successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
