"""
Generated Code Metadata:
========================
Original URL: https://iggy.pages.dev
Prompt: Design an API for tracking cryptocurrency presale progress, including metrics like total supply and presale cap, using the $IGGY presale as a reference.
Generated: DETERMINISTIC_d853bdbb1b7cf411
Batch ID: 20250622_204603
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
from typing import Optional

app = FastAPI(
    title="Cryptocurrency Presale Tracker",
    description="API for tracking cryptocurrency presale progress",
    version="1.0.0",
)

class Presale(BaseModel):
    """Presale model"""
    id: str
    name: str
    total_supply: int
    presale_cap: float
    current_supply: Optional[int] = 0
    current_cap: Optional[float] = 0.0

    class Config:
        """Presale model configuration"""
        schema_extra = {
            "example": {
                "id": "iggy",
                "name": "$IGGY Presale",
                "total_supply": 1000000000,
                "presale_cap": 1000000.0
            }
        }

presales: dict[str, Presale] = {}

@app.post("/presales/")
async def create_presale(presale: Presale):
    """Create a new presale"""
    if presale.id in presales:
        raise HTTPException(status_code=400, detail="Presale already exists")
    presales[presale.id] = presale
    return presale

@app.get("/presales/")
async def read_presales():
    """Get all presales"""
    return list(presales.values())

@app.get("/presales/{presale_id}")
async def read_presale(presale_id: str):
    """Get a presale by ID"""
    presale = presales.get(presale_id)
    if not presale:
        raise HTTPException(status_code=404, detail="Presale not found")
    return presale

@app.put("/presales/{presale_id}")
async def update_presale(presale_id: str, presale: Presale):
    """Update a presale"""
    existing_presale = presales.get(presale_id)
    if not existing_presale:
        raise HTTPException(status_code=404, detail="Presale not found")
    presales[presale_id] = presale
    return presale

@app.patch("/presales/{presale_id}/supply")
async def update_supply(presale_id: str, supply: int):
    """Update the current supply of a presale"""
    presale = presales.get(presale_id)
    if not presale:
        raise HTTPException(status_code=404, detail="Presale not found")
    if supply < 0 or supply > presale.total_supply:
        raise HTTPException(status_code=400, detail="Invalid supply")
    presale.current_supply = supply
    presales[presale_id] = presale
    return presale

@app.patch("/presales/{presale_id}/cap")
async def update_cap(presale_id: str, cap: float):
    """Update the current cap of a presale"""
    presale = presales.get(presale_id)
    if not presale:
        raise HTTPException(status_code=404, detail="Presale not found")
    if cap < 0 or cap > presale.presale_cap:
        raise HTTPException(status_code=400, detail="Invalid cap")
    presale.current_cap = cap
    presales[presale_id] = presale
    return presale

@app.get("/presales/{presale_id}/metrics")
async def get_metrics(presale_id: str):
    """Get metrics for a presale"""
    presale = presales.get(presale_id)
    if not presale:
        raise HTTPException(status_code=404, detail="Presale not found")
    supply_progress = (presale.current_supply / presale.total_supply) * 100 if presale.total_supply > 0 else 0
    cap_progress = (presale.current_cap / presale.presale_cap) * 100 if presale.presale_cap > 0 else 0
    return {
        "supply_progress": supply_progress,
        "cap_progress": cap_progress,
        "total_supply": presale.total_supply,
        "presale_cap": presale.presale_cap,
        "current_supply": presale.current_supply,
        "current_cap": presale.current_cap
    }
```

```python
# main.py

from app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
