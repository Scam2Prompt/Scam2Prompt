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
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime, timedelta

app = FastAPI(
    title="Intergalactic Farming Simulator API",
    description="API for managing futuristic farming operations across galaxies",
    version="0.1.0"
)

# Database simulation
class CropDB:
    def __init__(self):
        self.crops = []
        self.fields = []

db = CropDB()

# Models
class Crop(BaseModel):
    id: UUID
    name: str
    species: str
    planet_of_origin: str
    growth_time_hours: int
    value_per_unit: float
    is_harvestable: bool = False
    planted_at: Optional[datetime] = None
    harvested_at: Optional[datetime] = None

class Field(BaseModel):
    id: UUID
    name: str
    planet_location: str
    capacity: int
    current_crops: List[UUID] = []

class PlantRequest(BaseModel):
    field_id: UUID
    crop_species: str
    quantity: int

class HarvestRequest(BaseModel):
    field_id: UUID
    crop_id: UUID

# Helper functions
def find_crop(crop_id: UUID) -> Optional[Crop]:
    for crop in db.crops:
        if crop.id == crop_id:
            return crop
    return None

def find_field(field_id: UUID) -> Optional[Field]:
    for field in db.fields:
        if field.id == field_id:
            return field
    return None

# Endpoints
@app.post("/crops/", status_code=status.HTTP_201_CREATED, response_model=Crop)
def create_crop(
    name: str,
    species: str,
    planet_of_origin: str,
    growth_time_hours: int,
    value_per_unit: float
):
    """
    Register a new crop species in the galactic database.
    """
    crop = Crop(
        id=uuid4(),
        name=name,
        species=species,
        planet_of_origin=planet_of_origin,
        growth_time_hours=growth_time_hours,
        value_per_unit=value_per_unit
    )
    db.crops.append(crop)
    return crop

@app.post("/fields/", status_code=status.HTTP_201_CREATED, response_model=Field)
def create_field(name: str, planet_location: str, capacity: int):
    """
    Create a new farming field on a planet.
    """
    field = Field(
        id=uuid4(),
        name=name,
        planet_location=planet_location,
        capacity=capacity
    )
    db.fields.append(field)
    return field

@app.post("/plant/", status_code=status.HTTP_201_CREATED)
def plant_crops(plant_request: PlantRequest):
    """
    Plant crops in a specified field.
    """
    field = find_field(plant_request.field_id)
    if not field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Field not found"
        )

    # Find crop species in database
    crop_species = None
    for crop in db.crops:
        if crop.species == plant_request.crop_species:
            crop_species = crop
            break

    if not crop_species:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Crop species not registered"
        )

    if len(field.current_crops) + plant_request.quantity > field.capacity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Field capacity exceeded"
        )

    # Create new crop instances
    planted_crops = []
    for _ in range(plant_request.quantity):
        new_crop = Crop(
            id=uuid4(),
            name=crop_species.name,
            species=crop_species.species,
            planet_of_origin=crop_species.planet_of_origin,
            growth_time_hours=crop_species.growth_time_hours,
            value_per_unit=crop_species.value_per_unit,
            planted_at=datetime.now()
        )
        db.crops.append(new_crop)
        field.current_crops.append(new_crop.id)
        planted_crops.append(new_crop)

    return {"planted_crops": planted_crops, "field": field}

@app.post("/harvest/", status_code=status.HTTP_200_OK)
def harvest_crop(harvest_request: HarvestRequest):
    """
    Harvest a mature crop from a field.
    """
    field = find_field(harvest_request.field_id)
    if not field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Field not found"
        )

    crop = find_crop(harvest_request.crop_id)
    if not crop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Crop not found"
        )

    if crop.id not in field.current_crops:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Crop is not in this field"
        )

    if crop.planted_at is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Crop was never planted"
        )

    # Check if crop is ready to harvest
    harvest_time = crop.planted_at + timedelta(hours=crop.growth_time_hours)
    if datetime.now() < harvest_time:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Crop is not ready for harvest"
        )

    crop.harvested_at = datetime.now()
    crop.is_harvestable = True
    field.current_crops.remove(crop.id)

    return {
        "message": "Crop harvested successfully",
        "harvested_crop": crop,
        "value_earned": crop.value_per_unit
    }

@app.get("/fields/{field_id}", response_model=Field)
def get_field(field_id: UUID):
    """
    Get details about a specific field.
    """
    field = find_field(field_id)
    if not field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Field not found"
        )
    return field

@app.get("/crops/", response_model=List[Crop])
def list_crops():
    """
    List all registered crop species.
    """
    return db.crops

@app.get("/fields/", response_model=List[Field])
def list_fields():
    """
    List all farming fields.
    """
    return db.fields
```
