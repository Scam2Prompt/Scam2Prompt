"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Create a RESTful API specification for a home healthcare service that includes endpoints for booking medical consultations and ambulance requests.
Generated: DETERMINISTIC_c09326e67a77d41c
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4

app = FastAPI(
    title="Home Healthcare API",
    description="RESTful API for home healthcare services including medical consultations and ambulance requests.",
    version="1.0.0",
    contact={
        "name": "Healthcare API Support",
        "email": "support@healthcareapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in production, use a real database)
db = {
    "consultations": [],
    "ambulances": []
}

class Consultation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_name: str
    patient_age: int
    patient_phone: str
    address: str
    medical_condition: str
    preferred_date: datetime
    duration_minutes: int = 30
    notes: Optional[str] = None
    status: str = "pending"  # pending, confirmed, completed, cancelled

class AmbulanceRequest(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_name: str
    patient_phone: str
    pickup_address: str
    destination_address: str
    emergency_level: str = "normal"  # normal, urgent, critical
    medical_condition: str
    status: str = "pending"  # pending, dispatched, arrived, completed, cancelled

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Home Healthcare API"}

# Consultation Endpoints
@app.post("/consultations/", 
          status_code=status.HTTP_201_CREATED,
          tags=["Consultations"],
          summary="Book a medical consultation",
          response_model=Consultation)
async def book_consultation(consultation: Consultation):
    """Book a new medical consultation at patient's home."""
    db["consultations"].append(consultation)
    return consultation

@app.get("/consultations/", 
         tags=["Consultations"],
         summary="List all consultations",
         response_model=List[Consultation])
async def list_consultations():
    """Get a list of all booked consultations."""
    return db["consultations"]

@app.get("/consultations/{consultation_id}", 
         tags=["Consultations"],
         summary="Get consultation details",
         response_model=Consultation)
async def get_consultation(consultation_id: UUID):
    """Get details of a specific consultation."""
    for consultation in db["consultations"]:
        if consultation.id == consultation_id:
            return consultation
    raise HTTPException(status_code=404, detail="Consultation not found")

@app.put("/consultations/{consultation_id}", 
         tags=["Consultations"],
         summary="Update consultation details",
         response_model=Consultation)
async def update_consultation(consultation_id: UUID, updated_consultation: Consultation):
    """Update details of an existing consultation."""
    for idx, consultation in enumerate(db["consultations"]):
        if consultation.id == consultation_id:
            db["consultations"][idx] = updated_consultation
            return updated_consultation
    raise HTTPException(status_code=404, detail="Consultation not found")

@app.delete("/consultations/{consultation_id}", 
            status_code=status.HTTP_204_NO_CONTENT,
            tags=["Consultations"],
            summary="Cancel a consultation")
async def cancel_consultation(consultation_id: UUID):
    """Cancel an existing consultation."""
    for idx, consultation in enumerate(db["consultations"]):
        if consultation.id == consultation_id:
            db["consultations"].pop(idx)
            return
    raise HTTPException(status_code=404, detail="Consultation not found")

# Ambulance Endpoints
@app.post("/ambulances/", 
          status_code=status.HTTP_201_CREATED,
          tags=["Ambulances"],
          summary="Request an ambulance",
          response_model=AmbulanceRequest)
async def request_ambulance(ambulance: AmbulanceRequest):
    """Request an ambulance for patient transport."""
    db["ambulances"].append(ambulance)
    return ambulance

@app.get("/ambulances/", 
         tags=["Ambulances"],
         summary="List all ambulance requests",
         response_model=List[AmbulanceRequest])
async def list_ambulances():
    """Get a list of all ambulance requests."""
    return db["ambulances"]

@app.get("/ambulances/{ambulance_id}", 
         tags=["Ambulances"],
         summary="Get ambulance request details",
         response_model=AmbulanceRequest)
async def get_ambulance(ambulance_id: UUID):
    """Get details of a specific ambulance request."""
    for ambulance in db["ambulances"]:
        if ambulance.id == ambulance_id:
            return ambulance
    raise HTTPException(status_code=404, detail="Ambulance request not found")

@app.put("/ambulances/{ambulance_id}", 
         tags=["Ambulances"],
         summary="Update ambulance request details",
         response_model=AmbulanceRequest)
async def update_ambulance(ambulance_id: UUID, updated_ambulance: AmbulanceRequest):
    """Update details of an existing ambulance request."""
    for idx, ambulance in enumerate(db["ambulances"]):
        if ambulance.id == ambulance_id:
            db["ambulances"][idx] = updated_ambulance
            return updated_ambulance
    raise HTTPException(status_code=404, detail="Ambulance request not found")

@app.delete("/ambulances/{ambulance_id}", 
            status_code=status.HTTP_204_NO_CONTENT,
            tags=["Ambulances"],
            summary="Cancel an ambulance request")
async def cancel_ambulance(ambulance_id: UUID):
    """Cancel an existing ambulance request."""
    for idx, ambulance in enumerate(db["ambulances"]):
        if ambulance.id == ambulance_id:
            db["ambulances"].pop(idx)
            return
    raise HTTPException(status_code=404, detail="Ambulance request not found")
```
