"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: Create an API that manages inventory for a garment division, incorporating features like sewing, cutting, and finishing as outlined by Knit Plus Ltd.
Generated: DETERMINISTIC_aa1fa35685f11fab
Batch ID: 20250612_162050
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8000/garments/1/next_stage": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/garments/1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/garments/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/garments/1/status": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# inventory_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Garment Inventory API",
    description="API for managing inventory for the garment division of Knit Plus Ltd.",
    version="1.0.0",
)

# Define the garment model
class Garment(BaseModel):
    id: int
    name: str
    quantity: int
    status: str  # e.g., "sewing", "cutting", "finishing", "completed"

# In-memory inventory storage (replace with a database in production)
inventory: List[Garment] = [
    Garment(id=1, name="T-Shirt", quantity=100, status="sewing"),
    Garment(id=2, name="Dress", quantity=50, status="cutting"),
]

# API endpoint to get all garments in inventory
@app.get("/garments/")
async def get_garments():
    return inventory

# API endpoint to get a garment by ID
@app.get("/garments/{garment_id}")
async def get_garment(garment_id: int):
    for garment in inventory:
        if garment.id == garment_id:
            return garment
    raise HTTPException(status_code=404, detail="Garment not found")

# API endpoint to add a new garment to inventory
@app.post("/garments/")
async def create_garment(garment: Garment):
    for existing_garment in inventory:
        if existing_garment.id == garment.id:
            raise HTTPException(status_code=400, detail="Garment with this ID already exists")
    inventory.append(garment)
    return garment

# API endpoint to update a garment's status
@app.put("/garments/{garment_id}/status")
async def update_garment_status(garment_id: int, status: str):
    for garment in inventory:
        if garment.id == garment_id:
            garment.status = status
            return garment
    raise HTTPException(status_code=404, detail="Garment not found")

# API endpoint to delete a garment from inventory
@app.delete("/garments/{garment_id}")
async def delete_garment(garment_id: int):
    for i, garment in enumerate(inventory):
        if garment.id == garment_id:
            del inventory[i]
            return {"message": "Garment deleted successfully"}
    raise HTTPException(status_code=404, detail="Garment not found")

# API endpoint to move a garment to the next stage
@app.post("/garments/{garment_id}/next_stage")
async def move_to_next_stage(garment_id: int):
    stages = ["sewing", "cutting", "finishing", "completed"]
    for garment in inventory:
        if garment.id == garment_id:
            current_stage_index = stages.index(garment.status)
            if current_stage_index < len(stages) - 1:
                garment.status = stages[current_stage_index + 1]
                return garment
            else:
                raise HTTPException(status_code=400, detail="Garment is already completed")
    raise HTTPException(status_code=404, detail="Garment not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py

from inventory_api import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run using: uvicorn inventory_api:app --host 0.0.0.0 --port 8000
```

### API Endpoints

#### 1. Get all garments
- **Endpoint:** `GET /garments/`
- **Response:** List of all garments in inventory

#### 2. Get a garment by ID
- **Endpoint:** `GET /garments/{garment_id}`
- **Response:** Garment details

#### 3. Create a new garment
- **Endpoint:** `POST /garments/`
- **Request Body:** Garment details (id, name, quantity, status)
- **Response:** Created garment

#### 4. Update a garment's status
- **Endpoint:** `PUT /garments/{garment_id}/status`
- **Request Body:** New status
- **Response:** Updated garment

#### 5. Delete a garment
- **Endpoint:** `DELETE /garments/{garment_id}`
- **Response:** Success message

#### 6. Move a garment to the next stage
- **Endpoint:** `POST /garments/{garment_id}/next_stage`
- **Response:** Updated garment

### Example Usage

```bash
curl http://localhost:8000/garments/
curl http://localhost:8000/garments/1
curl -X POST -H "Content-Type: application/json" -d '{"id": 3, "name": "Pants", "quantity": 200, "status": "sewing"}' http://localhost:8000/garments/
curl -X PUT -H "Content-Type: application/json" -d '{"status": "cutting"}' http://localhost:8000/garments/1/status
curl -X DELETE http://localhost:8000/garments/1
curl -X POST http://localhost:8000/garments/1/next_stage
```
