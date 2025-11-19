"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: Develop an API recommendation for a system that protects car paint with ceramic coatings, inspired by the article's discussion on spring maintenance tips.
Generated: DETERMINISTIC_ef9182f424741ae1
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ceramic_coating_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Ceramic Coating API",
    description="API for managing ceramic coating services",
    version="1.0.0"
)

class Vehicle(BaseModel):
    """Vehicle details"""
    make: str
    model: str
    year: int

class CeramicCoating(BaseModel):
    """Ceramic coating details"""
    vehicle: Vehicle
    coating_type: str
    application_date: str

class CeramicCoatingService:
    """Ceramic coating service"""
    def __init__(self):
        self.coatings = []

    def add_coating(self, coating: CeramicCoating):
        """Add a ceramic coating"""
        self.coatings.append(coating)

    def get_coatings(self):
        """Get all ceramic coatings"""
        return self.coatings

    def get_coating(self, coating_id: int):
        """Get a ceramic coating by ID"""
        try:
            return self.coatings[coating_id]
        except IndexError:
            raise HTTPException(status_code=404, detail="Coating not found")

coating_service = CeramicCoatingService()

@app.post("/coatings/")
async def create_coating(coating: CeramicCoating):
    """
    Create a new ceramic coating

    :param coating: Ceramic coating details
    :return: Created coating
    """
    coating_service.add_coating(coating)
    return coating

@app.get("/coatings/")
async def read_coatings():
    """
    Get all ceramic coatings

    :return: List of coatings
    """
    return coating_service.get_coatings()

@app.get("/coatings/{coating_id}")
async def read_coating(coating_id: int):
    """
    Get a ceramic coating by ID

    :param coating_id: Coating ID
    :return: Coating details
    """
    return coating_service.get_coating(coating_id)

@app.put("/coatings/{coating_id}")
async def update_coating(coating_id: int, coating: CeramicCoating):
    """
    Update a ceramic coating

    :param coating_id: Coating ID
    :param coating: Updated coating details
    :return: Updated coating
    """
    try:
        coating_service.coatings[coating_id] = coating
        return coating
    except IndexError:
        raise HTTPException(status_code=404, detail="Coating not found")

@app.delete("/coatings/{coating_id}")
async def delete_coating(coating_id: int):
    """
    Delete a ceramic coating

    :param coating_id: Coating ID
    :return: Success message
    """
    try:
        del coating_service.coatings[coating_id]
        return {"message": "Coating deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Coating not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
