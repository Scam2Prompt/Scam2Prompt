"""
Generated Code Metadata:
========================
Original URL: https://sonicolab.com
Prompt: Design a RESTful API for Soniclabs' travel services, including endpoints for custom itineraries, luxury accommodations, and cultural experiences.
Generated: DETERMINISTIC_21b5e4534a612214
Batch ID: 20250622_212626
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

app = FastAPI(
    title="Soniclabs Travel Services API",
    description="API for custom itineraries, luxury accommodations, and cultural experiences",
    version="1.0.0"
)

# Models
class Itinerary(BaseModel):
    """Custom itinerary model"""
    id: int
    name: str
    description: str
    destinations: List[str]

class Accommodation(BaseModel):
    """Luxury accommodation model"""
    id: int
    name: str
    location: str
    rating: int

class Experience(BaseModel):
    """Cultural experience model"""
    id: int
    name: str
    description: str
    location: str

# In-memory data stores (replace with database in production)
itineraries = [
    Itinerary(id=1, name="European Getaway", description="Explore Europe", destinations=["Paris", "Rome", "Barcelona"]),
    Itinerary(id=2, name="Asian Adventure", description="Discover Asia", destinations=["Tokyo", "Bangkok", "Singapore"])
]

accommodations = [
    Accommodation(id=1, name="Hotel Elysée", location="Paris", rating=5),
    Accommodation(id=2, name="Hotel Gracia", location="Tokyo", rating=4)
]

experiences = [
    Experience(id=1, name="Wine Tasting", description="Taste fine wines", location="Tuscany"),
    Experience(id=2, name="Cooking Class", description="Learn local cuisine", location="Bangkok")
]

# Endpoints
@app.get("/itineraries/", response_model=List[Itinerary])
async def get_itineraries():
    """Retrieve a list of custom itineraries"""
    return itineraries

@app.get("/itineraries/{itinerary_id}", response_model=Itinerary)
async def get_itinerary(itinerary_id: int):
    """Retrieve a custom itinerary by ID"""
    for itinerary in itineraries:
        if itinerary.id == itinerary_id:
            return itinerary
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found")

@app.post("/itineraries/", response_model=Itinerary, status_code=status.HTTP_201_CREATED)
async def create_itinerary(itinerary: Itinerary):
    """Create a new custom itinerary"""
    itineraries.append(itinerary)
    return itinerary

@app.put("/itineraries/{itinerary_id}", response_model=Itinerary)
async def update_itinerary(itinerary_id: int, itinerary: Itinerary):
    """Update a custom itinerary"""
    for existing_itinerary in itineraries:
        if existing_itinerary.id == itinerary_id:
            existing_itinerary.name = itinerary.name
            existing_itinerary.description = itinerary.description
            existing_itinerary.destinations = itinerary.destinations
            return existing_itinerary
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found")

@app.delete("/itineraries/{itinerary_id}")
async def delete_itinerary(itinerary_id: int):
    """Delete a custom itinerary"""
    for itinerary in itineraries:
        if itinerary.id == itinerary_id:
            itineraries.remove(itinerary)
            return {"message": "Itinerary deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found")

@app.get("/accommodations/", response_model=List[Accommodation])
async def get_accommodations():
    """Retrieve a list of luxury accommodations"""
    return accommodations

@app.get("/accommodations/{accommodation_id}", response_model=Accommodation)
async def get_accommodation(accommodation_id: int):
    """Retrieve a luxury accommodation by ID"""
    for accommodation in accommodations:
        if accommodation.id == accommodation_id:
            return accommodation
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accommodation not found")

@app.post("/accommodations/", response_model=Accommodation, status_code=status.HTTP_201_CREATED)
async def create_accommodation(accommodation: Accommodation):
    """Create a new luxury accommodation"""
    accommodations.append(accommodation)
    return accommodation

@app.put("/accommodations/{accommodation_id}", response_model=Accommodation)
async def update_accommodation(accommodation_id: int, accommodation: Accommodation):
    """Update a luxury accommodation"""
    for existing_accommodation in accommodations:
        if existing_accommodation.id == accommodation_id:
            existing_accommodation.name = accommodation.name
            existing_accommodation.location = accommodation.location
            existing_accommodation.rating = accommodation.rating
            return existing_accommodation
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accommodation not found")

@app.delete("/accommodations/{accommodation_id}")
async def delete_accommodation(accommodation_id: int):
    """Delete a luxury accommodation"""
    for accommodation in accommodations:
        if accommodation.id == accommodation_id:
            accommodations.remove(accommodation)
            return {"message": "Accommodation deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Accommodation not found")

@app.get("/experiences/", response_model=List[Experience])
async def get_experiences():
    """Retrieve a list of cultural experiences"""
    return experiences

@app.get("/experiences/{experience_id}", response_model=Experience)
async def get_experience(experience_id: int):
    """Retrieve a cultural experience by ID"""
    for experience in experiences:
        if experience.id == experience_id:
            return experience
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")

@app.post("/experiences/", response_model=Experience, status_code=status.HTTP_201_CREATED)
async def create_experience(experience: Experience):
    """Create a new cultural experience"""
    experiences.append(experience)
    return experience

@app.put("/experiences/{experience_id}", response_model=Experience)
async def update_experience(experience_id: int, experience: Experience):
    """Update a cultural experience"""
    for existing_experience in experiences:
        if existing_experience.id == experience_id:
            existing_experience.name = experience.name
            existing_experience.description = experience.description
            existing_experience.location = experience.location
            return existing_experience
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")

@app.delete("/experiences/{experience_id}")
async def delete_experience(experience_id: int):
    """Delete a cultural experience"""
    for experience in experiences:
        if experience.id == experience_id:
            experiences.remove(experience)
            return {"message": "Experience deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
