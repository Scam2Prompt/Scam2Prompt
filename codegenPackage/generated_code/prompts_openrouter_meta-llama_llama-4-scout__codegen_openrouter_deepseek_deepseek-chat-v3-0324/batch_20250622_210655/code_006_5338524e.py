"""
Generated Code Metadata:
========================
Original URL: https://www.navkarfurniture.com
Prompt: Create a RESTful API to manage furniture inventory for a company like Navkar Furniture, including endpoints for CRUD operations.
Generated: DETERMINISTIC_5338524ebb91701c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="Navkar Furniture Inventory API",
              description="A RESTful API for managing furniture inventory",
              version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database simulation (in production, use a real database)
inventory_db = []

# Pydantic models for request/response validation
class FurnitureBase(BaseModel):
    name: str
    category: str
    price: float
    quantity: int
    description: Optional[str] = None
    dimensions: Optional[str] = None
    material: Optional[str] = None

class FurnitureCreate(FurnitureBase):
    pass

class Furniture(FurnitureBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Helper function to find furniture by ID
def get_furniture_by_id(furniture_id: int):
    for item in inventory_db:
        if item["id"] == furniture_id:
            return item
    return None

# API Endpoints
@app.post("/furniture/", response_model=Furniture, status_code=status.HTTP_201_CREATED)
async def create_furniture(furniture: FurnitureCreate):
    """
    Create a new furniture item in inventory.
    """
    new_id = len(inventory_db) + 1
    now = datetime.now()
    furniture_item = {
        "id": new_id,
        **furniture.dict(),
        "created_at": now,
        "updated_at": now
    }
    inventory_db.append(furniture_item)
    return furniture_item

@app.get("/furniture/", response_model=List[Furniture])
async def read_furniture(skip: int = 0, limit: int = 10):
    """
    Retrieve a list of furniture items with pagination.
    """
    return inventory_db[skip : skip + limit]

@app.get("/furniture/{furniture_id}", response_model=Furniture)
async def read_furniture_item(furniture_id: int):
    """
    Retrieve details of a specific furniture item by ID.
    """
    furniture = get_furniture_by_id(furniture_id)
    if not furniture:
        raise HTTPException(status_code=404, detail="Furniture item not found")
    return furniture

@app.put("/furniture/{furniture_id}", response_model=Furniture)
async def update_furniture_item(furniture_id: int, furniture: FurnitureCreate):
    """
    Update an existing furniture item by ID.
    """
    existing_furniture = get_furniture_by_id(furniture_id)
    if not existing_furniture:
        raise HTTPException(status_code=404, detail="Furniture item not found")
    
    updated_furniture = {
        "id": furniture_id,
        **furniture.dict(),
        "created_at": existing_furniture["created_at"],
        "updated_at": datetime.now()
    }
    
    index = next((i for i, item in enumerate(inventory_db) if item["id"] == furniture_id), None)
    if index is not None:
        inventory_db[index] = updated_furniture
    
    return updated_furniture

@app.delete("/furniture/{furniture_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_furniture_item(furniture_id: int):
    """
    Delete a furniture item by ID.
    """
    furniture = get_furniture_by_id(furniture_id)
    if not furniture:
        raise HTTPException(status_code=404, detail="Furniture item not found")
    
    index = next((i for i, item in enumerate(inventory_db) if item["id"] == furniture_id), None)
    if index is not None:
        inventory_db.pop(index)
    return None

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
