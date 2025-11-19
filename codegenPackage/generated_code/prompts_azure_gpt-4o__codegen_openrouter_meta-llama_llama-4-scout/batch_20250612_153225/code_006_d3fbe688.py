"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Develop a REST API that allows users to retrieve information about wine tasting seminars, including details like location, time, and sommelier information, as seen in the FestiVin Caraquet program.
Generated: DETERMINISTIC_d3fbe6886cd77419
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
from datetime import datetime

app = FastAPI(
    title="Wine Tasting Seminars API",
    description="Retrieve information about wine tasting seminars",
    version="1.0.0"
)

# Define the Sommelier model
class Sommelier(BaseModel):
    """Sommelier information"""
    name: str
    bio: str

# Define the Seminar model
class Seminar(BaseModel):
    """Seminar information"""
    id: int
    location: str
    time: datetime
    sommelier: Sommelier
    description: str

# In-memory seminar data store (replace with a database in production)
seminars: List[Seminar] = [
    Seminar(
        id=1,
        location="Salle des vins, Caraquet",
        time=datetime(2024, 9, 17, 10, 0, 0),
        sommelier=Sommelier(
            name="Jean-Pierre LaFleur",
            bio="Certified sommelier with 10+ years of experience"
        ),
        description="Introduction to wine tasting"
    ),
    Seminar(
        id=2,
        location="Salle des vins, Caraquet",
        time=datetime(2024, 9, 18, 14, 0, 0),
        sommelier=Sommelier(
            name="Marie-Eve Gagnon",
            bio="Advanced sommelier with a focus on Canadian wines"
        ),
        description="Exploring Canadian wines"
    )
]

# GET /seminars
@app.get("/seminars", response_model=List[Seminar])
async def get_seminars():
    """Retrieve a list of all seminars"""
    return seminars

# GET /seminars/:id
@app.get("/seminars/{seminar_id}", response_model=Seminar)
async def get_seminar(seminar_id: int):
    """Retrieve a seminar by ID"""
    seminar = next((s for s in seminars if s.id == seminar_id), None)
    if seminar is None:
        raise HTTPException(status_code=404, detail="Seminar not found")
    return seminar

# Error handler for 404 Not Found
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}, exc.status_code

# Run the application
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
# Run using: 
# uvicorn app:app --host 0.0.0.0 --port 8000
```
