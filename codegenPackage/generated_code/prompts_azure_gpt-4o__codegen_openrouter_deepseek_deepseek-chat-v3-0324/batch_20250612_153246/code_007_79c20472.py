"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Develop a REST API for a diesel turbo repair service that allows users to submit diagnostic data, book appointments, and receive repair status updates.
Generated: DETERMINISTIC_79c20472b94aa0f2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import uuid4, UUID
from enum import Enum

# Initialize FastAPI app
app = FastAPI(
    title="Diesel Turbo Repair Service API",
    description="API for submitting diagnostic data, booking appointments, and receiving repair status updates",
    version="1.0.0"
)

# Database simulation (in-memory for this example)
class Database:
    def __init__(self):
        self.customers = []
        self.appointments = []
        self.diagnostics = []
        self.repairs = []

db = Database()

# Enums for status and repair types
class RepairStatus(str, Enum):
    DIAGNOSIS = "diagnosis"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class RepairType(str, Enum):
    TURBO_REPLACEMENT = "turbo_replacement"
    TURBO_REBUILD = "turbo_rebuild"
    MAINTENANCE = "maintenance"
    DIAGNOSTIC = "diagnostic"

# Pydantic models for request/response validation
class Customer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    phone: str
    address: str

class DiagnosticData(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    turbo_model: str
    symptoms: List[str]
    error_codes: Optional[List[str]] = None
    mileage: Optional[int] = None
    submitted_at: datetime = Field(default_factory=datetime.now)

class Appointment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    scheduled_time: datetime
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

class Repair(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    diagnostic_id: UUID
    appointment_id: UUID
    repair_type: RepairType
    status: RepairStatus = RepairStatus.DIAGNOSIS
    estimated_cost: float
    estimated_duration_hours: float
    notes: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

class RepairUpdate(BaseModel):
    status: Optional[RepairStatus] = None
    estimated_cost: Optional[float] = None
    estimated_duration_hours: Optional[float] = None
    notes: Optional[str] = None

# Helper functions
def get_customer(customer_id: UUID):
    customer = next((c for c in db.customers if c.id == customer_id), None)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer

def get_diagnostic(diagnostic_id: UUID):
    diagnostic = next((d for d in db.diagnostics if d.id == diagnostic_id), None)
    if not diagnostic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Diagnostic data not found"
        )
    return diagnostic

def get_appointment(appointment_id: UUID):
    appointment = next((a for a in db.appointments if a.id == appointment_id), None)
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    return appointment

def get_repair(repair_id: UUID):
    repair = next((r for r in db.repairs if r.id == repair_id), None)
    if not repair:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Repair not found"
        )
    return repair

# API endpoints
@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    db.customers.append(customer)
    return customer

@app.get("/customers/{customer_id}", response_model=Customer)
async def read_customer(customer_id: UUID):
    return get_customer(customer_id)

@app.post("/diagnostics/", response_model=DiagnosticData, status_code=status.HTTP_201_CREATED)
async def submit_diagnostic(diagnostic: DiagnosticData):
    get_customer(diagnostic.customer_id)  # Validate customer exists
    db.diagnostics.append(diagnostic)
    return diagnostic

@app.get("/diagnostics/{diagnostic_id}", response_model=DiagnosticData)
async def read_diagnostic(diagnostic_id: UUID):
    return get_diagnostic(diagnostic_id)

@app.post("/appointments/", response_model=Appointment, status_code=status.HTTP_201_CREATED)
async def book_appointment(appointment: Appointment):
    get_customer(appointment.customer_id)  # Validate customer exists
    db.appointments.append(appointment)
    return appointment

@app.get("/appointments/{appointment_id}", response_model=Appointment)
async def read_appointment(appointment_id: UUID):
    return get_appointment(appointment_id)

@app.post("/repairs/", response_model=Repair, status_code=status.HTTP_201_CREATED)
async def create_repair(repair: Repair):
    # Validate all references exist
    get_customer(repair.customer_id)
    get_diagnostic(repair.diagnostic_id)
    get_appointment(repair.appointment_id)
    
    db.repairs.append(repair)
    return repair

@app.get("/repairs/{repair_id}", response_model=Repair)
async def read_repair(repair_id: UUID):
    return get_repair(repair_id)

@app.patch("/repairs/{repair_id}", response_model=Repair)
async def update_repair(repair_id: UUID, repair_update: RepairUpdate):
    repair = get_repair(repair_id)
    
    if repair_update.status is not None:
        repair.status = repair_update.status
        if repair_update.status == RepairStatus.IN_PROGRESS and not repair.started_at:
            repair.started_at = datetime.now()
        elif repair_update.status == RepairStatus.COMPLETED and not repair.completed_at:
            repair.completed_at = datetime.now()
    
    if repair_update.estimated_cost is not None:
        repair.estimated_cost = repair_update.estimated_cost
    
    if repair_update.estimated_duration_hours is not None:
        repair.estimated_duration_hours = repair_update.estimated_duration_hours
    
    if repair_update.notes is not None:
        repair.notes = repair_update.notes
    
    return repair

@app.get("/customers/{customer_id}/repairs", response_model=List[Repair])
async def get_customer_repairs(customer_id: UUID):
    get_customer(customer_id)
    return [r for r in db.repairs if r.customer_id == customer_id]

@app.get("/repairs/", response_model=List[Repair])
async def list_repairs(status: Optional[RepairStatus] = None):
    if status:
        return [r for r in db.repairs if r.status == status]
    return db.repairs
```
