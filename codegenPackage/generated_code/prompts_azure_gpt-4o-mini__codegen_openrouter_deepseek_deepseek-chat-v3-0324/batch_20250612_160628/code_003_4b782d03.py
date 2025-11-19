"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: How can I create an API to manage the specifications and pricing of different types of lifts, such as passenger and freight elevators?
Generated: DETERMINISTIC_4b782d0340f1c4af
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import uuid
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title="Elevator Management API",
    description="API for managing specifications and pricing of different types of lifts",
    version="1.0.0"
)

# Database simulation
db = {}

# Enums and Models
class LiftType(str, Enum):
    PASSENGER = "passenger"
    FREIGHT = "freight"

class LiftSpecs(BaseModel):
    max_capacity_kg: float = Field(..., gt=0, description="Maximum weight capacity in kilograms")
    max_speed_mps: float = Field(..., gt=0, description="Maximum speed in meters per second")
    floors_served: int = Field(..., gt=0, description="Number of floors served")
    motor_power_kw: float = Field(..., gt=0, description="Motor power in kilowatts")

class Pricing(BaseModel):
    base_price: float = Field(..., gt=0, description="Base price in USD")
    installation_cost: float = Field(..., gt=0, description="Installation cost in USD")
    maintenance_cost_per_month: float = Field(..., gt=0, description="Monthly maintenance cost in USD")

class Lift(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier")
    name: str = Field(..., min_length=2, max_length=50, description="Name of the lift model")
    type: LiftType = Field(..., description="Type of lift")
    manufacturer: str = Field(..., min_length=2, max_length=50, description="Manufacturer name")
    specs: LiftSpecs = Field(..., description="Technical specifications")
    pricing: Pricing = Field(..., description="Pricing information")
    description: Optional[str] = Field(None, max_length=500, description="Optional description")

# API Endpoints
@app.post("/lifts/", response_model=Lift, status_code=status.HTTP_201_CREATED)
async def create_lift(lift: Lift):
    """Create a new lift entry"""
    if lift.id in db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Lift with this ID already exists"
        )
    db[lift.id] = jsonable_encoder(lift)
    return lift

@app.get("/lifts/", response_model=List[Lift])
async def list_lifts(type: Optional[LiftType] = None):
    """List all lifts, optionally filtered by type"""
    lifts = list(db.values())
    if type:
        lifts = [lift for lift in lifts if lift["type"] == type]
    return lifts

@app.get("/lifts/{lift_id}", response_model=Lift)
async def get_lift(lift_id: str):
    """Get a specific lift by ID"""
    if lift_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lift not found"
        )
    return db[lift_id]

@app.put("/lifts/{lift_id}", response_model=Lift)
async def update_lift(lift_id: str, lift: Lift):
    """Update an existing lift"""
    if lift_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lift not found"
        )
    if lift.id != lift_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID in payload does not match URL ID"
        )
    db[lift_id] = jsonable_encoder(lift)
    return lift

@app.delete("/lifts/{lift_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lift(lift_id: str):
    """Delete a lift"""
    if lift_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lift not found"
        )
    del db[lift_id]
    return None

@app.get("/lifts/{lift_id}/total-cost", response_model=dict)
async def calculate_total_cost(lift_id: str, years: int = Field(5, gt=0)):
    """Calculate total cost of ownership for a given number of years"""
    if lift_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lift not found"
        )
    lift = db[lift_id]
    total_cost = (
        lift["pricing"]["base_price"] +
        lift["pricing"]["installation_cost"] +
        (lift["pricing"]["maintenance_cost_per_month"] * 12 * years)
    )
    return {
        "lift_id": lift_id,
        "years": years,
        "total_cost": round(total_cost, 2),
        "currency": "USD"
    }
```
