"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Design a RESTful API for a fitness consulting platform that allows clients to select a plan, schedule appointments, and access their personalized workout plans, and provide example API endpoints and request/response formats.
Generated: DETERMINISTIC_f732fdb45270bf9e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(
    title="Fitness Consulting Platform API",
    description="API for managing fitness plans, appointments, and workout routines",
    version="1.0.0"
)

# Database Models
class PlanType(str, Enum):
    BASIC = "basic"
    PREMIUM = "premium"
    ELITE = "elite"

class AppointmentStatus(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Exercise(BaseModel):
    name: str
    sets: int
    reps: int
    duration_minutes: Optional[int] = None
    notes: Optional[str] = None

class WorkoutPlan(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    exercises: List[Exercise]
    created_at: datetime = Field(default_factory=datetime.now)

class Client(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    phone: Optional[str] = None
    plan_type: PlanType
    appointments: List['Appointment'] = []
    workout_plans: List[WorkoutPlan] = []

class Appointment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    client_id: UUID
    trainer_id: UUID
    date_time: datetime
    duration_minutes: int
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    notes: Optional[str] = None

# Database (in-memory for example)
db_clients: List[Client] = []
db_appointments: List[Appointment] = []
db_workout_plans: List[WorkoutPlan] = []

# Request Models
class ClientCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    plan_type: PlanType

class AppointmentCreate(BaseModel):
    client_id: UUID
    trainer_id: UUID
    date_time: datetime
    duration_minutes: int
    notes: Optional[str] = None

class WorkoutPlanCreate(BaseModel):
    name: str
    description: str
    exercises: List[Exercise]

# Response Models
class ClientResponse(BaseModel):
    id: UUID
    name: str
    email: str
    phone: Optional[str] = None
    plan_type: PlanType

class AppointmentResponse(BaseModel):
    id: UUID
    client_id: UUID
    trainer_id: UUID
    date_time: datetime
    duration_minutes: int
    status: AppointmentStatus
    notes: Optional[str] = None

class WorkoutPlanResponse(BaseModel):
    id: UUID
    name: str
    description: str
    exercises: List[Exercise]
    created_at: datetime

# Utility Functions
def get_client(client_id: UUID) -> Client:
    for client in db_clients:
        if client.id == client_id:
            return client
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Client with id {client_id} not found"
    )

# API Endpoints
@app.post("/clients/", response_model=ClientResponse, status_code=status.HTTP_201_CREATED)
async def create_client(client: ClientCreate):
    new_client = Client(**client.dict())
    db_clients.append(new_client)
    return new_client

@app.get("/clients/", response_model=List[ClientResponse])
async def get_all_clients():
    return db_clients

@app.get("/clients/{client_id}", response_model=ClientResponse)
async def get_client_by_id(client_id: UUID):
    return get_client(client_id)

@app.post("/appointments/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
async def create_appointment(appointment: AppointmentCreate):
    # Verify client exists
    get_client(appointment.client_id)
    
    new_appointment = Appointment(**appointment.dict())
    db_appointments.append(new_appointment)
    
    # Add appointment to client
    for client in db_clients:
        if client.id == appointment.client_id:
            client.appointments.append(new_appointment)
            break
    
    return new_appointment

@app.get("/appointments/{client_id}", response_model=List[AppointmentResponse])
async def get_client_appointments(client_id: UUID):
    get_client(client_id)  # Verify client exists
    return [appt for appt in db_appointments if appt.client_id == client_id]

@app.patch("/appointments/{appointment_id}/cancel", response_model=AppointmentResponse)
async def cancel_appointment(appointment_id: UUID):
    for appt in db_appointments:
        if appt.id == appointment_id:
            if appt.status == AppointmentStatus.CANCELLED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Appointment already cancelled"
                )
            appt.status = AppointmentStatus.CANCELLED
            return appt
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Appointment with id {appointment_id} not found"
    )

@app.post("/workout-plans/{client_id}", response_model=WorkoutPlanResponse, status_code=status.HTTP_201_CREATED)
async def create_workout_plan(client_id: UUID, workout_plan: WorkoutPlanCreate):
    client = get_client(client_id)
    new_workout_plan = WorkoutPlan(**workout_plan.dict())
    db_workout_plans.append(new_workout_plan)
    client.workout_plans.append(new_workout_plan)
    return new_workout_plan

@app.get("/workout-plans/{client_id}", response_model=List[WorkoutPlanResponse])
async def get_client_workout_plans(client_id: UUID):
    client = get_client(client_id)
    return client.workout_plans

@app.get("/workout-plans/details/{workout_plan_id}", response_model=WorkoutPlanResponse)
async def get_workout_plan_details(workout_plan_id: UUID):
    for plan in db_workout_plans:
        if plan.id == workout_plan_id:
            return plan
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Workout plan with id {workout_plan_id} not found"
    )
```
