"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Create a RESTful API specification for a dental practice that includes endpoints for services such as sbiancamento dentale and ortodonzia invisibile, inspired by the offerings of Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_e59f908cc2a291c5
Batch ID: 20250612_135547
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

app = FastAPI(
    title="Dental Practice API",
    description="API for Studio Dentistico dott.ssa Vira Palazzo services",
    version="1.0.0"
)

# Define a model for services
class Service(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Define a model for appointments
class Appointment(BaseModel):
    id: int
    patient_name: str
    service_id: int
    date: str

# In-memory data store for services and appointments
services: List[Service] = [
    Service(id=1, name="Sbiancamento Dentale", description="Teeth whitening service", price=200.0),
    Service(id=2, name="Ortodonzìa Invisibile", description="Invisible orthodontic service", price=500.0)
]

appointments: List[Appointment] = []

# Endpoint to get all services
@app.get("/services/")
async def get_services():
    """Returns a list of all services offered by the dental practice"""
    return services

# Endpoint to get a service by ID
@app.get("/services/{service_id}")
async def get_service(service_id: int):
    """Returns a service by ID"""
    for service in services:
        if service.id == service_id:
            return service
    raise HTTPException(status_code=404, detail="Service not found")

# Endpoint to create a new appointment
@app.post("/appointments/")
async def create_appointment(appointment: Appointment):
    """Creates a new appointment"""
    for service in services:
        if service.id == appointment.service_id:
            appointments.append(appointment)
            return appointment
    raise HTTPException(status_code=400, detail="Invalid service ID")

# Endpoint to get all appointments
@app.get("/appointments/")
async def get_appointments():
    """Returns a list of all appointments"""
    return appointments

# Endpoint to get an appointment by ID
@app.get("/appointments/{appointment_id}")
async def get_appointment(appointment_id: int):
    """Returns an appointment by ID"""
    for appointment in appointments:
        if appointment.id == appointment_id:
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found")

# Error handler for 404 errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
