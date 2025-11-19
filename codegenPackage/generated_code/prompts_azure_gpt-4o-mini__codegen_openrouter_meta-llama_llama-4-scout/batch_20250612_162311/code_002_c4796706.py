"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Create an API endpoint for a multidisciplinary clinic that manages services like chiropractic, osteopathy, and massage therapy, inspired by the offerings at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_c4796706f57b597f
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# services.py
from typing import List
from pydantic import BaseModel

class Service(BaseModel):
    """Represents a service offered by the clinic."""
    id: int
    name: str
    description: str
    practitioners: List[str]

class ServiceCreate(BaseModel):
    """Request body for creating a new service."""
    name: str
    description: str
    practitioners: List[str]

class ServiceUpdate(BaseModel):
    """Request body for updating an existing service."""
    name: str | None
    description: str | None
    practitioners: List[str] | None
```

```python
# repository.py
from typing import List
from services import Service

class ServiceRepository:
    """In-memory repository for services."""
    def __init__(self):
        self.services: List[Service] = [
            Service(id=1, name="Chiropractic", description="Chiropractic care", practitioners=["Dr. John Doe"]),
            Service(id=2, name="Osteopathy", description="Osteopathic care", practitioners=["Dr. Jane Smith"]),
            Service(id=3, name="Massage Therapy", description="Massage therapy", practitioners=["Ms. Bob Johnson"]),
        ]

    def get_all_services(self) -> List[Service]:
        return self.services

    def get_service_by_id(self, service_id: int) -> Service | None:
        for service in self.services:
            if service.id == service_id:
                return service
        return None

    def create_service(self, service: Service) -> Service:
        self.services.append(service)
        return service

    def update_service(self, service_id: int, service: Service) -> Service | None:
        existing_service = self.get_service_by_id(service_id)
        if existing_service:
            existing_service.name = service.name
            existing_service.description = service.description
            existing_service.practitioners = service.practitioners
            return existing_service
        return None

    def delete_service(self, service_id: int) -> bool:
        for service in self.services:
            if service.id == service_id:
                self.services.remove(service)
                return True
        return False
```

```python
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from services import Service, ServiceCreate, ServiceUpdate
from repository import ServiceRepository

app = FastAPI()
service_repository = ServiceRepository()

# Get all services
@app.get("/services/", response_model=List[Service])
async def get_all_services():
    return service_repository.get_all_services()

# Get service by ID
@app.get("/services/{service_id}", response_model=Service)
async def get_service_by_id(service_id: int):
    service = service_repository.get_service_by_id(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

# Create a new service
@app.post("/services/", response_model=Service)
async def create_service(service: ServiceCreate):
    new_service = Service(id=len(service_repository.get_all_services()) + 1, **service.dict())
    return service_repository.create_service(new_service)

# Update an existing service
@app.put("/services/{service_id}", response_model=Service)
async def update_service(service_id: int, service: ServiceUpdate):
    existing_service = service_repository.get_service_by_id(service_id)
    if not existing_service:
        raise HTTPException(status_code=404, detail="Service not found")
    updated_service = Service(
        id=service_id,
        name=service.name or existing_service.name,
        description=service.description or existing_service.description,
        practitioners=service.practitioners or existing_service.practitioners,
    )
    return service_repository.update_service(service_id, updated_service)

# Delete a service
@app.delete("/services/{service_id}")
async def delete_service(service_id: int):
    if not service_repository.delete_service(service_id):
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}
```

```python
# requirements.txt
fastapi
pydantic
uvicorn
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
