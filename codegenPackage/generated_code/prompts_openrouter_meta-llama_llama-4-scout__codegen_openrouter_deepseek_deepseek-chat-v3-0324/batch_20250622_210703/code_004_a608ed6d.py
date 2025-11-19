"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Design a simple API to manage hot tub inventory, including endpoints for adding, removing, and updating hot tub models, using the brands and products offered by Oasis Hot Tubs.
Generated: DETERMINISTIC_a608ed6d82bdce9f
Batch ID: 20250622_210703
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
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI(title="Oasis Hot Tubs Inventory API")

# Database simulation
inventory_db = []

# Models
class HotTubModel(BaseModel):
    id: UUID
    brand: str
    model_name: str
    capacity: int
    jets: int
    price: float
    in_stock: bool

class HotTubCreate(BaseModel):
    brand: str
    model_name: str
    capacity: int
    jets: int
    price: float
    in_stock: bool = True

class HotTubUpdate(BaseModel):
    brand: Optional[str] = None
    model_name: Optional[str] = None
    capacity: Optional[int] = None
    jets: Optional[int] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None

# Endpoints
@app.post("/hot-tubs/", response_model=HotTubModel, status_code=status.HTTP_201_CREATED)
async def add_hot_tub(hot_tub: HotTubCreate):
    """
    Add a new hot tub model to inventory.
    """
    new_hot_tub = HotTubModel(
        id=uuid4(),
        **hot_tub.dict()
    )
    inventory_db.append(new_hot_tub)
    return new_hot_tub

@app.get("/hot-tubs/", response_model=List[HotTubModel])
async def get_all_hot_tubs():
    """
    Retrieve all hot tub models in inventory.
    """
    return inventory_db

@app.get("/hot-tubs/{hot_tub_id}", response_model=HotTubModel)
async def get_hot_tub(hot_tub_id: UUID):
    """
    Retrieve a specific hot tub model by ID.
    """
    for hot_tub in inventory_db:
        if hot_tub.id == hot_tub_id:
            return hot_tub
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Hot tub model not found"
    )

@app.put("/hot-tubs/{hot_tub_id}", response_model=HotTubModel)
async def update_hot_tub(hot_tub_id: UUID, hot_tub_update: HotTubUpdate):
    """
    Update a hot tub model's details.
    """
    for index, hot_tub in enumerate(inventory_db):
        if hot_tub.id == hot_tub_id:
            update_data = hot_tub_update.dict(exclude_unset=True)
            updated_hot_tub = hot_tub.copy(update=update_data)
            inventory_db[index] = updated_hot_tub
            return updated_hot_tub
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Hot tub model not found"
    )

@app.delete("/hot-tubs/{hot_tub_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hot_tub(hot_tub_id: UUID):
    """
    Remove a hot tub model from inventory.
    """
    for index, hot_tub in enumerate(inventory_db):
        if hot_tub.id == hot_tub_id:
            inventory_db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Hot tub model not found"
    )

@app.get("/hot-tubs/brand/{brand_name}", response_model=List[HotTubModel])
async def get_hot_tubs_by_brand(brand_name: str):
    """
    Retrieve all hot tub models by brand.
    """
    return [hot_tub for hot_tub in inventory_db if hot_tub.brand.lower() == brand_name.lower()]

@app.get("/hot-tubs/in-stock", response_model=List[HotTubModel])
async def get_in_stock_hot_tubs():
    """
    Retrieve all hot tub models currently in stock.
    """
    return [hot_tub for hot_tub in inventory_db if hot_tub.in_stock]
```
