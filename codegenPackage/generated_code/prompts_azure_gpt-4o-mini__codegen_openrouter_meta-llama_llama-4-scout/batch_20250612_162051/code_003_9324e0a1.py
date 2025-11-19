"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: Develop a REST API endpoint that allows users to submit requests for roofing services, including fields for type of service (repair, installation, etc.) and location in Toulouse.
Generated: DETERMINISTIC_9324e0a1c3dc31a1
Batch ID: 20250612_162051
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
    title="Roofing Services API",
    description="API for submitting requests for roofing services in Toulouse",
    version="1.0.0"
)

class RoofingRequest(BaseModel):
    """Request model for roofing services"""
    service_type: str  # repair, installation, etc.
    location: str  # address in Toulouse
    description: Optional[str] = None  # additional details

    class Config:
        schema_extra = {
            "example": {
                "service_type": "repair",
                "location": "123 Rue de la République, Toulouse",
                "description": "Leak in the roof"
            }
        }

# In-memory storage for demonstration purposes
# Replace with a proper database in production
roofing_requests = []

@app.post("/requests/")
async def create_roofing_request(request: RoofingRequest):
    """Create a new roofing request"""
    try:
        # Validate service type (for demonstration purposes)
        valid_service_types = ["repair", "installation", "maintenance"]
        if request.service_type not in valid_service_types:
            raise HTTPException(status_code=400, detail="Invalid service type")

        # Store the request
        roofing_requests.append(request.dict())
        return {"message": "Request created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/requests/")
async def get_roofing_requests():
    """Retrieve all roofing requests"""
    return roofing_requests

@app.get("/requests/{request_id}")
async def get_roofing_request(request_id: int):
    """Retrieve a roofing request by ID"""
    try:
        request = roofing_requests[request_id]
        return request
    except IndexError:
        raise HTTPException(status_code=404, detail="Request not found")

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
