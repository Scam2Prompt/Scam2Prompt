"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Develop a RESTful API endpoint for managing project and heavy lift cargo shipments, inspired by the logistics solutions offered by Portline Shipping.
Generated: DETERMINISTIC_99d3f84bfe427f38
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Portline Shipping API",
    description="RESTful API for managing project and heavy lift cargo shipments",
    version="1.0.0"
)

# Database simulation
shipments_db = []

# Models
class Dimensions(BaseModel):
    length: float = Field(..., gt=0, description="Length in meters")
    width: float = Field(..., gt=0, description="Width in meters")
    height: float = Field(..., gt=0, description="Height in meters")
    weight: float = Field(..., gt=0, description="Weight in metric tons")

class ShipmentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    origin: str = Field(..., min_length=2, max_length=100)
    destination: str = Field(..., min_length=2, max_length=100)
    dimensions: Dimensions
    cargo_type: str = Field(..., regex="^(project|heavy_lift)$")
    special_requirements: Optional[List[str]] = None

class ShipmentCreate(ShipmentBase):
    pass

class Shipment(ShipmentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    status: str = Field("pending", regex="^(pending|in_transit|delivered|canceled)$")

    class Config:
        orm_mode = True

# Helper functions
def get_shipment(shipment_id: UUID):
    for shipment in shipments_db:
        if shipment.id == shipment_id:
            return shipment
    return None

# Endpoints
@app.post("/shipments/", response_model=Shipment, status_code=status.HTTP_201_CREATED)
async def create_shipment(shipment: ShipmentCreate):
    """
    Create a new shipment (project or heavy lift cargo).
    """
    try:
        db_shipment = Shipment(
            id=uuid4(),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **shipment.dict()
        )
        shipments_db.append(db_shipment)
        logger.info(f"Created shipment with ID: {db_shipment.id}")
        return db_shipment
    except Exception as e:
        logger.error(f"Error creating shipment: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create shipment"
        )

@app.get("/shipments/", response_model=List[Shipment])
async def list_shipments(cargo_type: Optional[str] = None):
    """
    List all shipments, optionally filtered by cargo type.
    """
    try:
        if cargo_type:
            return [s for s in shipments_db if s.cargo_type == cargo_type]
        return shipments_db
    except Exception as e:
        logger.error(f"Error listing shipments: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve shipments"
        )

@app.get("/shipments/{shipment_id}", response_model=Shipment)
async def get_shipment_by_id(shipment_id: UUID):
    """
    Get details of a specific shipment by ID.
    """
    shipment = get_shipment(shipment_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )
    return shipment

@app.put("/shipments/{shipment_id}", response_model=Shipment)
async def update_shipment(shipment_id: UUID, shipment_update: ShipmentCreate):
    """
    Update an existing shipment.
    """
    try:
        shipment = get_shipment(shipment_id)
        if not shipment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shipment not found"
            )

        update_data = shipment_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(shipment, field, value)
        shipment.updated_at = datetime.utcnow()

        logger.info(f"Updated shipment with ID: {shipment_id}")
        return shipment
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating shipment: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update shipment"
        )

@app.patch("/shipments/{shipment_id}/status", response_model=Shipment)
async def update_shipment_status(shipment_id: UUID, status: str = Field(..., regex="^(pending|in_transit|delivered|canceled)$")):
    """
    Update the status of a shipment.
    """
    try:
        shipment = get_shipment(shipment_id)
        if not shipment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shipment not found"
            )

        shipment.status = status
        shipment.updated_at = datetime.utcnow()

        logger.info(f"Updated status for shipment {shipment_id} to {status}")
        return shipment
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating shipment status: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update shipment status"
        )

@app.delete("/shipments/{shipment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment(shipment_id: UUID):
    """
    Delete a shipment.
    """
    try:
        global shipments_db
        shipment = get_shipment(shipment_id)
        if not shipment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shipment not found"
            )

        shipments_db = [s for s in shipments_db if s.id != shipment_id]
        logger.info(f"Deleted shipment with ID: {shipment_id}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting shipment: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete shipment"
        )
```
