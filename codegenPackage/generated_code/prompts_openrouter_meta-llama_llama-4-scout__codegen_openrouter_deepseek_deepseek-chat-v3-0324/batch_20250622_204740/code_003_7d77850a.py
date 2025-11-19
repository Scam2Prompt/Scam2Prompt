"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Design an API for managing virtual land plots with varying acreage and capabilities in a game, and provide example use cases for multiplying land capabilities with Farmers.
Generated: DETERMINISTIC_7d77850a391233b3
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Virtual Land Management API for Game Environments
"""

from typing import List, Dict, Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title="Virtual Land Management API",
    description="API for managing virtual land plots in a game environment",
    version="1.0.0"
)

class LandCapability(str, Enum):
    FARMING = "farming"
    MINING = "mining"
    FORESTRY = "forestry"
    HABITATION = "habitation"

class LandPlot(BaseModel):
    id: str = Field(..., description="Unique identifier for the land plot")
    name: str = Field(..., description="Name of the land plot")
    acreage: float = Field(..., gt=0, description="Size of the land plot in acres")
    capabilities: List[LandCapability] = Field(..., description="List of capabilities this land has")
    farmer_multipliers: Dict[LandCapability, float] = Field(
        default_factory=dict,
        description="Multipliers applied to capabilities when farmed by farmers"
    )
    
    @validator('farmer_multipliers')
    def validate_multipliers(cls, v, values):
        for capability in values.get('capabilities', []):
            if capability not in v:
                v[capability] = 1.0  # Default multiplier if not specified
        return v

class Farmer(BaseModel):
    id: str = Field(..., description="Unique identifier for the farmer")
    name: str = Field(..., description="Name of the farmer")
    skill_level: int = Field(1, ge=1, le=10, description="Skill level from 1 to 10")
    specialization: LandCapability = Field(..., description="Farmer's specialized capability")

# In-memory database
land_plots_db: Dict[str, LandPlot] = {}
farmers_db: Dict[str, Farmer] = {}

@app.post("/land/", response_model=LandPlot, status_code=status.HTTP_201_CREATED)
def create_land_plot(land_plot: LandPlot):
    """Create a new land plot"""
    if land_plot.id in land_plots_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Land plot with this ID already exists"
        )
    land_plots_db[land_plot.id] = land_plot
    return land_plot

@app.get("/land/{land_id}", response_model=LandPlot)
def get_land_plot(land_id: str):
    """Retrieve a land plot by ID"""
    if land_id not in land_plots_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Land plot not found"
        )
    return land_plots_db[land_id]

@app.post("/farmers/", response_model=Farmer, status_code=status.HTTP_201_CREATED)
def create_farmer(farmer: Farmer):
    """Create a new farmer"""
    if farmer.id in farmers_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Farmer with this ID already exists"
        )
    farmers_db[farmer.id] = farmer
    return farmer

@app.get("/farmers/{farmer_id}", response_model=Farmer)
def get_farmer(farmer_id: str):
    """Retrieve a farmer by ID"""
    if farmer_id not in farmers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farmer not found"
        )
    return farmers_db[farmer_id]

@app.post("/land/{land_id}/farm/{farmer_id}", response_model=LandPlot)
def farm_land(land_id: str, farmer_id: str):
    """
    Apply farmer's multipliers to land capabilities
    Returns the modified land plot with enhanced capabilities
    """
    if land_id not in land_plots_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Land plot not found"
        )
    if farmer_id not in farmers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farmer not found"
        )
    
    land_plot = land_plots_db[land_id]
    farmer = farmers_db[farmer_id]
    
    # Apply farmer's skill level as a multiplier to their specialized capability
    if farmer.specialization in land_plot.capabilities:
        multiplier = 1 + (farmer.skill_level * 0.1)  # Each skill level adds 10%
        land_plot.farmer_multipliers[farmer.specialization] = multiplier
    
    return land_plot

@app.get("/land/{land_id}/production")
def calculate_production(land_id: str):
    """
    Calculate production output based on land capabilities and farmer multipliers
    """
    if land_id not in land_plots_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Land plot not found"
        )
    
    land_plot = land_plots_db[land_id]
    production = {}
    
    for capability in land_plot.capabilities:
        base_output = land_plot.acreage * 10  # Base output per acre
        multiplier = land_plot.farmer_multipliers.get(capability, 1.0)
        production[capability.value] = base_output * multiplier
    
    return production

# Example use cases
if __name__ == "__main__":
    import uvicorn
    
    # Create example land plot
    wheat_field = LandPlot(
        id="field1",
        name="Wheat Field",
        acreage=50.0,
        capabilities=[LandCapability.FARMING],
        farmer_multipliers={LandCapability.FARMING: 1.0}
    )
    
    # Create example farmer
    farmer_john = Farmer(
        id="farmer1",
        name="John the Farmer",
        skill_level=5,
        specialization=LandCapability.FARMING
    )
    
    # Demonstrate farming effect
    print("Before farming:", wheat_field.farmer_multipliers)
    farm_land(wheat_field.id, farmer_john.id)
    print("After farming:", wheat_field.farmer_multipliers)
    
    # Calculate production
    production = calculate_production(wheat_field.id)
    print("Production output:", production)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
