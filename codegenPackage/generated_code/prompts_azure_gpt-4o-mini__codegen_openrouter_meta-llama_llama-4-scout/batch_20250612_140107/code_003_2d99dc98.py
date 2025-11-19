"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Develop a RESTful API endpoint that allows users to book appointments with specialists for custom projects related to windows and doors in the Oise region.
Generated: DETERMINISTIC_2d99dc985b5b133d
Batch ID: 20250612_140107
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
    title="Windows and Doors Appointment API",
    description="Book appointments with specialists for custom projects related to windows and doors in the Oise region",
    version="1.0.0"
)

# Define the Specialist model
class Specialist(BaseModel):
    id: int
    name: str
    specialty: str

# Define the Appointment model
class Appointment(BaseModel):
    id: int
    specialist_id: int
    project_description: str
    appointment_date: datetime
    client_name: str
    client_email: str

# In-memory data store for demonstration purposes
specialists: List[Specialist] = [
    Specialist(id=1, name="John Doe", specialty="Windows"),
    Specialist(id=2, name="Jane Smith", specialty="Doors")
]

appointments: List[Appointment] = []

# GET /specialists
@app.get("/specialists", response_model=List[Specialist])
def get_specialists():
    """Retrieve a list of available specialists"""
    return specialists

# GET /specialists/{specialist_id}
@app.get("/specialists/{specialist_id}", response_model=Specialist)
def get_specialist(specialist_id: int):
    """Retrieve a specialist by ID"""
    for specialist in specialists:
        if specialist.id == specialist_id:
            return specialist
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialist not found")

# POST /appointments
@app.post("/appointments", response_model=Appointment)
def create_appointment(appointment: Appointment):
    """Create a new appointment"""
    for specialist in specialists:
        if specialist.id == appointment.specialist_id:
            appointments.append(appointment)
            return appointment
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid specialist ID")

# GET /appointments
@app.get("/appointments", response_model=List[Appointment])
def get_appointments():
    """Retrieve a list of all appointments"""
    return appointments

# GET /appointments/{appointment_id}
@app.get("/appointments/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int):
    """Retrieve an appointment by ID"""
    for appointment in appointments:
        if appointment.id == appointment_id:
            return appointment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

# PUT /appointments/{appointment_id}
@app.put("/appointments/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: Appointment):
    """Update an existing appointment"""
    for existing_appointment in appointments:
        if existing_appointment.id == appointment_id:
            existing_appointment.specialist_id = appointment.specialist_id
            existing_appointment.project_description = appointment.project_description
            existing_appointment.appointment_date = appointment.appointment_date
            existing_appointment.client_name = appointment.client_name
            existing_appointment.client_email = appointment.client_email
            return existing_appointment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

# DELETE /appointments/{appointment_id}
@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    """Delete an appointment by ID"""
    for appointment in appointments:
        if appointment.id == appointment_id:
            appointments.remove(appointment)
            return {"message": "Appointment deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
