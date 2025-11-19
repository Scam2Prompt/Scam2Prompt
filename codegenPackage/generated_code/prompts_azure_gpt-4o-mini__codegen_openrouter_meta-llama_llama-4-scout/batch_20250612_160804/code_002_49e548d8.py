"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Create an API endpoint for a car repair service that allows users to request services such as engine repair, AC repair, and body shop services, inspired by the features of Mechanics.ae.
Generated: DETERMINISTIC_49e548d88882bbbc
Batch ID: 20250612_160804
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
from enum import Enum

app = FastAPI(
    title="Car Repair Service API",
    description="API for car repair services",
    version="1.0.0"
)

# Define an Enum for service types
class ServiceType(str, Enum):
    engine_repair = "engine_repair"
    ac_repair = "ac_repair"
    body_shop = "body_shop"

# Define a Pydantic model for ServiceRequest
class ServiceRequest(BaseModel):
    customer_name: str
    vehicle_make: str
    vehicle_model: str
    service_type: ServiceType
    description: str

# Define a Pydantic model for ServiceResponse
class ServiceResponse(BaseModel):
    request_id: int
    customer_name: str
    vehicle_make: str
    vehicle_model: str
    service_type: ServiceType
    description: str
    status: str

# In-memory database for demonstration purposes
services: List[ServiceResponse] = []
request_id_counter = 1

# API endpoint to request a service
@app.post("/services/", response_model=ServiceResponse)
async def create_service(request: ServiceRequest):
    global request_id_counter
    try:
        new_service = ServiceResponse(
            request_id=request_id_counter,
            customer_name=request.customer_name,
            vehicle_make=request.vehicle_make,
            vehicle_model=request.vehicle_model,
            service_type=request.service_type,
            description=request.description,
            status="pending"
        )
        services.append(new_service)
        request_id_counter += 1
        return new_service
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all services
@app.get("/services/", response_model=List[ServiceResponse])
async def get_services():
    try:
        return services
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get a service by ID
@app.get("/services/{service_id}", response_model=ServiceResponse)
async def get_service(service_id: int):
    try:
        for service in services:
            if service.request_id == service_id:
                return service
        raise HTTPException(status_code=404, detail="Service not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to update a service status
@app.put("/services/{service_id}", response_model=ServiceResponse)
async def update_service(service_id: int, status: str):
    try:
        for service in services:
            if service.request_id == service_id:
                service.status = status
                return service
        raise HTTPException(status_code=404, detail="Service not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to delete a service
@app.delete("/services/{service_id}")
async def delete_service(service_id: int):
    try:
        for service in services:
            if service.request_id == service_id:
                services.remove(service)
                return {"message": "Service deleted successfully"}
        raise HTTPException(status_code=404, detail="Service not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
