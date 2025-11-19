"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: Develop a REST API endpoint that retrieves details about "tủ rượu mini" (mini wine cabinets), including storage capacity, material type, and design ideas.
Generated: DETERMINISTIC_f346ad54b880aa52
Batch ID: 20250612_153225
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
    title="Mini Wine Cabinet API",
    description="Retrieve details about mini wine cabinets",
    version="1.0.0"
)

class MiniWineCabinet(BaseModel):
    """Model for mini wine cabinet"""
    id: int
    storage_capacity: int  # number of bottles
    material_type: str
    design_ideas: str

# In-memory data store (replace with a database in production)
mini_wine_cabinets: List[MiniWineCabinet] = [
    MiniWineCabinet(
        id=1,
        storage_capacity=6,
        material_type="Wood",
        design_ideas="Modern, compact design with glass door"
    ),
    MiniWineCabinet(
        id=2,
        storage_capacity=12,
        material_type="Metal",
        design_ideas="Industrial-style with LED lighting"
    )
]

@app.get("/mini-wine-cabinets/")
async def read_mini_wine_cabinets():
    """Retrieve a list of mini wine cabinets"""
    return mini_wine_cabinets

@app.get("/mini-wine-cabinets/{mini_wine_cabinet_id}")
async def read_mini_wine_cabinet(mini_wine_cabinet_id: int):
    """Retrieve a mini wine cabinet by ID"""
    for cabinet in mini_wine_cabinets:
        if cabinet.id == mini_wine_cabinet_id:
            return cabinet
    raise HTTPException(status_code=404, detail="Mini wine cabinet not found")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return {"error": exc.detail}, exc.status_code

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
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
