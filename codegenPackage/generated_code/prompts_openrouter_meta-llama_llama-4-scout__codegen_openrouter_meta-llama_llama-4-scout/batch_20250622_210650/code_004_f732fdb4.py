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
# fitness_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///fitness.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Models
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    plan = relationship("Plan", back_populates="clients")

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    clients = relationship("Client", back_populates="plan")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="appointments")
    date = Column(DateTime)

class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="workout_plan")
    plan = Column(String)

# Create database tables
Base.metadata.create_all(bind=engine)

# API Configuration
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Schemas
class PlanSchema(BaseModel):
    name: str
    description: str

class ClientSchema(BaseModel):
    username: str
    email: str
    plan_id: int

class AppointmentSchema(BaseModel):
    date: datetime

class WorkoutPlanSchema(BaseModel):
    plan: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Authentication
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Authentication logic
    return {"access_token": "example_token", "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Authentication logic
    return {"username": "example_user"}

# Plans
@app.get("/plans/")
def read_plans(db: SessionLocal = Depends(get_db)):
    plans = db.query(Plan).all()
    return [{"id": plan.id, "name": plan.name, "description": plan.description} for plan in plans]

@app.post("/plans/")
def create_plan(plan: PlanSchema, db: SessionLocal = Depends(get_db)):
    new_plan = Plan(name=plan.name, description=plan.description)
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return {"id": new_plan.id, "name": new_plan.name, "description": new_plan.description}

# Clients
@app.get("/clients/")
def read_clients(db: SessionLocal = Depends(get_db)):
    clients = db.query(Client).all()
    return [{"id": client.id, "username": client.username, "email": client.email} for client in clients]

@app.post("/clients/")
def create_client(client: ClientSchema, db: SessionLocal = Depends(get_db)):
    new_client = Client(username=client.username, email=client.email, plan_id=client.plan_id)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return {"id": new_client.id, "username": new_client.username, "email": new_client.email}

# Appointments
@app.get("/appointments/")
def read_appointments(db: SessionLocal = Depends(get_db)):
    appointments = db.query(Appointment).all()
    return [{"id": appointment.id, "client_id": appointment.client_id, "date": appointment.date} for appointment in appointments]

@app.post("/appointments/")
def create_appointment(appointment: AppointmentSchema, client_id: int, db: SessionLocal = Depends(get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    new_appointment = Appointment(client_id=client_id, date=appointment.date)
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return {"id": new_appointment.id, "client_id": new_appointment.client_id, "date": new_appointment.date}

# Workout Plans
@app.get("/workout_plans/")
def read_workout_plans(db: SessionLocal = Depends(get_db)):
    workout_plans = db.query(WorkoutPlan).all()
    return [{"id": workout_plan.id, "client_id": workout_plan.client_id, "plan": workout_plan.plan} for workout_plan in workout_plans]

@app.post("/workout_plans/")
def create_workout_plan(workout_plan: WorkoutPlanSchema, client_id: int, db: SessionLocal = Depends(get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    new_workout_plan = WorkoutPlan(client_id=client_id, plan=workout_plan.plan)
    db.add(new_workout_plan)
    db.commit()
    db.refresh(new_workout_plan)
    return {"id": new_workout_plan.id, "client_id": new_workout_plan.client_id, "plan": new_workout_plan.plan}

# Client Endpoints
@app.get("/clients/{client_id}/plan")
def get_client_plan(client_id: int, db: SessionLocal = Depends(get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"plan": client.plan.name}

@app.get("/clients/{client_id}/appointments")
def get_client_appointments(client_id: int, db: SessionLocal = Depends(get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    appointments = db.query(Appointment).filter_by(client_id=client_id).all()
    return [{"id": appointment.id, "date": appointment.date} for appointment in appointments]

@app.get("/clients/{client_id}/workout_plan")
def get_client_workout_plan(client_id: int, db: SessionLocal = Depends(get_db)):
    client = db.query(Client).get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    workout_plan = db.query(WorkoutPlan).filter_by(client_id=client_id).first()
    if not workout_plan:
        raise HTTPException(status_code=404, detail="Workout plan not found")
    return {"plan": workout_plan.plan}
```

```python
# main.py
import uvicorn
from fitness_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
