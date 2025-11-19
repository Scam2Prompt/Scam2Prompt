"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Develop an API endpoint that provides details about the types of cookware available at Varejão das Louças, including options for restaurants and hotels.
Generated: DETERMINISTIC_34395a76dd3887cd
Batch ID: 20250612_160657
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
from enum import Enum

app = FastAPI(
    title="Varejão das Louças API",
    description="API for retrieving cookware details for restaurants and hotels",
    version="1.0.0"
)

class CookwareType(str, Enum):
    PAN = "pan"
    POT = "pot"
    BAKING_DISH = "baking_dish"
    UTENSIL = "utensil"
    PLATE = "plate"
    GLASS = "glass"
    CUTLERY = "cutlery"

class Material(str, Enum):
    STAINLESS_STEEL = "stainless_steel"
    ALUMINUM = "aluminum"
    CERAMIC = "ceramic"
    CAST_IRON = "cast_iron"
    GLASS = "glass"
    PLASTIC = "plastic"

class CookwareItem(BaseModel):
    id: int
    name: str
    type: CookwareType
    material: Material
    capacity_ml: Optional[int] = None
    diameter_cm: Optional[float] = None
    is_commercial_grade: bool
    suitable_for: List[str]  # e.g., ["restaurant", "hotel"]

# Mock database
cookware_db = [
    CookwareItem(
        id=1,
        name="Professional Chef's Pan",
        type=CookwareType.PAN,
        material=Material.STAINLESS_STEEL,
        diameter_cm=30.5,
        is_commercial_grade=True,
        suitable_for=["restaurant", "hotel"]
    ),
    CookwareItem(
        id=2,
        name="Large Stock Pot",
        type=CookwareType.POT,
        material=Material.ALUMINUM,
        capacity_ml=20000,
        is_commercial_grade=True,
        suitable_for=["restaurant", "hotel"]
    ),
    CookwareItem(
        id=3,
        name="Ceramic Baking Dish",
        type=CookwareType.BAKING_DISH,
        material=Material.CERAMIC,
        is_commercial_grade=False,
        suitable_for=["hotel"]
    ),
    CookwareItem(
        id=4,
        name="Commercial Grade Cutlery Set",
        type=CookwareType.CUTLERY,
        material=Material.STAINLESS_STEEL,
        is_commercial_grade=True,
        suitable_for=["restaurant", "hotel"]
    )
]

@app.get("/cookware", response_model=List[CookwareItem], tags=["Cookware"])
def get_all_cookware():
    """Get all available cookware items"""
    return cookware_db

@app.get("/cookware/{item_id}", response_model=CookwareItem, tags=["Cookware"])
def get_cookware_item(item_id: int):
    """Get a specific cookware item by ID"""
    item = next((item for item in cookware_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Cookware item not found")
    return item

@app.get("/cookware/type/{type}", response_model=List[CookwareItem], tags=["Cookware"])
def get_cookware_by_type(type: CookwareType):
    """Get cookware items by type"""
    return [item for item in cookware_db if item.type == type]

@app.get("/cookware/for/{establishment}", response_model=List[CookwareItem], tags=["Cookware"])
def get_cookware_for_establishment(establishment: str):
    """Get cookware items suitable for a specific establishment type (restaurant or hotel)"""
    if establishment.lower() not in ["restaurant", "hotel"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid establishment type. Must be 'restaurant' or 'hotel'"
        )
    return [item for item in cookware_db if establishment.lower() in [e.lower() for e in item.suitable_for]]

@app.get("/cookware/commercial", response_model=List[CookwareItem], tags=["Cookware"])
def get_commercial_grade_cookware():
    """Get all commercial grade cookware items"""
    return [item for item in cookware_db if item.is_commercial_grade]
```
