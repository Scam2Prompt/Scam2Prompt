"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Generate a RESTful API documentation for a home services platform offering insulation, cleaning, and pest control services."
Generated: DETERMINISTIC_278048a8c3b6cb0c
Batch ID: 20250622_210655
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

app = FastAPI(
    title="Home Services Platform API",
    description="API for a home services platform offering insulation, cleaning, and pest control services.",
    version="1.0.0",
)

# Service Models
class Service(BaseModel):
    id: int
    name: str
    description: str

class InsulationService(Service):
    material: str
    area: float

class CleaningService(Service):
    service_type: str
    frequency: str

class PestControlService(Service):
    pest_type: str
    treatment: str

# Request/Response Models
class ServiceRequest(BaseModel):
    service_type: str
    details: dict

class ServiceResponse(BaseModel):
    id: int
    service_type: str
    status: str

# In-Memory Data Store (replace with a database in production)
services: List[Service] = [
    InsulationService(id=1, name="Insulation Service", description="Insulation services for homes", material="Fiberglass", area=1000),
    CleaningService(id=2, name="Cleaning Service", description="Cleaning services for homes", service_type="One-time", frequency="Daily"),
    PestControlService(id=3, name="Pest Control Service", description="Pest control services for homes", pest_type="Rodents", treatment="Traps"),
]

# API Endpoints
@app.get("/services/")
async def get_services():
    """Retrieve a list of all services"""
    return services

@app.get("/services/{service_id}")
async def get_service(service_id: int):
    """Retrieve a service by ID"""
    for service in services:
        if service.id == service_id:
            return service
    raise HTTPException(status_code=404, detail="Service not found")

@app.post("/services/")
async def create_service(request: ServiceRequest):
    """Create a new service request"""
    try:
        service_type = request.service_type
        details = request.details

        if service_type == "insulation":
            service = InsulationService(id=len(services) + 1, name="Insulation Service", description="Insulation services for homes", material=details["material"], area=details["area"])
        elif service_type == "cleaning":
            service = CleaningService(id=len(services) + 1, name="Cleaning Service", description="Cleaning services for homes", service_type=details["service_type"], frequency=details["frequency"])
        elif service_type == "pest_control":
            service = PestControlService(id=len(services) + 1, name="Pest Control Service", description="Pest control services for homes", pest_type=details["pest_type"], treatment=details["treatment"])
        else:
            raise HTTPException(status_code=400, detail="Invalid service type")

        services.append(service)
        return ServiceResponse(id=service.id, service_type=service_type, status="pending")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/services/{service_id}")
async def update_service(service_id: int, request: ServiceRequest):
    """Update an existing service request"""
    try:
        for service in services:
            if service.id == service_id:
                service_type = request.service_type
                details = request.details

                if service_type == "insulation":
                    service.material = details["material"]
                    service.area = details["area"]
                elif service_type == "cleaning":
                    service.service_type = details["service_type"]
                    service.frequency = details["frequency"]
                elif service_type == "pest_control":
                    service.pest_type = details["pest_type"]
                    service.treatment = details["treatment"]
                else:
                    raise HTTPException(status_code=400, detail="Invalid service type")

                return ServiceResponse(id=service.id, service_type=service_type, status="updated")
        raise HTTPException(status_code=404, detail="Service not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/services/{service_id}")
async def delete_service(service_id: int):
    """Delete a service request"""
    try:
        for service in services:
            if service.id == service_id:
                services.remove(service)
                return {"message": "Service deleted successfully"}
        raise HTTPException(status_code=404, detail="Service not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

```python
# main.py

from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000
```
