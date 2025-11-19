"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Illustrate how to implement a booking system for service appointments at a 3S workshop, inspired by the services provided by Suzuki Capital Motors.
Generated: DETERMINISTIC_57ee35b11325ee5e
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(
    title="3S Workshop Booking System",
    description="API for managing service appointments at a 3S workshop",
    version="1.0.0"
)

# Database simulation
db = {
    "appointments": {},
    "customers": {},
    "services": {},
    "vehicles": {},
    "time_slots": {}
}

class ServiceType(str, Enum):
    MAINTENANCE = "Maintenance"
    REPAIR = "Repair"
    INSPECTION = "Inspection"
    CUSTOM = "Custom Service"

class VehicleType(str, Enum):
    MOTORCYCLE = "Motorcycle"
    CAR = "Car"
    SUV = "SUV"
    COMMERCIAL = "Commercial Vehicle"

class Customer(BaseModel):
    id: str = Field(default_factory=lambda: str(len(db["customers"]) + 1))
    name: str
    email: str
    phone: str
    address: Optional[str] = None

    @validator('email')
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v

class Vehicle(BaseModel):
    id: str = Field(default_factory=lambda: str(len(db["vehicles"]) + 1))
    customer_id: str
    make: str
    model: str
    year: int
    license_plate: str
    type: VehicleType
    mileage: Optional[int] = None

    @validator('year')
    def validate_year(cls, v):
        current_year = datetime.datetime.now().year
        if v < 1900 or v > current_year + 1:
            raise ValueError(f"Year must be between 1900 and {current_year + 1}")
        return v

class Service(BaseModel):
    id: str = Field(default_factory=lambda: str(len(db["services"]) + 1))
    name: str
    description: str
    service_type: ServiceType
    estimated_duration: int  # in minutes
    base_price: float

class TimeSlot(BaseModel):
    id: str = Field(default_factory=lambda: str(len(db["time_slots"]) + 1))
    start_time: datetime.datetime
    end_time: datetime.datetime
    mechanic_id: str
    is_available: bool = True

    @validator('end_time')
    def validate_times(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError("End time must be after start time")
        return v

class Appointment(BaseModel):
    id: str = Field(default_factory=lambda: str(len(db["appointments"]) + 1))
    customer_id: str
    vehicle_id: str
    service_id: str
    time_slot_id: str
    notes: Optional[str] = None
    status: str = "Scheduled"
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    customer_data = jsonable_encoder(customer)
    db["customers"][customer.id] = customer_data
    return JSONResponse(content=customer_data, status_code=status.HTTP_201_CREATED)

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: str):
    if customer_id not in db["customers"]:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db["customers"][customer_id]

@app.post("/vehicles/", response_model=Vehicle, status_code=status.HTTP_201_CREATED)
async def create_vehicle(vehicle: Vehicle):
    if vehicle.customer_id not in db["customers"]:
        raise HTTPException(status_code=400, detail="Customer does not exist")
    vehicle_data = jsonable_encoder(vehicle)
    db["vehicles"][vehicle.id] = vehicle_data
    return JSONResponse(content=vehicle_data, status_code=status.HTTP_201_CREATED)

@app.get("/vehicles/{vehicle_id}", response_model=Vehicle)
async def get_vehicle(vehicle_id: str):
    if vehicle_id not in db["vehicles"]:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db["vehicles"][vehicle_id]

@app.post("/services/", response_model=Service, status_code=status.HTTP_201_CREATED)
async def create_service(service: Service):
    service_data = jsonable_encoder(service)
    db["services"][service.id] = service_data
    return JSONResponse(content=service_data, status_code=status.HTTP_201_CREATED)

@app.get("/services/", response_model=List[Service])
async def list_services():
    return list(db["services"].values())

@app.post("/timeslots/", response_model=TimeSlot, status_code=status.HTTP_201_CREATED)
async def create_timeslot(timeslot: TimeSlot):
    timeslot_data = jsonable_encoder(timeslot)
    db["time_slots"][timeslot.id] = timeslot_data
    return JSONResponse(content=timeslot_data, status_code=status.HTTP_201_CREATED)

@app.get("/timeslots/available", response_model=List[TimeSlot])
async def get_available_timeslots():
    available = [ts for ts in db["time_slots"].values() if ts["is_available"]]
    return available

@app.post("/appointments/", response_model=Appointment, status_code=status.HTTP_201_CREATED)
async def create_appointment(appointment: Appointment):
    # Validate references exist
    if appointment.customer_id not in db["customers"]:
        raise HTTPException(status_code=400, detail="Customer does not exist")
    if appointment.vehicle_id not in db["vehicles"]:
        raise HTTPException(status_code=400, detail="Vehicle does not exist")
    if appointment.service_id not in db["services"]:
        raise HTTPException(status_code=400, detail="Service does not exist")
    if appointment.time_slot_id not in db["time_slots"]:
        raise HTTPException(status_code=400, detail="Time slot does not exist")
    
    # Check time slot availability
    timeslot = db["time_slots"][appointment.time_slot_id]
    if not timeslot["is_available"]:
        raise HTTPException(status_code=400, detail="Time slot is not available")
    
    # Mark time slot as booked
    timeslot["is_available"] = False
    db["time_slots"][appointment.time_slot_id] = timeslot
    
    # Create appointment
    appointment_data = jsonable_encoder(appointment)
    db["appointments"][appointment.id] = appointment_data
    
    return JSONResponse(content=appointment_data, status_code=status.HTTP_201_CREATED)

@app.get("/appointments/{appointment_id}", response_model=Appointment)
async def get_appointment(appointment_id: str):
    if appointment_id not in db["appointments"]:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db["appointments"][appointment_id]

@app.get("/appointments/customer/{customer_id}", response_model=List[Appointment])
async def get_customer_appointments(customer_id: str):
    if customer_id not in db["customers"]:
        raise HTTPException(status_code=404, detail="Customer not found")
    return [appt for appt in db["appointments"].values() if appt["customer_id"] == customer_id]

@app.put("/appointments/{appointment_id}/cancel", response_model=Appointment)
async def cancel_appointment(appointment_id: str):
    if appointment_id not in db["appointments"]:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    appointment = db["appointments"][appointment_id]
    appointment["status"] = "Cancelled"
    
    # Free up the time slot
    timeslot_id = appointment["time_slot_id"]
    db["time_slots"][timeslot_id]["is_available"] = True
    
    return appointment

@app.get("/")
async def root():
    return {"message": "3S Workshop Booking System API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
