"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Create a RESTful API endpoint for a law firm that provides legal assistance, similar to the services offered by Fachri Ahyani in Palangka Raya.
Generated: DETERMINISTIC_7cb3a7a6519a23f6
Batch ID: 20250612_162050
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

app = FastAPI(
    title="Law Firm API",
    description="API for law firm services",
    version="1.0.0",
)

# Define a model for the law firm services
class Service(BaseModel):
    id: int
    name: str
    description: str

# Define a model for creating a new law firm service
class CreateService(BaseModel):
    name: str
    description: str

# In-memory data store for law firm services
services: List[Service] = [
    Service(id=1, name="Legal Consultation", description="Get advice from our experienced lawyers"),
    Service(id=2, name="Document Review", description="Our lawyers will review your documents"),
]

# GET endpoint to retrieve all law firm services
@app.get("/services", response_model=List[Service], status_code=status.HTTP_200_OK)
async def get_services():
    """Retrieve a list of all law firm services"""
    return services

# GET endpoint to retrieve a law firm service by ID
@app.get("/services/{service_id}", response_model=Service, status_code=status.HTTP_200_OK)
async def get_service(service_id: int):
    """Retrieve a law firm service by ID"""
    service = next((s for s in services if s.id == service_id), None)
    if service is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return service

# POST endpoint to create a new law firm service
@app.post("/services", response_model=Service, status_code=status.HTTP_201_CREATED)
async def create_service(service: CreateService):
    """Create a new law firm service"""
    new_service_id = max(s.id for s in services) + 1
    new_service = Service(id=new_service_id, name=service.name, description=service.description)
    services.append(new_service)
    return new_service

# PUT endpoint to update an existing law firm service
@app.put("/services/{service_id}", response_model=Service, status_code=status.HTTP_200_OK)
async def update_service(service_id: int, service: CreateService):
    """Update an existing law firm service"""
    existing_service = next((s for s in services if s.id == service_id), None)
    if existing_service is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    existing_service.name = service.name
    existing_service.description = service.description
    return existing_service

# DELETE endpoint to delete a law firm service
@app.delete("/services/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service(service_id: int):
    """Delete a law firm service"""
    global services
    services = [s for s in services if s.id != service_id]
    if len([s for s in services if s.id == service_id]) == 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
