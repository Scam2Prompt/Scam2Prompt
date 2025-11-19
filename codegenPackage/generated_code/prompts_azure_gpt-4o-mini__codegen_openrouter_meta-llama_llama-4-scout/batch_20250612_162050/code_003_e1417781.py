"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Develop a REST API endpoint for managing inventory of car chargers, inspired by the product categories listed on Volport's website.
Generated: DETERMINISTIC_e1417781284ef76e
Batch ID: 20250612_162050
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
    title="Car Charger Inventory API",
    description="Manage inventory of car chargers",
    version="1.0.0"
)

# Define the CarCharger model
class CarCharger(BaseModel):
    id: int
    name: str
    category: str
    quantity: int
    price: float

# In-memory inventory storage (replace with a database in production)
inventory: List[CarCharger] = [
    CarCharger(id=1, name="Volport Fast Charger", category="Fast Chargers", quantity=10, price=99.99),
    CarCharger(id=2, name="Volport Standard Charger", category="Standard Chargers", quantity=20, price=49.99),
]

# GET /car-chargers
@app.get("/car-chargers/", response_model=List[CarCharger])
async def read_car_chargers():
    """Retrieve a list of all car chargers in the inventory"""
    return inventory

# GET /car-chargers/{charger_id}
@app.get("/car-chargers/{charger_id}", response_model=CarCharger)
async def read_car_charger(charger_id: int):
    """Retrieve a car charger by ID"""
    charger = next((c for c in inventory if c.id == charger_id), None)
    if charger is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car charger not found")
    return charger

# POST /car-chargers
@app.post("/car-chargers/", response_model=CarCharger, status_code=status.HTTP_201_CREATED)
async def create_car_charger(car_charger: CarCharger):
    """Create a new car charger in the inventory"""
    # Check for duplicate IDs
    if any(c.id == car_charger.id for c in inventory):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate ID")
    inventory.append(car_charger)
    return car_charger

# PUT /car-chargers/{charger_id}
@app.put("/car-chargers/{charger_id}", response_model=CarCharger)
async def update_car_charger(charger_id: int, car_charger: CarCharger):
    """Update an existing car charger in the inventory"""
    charger = next((c for c in inventory if c.id == charger_id), None)
    if charger is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car charger not found")
    charger.name = car_charger.name
    charger.category = car_charger.category
    charger.quantity = car_charger.quantity
    charger.price = car_charger.price
    return charger

# DELETE /car-chargers/{charger_id}
@app.delete("/car-chargers/{charger_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_car_charger(charger_id: int):
    """Delete a car charger from the inventory"""
    global inventory
    inventory = [c for c in inventory if c.id != charger_id]
    # If the charger was not found, return a 404
    if len(inventory) == len([c for c in inventory if c.id != charger_id]):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car charger not found")

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
