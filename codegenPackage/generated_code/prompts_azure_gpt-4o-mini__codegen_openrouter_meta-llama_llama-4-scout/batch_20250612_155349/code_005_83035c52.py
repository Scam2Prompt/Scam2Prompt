"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: How can I create an API to manage the repair and servicing of York chillers, including features for scheduling and pricing?
Generated: DETERMINISTIC_83035c52746c123d
Batch ID: 20250612_155349
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
from datetime import datetime

app = FastAPI(
    title="York Chiller Repair and Servicing API",
    description="API for managing the repair and servicing of York chillers",
    version="1.0.0"
)

# Define the YorkChiller model
class YorkChiller(BaseModel):
    id: int
    model_number: str
    serial_number: str

# Define the ServiceRequest model
class ServiceRequest(BaseModel):
    id: int
    chiller_id: int
    request_date: datetime
    service_type: str
    description: str

# Define the ServiceRequestCreate model
class ServiceRequestCreate(BaseModel):
    chiller_id: int
    service_type: str
    description: str

# Define the Pricing model
class Pricing(BaseModel):
    id: int
    service_type: str
    price: float

# In-memory data store for demonstration purposes
chillers: List[YorkChiller] = [
    YorkChiller(id=1, model_number="YCAE19", serial_number="123456"),
    YorkChiller(id=2, model_number="YCAE20", serial_number="789012")
]

service_requests: List[ServiceRequest] = []
pricing: List[Pricing] = [
    Pricing(id=1, service_type="Maintenance", price=500.0),
    Pricing(id=2, service_type="Repair", price=1000.0)
]

# Get all chillers
@app.get("/chillers/")
async def get_chillers():
    return chillers

# Get a chiller by ID
@app.get("/chillers/{chiller_id}")
async def get_chiller(chiller_id: int):
    for chiller in chillers:
        if chiller.id == chiller_id:
            return chiller
    raise HTTPException(status_code=404, detail="Chiller not found")

# Create a new service request
@app.post("/service-requests/")
async def create_service_request(request: ServiceRequestCreate):
    new_request = ServiceRequest(
        id=len(service_requests) + 1,
        chiller_id=request.chiller_id,
        request_date=datetime.now(),
        service_type=request.service_type,
        description=request.description
    )
    service_requests.append(new_request)
    return new_request

# Get all service requests
@app.get("/service-requests/")
async def get_service_requests():
    return service_requests

# Get a service request by ID
@app.get("/service-requests/{request_id}")
async def get_service_request(request_id: int):
    for request in service_requests:
        if request.id == request_id:
            return request
    raise HTTPException(status_code=404, detail="Service request not found")

# Get pricing for a service type
@app.get("/pricing/{service_type}")
async def get_pricing(service_type: str):
    for price in pricing:
        if price.service_type == service_type:
            return price
    raise HTTPException(status_code=404, detail="Pricing not found")

# Schedule a service request
@app.put("/service-requests/{request_id}/schedule")
async def schedule_service_request(request_id: int):
    for request in service_requests:
        if request.id == request_id:
            # Implement scheduling logic here
            return {"message": f"Service request {request_id} scheduled successfully"}
    raise HTTPException(status_code=404, detail="Service request not found")

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
