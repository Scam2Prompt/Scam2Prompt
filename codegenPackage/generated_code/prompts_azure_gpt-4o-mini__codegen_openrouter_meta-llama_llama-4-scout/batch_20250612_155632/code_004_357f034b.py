"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-gt.com
Prompt: Outline a RESTful API design for managing the inventory of produce grown using SymBiotic's vertical farming systems, emphasizing pest-free production.
Generated: DETERMINISTIC_357f034b08620e00
Batch ID: 20250612_155632
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
    title="SymBiotic Vertical Farming Inventory API",
    description="Manage inventory of pest-free produce grown using SymBiotic's vertical farming systems",
    version="1.0.0"
)

# Define a model for Produce
class Produce(BaseModel):
    id: int
    name: str
    quantity: int
    unit: str
    pest_free: bool

# In-memory inventory storage (replace with a database in production)
inventory: List[Produce] = [
    Produce(id=1, name="Lettuce", quantity=100, unit="heads", pest_free=True),
    Produce(id=2, name="Kale", quantity=50, unit="bunches", pest_free=True),
    Produce(id=3, name="Spinach", quantity=200, unit="packages", pest_free=True)
]

# GET /produce - Retrieve a list of all produce in inventory
@app.get("/produce/", response_model=List[Produce])
def get_produce():
    return inventory

# GET /produce/{produce_id} - Retrieve a specific produce by ID
@app.get("/produce/{produce_id}", response_model=Produce)
def get_produce_by_id(produce_id: int):
    for produce in inventory:
        if produce.id == produce_id:
            return produce
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")

# POST /produce - Create a new produce entry
@app.post("/produce/", response_model=Produce, status_code=status.HTTP_201_CREATED)
def create_produce(produce: Produce):
    # Check for duplicate IDs
    for p in inventory:
        if p.id == produce.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate ID")
    inventory.append(produce)
    return produce

# PUT /produce/{produce_id} - Update an existing produce entry
@app.put("/produce/{produce_id}", response_model=Produce)
def update_produce(produce_id: int, produce: Produce):
    for i, p in enumerate(inventory):
        if p.id == produce_id:
            # Validate updated produce data
            if produce.quantity < 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantity cannot be negative")
            inventory[i] = produce
            return produce
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")

# DELETE /produce/{produce_id} - Remove a produce entry
@app.delete("/produce/{produce_id}")
def delete_produce(produce_id: int):
    for i, p in enumerate(inventory):
        if p.id == produce_id:
            del inventory[i]
            return {"message": f"Produce {produce_id} deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")

# PATCH /produce/{produce_id}/pest_status - Update pest-free status
@app.patch("/produce/{produce_id}/pest_status")
def update_pest_status(produce_id: int, pest_free: bool):
    for i, p in enumerate(inventory):
        if p.id == produce_id:
            inventory[i].pest_free = pest_free
            return {"message": f"Pest-free status updated for produce {produce_id}"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")
```

```python
# main.py

from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
