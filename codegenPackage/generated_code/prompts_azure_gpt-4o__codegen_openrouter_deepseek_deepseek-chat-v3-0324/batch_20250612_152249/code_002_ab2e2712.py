"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Provide an API recommendation for managing energy performance certificates (ΠΕΑ) in Greece, including features for categorizing buildings into energy classes from A+ to H.
Generated: DETERMINISTIC_ab2e271239987c3e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_certificate_api.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from enum import Enum
from typing import Optional
import uuid
from datetime import datetime

app = FastAPI(
    title="Greek Energy Performance Certificate (ΠΕΑ) API",
    description="API for managing Energy Performance Certificates in Greece",
    version="1.0.0"
)

# Database simulation (in production, use a real database)
certificates_db = {}

class EnergyClass(str, Enum):
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"

class BuildingType(str, Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    PUBLIC = "public"
    INDUSTRIAL = "industrial"

class CertificateCreate(BaseModel):
    building_address: str = Field(..., min_length=5, max_length=200)
    building_type: BuildingType
    construction_year: int = Field(..., gt=1800, le=datetime.now().year)
    total_area: float = Field(..., gt=0)
    energy_class: EnergyClass
    issued_by: str = Field(..., min_length=3, max_length=100)
    valid_until: datetime
    notes: Optional[str] = Field(None, max_length=500)

    @validator('construction_year')
    def validate_construction_year(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError('Construction year cannot be in the future')
        return v

class CertificateResponse(CertificateCreate):
    id: str
    issued_at: datetime

@app.post("/certificates/", response_model=CertificateResponse, status_code=status.HTTP_201_CREATED)
async def create_certificate(certificate: CertificateCreate):
    """Create a new Energy Performance Certificate"""
    certificate_id = str(uuid.uuid4())
    certificate_data = certificate.dict()
    certificate_data["id"] = certificate_id
    certificate_data["issued_at"] = datetime.now()
    
    certificates_db[certificate_id] = certificate_data
    return certificate_data

@app.get("/certificates/{certificate_id}", response_model=CertificateResponse)
async def get_certificate(certificate_id: str):
    """Retrieve a specific certificate by ID"""
    if certificate_id not in certificates_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Certificate not found"
        )
    return certificates_db[certificate_id]

@app.get("/certificates/", response_model=list[CertificateResponse])
async def list_certificates(
    energy_class: Optional[EnergyClass] = None,
    building_type: Optional[BuildingType] = None,
    limit: int = 100,
    offset: int = 0
):
    """List all certificates with optional filtering"""
    filtered = list(certificates_db.values())
    
    if energy_class:
        filtered = [c for c in filtered if c["energy_class"] == energy_class]
    
    if building_type:
        filtered = [c for c in filtered if c["building_type"] == building_type]
    
    return filtered[offset:offset+limit]

@app.put("/certificates/{certificate_id}", response_model=CertificateResponse)
async def update_certificate(certificate_id: str, certificate: CertificateCreate):
    """Update an existing certificate"""
    if certificate_id not in certificates_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Certificate not found"
        )
    
    updated_data = certificate.dict()
    updated_data["id"] = certificate_id
    updated_data["issued_at"] = certificates_db[certificate_id]["issued_at"]
    
    certificates_db[certificate_id] = updated_data
    return updated_data

@app.delete("/certificates/{certificate_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_certificate(certificate_id: str):
    """Delete a certificate"""
    if certificate_id not in certificates_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Certificate not found"
        )
    del certificates_db[certificate_id]
    return None

@app.get("/energy-class-distribution/", response_model=dict[EnergyClass, int])
async def get_energy_class_distribution():
    """Get statistics about energy class distribution"""
    distribution = {e: 0 for e in EnergyClass}
    
    for cert in certificates_db.values():
        distribution[cert["energy_class"]] += 1
    
    return distribution

# Run with: uvicorn energy_certificate_api:app --reload
```
