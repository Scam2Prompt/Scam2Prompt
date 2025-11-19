"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Create an API endpoint for managing plumbing service requests, including features like leak detection and urgent repairs, based on the offerings of ERA Engineering.
Generated: DETERMINISTIC_03db7fb54c57ae6f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid
from enum import Enum

app = FastAPI(
    title="ERA Engineering Plumbing Service API",
    description="API for managing plumbing service requests including leak detection and urgent repairs",
    version="1.0.0"
)

# Database simulation (in production, use a real database)
service_requests_db = []

class ServiceType(str, Enum):
    LEAK_DETECTION = "leak_detection"
    URGENT_REPAIR = "urgent_repair"
    GENERAL_MAINTENANCE = "general_maintenance"
    PIPE_REPLACEMENT = "pipe_replacement"
    DRAIN_CLEANING = "drain_cleaning"

class ServiceStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class ServiceRequest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = None
    address: str
    service_type: ServiceType
    description: str
    is_urgent: bool = False
    status: ServiceStatus = ServiceStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    scheduled_time: Optional[datetime] = None
    assigned_technician: Optional[str] = None

class ServiceRequestCreate(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = None
    address: str
    service_type: ServiceType
    description: str
    is_urgent: bool = False
    scheduled_time: Optional[datetime] = None

class ServiceRequestUpdate(BaseModel):
    status: Optional[ServiceStatus] = None
    assigned_technician: Optional[str] = None
    scheduled_time: Optional[datetime] = None

@app.post("/service-requests/", response_model=ServiceRequest, status_code=status.HTTP_201_CREATED)
async def create_service_request(request: ServiceRequestCreate):
    """
    Create a new plumbing service request.
    """
    new_request = ServiceRequest(**request.dict())
    service_requests_db.append(new_request)
    return new_request

@app.get("/service-requests/", response_model=List[ServiceRequest])
async def get_service_requests(status: Optional[ServiceStatus] = None, urgent: Optional[bool] = None):
    """
    Get all service requests, optionally filtered by status or urgency.
    """
    result = service_requests_db
    
    if status is not None:
        result = [req for req in result if req.status == status]
    
    if urgent is not None:
        result = [req for req in result if req.is_urgent == urgent]
    
    return result

@app.get("/service-requests/{request_id}", response_model=ServiceRequest)
async def get_service_request(request_id: str):
    """
    Get a specific service request by ID.
    """
    for request in service_requests_db:
        if request.id == request_id:
            return request
    raise HTTPException(status_code=404, detail="Service request not found")

@app.put("/service-requests/{request_id}", response_model=ServiceRequest)
async def update_service_request(request_id: str, update: ServiceRequestUpdate):
    """
    Update a service request (status, technician assignment, or schedule).
    """
    for request in service_requests_db:
        if request.id == request_id:
            update_data = update.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(request, field, value)
            return request
    raise HTTPException(status_code=404, detail="Service request not found")

@app.delete("/service-requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service_request(request_id: str):
    """
    Delete a service request.
    """
    for i, request in enumerate(service_requests_db):
        if request.id == request_id:
            service_requests_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Service request not found")

@app.get("/service-types/", response_model=List[str])
async def get_service_types():
    """
    Get all available service types.
    """
    return [service_type.value for service_type in ServiceType]

@app.get("/urgent-requests/", response_model=List[ServiceRequest])
async def get_urgent_requests():
    """
    Get all urgent service requests.
    """
    return [req for req in service_requests_db if req.is_urgent and req.status != ServiceStatus.COMPLETED]
```
