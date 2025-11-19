"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Create a REST API endpoint for managing property listings, inspired by the services offered on Dominguez Parra's website, including endpoints for adding, updating, and deleting properties.
Generated: DETERMINISTIC_33d953d18bf31869
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime
import uvicorn

app = FastAPI(
    title="Property Listing API",
    description="API for managing property listings inspired by Dominguez Parra",
    version="1.0.0"
)

# Database mock (in production, use a real database)
property_db = []

# Models
class PropertyBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    price: float = Field(..., gt=0)
    location: str = Field(..., min_length=3, max_length=100)
    property_type: str = Field(..., min_length=3, max_length=50)
    bedrooms: int = Field(..., ge=0)
    bathrooms: int = Field(..., ge=0)
    area_sqft: float = Field(..., gt=0)
    amenities: Optional[List[str]] = None

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Helper functions
def get_property_by_id(property_id: UUID):
    for prop in property_db:
        if prop["id"] == property_id:
            return prop
    return None

# Endpoints
@app.post("/properties/", response_model=Property, status_code=status.HTTP_201_CREATED)
async def create_property(property_data: PropertyCreate):
    """
    Create a new property listing.
    """
    property_dict = property_data.dict()
    property_dict["id"] = uuid4()
    now = datetime.now()
    property_dict["created_at"] = now
    property_dict["updated_at"] = now
    
    property_db.append(property_dict)
    return property_dict

@app.get("/properties/", response_model=List[Property])
async def list_properties():
    """
    Get all property listings.
    """
    return property_db

@app.get("/properties/{property_id}", response_model=Property)
async def get_property(property_id: UUID):
    """
    Get a specific property by ID.
    """
    property = get_property_by_id(property_id)
    if not property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found"
        )
    return property

@app.put("/properties/{property_id}", response_model=Property)
async def update_property(property_id: UUID, property_data: PropertyCreate):
    """
    Update an existing property listing.
    """
    property = get_property_by_id(property_id)
    if not property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found"
        )
    
    update_data = property_data.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now()
    
    for key, value in update_data.items():
        property[key] = value
    
    return property

@app.delete("/properties/{property_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_property(property_id: UUID):
    """
    Delete a property listing.
    """
    global property_db
    property = get_property_by_id(property_id)
    if not property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found"
        )
    
    property_db = [prop for prop in property_db if prop["id"] != property_id]
    return None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
