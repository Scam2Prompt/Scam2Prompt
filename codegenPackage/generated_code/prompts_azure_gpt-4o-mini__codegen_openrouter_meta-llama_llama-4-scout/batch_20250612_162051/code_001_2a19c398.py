"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Generate a REST API specification for a hospice care service that includes endpoints for patient intake, symptom tracking, and family support, inspired by the services offered by Amalfi Hospice Care.
Generated: DETERMINISTIC_2a19c398b29ea495
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Hospice Care Service API",
    description="API for hospice care services",
    version="1.0.0"
)

# Patient Model
class Patient(BaseModel):
    patient_id: int
    name: str
    diagnosis: str
    admission_date: str

# Symptom Model
class Symptom(BaseModel):
    symptom_id: int
    patient_id: int
    symptom_name: str
    severity: str
    date_reported: str

# Family Support Model
class FamilySupport(BaseModel):
    support_id: int
    patient_id: int
    support_type: str
    date_provided: str

# In-Memory Data Store (replace with a database in production)
patients: List[Patient] = []
symptoms: List[Symptom] = []
family_support: List[FamilySupport] = []

# Patient Endpoints
@app.post("/patients/")
async def create_patient(patient: Patient):
    patients.append(patient)
    return patient

@app.get("/patients/")
async def read_patients():
    return patients

@app.get("/patients/{patient_id}")
async def read_patient(patient_id: int):
    for patient in patients:
        if patient.patient_id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@app.put("/patients/{patient_id}")
async def update_patient(patient_id: int, patient: Patient):
    for i, existing_patient in enumerate(patients):
        if existing_patient.patient_id == patient_id:
            patients[i] = patient
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@app.delete("/patients/{patient_id}")
async def delete_patient(patient_id: int):
    for i, patient in enumerate(patients):
        if patient.patient_id == patient_id:
            del patients[i]
            return {"message": "Patient deleted"}
    raise HTTPException(status_code=404, detail="Patient not found")

# Symptom Endpoints
@app.post("/symptoms/")
async def create_symptom(symptom: Symptom):
    symptoms.append(symptom)
    return symptom

@app.get("/symptoms/")
async def read_symptoms():
    return symptoms

@app.get("/symptoms/{symptom_id}")
async def read_symptom(symptom_id: int):
    for symptom in symptoms:
        if symptom.symptom_id == symptom_id:
            return symptom
    raise HTTPException(status_code=404, detail="Symptom not found")

@app.put("/symptoms/{symptom_id}")
async def update_symptom(symptom_id: int, symptom: Symptom):
    for i, existing_symptom in enumerate(symptoms):
        if existing_symptom.symptom_id == symptom_id:
            symptoms[i] = symptom
            return symptom
    raise HTTPException(status_code=404, detail="Symptom not found")

@app.delete("/symptoms/{symptom_id}")
async def delete_symptom(symptom_id: int):
    for i, symptom in enumerate(symptoms):
        if symptom.symptom_id == symptom_id:
            del symptoms[i]
            return {"message": "Symptom deleted"}
    raise HTTPException(status_code=404, detail="Symptom not found")

# Family Support Endpoints
@app.post("/family-support/")
async def create_family_support(support: FamilySupport):
    family_support.append(support)
    return support

@app.get("/family-support/")
async def read_family_support():
    return family_support

@app.get("/family-support/{support_id}")
async def read_family_support_detail(support_id: int):
    for support in family_support:
        if support.support_id == support_id:
            return support
    raise HTTPException(status_code=404, detail="Family support not found")

@app.put("/family-support/{support_id}")
async def update_family_support(support_id: int, support: FamilySupport):
    for i, existing_support in enumerate(family_support):
        if existing_support.support_id == support_id:
            family_support[i] = support
            return support
    raise HTTPException(status_code=404, detail="Family support not found")

@app.delete("/family-support/{support_id}")
async def delete_family_support(support_id: int):
    for i, support in enumerate(family_support):
        if support.support_id == support_id:
            del family_support[i]
            return {"message": "Family support deleted"}
    raise HTTPException(status_code=404, detail="Family support not found")
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
