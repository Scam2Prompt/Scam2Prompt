"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Generate an API specification for a health service application that integrates with the Sistema Único de Saúde, focusing on patient data management and service accessibility.
Generated: DETERMINISTIC_3abc4e5fe7fe16e1
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from uuid import UUID, uuid4

app = FastAPI(
    title="SUS Health Service API",
    description="API for managing patient data and service accessibility in the Sistema Único de Saúde (SUS)",
    version="1.0.0",
    contact={
        "name": "SUS API Support",
        "email": "sus-api@saude.gov.br"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in production, replace with actual database)
patients_db = []
appointments_db = []
health_units_db = []

class Address(BaseModel):
    street: str = Field(..., example="Rua das Flores")
    number: str = Field(..., example="123")
    complement: Optional[str] = Field(None, example="Apto 101")
    neighborhood: str = Field(..., example="Centro")
    city: str = Field(..., example="São Paulo")
    state: str = Field(..., example="SP")
    postal_code: str = Field(..., example="01001000")

class Patient(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., example="João da Silva")
    cpf: str = Field(..., example="12345678901", min_length=11, max_length=11)
    birth_date: date = Field(..., example="1980-01-01")
    gender: str = Field(..., example="M", min_length=1, max_length=1)
    phone: str = Field(..., example="11987654321")
    email: Optional[str] = Field(None, example="joao@example.com")
    address: Address
    sus_card_number: str = Field(..., example="1234567890123456")

class HealthUnit(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., example="UBS Jardim das Flores")
    unit_type: str = Field(..., example="UBS")
    address: Address
    phone: str = Field(..., example="1133334444")
    services: List[str] = Field(..., example=["Consultas", "Vacinação"])

class Appointment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_id: UUID
    health_unit_id: UUID
    date: date = Field(..., example="2023-12-01")
    time: str = Field(..., example="14:00")
    service_type: str = Field(..., example="Consulta médica")
    status: str = Field(..., example="Agendado")

@app.get("/patients/", response_model=List[Patient], tags=["Patients"])
async def list_patients():
    """List all registered patients"""
    return patients_db

@app.post("/patients/", response_model=Patient, status_code=status.HTTP_201_CREATED, tags=["Patients"])
async def create_patient(patient: Patient):
    """Register a new patient"""
    if any(p.cpf == patient.cpf for p in patients_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient with this CPF already exists"
        )
    patients_db.append(patient)
    return patient

@app.get("/patients/{patient_id}", response_model=Patient, tags=["Patients"])
async def get_patient(patient_id: UUID):
    """Get patient details by ID"""
    patient = next((p for p in patients_db if p.id == patient_id), None)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    return patient

@app.get("/health-units/", response_model=List[HealthUnit], tags=["Health Units"])
async def list_health_units():
    """List all available health units"""
    return health_units_db

@app.post("/health-units/", response_model=HealthUnit, status_code=status.HTTP_201_CREATED, tags=["Health Units"])
async def create_health_unit(unit: HealthUnit):
    """Register a new health unit"""
    health_units_db.append(unit)
    return unit

@app.get("/health-units/{unit_id}", response_model=HealthUnit, tags=["Health Units"])
async def get_health_unit(unit_id: UUID):
    """Get health unit details by ID"""
    unit = next((u for u in health_units_db if u.id == unit_id), None)
    if not unit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Health unit not found"
        )
    return unit

@app.get("/appointments/", response_model=List[Appointment], tags=["Appointments"])
async def list_appointments():
    """List all scheduled appointments"""
    return appointments_db

@app.post("/appointments/", response_model=Appointment, status_code=status.HTTP_201_CREATED, tags=["Appointments"])
async def create_appointment(appointment: Appointment):
    """Schedule a new appointment"""
    # Check if patient exists
    if not any(p.id == appointment.patient_id for p in patients_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    
    # Check if health unit exists
    if not any(u.id == appointment.health_unit_id for u in health_units_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Health unit not found"
        )
    
    appointments_db.append(appointment)
    return appointment

@app.get("/appointments/{appointment_id}", response_model=Appointment, tags=["Appointments"])
async def get_appointment(appointment_id: UUID):
    """Get appointment details by ID"""
    appointment = next((a for a in appointments_db if a.id == appointment_id), None)
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    return appointment

@app.get("/health-units/nearby", response_model=List[HealthUnit], tags=["Health Units"])
async def find_nearby_health_units(
    latitude: float,
    longitude: float,
    radius: float = 5.0,
    service_type: Optional[str] = None
):
    """Find health units near a location, optionally filtered by service type"""
    # In production, this would query a geospatial database
    units = health_units_db
    
    if service_type:
        units = [u for u in units if service_type in u.services]
    
    return units[:10]  # Return first 10 results for demo purposes
```
