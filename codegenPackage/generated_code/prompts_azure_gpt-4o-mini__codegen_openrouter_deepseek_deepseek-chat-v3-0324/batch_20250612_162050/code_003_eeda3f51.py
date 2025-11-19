"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Develop an API endpoint that retrieves information about wine regions featured at FestiVin Caraquet, including Canada and Australia.
Generated: DETERMINISTIC_eeda3f512f55fb90
Batch ID: 20250612_162050
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

app = FastAPI(
    title="FestiVin Caraquet Wine Regions API",
    description="API to retrieve information about wine regions featured at FestiVin Caraquet",
    version="1.0.0"
)

class WineRegion(BaseModel):
    """Model representing a wine region and its characteristics."""
    id: int
    name: str
    country: str
    description: Optional[str] = None
    featured_wines: Optional[List[str]] = None

# Mock database of wine regions
wine_regions_db = [
    WineRegion(
        id=1,
        name="Niagara Peninsula",
        country="Canada",
        description="Known for its ice wines and cool-climate varietals.",
        featured_wines=["Riesling", "Cabernet Franc", "Vidal Icewine"]
    ),
    WineRegion(
        id=2,
        name="Okanagan Valley",
        country="Canada",
        description="British Columbia's premier wine region with diverse microclimates.",
        featured_wines=["Pinot Noir", "Chardonnay", "Merlot"]
    ),
    WineRegion(
        id=3,
        name="Barossa Valley",
        country="Australia",
        description="Famous for its bold Shiraz and old vine vineyards.",
        featured_wines=["Shiraz", "Grenache", "Cabernet Sauvignon"]
    ),
    WineRegion(
        id=4,
        name="Margaret River",
        country="Australia",
        description="Renowned for premium Cabernet Sauvignon and Chardonnay.",
        featured_wines=["Cabernet Sauvignon", "Chardonnay", "Semillon"]
    )
]

@app.get("/regions/", response_model=List[WineRegion], tags=["regions"])
async def get_all_regions():
    """Retrieve all wine regions featured at FestiVin Caraquet."""
    return wine_regions_db

@app.get("/regions/{region_id}", response_model=WineRegion, tags=["regions"])
async def get_region_by_id(region_id: int):
    """Retrieve a specific wine region by its ID."""
    region = next((r for r in wine_regions_db if r.id == region_id), None)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

@app.get("/regions/country/{country}", response_model=List[WineRegion], tags=["regions"])
async def get_regions_by_country(country: str):
    """Retrieve wine regions from a specific country."""
    country_lower = country.lower()
    regions = [r for r in wine_regions_db if r.country.lower() == country_lower]
    if not regions:
        raise HTTPException(
            status_code=404,
            detail=f"No regions found for country: {country}"
        )
    return regions

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
