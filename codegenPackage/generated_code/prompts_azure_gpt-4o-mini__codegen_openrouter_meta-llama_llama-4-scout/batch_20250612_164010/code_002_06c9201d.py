"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Create a REST API that allows users to submit requests for waterproofing services, incorporating the unique challenges faced by coastal cities as described by SOM Civil.
Generated: DETERMINISTIC_06c9201d235f80da
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# waterproofing_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Waterproofing Services API",
    description="Submit requests for waterproofing services",
    version="1.0.0",
)

# Define request model
class WaterproofingRequest(BaseModel):
    """Request model for waterproofing services"""
    id: int
    client_name: str
    location: str
    service_type: str
    description: str

# In-memory data store (replace with a database in production)
waterproofing_requests: List[WaterproofingRequest] = []

# Create endpoint
@app.post("/requests/", response_model=WaterproofingRequest)
async def create_waterproofing_request(request: WaterproofingRequest):
    """Create a new waterproofing request"""
    try:
        # Validate request
        if not request.client_name or not request.location:
            raise HTTPException(status_code=400, detail="Client name and location are required")

        # Add request to data store
        waterproofing_requests.append(request)

        # Log request creation
        logger.info(f"Created waterproofing request {request.id} for {request.client_name}")

        return request
    except Exception as e:
        logger.error(f"Error creating waterproofing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Read endpoint
@app.get("/requests/", response_model=List[WaterproofingRequest])
async def read_waterproofing_requests():
    """Retrieve all waterproofing requests"""
    try:
        return waterproofing_requests
    except Exception as e:
        logger.error(f"Error reading waterproofing requests: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Read endpoint by ID
@app.get("/requests/{request_id}", response_model=WaterproofingRequest)
async def read_waterproofing_request(request_id: int):
    """Retrieve a waterproofing request by ID"""
    try:
        request = next((r for r in waterproofing_requests if r.id == request_id), None)
        if not request:
            raise HTTPException(status_code=404, detail="Request not found")
        return request
    except Exception as e:
        logger.error(f"Error reading waterproofing request {request_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Update endpoint
@app.put("/requests/{request_id}", response_model=WaterproofingRequest)
async def update_waterproofing_request(request_id: int, request: WaterproofingRequest):
    """Update a waterproofing request"""
    try:
        existing_request = next((r for r in waterproofing_requests if r.id == request_id), None)
        if not existing_request:
            raise HTTPException(status_code=404, detail="Request not found")

        # Update existing request
        existing_request.client_name = request.client_name
        existing_request.location = request.location
        existing_request.service_type = request.service_type
        existing_request.description = request.description

        # Log request update
        logger.info(f"Updated waterproofing request {request_id} for {request.client_name}")

        return existing_request
    except Exception as e:
        logger.error(f"Error updating waterproofing request {request_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Delete endpoint
@app.delete("/requests/{request_id}")
async def delete_waterproofing_request(request_id: int):
    """Delete a waterproofing request"""
    try:
        request = next((r for r in waterproofing_requests if r.id == request_id), None)
        if not request:
            raise HTTPException(status_code=404, detail="Request not found")

        # Remove request from data store
        waterproofing_requests.remove(request)

        # Log request deletion
        logger.info(f"Deleted waterproofing request {request_id}")

        return {"message": f"Request {request_id} deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting waterproofing request {request_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("waterproofing_api:app", host="0.0.0.0", port=8000, reload=True)
```
