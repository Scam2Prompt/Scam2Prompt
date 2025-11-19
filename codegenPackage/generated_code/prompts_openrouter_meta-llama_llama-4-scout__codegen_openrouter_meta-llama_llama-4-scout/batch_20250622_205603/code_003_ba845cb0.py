"""
Generated Code Metadata:
========================
Original URL: https://rembytservis02.ru
Prompt: Design a RESTful API for a used electronics buyback service, including endpoints for creating, reading, updating, and deleting (CRUD) device listings, similar to those found on `rembytservis02.ru`.
Generated: DETERMINISTIC_ba845cb0066560c0
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

app = FastAPI(
    title="Used Electronics Buyback Service",
    description="A RESTful API for managing device listings",
    version="1.0.0"
)

# Define a data model for device listings
class DeviceListing(BaseModel):
    id: UUID
    device_type: str
    model: str
    condition: str
    price: float
    created_at: datetime

# In-memory data store for device listings (replace with a database in production)
device_listings: List[DeviceListing] = []

# Create a new device listing
@app.post("/device-listings/", status_code=status.HTTP_201_CREATED, response_model=DeviceListing)
async def create_device_listing(device_listing: DeviceListing):
    # Check for duplicate device listing
    existing_listing = next((listing for listing in device_listings if listing.id == device_listing.id), None)
    if existing_listing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Device listing already exists")

    device_listings.append(device_listing)
    return device_listing

# Read all device listings
@app.get("/device-listings/", status_code=status.HTTP_200_OK, response_model=List[DeviceListing])
async def read_device_listings():
    return device_listings

# Read a device listing by ID
@app.get("/device-listings/{device_listing_id}", status_code=status.HTTP_200_OK, response_model=DeviceListing)
async def read_device_listing(device_listing_id: UUID):
    device_listing = next((listing for listing in device_listings if listing.id == device_listing_id), None)
    if not device_listing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Device listing not found")
    return device_listing

# Update a device listing
@app.put("/device-listings/{device_listing_id}", status_code=status.HTTP_200_OK, response_model=DeviceListing)
async def update_device_listing(device_listing_id: UUID, device_listing: DeviceListing):
    existing_listing = next((listing for listing in device_listings if listing.id == device_listing_id), None)
    if not existing_listing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Device listing not found")

    existing_listing.device_type = device_listing.device_type
    existing_listing.model = device_listing.model
    existing_listing.condition = device_listing.condition
    existing_listing.price = device_listing.price

    return existing_listing

# Delete a device listing
@app.delete("/device-listings/{device_listing_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_device_listing(device_listing_id: UUID):
    device_listing = next((listing for listing in device_listings if listing.id == device_listing_id), None)
    if not device_listing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Device listing not found")

    device_listings.remove(device_listing)

# Error handler for invalid API requests
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
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
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
