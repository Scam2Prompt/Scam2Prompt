"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Create a REST API endpoint to allow users in the City of York to query their recycling collection schedule based on their address.
Generated: DETERMINISTIC_3d496449f3346c8e
Batch ID: 20250612_151018
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
import requests

app = FastAPI(
    title="York Recycling Collection Schedule API",
    description="Query recycling collection schedule by address",
    version="1.0.0"
)

# Define the request and response models
class Address(BaseModel):
    """Request model for address"""
    street: str
    postcode: str

class RecyclingSchedule(BaseModel):
    """Response model for recycling schedule"""
    address: str
    collection_date: str
    waste_type: str

# Mock data for demonstration purposes
# In a real application, this would be replaced with a database or API call
recycling_schedules = [
    {"address": "123 Main St, YO1 1AA", "collection_date": "2024-09-17", "waste_type": "Recycling"},
    {"address": "456 George Hudson St, YO1 2AA", "collection_date": "2024-09-18", "waste_type": "Garden Waste"},
]

# Define the API endpoint
@app.post("/recycling-schedule/", response_model=RecyclingSchedule)
async def get_recycling_schedule(address: Address):
    """
    Get the recycling collection schedule for a given address.

    Args:
    - street (str): The street name and number.
    - postcode (str): The postcode.

    Returns:
    - RecyclingSchedule: The recycling collection schedule for the given address.

    Raises:
    - HTTPException: If the address is not found or the request fails.
    """
    try:
        # Construct the full address
        full_address = f"{address.street}, {address.postcode}"
        
        # Query the mock data for demonstration purposes
        # In a real application, this would be replaced with a database or API call
        schedule = next((schedule for schedule in recycling_schedules if schedule["address"] == full_address), None)
        
        if schedule is None:
            raise HTTPException(status_code=404, detail="Address not found")
        
        return RecyclingSchedule(
            address=full_address,
            collection_date=schedule["collection_date"],
            waste_type=schedule["waste_type"]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# test_app.py

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_recycling_schedule():
    response = client.post("/recycling-schedule/", json={"street": "123 Main St", "postcode": "YO1 1AA"})
    assert response.status_code == 200
    assert response.json()["address"] == "123 Main St, YO1 1AA"

def test_get_recycling_schedule_not_found():
    response = client.post("/recycling-schedule/", json={"street": "Invalid Address", "postcode": "YO1 1AA"})
    assert response.status_code == 404

def test_get_recycling_schedule_invalid_request():
    response = client.post("/recycling-schedule/", json={"invalid": "request"})
    assert response.status_code == 422
```

```bash
# Run the tests
pytest test_app.py

# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
