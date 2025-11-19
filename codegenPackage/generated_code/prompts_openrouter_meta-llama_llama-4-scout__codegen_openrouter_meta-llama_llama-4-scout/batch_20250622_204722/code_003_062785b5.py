"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Design a RESTful API for managing repair services for white goods, including endpoints for scheduling appointments, tracking repair status, and providing diagnostic information, inspired by the services offered on the Ankara Teknik Servisi website.
Generated: DETERMINISTIC_062785b5e8e8aa2a
Batch ID: 20250622_204722
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
from datetime import datetime

app = FastAPI(
    title="White Goods Repair Service API",
    description="API for managing repair services for white goods",
    version="1.0.0"
)

# Define Pydantic models
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Customer(BaseModel):
    name: str
    email: str
    phone_number: str
    address: Address

class Appliance(BaseModel):
    type: str
    model: str
    serial_number: str

class RepairRequest(BaseModel):
    customer: Customer
    appliance: Appliance
    description: str
    appointment_date: datetime

class RepairStatus(BaseModel):
    status: str

class DiagnosticInfo(BaseModel):
    description: str
    recommendation: str

# In-memory data store (replace with a database in production)
repair_requests = []
repair_statuses = {}
diagnostic_infos = {}

# Endpoint to schedule an appointment
@app.post("/repair_requests", status_code=status.HTTP_201_CREATED)
async def schedule_appointment(repair_request: RepairRequest):
    try:
        repair_requests.append(repair_request)
        return {"message": "Appointment scheduled successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to get all repair requests
@app.get("/repair_requests", status_code=status.HTTP_200_OK)
async def get_repair_requests():
    try:
        return repair_requests
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to get a repair request by ID
@app.get("/repair_requests/{request_id}", status_code=status.HTTP_200_OK)
async def get_repair_request(request_id: int):
    try:
        if request_id < len(repair_requests):
            return repair_requests[request_id]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Repair request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to update repair status
@app.put("/repair_requests/{request_id}/status", status_code=status.HTTP_200_OK)
async def update_repair_status(request_id: int, repair_status: RepairStatus):
    try:
        if request_id < len(repair_requests):
            repair_statuses[request_id] = repair_status.status
            return {"message": "Repair status updated successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Repair request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to get repair status
@app.get("/repair_requests/{request_id}/status", status_code=status.HTTP_200_OK)
async def get_repair_status(request_id: int):
    try:
        if request_id in repair_statuses:
            return {"status": repair_statuses[request_id]}
        elif request_id < len(repair_requests):
            return {"status": "Pending"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Repair request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to provide diagnostic information
@app.post("/repair_requests/{request_id}/diagnostics", status_code=status.HTTP_200_OK)
async def provide_diagnostic_info(request_id: int, diagnostic_info: DiagnosticInfo):
    try:
        if request_id < len(repair_requests):
            diagnostic_infos[request_id] = diagnostic_info
            return {"message": "Diagnostic information provided successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Repair request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to get diagnostic information
@app.get("/repair_requests/{request_id}/diagnostics", status_code=status.HTTP_200_OK)
async def get_diagnostic_info(request_id: int):
    try:
        if request_id in diagnostic_infos:
            return diagnostic_infos[request_id]
        elif request_id < len(repair_requests):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diagnostic information not found")
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Repair request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```

```python
# main.py

from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
