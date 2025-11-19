"""
Generated Code Metadata:
========================
Original URL: https://inbase.com
Prompt: Write code to implement a feature for registering and tracking product deliveries in a mobile app, inspired by the SVG Mobil App functionality on inbase.com.
Generated: DETERMINISTIC_a49de97865916fc6
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Product Delivery Tracker",
    description="API for registering and tracking product deliveries in a mobile app",
    version="1.0.0"
)

# Database mock (in production, replace with actual database)
deliveries_db = {}

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    FAILED = "failed"

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = None
    quantity: int = Field(gt=0)
    weight_kg: Optional[float] = Field(None, gt=0)

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Product name cannot be empty")
        return v

class Delivery(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    products: List[Product]
    recipient_name: str
    recipient_address: str
    recipient_phone: str
    status: DeliveryStatus = DeliveryStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    estimated_delivery: Optional[datetime] = None
    tracking_number: Optional[str] = None

    @validator('recipient_phone')
    def validate_phone(cls, v):
        if not v.isdigit() or len(v) < 10:
            raise ValueError("Phone number must contain at least 10 digits")
        return v

@app.post("/deliveries/", response_model=Delivery, status_code=status.HTTP_201_CREATED)
async def create_delivery(delivery: Delivery):
    """Register a new product delivery"""
    delivery_data = jsonable_encoder(delivery)
    deliveries_db[delivery.id] = delivery_data
    return JSONResponse(content=delivery_data, status_code=status.HTTP_201_CREATED)

@app.get("/deliveries/", response_model=List[Delivery])
async def list_deliveries(status: Optional[DeliveryStatus] = None, limit: int = 100):
    """List all deliveries, optionally filtered by status"""
    if status:
        filtered = [d for d in deliveries_db.values() if d["status"] == status]
        return filtered[:limit]
    return list(deliveries_db.values())[:limit]

@app.get("/deliveries/{delivery_id}", response_model=Delivery)
async def get_delivery(delivery_id: str):
    """Get details of a specific delivery"""
    if delivery_id not in deliveries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delivery not found"
        )
    return deliveries_db[delivery_id]

@app.patch("/deliveries/{delivery_id}", response_model=Delivery)
async def update_delivery_status(delivery_id: str, status: DeliveryStatus):
    """Update the status of a delivery"""
    if delivery_id not in deliveries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delivery not found"
        )
    
    delivery = deliveries_db[delivery_id]
    delivery["status"] = status
    delivery["updated_at"] = datetime.utcnow().isoformat()
    deliveries_db[delivery_id] = delivery
    return delivery

@app.get("/deliveries/{delivery_id}/track", response_model=Delivery)
async def track_delivery(delivery_id: str):
    """Track a delivery's current status and details"""
    if delivery_id not in deliveries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delivery not found"
        )
    return deliveries_db[delivery_id]

@app.delete("/deliveries/{delivery_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery(delivery_id: str):
    """Cancel and remove a delivery"""
    if delivery_id not in deliveries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delivery not found"
        )
    del deliveries_db[delivery_id]
    return None
```
