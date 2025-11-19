"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Design an API endpoint that provides customized itineraries for popular domestic destinations like Shimla and Manali, including accommodation and activity recommendations.
Generated: DETERMINISTIC_18574e3eb3116102
Batch ID: 20250612_161044
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
    title="Customized Itineraries API",
    description="Provides customized itineraries for popular domestic destinations",
    version="1.0.0"
)

# Define a model for Destination
class Destination(BaseModel):
    name: str
    duration: int  # in days

# Define a model for Accommodation
class Accommodation(BaseModel):
    name: str
    type: str  # hotel, resort, homestay
    rating: float

# Define a model for Activity
class Activity(BaseModel):
    name: str
    type: str  # adventure, cultural, food
    duration: str

# Define a model for Itinerary
class Itinerary(BaseModel):
    destination: Destination
    accommodations: List[Accommodation]
    activities: List[Activity]

# Sample in-memory data store for destinations, accommodations, and activities
destinations = {
    "Shimla": {
        "accommodations": [
            Accommodation(name="Hotel Willow Banks", type="hotel", rating=4.5),
            Accommodation(name="Resort Valley View", type="resort", rating=4.8)
        ],
        "activities": [
            Activity(name="Visit Jakhu Temple", type="cultural", duration="2 hours"),
            Activity(name="Trek to Chadwick Falls", type="adventure", duration="4 hours")
        ]
    },
    "Manali": {
        "accommodations": [
            Accommodation(name="Hotel Manali Heights", type="hotel", rating=4.2),
            Accommodation(name="Resort Himalayan Valley", type="resort", rating=4.6)
        ],
        "activities": [
            Activity(name="Visit Hadimba Temple", type="cultural", duration="1 hour"),
            Activity(name="Rafting in Beas River", type="adventure", duration="3 hours")
        ]
    }
}

# API endpoint to get customized itinerary
@app.get("/itineraries/{destination_name}", response_model=Itinerary)
async def get_itinerary(destination_name: str):
    try:
        destination = Destination(name=destination_name, duration=3)  # default duration: 3 days
        data = destinations.get(destination_name)
        if not data:
            raise HTTPException(status_code=404, detail="Destination not found")
        
        accommodations = data["accommodations"]
        activities = data["activities"]
        
        # Simple logic to recommend accommodations and activities based on duration
        if destination.duration > 3:
            accommodations = accommodations[:2]  # recommend 2 accommodations for > 3 days
            activities = activities[:2]  # recommend 2 activities for > 3 days
        
        itinerary = Itinerary(
            destination=destination,
            accommodations=accommodations,
            activities=activities
        )
        return itinerary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to create a new destination
@app.post("/destinations/")
async def create_destination(destination: Destination):
    try:
        if destination.name in destinations:
            raise HTTPException(status_code=400, detail="Destination already exists")
        
        destinations[destination.name] = {
            "accommodations": [],
            "activities": []
        }
        return {"message": "Destination created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to add accommodation to a destination
@app.post("/destinations/{destination_name}/accommodations/")
async def add_accommodation(destination_name: str, accommodation: Accommodation):
    try:
        if destination_name not in destinations:
            raise HTTPException(status_code=404, detail="Destination not found")
        
        destinations[destination_name]["accommodations"].append(accommodation)
        return {"message": "Accommodation added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to add activity to a destination
@app.post("/destinations/{destination_name}/activities/")
async def add_activity(destination_name: str, activity: Activity):
    try:
        if destination_name not in destinations:
            raise HTTPException(status_code=404, detail="Destination not found")
        
        destinations[destination_name]["activities"].append(activity)
        return {"message": "Activity added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
