"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Suggest an API for integrating appointment scheduling and case updates for a law firm specializing in family and criminal law, referencing Majeli Avocat's client-focused approach and services.
Generated: DETERMINISTIC_beb0aabcaa4abf06
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
API for Law Firm Appointment Scheduling and Case Management System
Inspired by Majeli Avocat's client-focused approach
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, date
from typing import Optional, List
from enum import Enum
import uuid

app = FastAPI(
    title="Law Firm Management API",
    description="API for appointment scheduling and case management for family and criminal law firms",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@lawfirmapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database simulation
db = {
    "clients": {},
    "cases": {},
    "appointments": {},
    "lawyers": {
        "lawyer1": {
            "id": "lawyer1",
            "name": "John Doe",
            "email": "john@lawfirm.com",
            "specializations": ["family", "criminal"],
            "available_slots": []
        }
    }
}

class CaseType(str, Enum):
    FAMILY = "family"
    CRIMINAL = "criminal"

class CaseStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class AppointmentStatus(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Client(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    phone: str
    address: str

class Case(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_id: str
    title: str
    description: str
    case_type: CaseType
    status: CaseStatus = CaseStatus.OPEN
    lawyer_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Appointment(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_id: str
    lawyer_id: str
    case_id: Optional[str] = None
    date_time: datetime
    duration: int = 30  # in minutes
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    notes: Optional[str] = None

class CaseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[CaseStatus] = None

class AppointmentUpdate(BaseModel):
    date_time: Optional[datetime] = None
    status: Optional[AppointmentStatus] = None
    notes: Optional[str] = None

@app.post("/clients/", status_code=status.HTTP_201_CREATED)
async def create_client(client: Client):
    """Register a new client"""
    if client.email in [c.email for c in db["clients"].values()]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client with this email already exists"
        )
    db["clients"][client.id] = client
    return {"message": "Client created successfully", "client_id": client.id}

@app.get("/clients/{client_id}", response_model=Client)
async def get_client(client_id: str):
    """Get client details"""
    if client_id not in db["clients"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found"
        )
    return db["clients"][client_id]

@app.post("/cases/", status_code=status.HTTP_201_CREATED)
async def create_case(case: Case):
    """Create a new case"""
    if case.client_id not in db["clients"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found"
        )
    if case.lawyer_id not in db["lawyers"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lawyer not found"
        )
    db["cases"][case.id] = case
    return {"message": "Case created successfully", "case_id": case.id}

@app.patch("/cases/{case_id}", response_model=Case)
async def update_case(case_id: str, update: CaseUpdate):
    """Update case details"""
    if case_id not in db["cases"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case not found"
        )
    case = db["cases"][case_id]
    update_data = update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(case, field, value)
    
    case.updated_at = datetime.now()
    db["cases"][case_id] = case
    return case

@app.get("/cases/client/{client_id}", response_model=List[Case])
async def get_client_cases(client_id: str):
    """Get all cases for a client"""
    if client_id not in db["clients"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found"
        )
    return [case for case in db["cases"].values() if case.client_id == client_id]

@app.post("/appointments/", status_code=status.HTTP_201_CREATED)
async def create_appointment(appointment: Appointment):
    """Schedule a new appointment"""
    if appointment.client_id not in db["clients"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found"
        )
    if appointment.lawyer_id not in db["lawyers"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lawyer not found"
        )
    if appointment.case_id and appointment.case_id not in db["cases"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case not found"
        )
    
    # Check for conflicting appointments
    for existing in db["appointments"].values():
        if existing.lawyer_id == appointment.lawyer_id:
            existing_end = existing.date_time + timedelta(minutes=existing.duration)
            new_end = appointment.date_time + timedelta(minutes=appointment.duration)
            if (appointment.date_time < existing_end) and (new_end > existing.date_time):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Appointment conflicts with existing appointment"
                )
    
    db["appointments"][appointment.id] = appointment
    return {"message": "Appointment created successfully", "appointment_id": appointment.id}

@app.patch("/appointments/{appointment_id}", response_model=Appointment)
async def update_appointment(appointment_id: str, update: AppointmentUpdate):
    """Update appointment details"""
    if appointment_id not in db["appointments"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    appointment = db["appointments"][appointment_id]
    update_data = update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(appointment, field, value)
    
    db["appointments"][appointment_id] = appointment
    return appointment

@app.get("/appointments/client/{client_id}", response_model=List[Appointment])
async def get_client_appointments(client_id: str):
    """Get all appointments for a client"""
    if client_id not in db["clients"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found"
        )
    return [appt for appt in db["appointments"].values() if appt.client_id == client_id]

@app.get("/appointments/lawyer/{lawyer_id}", response_model=List[Appointment])
async def get_lawyer_appointments(lawyer_id: str):
    """Get all appointments for a lawyer"""
    if lawyer_id not in db["lawyers"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lawyer not found"
        )
    return [appt for appt in db["appointments"].values() if appt.lawyer_id == lawyer_id]

@app.get("/cases/status/{status}", response_model=List[Case])
async def get_cases_by_status(status: CaseStatus):
    """Get cases by status"""
    return [case for case in db["cases"].values() if case.status == status]

@app.get("/cases/type/{case_type}", response_model=List[Case])
async def get_cases_by_type(case_type: CaseType):
    """Get cases by type (family or criminal)"""
    return [case
