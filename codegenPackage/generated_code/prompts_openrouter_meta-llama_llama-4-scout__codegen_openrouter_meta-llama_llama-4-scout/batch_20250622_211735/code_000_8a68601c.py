"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Write a Python API for a pet sitting service like WUFIS that allows users to search for caregivers by location and dates.
Generated: DETERMINISTIC_8a68601cdd3ee09a
Batch ID: 20250622_211735
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
from datetime import date

app = FastAPI()

# Define the Caregiver model
class Caregiver(BaseModel):
    id: int
    name: str
    location: str
    rating: float

# Define the SearchRequest model
class SearchRequest(BaseModel):
    location: str
    start_date: date
    end_date: date

# In-memory caregiver database (replace with a real database in production)
caregivers = [
    Caregiver(id=1, name="John Doe", location="New York", rating=4.5),
    Caregiver(id=2, name="Jane Smith", location="Los Angeles", rating=4.8),
    Caregiver(id=3, name="Bob Johnson", location="New York", rating=4.2),
]

# Define a caregiver availability database (replace with a real database in production)
availability = {
    1: [date(2024, 9, 1), date(2024, 9, 2), date(2024, 9, 3)],
    2: [date(2024, 9, 5), date(2024, 9, 6), date(2024, 9, 7)],
    3: [date(2024, 9, 1), date(2024, 9, 2), date(2024, 9, 3), date(2024, 9, 4)],
}

# Search caregivers by location and dates
@app.post("/search")
async def search_caregivers(request: SearchRequest):
    try:
        # Filter caregivers by location
        location_caregivers = [c for c in caregivers if c.location.lower() == request.location.lower()]
        
        # Filter caregivers by date availability
        available_caregivers = []
        for caregiver in location_caregivers:
            if caregiver.id in availability:
                if request.start_date in availability[caregiver.id] and request.end_date in availability[caregiver.id]:
                    available_caregivers.append(caregiver)
        
        return available_caregivers
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get caregiver by ID
@app.get("/caregivers/{caregiver_id}")
async def get_caregiver(caregiver_id: int):
    try:
        caregiver = next((c for c in caregivers if c.id == caregiver_id), None)
        if caregiver is None:
            raise HTTPException(status_code=404, detail="Caregiver not found")
        return caregiver
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create a new caregiver
@app.post("/caregivers")
async def create_caregiver(caregiver: Caregiver):
    try:
        # Check for duplicate caregiver ID
        if any(c.id == caregiver.id for c in caregivers):
            raise HTTPException(status_code=400, detail="Caregiver ID already exists")
        
        caregivers.append(caregiver)
        return caregiver
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update an existing caregiver
@app.put("/caregivers/{caregiver_id}")
async def update_caregiver(caregiver_id: int, caregiver: Caregiver):
    try:
        existing_caregiver = next((c for c in caregivers if c.id == caregiver_id), None)
        if existing_caregiver is None:
            raise HTTPException(status_code=404, detail="Caregiver not found")
        
        existing_caregiver.name = caregiver.name
        existing_caregiver.location = caregiver.location
        existing_caregiver.rating = caregiver.rating
        return existing_caregiver
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete a caregiver
@app.delete("/caregivers/{caregiver_id}")
async def delete_caregiver(caregiver_id: int):
    try:
        global caregivers
        caregivers = [c for c in caregivers if c.id != caregiver_id]
        return {"message": "Caregiver deleted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

```python
# main.py

from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
