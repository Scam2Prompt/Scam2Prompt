"""
Generated Code Metadata:
========================
Original URL: https://jaguarlandroverjakarta.com
Prompt: Create a RESTful API to manage Jaguar Land Rover vehicle inventory, including endpoints for retrieving vehicle information, prices, and promotions.
Generated: DETERMINISTIC_a68f874425a9e7e0
Batch ID: 20250622_212854
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
import uuid
from datetime import date

app = FastAPI(
    title="Jaguar Land Rover Inventory API",
    description="API for managing Jaguar Land Rover vehicle inventory",
    version="1.0.0"
)

# Database simulation
inventory_db = []
promotions_db = []

# Models
class Vehicle(BaseModel):
    id: str
    model: str
    year: int
    color: str
    price: float
    features: List[str]
    in_stock: bool
    last_updated: date

class VehicleCreate(BaseModel):
    model: str
    year: int
    color: str
    price: float
    features: List[str]
    in_stock: bool

class VehicleUpdate(BaseModel):
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[str] = None
    price: Optional[float] = None
    features: Optional[List[str]] = None
    in_stock: Optional[bool] = None

class Promotion(BaseModel):
    id: str
    vehicle_id: str
    name: str
    description: str
    discount_percentage: float
    start_date: date
    end_date: date

class PromotionCreate(BaseModel):
    vehicle_id: str
    name: str
    description: str
    discount_percentage: float
    start_date: date
    end_date: date

# Helper functions
def find_vehicle(vehicle_id: str):
    for vehicle in inventory_db:
        if vehicle["id"] == vehicle_id:
            return vehicle
    return None

def find_promotion(promotion_id: str):
    for promotion in promotions_db:
        if promotion["id"] == promotion_id:
            return promotion
    return None

# Vehicle endpoints
@app.post("/vehicles/", response_model=Vehicle, status_code=status.HTTP_201_CREATED)
async def create_vehicle(vehicle: VehicleCreate):
    """
    Add a new vehicle to the inventory.
    """
    vehicle_id = str(uuid.uuid4())
    new_vehicle = {
        "id": vehicle_id,
        "model": vehicle.model,
        "year": vehicle.year,
        "color": vehicle.color,
        "price": vehicle.price,
        "features": vehicle.features,
        "in_stock": vehicle.in_stock,
        "last_updated": date.today()
    }
    inventory_db.append(new_vehicle)
    return new_vehicle

@app.get("/vehicles/", response_model=List[Vehicle])
async def get_all_vehicles(in_stock: Optional[bool] = None):
    """
    Get all vehicles in inventory, optionally filtered by stock status.
    """
    if in_stock is not None:
        return [v for v in inventory_db if v["in_stock"] == in_stock]
    return inventory_db

@app.get("/vehicles/{vehicle_id}", response_model=Vehicle)
async def get_vehicle(vehicle_id: str):
    """
    Get a specific vehicle by ID.
    """
    vehicle = find_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found"
        )
    return vehicle

@app.put("/vehicles/{vehicle_id}", response_model=Vehicle)
async def update_vehicle(vehicle_id: str, vehicle_update: VehicleUpdate):
    """
    Update a vehicle's information.
    """
    vehicle = find_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found"
        )
    
    update_data = vehicle_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        vehicle[key] = value
    vehicle["last_updated"] = date.today()
    
    return vehicle

@app.delete("/vehicles/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle(vehicle_id: str):
    """
    Remove a vehicle from inventory.
    """
    vehicle = find_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found"
        )
    inventory_db.remove(vehicle)
    return None

# Promotion endpoints
@app.post("/promotions/", response_model=Promotion, status_code=status.HTTP_201_CREATED)
async def create_promotion(promotion: PromotionCreate):
    """
    Create a new promotion for a vehicle.
    """
    if not find_vehicle(promotion.vehicle_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found"
        )
    
    promotion_id = str(uuid.uuid4())
    new_promotion = {
        "id": promotion_id,
        "vehicle_id": promotion.vehicle_id,
        "name": promotion.name,
        "description": promotion.description,
        "discount_percentage": promotion.discount_percentage,
        "start_date": promotion.start_date,
        "end_date": promotion.end_date
    }
    promotions_db.append(new_promotion)
    return new_promotion

@app.get("/promotions/", response_model=List[Promotion])
async def get_all_promotions():
    """
    Get all active promotions.
    """
    today = date.today()
    return [p for p in promotions_db if p["start_date"] <= today <= p["end_date"]]

@app.get("/promotions/{promotion_id}", response_model=Promotion)
async def get_promotion(promotion_id: str):
    """
    Get a specific promotion by ID.
    """
    promotion = find_promotion(promotion_id)
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )
    return promotion

@app.get("/vehicles/{vehicle_id}/promotions", response_model=List[Promotion])
async def get_vehicle_promotions(vehicle_id: str):
    """
    Get all promotions for a specific vehicle.
    """
    if not find_vehicle(vehicle_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found"
        )
    
    today = date.today()
    return [p for p in promotions_db 
            if p["vehicle_id"] == vehicle_id 
            and p["start_date"] <= today <= p["end_date"]]

@app.delete("/promotions/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_promotion(promotion_id: str):
    """
    Remove a promotion.
    """
    promotion = find_promotion(promotion_id)
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )
    promotions_db.remove(promotion)
    return None

# Price calculation endpoint
@app.get("/vehicles/{vehicle_id}/price", response_model=dict)
async def get_vehicle_price(vehicle_id: str):
    """
    Get the current price of a vehicle including any active promotions.
    """
    vehicle = find_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vehicle not found"
        )
    
    today = date.today()
    active_promotions = [p for p in promotions_db 
                         if p["vehicle_id"] == vehicle_id 
                         and p["start_date"] <= today <= p["end_date"]]
    
    max_discount = max([p["discount_percentage"] for p in active_promotions], default=0)
    discounted_price = vehicle["price"] * (1 - max_discount / 100)
    
    return {
        "original_price": vehicle["price"],
        "discounted_price": round(discounted_price, 2),
        "discount_percentage": max_discount,
        "active_promotions": len(active_promotions)
    }
```
