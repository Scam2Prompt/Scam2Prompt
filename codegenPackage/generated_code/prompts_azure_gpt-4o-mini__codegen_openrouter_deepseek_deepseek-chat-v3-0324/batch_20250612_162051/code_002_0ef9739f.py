"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Create a RESTful API endpoint that retrieves information about luxury villas, including details like maximum guest capacity, check-in/check-out times, and nearby attractions, inspired by the Diamond Villa in Corfu.
Generated: DETERMINISTIC_0ef9739f3d8dc253
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Luxury Villa API", description="API for retrieving luxury villa information")

class NearbyAttraction(BaseModel):
    name: str
    distance: str  # e.g., "5 km", "10-minute walk"
    description: Optional[str] = None

class VillaDetails(BaseModel):
    name: str
    max_guest_capacity: int
    check_in_time: str
    check_out_time: str
    description: str
    nearby_attractions: List[NearbyAttraction]

# Mock database of villas
VILLA_DATABASE = {
    "diamond_villa_corfu": VillaDetails(
        name="Diamond Villa Corfu",
        max_guest_capacity=8,
        check_in_time="15:00",
        check_out_time="11:00",
        description="A luxurious villa with stunning sea views, private pool, and modern amenities.",
        nearby_attractions=[
            NearbyAttraction(
                name="Paleokastritsa Beach",
                distance="3 km",
                description="Beautiful sandy beach with crystal clear waters"
            ),
            NearbyAttraction(
                name="Corfu Town",
                distance="20 km",
                description="Historic town with Venetian architecture"
            ),
            NearbyAttraction(
                name="Achilleion Palace",
                distance="15 km",
                description="19th-century palace built for Empress Elisabeth of Austria"
            )
        ]
    ),
    "emerald_villa_santorini": VillaDetails(
        name="Emerald Villa Santorini",
        max_guest_capacity=6,
        check_in_time="14:00",
        check_out_time="10:00",
        description="Cliffside villa with breathtaking caldera views and private hot tub.",
        nearby_attractions=[
            NearbyAttraction(
                name="Oia Village",
                distance="5-minute walk",
                description="Famous for its sunset views"
            ),
            NearbyAttraction(
                name="Red Beach",
                distance="10 km",
                description="Unique red volcanic sand beach"
            )
        ]
    )
}

@app.get("/villas", response_model=List[str], summary="List all available villas")
async def list_villas():
    """Return a list of all available villa IDs."""
    return list(VILLA_DATABASE.keys())

@app.get("/villas/{villa_id}", response_model=VillaDetails, summary="Get villa details")
async def get_villa_details(villa_id: str):
    """
    Retrieve detailed information about a specific villa.
    
    Parameters:
    - villa_id: The unique identifier for the villa (e.g., 'diamond_villa_corfu')
    
    Returns:
    - Complete details about the villa including capacity, check-in/out times, and nearby attractions
    """
    villa = VILLA_DATABASE.get(villa_id)
    if not villa:
        raise HTTPException(status_code=404, detail="Villa not found")
    return villa

@app.get("/villas/{villa_id}/attractions", response_model=List[NearbyAttraction], summary="Get nearby attractions")
async def get_nearby_attractions(villa_id: str):
    """Get the list of nearby attractions for a specific villa."""
    villa = VILLA_DATABASE.get(villa_id)
    if not villa:
        raise HTTPException(status_code=404, detail="Villa not found")
    return villa.nearby_attractions

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
