"""
Generated Code Metadata:
========================
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Create a RESTful API endpoint to request and manage towing services, inspired by the features and structure of Efem Oto Kurtarma's services in Ankara.
Generated: DETERMINISTIC_16140eeb04cc04ee
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import uuid
from enum import Enum

app = FastAPI(
    title="Efem Oto Kurtarma API",
    description="RESTful API for managing towing services in Ankara",
    version="1.0.0"
)

# Database simulation
fake_db = {}

# Models
class ServiceType(str, Enum):
    standard_towing = "standard_towing"
    flatbed_towing = "flatbed_towing"
    motorcycle_towing = "motorcycle_towing"
    heavy_duty_towing = "heavy_duty_towing"

class VehicleType(str, Enum):
    car = "car"
    motorcycle = "motorcycle"
    truck = "truck"
    bus = "bus"

class TowingRequest(BaseModel):
    customer_name: str
    customer_phone: str
    vehicle_type: VehicleType
    service_type: ServiceType
    location: str
    destination: Optional[str] = None
    license_plate: Optional[str] = None
    notes: Optional[str] = None

class TowingRequestResponse(TowingRequest):
    request_id: str
    status: str
    created_at: datetime
    updated_at: datetime

class StatusUpdate(BaseModel):
    status: str
    notes: Optional[str] = None

# Helper functions
def generate_request_id():
    return str(uuid.uuid4())

def get_current_time():
    return datetime.now()

# Endpoints
@app.post("/requests/", response_model=TowingRequestResponse, status_code=status.HTTP_201_CREATED)
async def create_towing_request(request: TowingRequest):
    """
    Create a new towing service request.
    """
    request_id = generate_request_id()
    current_time = get_current_time()
    
    new_request = {
        **request.dict(),
        "request_id": request_id,
        "status": "pending",
        "created_at": current_time,
        "updated_at": current_time
    }
    
    fake_db[request_id] = new_request
    return new_request

@app.get("/requests/", response_model=List[TowingRequestResponse])
async def list_towing_requests(status_filter: Optional[str] = None):
    """
    List all towing service requests, optionally filtered by status.
    """
    requests = list(fake_db.values())
    if status_filter:
        requests = [req for req in requests if req["status"].lower() == status_filter.lower()]
    return requests

@app.get("/requests/{request_id}", response_model=TowingRequestResponse)
async def get_towing_request(request_id: str):
    """
    Get details of a specific towing service request.
    """
    if request_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found"
        )
    return fake_db[request_id]

@app.patch("/requests/{request_id}/status", response_model=TowingRequestResponse)
async def update_request_status(request_id: str, update: StatusUpdate):
    """
    Update the status of a towing service request.
    """
    if request_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found"
        )
    
    request = fake_db[request_id]
    request["status"] = update.status
    if update.notes:
        request["notes"] = update.notes
    request["updated_at"] = get_current_time()
    
    return request

@app.delete("/requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_towing_request(request_id: str):
    """
    Delete a towing service request.
    """
    if request_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found"
        )
    del fake_db[request_id]
    return None

@app.get("/service-types", response_model=List[str])
async def get_service_types():
    """
    Get available towing service types.
    """
    return [service.value for service in ServiceType]

@app.get("/vehicle-types", response_model=List[str])
async def get_vehicle_types():
    """
    Get supported vehicle types.
    """
    return [vehicle.value for vehicle in VehicleType]
```
