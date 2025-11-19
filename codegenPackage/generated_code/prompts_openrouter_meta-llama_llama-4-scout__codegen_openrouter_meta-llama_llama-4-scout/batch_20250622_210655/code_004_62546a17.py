"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Design a RESTful API for managing vehicle showroom inventory, including endpoints for adding, removing, and updating vehicle listings, using Galopin Automobile as a reference.
Generated: DETERMINISTIC_62546a17309a141a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Galopin Automobile Showroom Inventory API",
    description="RESTful API for managing vehicle showroom inventory",
    version="1.0.0",
)

# Define the Vehicle model
class Vehicle(BaseModel):
    """Vehicle listing model"""
    id: int
    brand: str
    model: str
    year: int
    price: float

# In-memory vehicle inventory (replace with a database in production)
vehicle_inventory: List[Vehicle] = []

# Endpoint to add a new vehicle listing
@app.post("/vehicles/", status_code=status.HTTP_201_CREATED)
async def create_vehicle(vehicle: Vehicle):
    """Create a new vehicle listing"""
    # Check if vehicle already exists
    if any(v.id == vehicle.id for v in vehicle_inventory):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vehicle with this ID already exists")
    vehicle_inventory.append(vehicle)
    return vehicle

# Endpoint to retrieve all vehicle listings
@app.get("/vehicles/", response_model=List[Vehicle])
async def read_vehicles():
    """Retrieve all vehicle listings"""
    return vehicle_inventory

# Endpoint to retrieve a vehicle listing by ID
@app.get("/vehicles/{vehicle_id}", response_model=Vehicle)
async def read_vehicle(vehicle_id: int):
    """Retrieve a vehicle listing by ID"""
    vehicle = next((v for v in vehicle_inventory if v.id == vehicle_id), None)
    if vehicle is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle not found")
    return vehicle

# Endpoint to update a vehicle listing
@app.put("/vehicles/{vehicle_id}", response_model=Vehicle)
async def update_vehicle(vehicle_id: int, vehicle: Vehicle):
    """Update a vehicle listing"""
    existing_vehicle = next((v for v in vehicle_inventory if v.id == vehicle_id), None)
    if existing_vehicle is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle not found")
    existing_vehicle.brand = vehicle.brand
    existing_vehicle.model = vehicle.model
    existing_vehicle.year = vehicle.year
    existing_vehicle.price = vehicle.price
    return existing_vehicle

# Endpoint to remove a vehicle listing
@app.delete("/vehicles/{vehicle_id}")
async def delete_vehicle(vehicle_id: int):
    """Remove a vehicle listing"""
    global vehicle_inventory
    vehicle_inventory = [v for v in vehicle_inventory if v.id != vehicle_id]
    return {"message": f"Vehicle with ID {vehicle_id} removed successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
