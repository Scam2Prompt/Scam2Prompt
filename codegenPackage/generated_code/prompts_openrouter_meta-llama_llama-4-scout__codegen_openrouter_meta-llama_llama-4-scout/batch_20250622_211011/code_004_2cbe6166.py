"""
Generated Code Metadata:
========================
Original URL: https://berang.vercel.app
Prompt: Design a simple API for managing parts data in an application similar to Beerang Parts.
Generated: DETERMINISTIC_2cbe61663735e2ad
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# parts_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Parts API",
    description="A simple API for managing parts data",
    version="1.0.0"
)

# Define a Pydantic model for Parts
class Part(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

# In-memory data store (replace with a database in production)
parts_data = [
    Part(id=1, name="Part 1", description="This is part 1", price=10.99, quantity=100),
    Part(id=2, name="Part 2", description="This is part 2", price=5.99, quantity=50),
]

# GET /
@app.get("/")
def read_root():
    return {"message": "Parts API is running"}

# GET /parts
@app.get("/parts/", response_model=List[Part])
def read_parts():
    return parts_data

# GET /parts/{part_id}
@app.get("/parts/{part_id}", response_model=Part)
def read_part(part_id: int):
    for part in parts_data:
        if part.id == part_id:
            return part
    raise HTTPException(status_code=404, detail="Part not found")

# POST /parts
@app.post("/parts/", response_model=Part, status_code=201)
def create_part(part: Part):
    # Check for duplicate part ID
    for existing_part in parts_data:
        if existing_part.id == part.id:
            raise HTTPException(status_code=400, detail="Part with this ID already exists")
    parts_data.append(part)
    return part

# PUT /parts/{part_id}
@app.put("/parts/{part_id}", response_model=Part)
def update_part(part_id: int, part: Part):
    for existing_part in parts_data:
        if existing_part.id == part_id:
            existing_part.name = part.name
            existing_part.description = part.description
            existing_part.price = part.price
            existing_part.quantity = part.quantity
            return existing_part
    raise HTTPException(status_code=404, detail="Part not found")

# DELETE /parts/{part_id}
@app.delete("/parts/{part_id}")
def delete_part(part_id: int):
    for i, part in enumerate(parts_data):
        if part.id == part_id:
            del parts_data[i]
            return {"message": f"Part {part_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Part not found")
```

```python
# main.py

import uvicorn
from parts_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000
```
