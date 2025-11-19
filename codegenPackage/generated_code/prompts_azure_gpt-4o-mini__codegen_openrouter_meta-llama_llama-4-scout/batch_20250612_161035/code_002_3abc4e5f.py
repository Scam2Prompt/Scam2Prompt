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
# health_service_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
import uvicorn

# Define the FastAPI application
app = FastAPI(
    title="Health Service API",
    description="API specification for a health service application that integrates with the Sistema Único de Saúde",
    version="1.0.0"
)

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define the patient model
class Patient(BaseModel):
    id: int
    name: str
    cpf: str
    birth_date: str

# Define the service model
class Service(BaseModel):
    id: int
    name: str
    description: str

# In-memory patient and service storage (replace with a database in production)
patients: List[Patient] = [
    Patient(id=1, name="John Doe", cpf="12345678901", birth_date="1990-01-01"),
]

services: List[Service] = [
    Service(id=1, name="Medical Consultation", description="Medical consultation service"),
]

# Define the authentication endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Replace with actual authentication logic
    if form_data.username == "admin" and form_data.password == "password":
        return {"access_token": "admin_token", "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Define the patient endpoints
@app.get("/patients/")
async def read_patients(token: str = Depends(oauth2_scheme)):
    return patients

@app.get("/patients/{patient_id}")
async def read_patient(patient_id: int, token: str = Depends(oauth2_scheme)):
    patient = next((p for p in patients if p.id == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.post("/patients/")
async def create_patient(patient: Patient, token: str = Depends(oauth2_scheme)):
    patients.append(patient)
    return patient

@app.put("/patients/{patient_id}")
async def update_patient(patient_id: int, patient: Patient, token: str = Depends(oauth2_scheme)):
    existing_patient = next((p for p in patients if p.id == patient_id), None)
    if existing_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    existing_patient.name = patient.name
    existing_patient.cpf = patient.cpf
    existing_patient.birth_date = patient.birth_date
    return existing_patient

@app.delete("/patients/{patient_id}")
async def delete_patient(patient_id: int, token: str = Depends(oauth2_scheme)):
    patient = next((p for p in patients if p.id == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    patients.remove(patient)
    return {"message": "Patient deleted"}

# Define the service endpoints
@app.get("/services/")
async def read_services(token: str = Depends(oauth2_scheme)):
    return services

@app.get("/services/{service_id}")
async def read_service(service_id: int, token: str = Depends(oauth2_scheme)):
    service = next((s for s in services if s.id == service_id), None)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
