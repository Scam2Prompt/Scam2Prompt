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
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from enum import Enum
from datetime import datetime

app = FastAPI(
    title="Alphamor Domestic Services API",
    description="API for managing garden and pool maintenance service requests",
    version="1.0.0"
)

# Define an Enum for service types
class ServiceType(str, Enum):
    garden_maintenance = "garden_maintenance"
    pool_maintenance = "pool_maintenance"

# Define a Pydantic model for service requests
class ServiceRequest(BaseModel):
    id: int
    customer_name: str
    service_type: ServiceType
    description: str
    scheduled_date: datetime
    completed: bool = False

# In-memory database for demonstration purposes
service_requests: List[ServiceRequest] = [
    ServiceRequest(
        id=1,
        customer_name="John Doe",
        service_type=ServiceType.garden_maintenance,
        description="Lawn mowing and pruning",
        scheduled_date=datetime(2024, 9, 20),
        completed=False
    ),
    ServiceRequest(
        id=2,
        customer_name="Jane Smith",
        service_type=ServiceType.pool_maintenance,
        description="Pool cleaning and chemical check",
        scheduled_date=datetime(2024, 9, 22),
        completed=False
    )
]

# GET endpoint to retrieve all service requests
@app.get("/service-requests/", response_model=List[ServiceRequest])
async def get_service_requests():
    return service_requests

# GET endpoint to retrieve a service request by ID
@app.get("/service-requests/{request_id}", response_model=ServiceRequest)
async def get_service_request(request_id: int):
    for request in service_requests:
        if request.id == request_id:
            return request
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service request not found")

# POST endpoint to create a new service request
@app.post("/service-requests/", response_model=ServiceRequest, status_code=status.HTTP_201_CREATED)
async def create_service_request(request: ServiceRequest):
    service_requests.append(request)
    return request

# PUT endpoint to update an existing service request
@app.put("/service-requests/{request_id}", response_model=ServiceRequest)
async def update_service_request(request_id: int, request: ServiceRequest):
    for i, existing_request in enumerate(service_requests):
        if existing_request.id == request_id:
            service_requests[i] = request
            return request
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service request not found")

# PATCH endpoint to mark a service request as completed
@app.patch("/service-requests/{request_id}", response_model=ServiceRequest)
async def complete_service_request(request_id: int):
    for i, request in enumerate(service_requests):
        if request.id == request_id:
            service_requests[i].completed = True
            return service_requests[i]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service request not found")

# DELETE endpoint to delete a service request
@app.delete("/service-requests/{request_id}")
async def delete_service_request(request_id: int):
    for i, request in enumerate(service_requests):
        if request.id == request_id:
            del service_requests[i]
            return {"message": "Service request deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service request not found")
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
