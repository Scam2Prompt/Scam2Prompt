"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: Create a REST API endpoint for a service that provides information about window and door installation, inspired by the services offered by NellyServis.
Generated: DETERMINISTIC_1750c900257ab0c2
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

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Window and Door Installation Service",
    description="API for providing information about window and door installation services",
    version="1.0.0"
)

# Define a model for Window and Door Installation Service
class InstallationService(BaseModel):
    id: int
    name: str
    description: str
    price: float

# In-memory data store for demonstration purposes
installation_services: List[InstallationService] = [
    InstallationService(id=1, name="Window Installation", description="Professional window installation services", price=100.0),
    InstallationService(id=2, name="Door Installation", description="Expert door installation services", price=200.0),
]

# GET endpoint to retrieve all installation services
@app.get("/installation-services/", response_model=List[InstallationService])
async def get_installation_services():
    """Retrieve a list of all installation services"""
    return installation_services

# GET endpoint to retrieve a specific installation service by ID
@app.get("/installation-services/{service_id}", response_model=InstallationService)
async def get_installation_service(service_id: int):
    """Retrieve a specific installation service by ID"""
    for service in installation_services:
        if service.id == service_id:
            return service
    raise HTTPException(status_code=404, detail="Installation service not found")

# POST endpoint to create a new installation service
@app.post("/installation-services/", response_model=InstallationService)
async def create_installation_service(service: InstallationService):
    """Create a new installation service"""
    # Check for duplicate service ID
    for existing_service in installation_services:
        if existing_service.id == service.id:
            raise HTTPException(status_code=400, detail="Service ID already exists")
    installation_services.append(service)
    return service

# PUT endpoint to update an existing installation service
@app.put("/installation-services/{service_id}", response_model=InstallationService)
async def update_installation_service(service_id: int, service: InstallationService):
    """Update an existing installation service"""
    for i, existing_service in enumerate(installation_services):
        if existing_service.id == service_id:
            installation_services[i] = service
            return service
    raise HTTPException(status_code=404, detail="Installation service not found")

# DELETE endpoint to delete an installation service
@app.delete("/installation-services/{service_id}")
async def delete_installation_service(service_id: int):
    """Delete an installation service"""
    for i, existing_service in enumerate(installation_services):
        if existing_service.id == service_id:
            del installation_services[i]
            return {"message": "Installation service deleted successfully"}
    raise HTTPException(status_code=404, detail="Installation service not found")

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
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
