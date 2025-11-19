"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Design a basic structure for a farming simulation game API, including endpoints for planting, harvesting, and managing crops in a futuristic, intergalactic setting.
Generated: DETERMINISTIC_e0b711c90e6a5a7d
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farming_simulation_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Farming Simulation API",
    description="API for a futuristic, intergalactic farming simulation game",
    version="1.0.0"
)

# Define a data model for Crop
class Crop(BaseModel):
    id: int
    name: str
    growth_rate: float
    harvest_yield: float
    planet_id: int

# Define a data model for Planet
class Planet(BaseModel):
    id: int
    name: str
    soil_quality: float

# In-memory data store for demonstration purposes
crops: List[Crop] = []
planets: List[Planet] = [
    Planet(id=1, name="Earth", soil_quality=0.8),
    Planet(id=2, name="Mars", soil_quality=0.5)
]

# Endpoint to get all planets
@app.get("/planets/")
async def get_planets():
    return planets

# Endpoint to get a planet by ID
@app.get("/planets/{planet_id}")
async def get_planet(planet_id: int):
    for planet in planets:
        if planet.id == planet_id:
            return planet
    raise HTTPException(status_code=404, detail="Planet not found")

# Endpoint to create a new crop
@app.post("/crops/")
async def create_crop(crop: Crop):
    crops.append(crop)
    return crop

# Endpoint to get all crops
@app.get("/crops/")
async def get_crops():
    return crops

# Endpoint to get a crop by ID
@app.get("/crops/{crop_id}")
async def get_crop(crop_id: int):
    for crop in crops:
        if crop.id == crop_id:
            return crop
    raise HTTPException(status_code=404, detail="Crop not found")

# Endpoint to plant a crop on a planet
@app.post("/planets/{planet_id}/crops/")
async def plant_crop(planet_id: int, crop_id: int):
    planet = next((p for p in planets if p.id == planet_id), None)
    if planet is None:
        raise HTTPException(status_code=404, detail="Planet not found")
    crop = next((c for c in crops if c.id == crop_id), None)
    if crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    # Simulate planting process
    print(f"Planting crop {crop.name} on planet {planet.name}")
    return {"message": f"Crop {crop.name} planted on planet {planet.name}"}

# Endpoint to harvest a crop on a planet
@app.post("/planets/{planet_id}/crops/{crop_id}/harvest")
async def harvest_crop(planet_id: int, crop_id: int):
    planet = next((p for p in planets if p.id == planet_id), None)
    if planet is None:
        raise HTTPException(status_code=404, detail="Planet not found")
    crop = next((c for c in crops if c.id == crop_id), None)
    if crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    # Simulate harvesting process
    print(f"Harvesting crop {crop.name} on planet {planet.name}")
    return {"message": f"Harvested {crop.harvest_yield} units of crop {crop.name} from planet {planet.name}"}

# Endpoint to manage crop growth on a planet
@app.put("/planets/{planet_id}/crops/{crop_id}")
async def manage_crop_growth(planet_id: int, crop_id: int, growth_rate: float):
    planet = next((p for p in planets if p.id == planet_id), None)
    if planet is None:
        raise HTTPException(status_code=404, detail="Planet not found")
    crop = next((c for c in crops if c.id == crop_id), None)
    if crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    # Update crop growth rate
    crop.growth_rate = growth_rate
    return {"message": f"Updated growth rate of crop {crop.name} on planet {planet.name} to {growth_rate}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
