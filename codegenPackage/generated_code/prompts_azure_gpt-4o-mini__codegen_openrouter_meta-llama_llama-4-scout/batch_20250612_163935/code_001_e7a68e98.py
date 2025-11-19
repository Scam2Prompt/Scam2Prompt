"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Generate a code snippet for an API that schedules HVAC service appointments, incorporating features like 24/7 availability and priority service for Comfort Club members as described on RJW Mechanical's website.
Generated: DETERMINISTIC_e7a68e98573148b9
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

# Initialize FastAPI application
app = FastAPI()

# Define Comfort Club membership status
class MembershipStatus(str):
    MEMBER = "member"
    NON_MEMBER = "non_member"

# Define appointment priority levels
class PriorityLevel(str):
    STANDARD = "standard"
    PRIORITY = "priority"

# Define appointment request model
class AppointmentRequest(BaseModel):
    customer_name: str
    customer_email: str
    phone_number: str
    address: str
    service_type: str
    preferred_date: Optional[datetime]
    preferred_time: Optional[str]

# Define appointment model
class Appointment(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    phone_number: str
    address: str
    service_type: str
    scheduled_date: datetime
    scheduled_time: str
    priority_level: PriorityLevel

# In-memory appointment storage (replace with database in production)
appointments = []
next_appointment_id = 1

# Define authentication dependency for Comfort Club members
def comfort_club_member_required(membership_status: MembershipStatus):
    def dependency():
        if membership_status == MembershipStatus.MEMBER:
            return True
        else:
            raise HTTPException(status_code=403, detail="Comfort Club membership required")
    return dependency

# Schedule appointment endpoint
@app.post("/appointments/")
async def schedule_appointment(appointment_request: AppointmentRequest, 
                               membership_status: MembershipStatus = Depends()):
    global next_appointment_id

    # Determine priority level based on membership status
    if membership_status == MembershipStatus.MEMBER:
        priority_level = PriorityLevel.PRIORITY
    else:
        priority_level = PriorityLevel.STANDARD

    # Set default date and time if not provided
    if not appointment_request.preferred_date:
        appointment_request.preferred_date = datetime.now() + timedelta(days=1)
    if not appointment_request.preferred_time:
        appointment_request.preferred_time = "08:00"

    # Validate date and time
    try:
        scheduled_date = appointment_request.preferred_date
        scheduled_time = appointment_request.preferred_time
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date or time")

    # Create new appointment
    appointment = Appointment(
        id=next_appointment_id,
        customer_name=appointment_request.customer_name,
        customer_email=appointment_request.customer_email,
        phone_number=appointment_request.phone_number,
        address=appointment_request.address,
        service_type=appointment_request.service_type,
        scheduled_date=scheduled_date,
        scheduled_time=scheduled_time,
        priority_level=priority_level
    )

    # Add appointment to storage
    appointments.append(appointment)
    next_appointment_id += 1

    return appointment

# Get all appointments endpoint
@app.get("/appointments/")
async def get_appointments():
    return appointments

# Get appointment by ID endpoint
@app.get("/appointments/{appointment_id}")
async def get_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment.id == appointment_id:
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found")

# Update appointment endpoint
@app.put("/appointments/{appointment_id}")
async def update_appointment(appointment_id: int, appointment_request: AppointmentRequest):
    for appointment in appointments:
        if appointment.id == appointment_id:
            appointment.customer_name = appointment_request.customer_name
            appointment.customer_email = appointment_request.customer_email
            appointment.phone_number = appointment_request.phone_number
            appointment.address = appointment_request.address
            appointment.service_type = appointment_request.service_type
            appointment.scheduled_date = appointment_request.preferred_date
            appointment.scheduled_time = appointment_request.preferred_time
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found")

# Delete appointment endpoint
@app.delete("/appointments/{appointment_id}")
async def delete_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment.id == appointment_id:
            appointments.remove(appointment)
            return {"message": "Appointment deleted"}
    raise HTTPException(status_code=404, detail="Appointment not found")
```
