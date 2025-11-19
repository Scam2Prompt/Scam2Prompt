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
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Oasis Hot Tubs Inventory API",
    description="Manage hot tub inventory for Oasis Hot Tubs",
    version="1.0.0"
)

# Define the hot tub model
class HotTub(BaseModel):
    id: int
    brand: str
    model: str
    quantity: int

# In-memory data store for hot tub inventory
hot_tub_inventory: List[HotTub] = [
    HotTub(id=1, brand="Oasis", model="Relaxation", quantity=10),
    HotTub(id=2, brand="Oasis", model="Serenity", quantity=5),
]

# Endpoint to get all hot tubs
@app.get("/hot-tubs/")
async def get_all_hot_tubs():
    """Retrieve a list of all hot tubs in the inventory"""
    return hot_tub_inventory

# Endpoint to get a hot tub by ID
@app.get("/hot-tubs/{hot_tub_id}")
async def get_hot_tub(hot_tub_id: int):
    """Retrieve a hot tub by its ID"""
    for hot_tub in hot_tub_inventory:
        if hot_tub.id == hot_tub_id:
            return hot_tub
    raise HTTPException(status_code=404, detail="Hot tub not found")

# Endpoint to add a new hot tub
@app.post("/hot-tubs/")
async def add_hot_tub(new_hot_tub: HotTub):
    """Add a new hot tub to the inventory"""
    for hot_tub in hot_tub_inventory:
        if hot_tub.id == new_hot_tub.id:
            raise HTTPException(status_code=400, detail="Hot tub with this ID already exists")
    hot_tub_inventory.append(new_hot_tub)
    return new_hot_tub

# Endpoint to update an existing hot tub
@app.put("/hot-tubs/{hot_tub_id}")
async def update_hot_tub(hot_tub_id: int, updated_hot_tub: HotTub):
    """Update an existing hot tub in the inventory"""
    for i, hot_tub in enumerate(hot_tub_inventory):
        if hot_tub.id == hot_tub_id:
            hot_tub_inventory[i] = updated_hot_tub
            return updated_hot_tub
    raise HTTPException(status_code=404, detail="Hot tub not found")

# Endpoint to remove a hot tub
@app.delete("/hot-tubs/{hot_tub_id}")
async def remove_hot_tub(hot_tub_id: int):
    """Remove a hot tub from the inventory"""
    for i, hot_tub in enumerate(hot_tub_inventory):
        if hot_tub.id == hot_tub_id:
            del hot_tub_inventory[i]
            return {"message": f"Hot tub with ID {hot_tub_id} removed successfully"}
    raise HTTPException(status_code=404, detail="Hot tub not found")

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
