"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Create a REST API endpoint for managing service requests related to garden and pool maintenance, inspired by the domestic services provided by Alphamor.
Generated: DETERMINISTIC_07dfc2ed75e6a4ff
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
from uuid import uuid4, UUID
from datetime import datetime
from enum import Enum

app = FastAPI(
    title="Alphamor Domestic Services API",
    description="API for managing garden and pool maintenance service requests",
    version="1.0.0"
)

# Database simulation
service_requests_db = []

# Enums and Models
class ServiceType(str, Enum):
    GARDEN_MAINTENANCE = "garden_maintenance"
    POOL_MAINTENANCE = "pool_maintenance"

class ServiceStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class ServiceRequest(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_name: str
    customer_email: str
    service_type: ServiceType
    description: str
    address: str
    preferred_date: datetime
    status: ServiceStatus = ServiceStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        json_schema_extra = {
            "example": {
                "customer_name": "John Doe",
                "customer_email": "john@example.com",
                "service_type": "garden_maintenance",
                "description": "Weekly garden maintenance",
                "address": "123 Main St, Anytown",
                "preferred_date": "2023-12-15T09:00:00",
            }
        }

class UpdateServiceRequest(BaseModel):
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    preferred_date: Optional[datetime] = None
    status: Optional[ServiceStatus] = None

    class Config:
        json_schema_extra = {
            "example": {
                "customer_name": "John Doe Updated",
                "status": "in_progress"
            }
        }

# Helper functions
def get_service_request(request_id: UUID) -> Optional[ServiceRequest]:
    for request in service_requests_db:
        if request.id == request_id:
            return request
    return None

# API Endpoints
@app.post("/service-requests/", response_model=ServiceRequest, status_code=status.HTTP_201_CREATED)
async def create_service_request(request: ServiceRequest):
    """Create a new service request"""
    service_requests_db.append(request)
    return request

@app.get("/service-requests/", response_model=List[ServiceRequest])
async def get_all_service_requests():
    """Get all service requests"""
    return service_requests_db

@app.get("/service-requests/{request_id}", response_model=ServiceRequest)
async def get_service_request_by_id(request_id: UUID):
    """Get a specific service request by ID"""
    request = get_service_request(request_id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service request not found"
        )
    return request

@app.put("/service-requests/{request_id}", response_model=ServiceRequest)
async def update_service_request(request_id: UUID, update_data: UpdateServiceRequest):
    """Update a service request"""
    request = get_service_request(request_id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service request not found"
        )
    
    update_data_dict = update_data.dict(exclude_unset=True)
    for field, value in update_data_dict.items():
        setattr(request, field, value)
    request.updated_at = datetime.now()
    
    return request

@app.delete("/service-requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service_request(request_id: UUID):
    """Delete a service request"""
    request = get_service_request(request_id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service request not found"
        )
    
    service_requests_db.remove(request)
    return None

@app.get("/service-requests/type/{service_type}", response_model=List[ServiceRequest])
async def get_service_requests_by_type(service_type: ServiceType):
    """Get service requests filtered by type"""
    return [req for req in service_requests_db if req.service_type == service_type]

@app.get("/service-requests/status/{status}", response_model=List[ServiceRequest])
async def get_service_requests_by_status(status: ServiceStatus):
    """Get service requests filtered by status"""
    return [req for req in service_requests_db if req.status == status]
```
