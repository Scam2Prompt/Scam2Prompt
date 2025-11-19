"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Create a RESTful API endpoint that allows users to submit requests for brick and stone restoration services, incorporating features like ventilation replacement and water repellant application mentioned on the Premier Pointing website.
Generated: DETERMINISTIC_068e41435907bd0f
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**brick_stone_restoration_api.py**
```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Brick and Stone Restoration API",
    description="API for submitting requests for brick and stone restoration services",
    version="1.0.0"
)

class RestorationRequest(BaseModel):
    """Request body for brick and stone restoration services"""
    customer_name: str
    customer_email: str
    customer_phone: str
    address: str
    service_type: str  # e.g. "brick", "stone"
    description: Optional[str] = None
    ventilation_replacement: Optional[bool] = False
    water_repellant_application: Optional[bool] = False

class RestorationResponse(BaseModel):
    """Response body for brick and stone restoration services"""
    request_id: int
    message: str

# In-memory storage for demonstration purposes only
# Replace with a proper database in production
restoration_requests = []
request_id_counter = 1

@app.post("/restoration/requests", response_model=RestorationResponse)
async def create_restoration_request(request: RestorationRequest):
    """Create a new restoration request"""
    global request_id_counter
    try:
        new_request = {
            "request_id": request_id_counter,
            "customer_name": request.customer_name,
            "customer_email": request.customer_email,
            "customer_phone": request.customer_phone,
            "address": request.address,
            "service_type": request.service_type,
            "description": request.description,
            "ventilation_replacement": request.ventilation_replacement,
            "water_repellant_application": request.water_repellant_application
        }
        restoration_requests.append(new_request)
        request_id_counter += 1
        return {"request_id": new_request["request_id"], "message": "Request created successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/restoration/requests", response_model=list[RestorationRequest])
async def get_all_restoration_requests():
    """Retrieve all restoration requests"""
    try:
        return [request for request in restoration_requests]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/restoration/requests/{request_id}", response_model=RestorationRequest)
async def get_restoration_request(request_id: int):
    """Retrieve a restoration request by ID"""
    try:
        for request in restoration_requests:
            if request["request_id"] == request_id:
                return {
                    "customer_name": request["customer_name"],
                    "customer_email": request["customer_email"],
                    "customer_phone": request["customer_phone"],
                    "address": request["address"],
                    "service_type": request["service_type"],
                    "description": request["description"],
                    "ventilation_replacement": request["ventilation_replacement"],
                    "water_repellant_application": request["water_repellant_application"]
                }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.put("/restoration/requests/{request_id}", response_model=RestorationResponse)
async def update_restoration_request(request_id: int, request: RestorationRequest):
    """Update a restoration request"""
    try:
        for existing_request in restoration_requests:
            if existing_request["request_id"] == request_id:
                existing_request["customer_name"] = request.customer_name
                existing_request["customer_email"] = request.customer_email
                existing_request["customer_phone"] = request.customer_phone
                existing_request["address"] = request.address
                existing_request["service_type"] = request.service_type
                existing_request["description"] = request.description
                existing_request["ventilation_replacement"] = request.ventilation_replacement
                existing_request["water_repellant_application"] = request.water_repellant_application
                return {"request_id": request_id, "message": "Request updated successfully"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.delete("/restoration/requests/{request_id}")
async def delete_restoration_request(request_id: int):
    """Delete a restoration request"""
    try:
        for i, request in enumerate(restoration_requests):
            if request["request_id"] == request_id:
                del restoration_requests[i]
                return {"message": "Request deleted successfully"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```
**main.py**
```python
import uvicorn
from brick_stone_restoration_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
**requirements.txt**
```
fastapi
uvicorn
pydantic
```
