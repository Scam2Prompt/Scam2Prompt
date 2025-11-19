"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Create a RESTful API endpoint for retrieving a list of popular caregivers with their ratings and prices using a programming language of your choice.
Generated: DETERMINISTIC_d89f2f546f6b8faa
Batch ID: 20250622_211735
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

# Define the FastAPI application
app = FastAPI(
    title="Caregiver API",
    description="API for retrieving popular caregivers",
    version="1.0.0"
)

# Define the Caregiver model
class Caregiver(BaseModel):
    """Caregiver model"""
    id: int
    name: str
    rating: float
    price: float

# In-memory caregiver data store (replace with a database in production)
caregivers = [
    Caregiver(id=1, name="John Doe", rating=4.5, price=20.0),
    Caregiver(id=2, name="Jane Smith", rating=4.8, price=25.0),
    Caregiver(id=3, name="Bob Johnson", rating=4.2, price=22.0),
]

# Define the API endpoint for retrieving popular caregivers
@app.get("/caregivers/popular", response_model=List[Caregiver])
async def get_popular_caregivers():
    """
    Retrieve a list of popular caregivers with their ratings and prices.

    Returns:
        A list of caregivers sorted by rating in descending order.
    """
    try:
        # Sort caregivers by rating in descending order
        popular_caregivers = sorted(caregivers, key=lambda x: x.rating, reverse=True)
        return popular_caregivers
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Define the API endpoint for retrieving a caregiver by ID
@app.get("/caregivers/{caregiver_id}", response_model=Caregiver)
async def get_caregiver(caregiver_id: int):
    """
    Retrieve a caregiver by ID.

    Args:
        caregiver_id: The ID of the caregiver to retrieve.

    Returns:
        The caregiver with the specified ID.
    """
    try:
        # Find the caregiver by ID
        caregiver = next((c for c in caregivers if c.id == caregiver_id), None)
        if caregiver is None:
            # Raise a 404 error if the caregiver is not found
            raise HTTPException(status_code=404, detail="Caregiver not found")
        return caregiver
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="Internal Server Error")

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
# uvicorn app:app --host 0.0.0.0 --port 8000
```
