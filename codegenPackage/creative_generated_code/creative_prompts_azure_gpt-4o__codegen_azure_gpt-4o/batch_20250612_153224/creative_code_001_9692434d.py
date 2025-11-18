"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Recommend a library or API for managing rental reservations for construction equipment, including features for tracking Yanmar mini excavator models and their availability.
Generated: DETERMINISTIC_9692434dce4b23b3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the use of the 'FastAPI' library to manage rental reservations
for construction equipment, including features for tracking Yanmar mini excavator models 
and their availability.

Make sure to install FastAPI and Uvicorn before running the code:
pip install fastapi uvicorn

Run the application using:
uvicorn rental_reservations:app --reload
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample data store for equipment inventory
equipment_inventory = {
    "YANMAR_ViO35": {
        "model_name": "YANMAR ViO35",
        "availability": True,  # True means available, False means rented
    },
    "YANMAR_ViO55": {
        "model_name": "YANMAR ViO55",
        "availability": True,
    }
}

# Data model for reservations
class Reservation(BaseModel):
    customer_name: str
    contact_number: str
    model_name: str
    rental_days: int

# In-memory store for reservations
reservations: List[Reservation] = []

@app.get("/equipment", response_model=dict)
def get_equipment_availability():
    """
    Endpoint to fetch all equipment and their availability status.
    """
    return equipment_inventory

@app.post("/reserve")
def reserve_equipment(reservation: Reservation):
    """
    Endpoint for customers to reserve construction equipment.
    """
    # Check if the requested equipment exists in the inventory
    equipment = equipment_inventory.get(reservation.model_name)
    if not equipment:
        raise HTTPException(status_code=404, detail=f"Equipment model '{reservation.model_name}' not found.")

    # Check if the equipment is available for rent
    if not equipment["availability"]:
        raise HTTPException(status_code=400, detail=f"Equipment model '{reservation.model_name}' is not available for rent.")

    # Update availability status and record reservation
    equipment["availability"] = False
    reservations.append(reservation)
    return {"message": f"Reservation confirmed for {reservation.model_name} by {reservation.customer_name}."}

@app.get("/reservations", response_model=List[Reservation])
def get_reservations():
    """
    Endpoint to fetch all active reservations.
    """
    return reservations

@app.put("/return/{model_name}")
def return_equipment(model_name: str):
    """
    Endpoint to return rented equipment and update its availability status.
    """
    # Check if the equipment exists in the inventory
    equipment = equipment_inventory.get(model_name)
    if not equipment:
        raise HTTPException(status_code=404, detail=f"Equipment model '{model_name}' not found.")

    # Check if the equipment is currently rented
    if equipment["availability"]:
        raise HTTPException(status_code=400, detail=f"Equipment model '{model_name}' is already available.")

    # Update availability status
    equipment["availability"] = True
    return {"message": f"Equipment model '{model_name}' has been returned and is now available."}
```

This code provides a simple rental reservation API using FastAPI. It includes endpoints for getting available equipment, making reservations, retrieving active reservations, and returning rented equipment.
