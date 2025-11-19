"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Generate a REST API specification for a service that provides information on equine massage techniques and saddle fitting, referencing the services provided by Martin Godwin Equine Services.
Generated: DETERMINISTIC_2b9296ebaf4349a9
Batch ID: 20250612_163952
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
    title="Martin Godwin Equine Services API",
    description="Provides information on equine massage techniques and saddle fitting",
    version="1.0.0"
)

# Define a model for the equine massage techniques
class MassageTechnique(BaseModel):
    id: int
    name: str
    description: str

# Define a model for the saddle fitting services
class SaddleFittingService(BaseModel):
    id: int
    name: str
    description: str

# In-memory data store for demonstration purposes
massage_techniques: List[MassageTechnique] = [
    MassageTechnique(id=1, name="Trigger Point Therapy", description="Relieves pain and tension in specific areas"),
    MassageTechnique(id=2, name="Muscle Energy Techniques", description="Improves range of motion and reduces muscle strain")
]

saddle_fitting_services: List[SaddleFittingService] = [
    SaddleFittingService(id=1, name="Saddle Fitting Assessment", description="Evaluates the fit of the saddle on the horse"),
    SaddleFittingService(id=2, name="Custom Saddle Fitting", description="Provides a custom-fit saddle for the horse")
]

# GET endpoint to retrieve all massage techniques
@app.get("/massage-techniques/", response_model=List[MassageTechnique])
async def get_massage_techniques():
    """Retrieve a list of all equine massage techniques"""
    return massage_techniques

# GET endpoint to retrieve a specific massage technique by ID
@app.get("/massage-techniques/{technique_id}", response_model=MassageTechnique)
async def get_massage_technique(technique_id: int):
    """Retrieve a specific equine massage technique by ID"""
    technique = next((t for t in massage_techniques if t.id == technique_id), None)
    if technique is None:
        raise HTTPException(status_code=404, detail="Massage technique not found")
    return technique

# GET endpoint to retrieve all saddle fitting services
@app.get("/saddle-fitting-services/", response_model=List[SaddleFittingService])
async def get_saddle_fitting_services():
    """Retrieve a list of all saddle fitting services"""
    return saddle_fitting_services

# GET endpoint to retrieve a specific saddle fitting service by ID
@app.get("/saddle-fitting-services/{service_id}", response_model=SaddleFittingService)
async def get_saddle_fitting_service(service_id: int):
    """Retrieve a specific saddle fitting service by ID"""
    service = next((s for s in saddle_fitting_services if s.id == service_id), None)
    if service is None:
        raise HTTPException(status_code=404, detail="Saddle fitting service not found")
    return service

# Error handler for 404 exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

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
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
