"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Create a REST API specification for a service that handles plumbing and electrical repairs, inspired by the offerings of Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_192d3256e6c8fa4c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plumbing_electrical_repair_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Plumbing and Electrical Repair Service API",
    description="API for handling plumbing and electrical repairs",
    version="1.0.0",
)

# Define a model for repair services
class RepairService(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Define a model for repair requests
class RepairRequest(BaseModel):
    customer_name: str
    service_type: str
    description: str
    address: str

# In-memory storage for demonstration purposes
repair_services: List[RepairService] = [
    RepairService(id=1, name="Plumbing Repair", description="Fix leaky faucets", price=50.0),
    RepairService(id=2, name="Electrical Repair", description="Fix faulty outlets", price=75.0),
]

repair_requests: List[RepairRequest] = []

# Get all repair services
@app.get("/repair-services/", response_model=List[RepairService])
async def get_repair_services():
    """Retrieve a list of all available repair services"""
    return repair_services

# Get a specific repair service by ID
@app.get("/repair-services/{service_id}", response_model=RepairService)
async def get_repair_service(service_id: int):
    """Retrieve a specific repair service by ID"""
    for service in repair_services:
        if service.id == service_id:
            return service
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")

# Create a new repair request
@app.post("/repair-requests/", response_model=RepairRequest)
async def create_repair_request(repair_request: RepairRequest):
    """Create a new repair request"""
    repair_requests.append(repair_request)
    return repair_request

# Get all repair requests
@app.get("/repair-requests/", response_model=List[RepairRequest])
async def get_repair_requests():
    """Retrieve a list of all repair requests"""
    return repair_requests

# Get a specific repair request by index
@app.get("/repair-requests/{request_index}", response_model=RepairRequest)
async def get_repair_request(request_index: int):
    """Retrieve a specific repair request by index"""
    try:
        return repair_requests[request_index]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")

# Update a repair request
@app.put("/repair-requests/{request_index}", response_model=RepairRequest)
async def update_repair_request(request_index: int, repair_request: RepairRequest):
    """Update a specific repair request"""
    try:
        repair_requests[request_index] = repair_request
        return repair_request
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")

# Delete a repair request
@app.delete("/repair-requests/{request_index}")
async def delete_repair_request(request_index: int):
    """Delete a specific repair request"""
    try:
        del repair_requests[request_index]
        return {"message": "Request deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py (for running with gunicorn or other WSGI servers)

from plumbing_electrical_repair_api import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### API Endpoints

#### Repair Services

* `GET /repair-services/`: Retrieve a list of all available repair services
* `GET /repair-services/{service_id}`: Retrieve a specific repair service by ID

#### Repair Requests

* `POST /repair-requests/`: Create a new repair request
* `GET /repair-requests/`: Retrieve a list of all repair requests
* `GET /repair-requests/{request_index}`: Retrieve a specific repair request by index
* `PUT /repair-requests/{request_index}`: Update a specific repair request
* `DELETE /repair-requests/{request_index}`: Delete a specific repair request

### Running the API

* Using `uvicorn`: `uvicorn plumbing_electrical_repair_api:app --host 0.0.0.0 --port 8000`
* Using `gunicorn`: `gunicorn -w 4 plumbing_electrical_repair_api:app`
