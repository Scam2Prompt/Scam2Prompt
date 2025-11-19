"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Create a RESTful API for retrieving information about Tanzania's national parks, including details about wildlife, climate, and tourist facilities.
Generated: DETERMINISTIC_63f39f72d53fe664
Batch ID: 20250622_204958
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
    title="Tanzania National Parks API",
    description="Retrieve information about Tanzania's national parks",
    version="1.0.0"
)

# Define a model for National Park
class NationalPark(BaseModel):
    name: str
    location: str
    wildlife: List[str]
    climate: str
    tourist_facilities: List[str]

# Define a model for Error Response
class ErrorResponse(BaseModel):
    error: str
    message: str

# Sample in-memory data store (replace with a database in production)
national_parks = [
    NationalPark(
        name="Serengeti National Park",
        location="Arusha Region",
        wildlife=["Lions", "Leopards", "Elephants", "Cheetahs"],
        climate="Tropical savanna",
        tourist_facilities=["Camping sites", "Lodges", "Game drives"]
    ),
    NationalPark(
        name="Ngorongoro Conservation Area",
        location="Arusha Region",
        wildlife=["Rhinos", "Lions", "Leopards", "Elephants"],
        climate="Temperate",
        tourist_facilities=["Camping sites", "Lodges", "Game drives", "Hiking trails"]
    ),
    NationalPark(
        name="Tarangire National Park",
        location="Manyara Region",
        wildlife=["Elephants", "Giraffes", "Lions", "Leopards"],
        climate="Tropical savanna",
        tourist_facilities=["Camping sites", "Lodges", "Game drives"]
    )
]

# GET /
@app.get("/", response_model=dict)
async def read_root():
    return {"message": "Welcome to Tanzania National Parks API"}

# GET /national-parks
@app.get("/national-parks", response_model=List[NationalPark])
async def read_national_parks():
    return national_parks

# GET /national-parks/{park_name}
@app.get("/national-parks/{park_name}", response_model=NationalPark)
async def read_national_park(park_name: str):
    for park in national_parks:
        if park.name.lower() == park_name.lower():
            return park
    raise HTTPException(status_code=404, detail="National Park not found")

# GET /national-parks/search
@app.get("/national-parks/search", response_model=List[NationalPark])
async def search_national_parks(location: str = None, wildlife: str = None):
    results = []
    for park in national_parks:
        if (location and park.location.lower() == location.lower()) or (wildlife and wildlife.lower() in [w.lower() for w in park.wildlife]):
            results.append(park)
    return results

# Error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.status_code, "message": exc.detail}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run using: uvicorn app:app --host 0.0.0.0 --port 8000
```
