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
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Felipe Muñoz Reparaciones API",
    description="REST API for handling plumbing and electrical repair services",
    version="1.0.0"
)

class ServiceType(str, Enum):
    PLUMBING = "plumbing"
    ELECTRICAL = "electrical"

class RepairStatus(str, Enum):
    REQUESTED = "requested"
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Address(BaseModel):
    street: str
    city: str
    state: str
    postal_code: str
    country: str = "Spain"

class RepairRequest(BaseModel):
    service_type: ServiceType
    description: str
    client_name: str
    client_phone: str
    client_email: Optional[str] = None
    address: Address
    preferred_date: Optional[datetime] = None
    emergency: bool = False

class RepairResponse(RepairRequest):
    id: UUID
    status: RepairStatus
    created_at: datetime
    assigned_technician: Optional[str] = None
    estimated_cost: Optional[float] = None
    completion_date: Optional[datetime] = None

# In-memory database simulation
repairs_db = {}

@app.post("/repairs/", 
          response_model=RepairResponse, 
          status_code=status.HTTP_201_CREATED,
          summary="Create a new repair request",
          tags=["Repairs"])
async def create_repair(repair: RepairRequest):
    """
    Create a new repair request for plumbing or electrical services.
    
    - **service_type**: Type of service (plumbing or electrical)
    - **description**: Detailed description of the problem
    - **client_name**: Name of the client
    - **client_phone**: Contact phone number
    - **client_email**: Optional email address
    - **address**: Full service address
    - **preferred_date**: Optional preferred service date
    - **emergency**: Flag for emergency service
    """
    repair_id = uuid4()
    repair_response = RepairResponse(
        id=repair_id,
        status=RepairStatus.REQUESTED,
        created_at=datetime.now(),
        **repair.dict()
    )
    repairs_db[repair_id] = repair_response
    return repair_response

@app.get("/repairs/", 
         response_model=List[RepairResponse],
         summary="List all repair requests",
         tags=["Repairs"])
async def list_repairs(status: Optional[RepairStatus] = None):
    """
    Get a list of all repair requests, optionally filtered by status.
    """
    if status:
        return [repair for repair in repairs_db.values() if repair.status == status]
    return list(repairs_db.values())

@app.get("/repairs/{repair_id}", 
         response_model=RepairResponse,
         summary="Get repair request details",
         tags=["Repairs"])
async def get_repair(repair_id: UUID):
    """
    Get detailed information about a specific repair request.
    """
    if repair_id not in repairs_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Repair request not found"
        )
    return repairs_db[repair_id]

@app.put("/repairs/{repair_id}/status", 
         response_model=RepairResponse,
         summary="Update repair status",
         tags=["Repairs"])
async def update_repair_status(repair_id: UUID, status: RepairStatus):
    """
    Update the status of a repair request.
    
    Possible status values:
    - requested
    - scheduled
    - in_progress
    - completed
    - cancelled
    """
    if repair_id not in repairs_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Repair request not found"
        )
    
    repair = repairs_db[repair_id]
    repair.status = status
    
    if status == RepairStatus.COMPLETED:
        repair.completion_date = datetime.now()
    
    return repair

@app.put("/repairs/{repair_id}/assign", 
         response_model=RepairResponse,
         summary="Assign technician to repair",
         tags=["Repairs"])
async def assign_technician(repair_id: UUID, technician: str):
    """
    Assign a technician to a repair request and set status to scheduled.
    """
    if repair_id not in repairs_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Repair request not found"
        )
    
    repair = repairs_db[repair_id]
    repair.assigned_technician = technician
    repair.status = RepairStatus.SCHEDULED
    
    return repair

@app.put("/repairs/{repair_id}/estimate", 
         response_model=RepairResponse,
         summary="Provide cost estimate",
         tags=["Repairs"])
async def provide_estimate(repair_id: UUID, amount: float):
    """
    Provide a cost estimate for a repair request.
    """
    if repair_id not in repairs_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Repair request not found"
        )
    
    repair = repairs_db[repair_id]
    repair.estimated_cost = amount
    
    return repair

@app.delete("/repairs/{repair_id}", 
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Cancel a repair request",
            tags=["Repairs"])
async def cancel_repair(repair_id: UUID):
    """
    Cancel a repair request (sets status to cancelled).
    """
    if repair_id not in repairs_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Repair request not found"
        )
    
    repair = repairs_db[repair_id]
    repair.status = RepairStatus.CANCELLED
    return None
```
