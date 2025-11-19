"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Create a RESTful API endpoint for a logistics service that handles ocean freight, including container sizes and types, inspired by the offerings of Fealty Worldwide.
Generated: DETERMINISTIC_984bb218ffb77adc
Batch ID: 20250612_155142
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
    title="Logistics Service API",
    description="API for managing ocean freight logistics",
    version="1.0.0"
)

# Define container sizes and types
class ContainerSize(BaseModel):
    """Container size model"""
    size: str
    length: int
    width: int
    height: int

class ContainerType(BaseModel):
    """Container type model"""
    type: str
    description: str

class Freight(BaseModel):
    """Freight model"""
    container_size: ContainerSize
    container_type: ContainerType
    weight: float
    volume: float

# In-memory data store for demonstration purposes
container_sizes: List[ContainerSize] = [
    ContainerSize(size="20ft", length=20, width=8, height=8),
    ContainerSize(size="40ft", length=40, width=8, height=8),
    ContainerSize(size="40ft HC", length=40, width=8, height=9)
]

container_types: List[ContainerType] = [
    ContainerType(type="Dry", description="Standard dry cargo container"),
    ContainerType(type="Refrigerated", description="Temperature-controlled container"),
    ContainerType(type="Tank", description="Liquid cargo container")
]

freights: List[Freight] = []

# API Endpoints
@app.get("/container_sizes/")
async def get_container_sizes():
    """Retrieve a list of available container sizes"""
    return container_sizes

@app.get("/container_types/")
async def get_container_types():
    """Retrieve a list of available container types"""
    return container_types

@app.post("/freights/")
async def create_freight(freight: Freight):
    """Create a new freight entry"""
    freights.append(freight)
    return freight

@app.get("/freights/")
async def get_freights():
    """Retrieve a list of all freight entries"""
    return freights

@app.get("/freights/{freight_id}")
async def get_freight(freight_id: int):
    """Retrieve a freight entry by ID"""
    try:
        return freights[freight_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Freight not found")

@app.put("/freights/{freight_id}")
async def update_freight(freight_id: int, freight: Freight):
    """Update a freight entry by ID"""
    try:
        freights[freight_id] = freight
        return freight
    except IndexError:
        raise HTTPException(status_code=404, detail="Freight not found")

@app.delete("/freights/{freight_id}")
async def delete_freight(freight_id: int):
    """Delete a freight entry by ID"""
    try:
        del freights[freight_id]
        return {"message": "Freight deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Freight not found")

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
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
