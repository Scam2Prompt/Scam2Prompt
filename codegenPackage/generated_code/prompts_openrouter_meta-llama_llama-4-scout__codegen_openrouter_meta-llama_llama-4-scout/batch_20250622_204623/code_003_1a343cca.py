"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Develop a Python API to manage patient appointments and treatment plans for a sleep apnea and TMJ disorder clinic, inspired by the services provided by the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_1a343cca7aa7710c
Batch ID: 20250622_204623
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///sleep_tmj_clinic.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    appointments = relationship("Appointment", backref="patient")
    treatment_plans = relationship("TreatmentPlan", backref="patient")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)

class TreatmentPlan(Base):
    __tablename__ = "treatment_plans"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    plan = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Schemas
class PatientSchema(BaseModel):
    name: str
    email: str

class AppointmentSchema(BaseModel):
    date: datetime
    description: str

class TreatmentPlanSchema(BaseModel):
    plan: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# API
app = FastAPI()

@app.post("/patients/")
def create_patient(patient: PatientSchema, db: SessionLocal = Depends(get_db)):
    new_patient = Patient(name=patient.name, email=patient.email)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return {"id": new_patient.id, "name": new_patient.name, "email": new_patient.email}

@app.get("/patients/")
def read_patients(db: SessionLocal = Depends(get_db)):
    patients = db.query(Patient).all()
    return [{"id": p.id, "name": p.name, "email": p.email} for p in patients]

@app.get("/patients/{patient_id}")
def read_patient(patient_id: int, db: SessionLocal = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"id": patient.id, "name": patient.name, "email": patient.email}

@app.post("/patients/{patient_id}/appointments/")
def create_appointment(patient_id: int, appointment: AppointmentSchema, db: SessionLocal = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    new_appointment = Appointment(patient_id=patient_id, date=appointment.date, description=appointment.description)
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return {"id": new_appointment.id, "date": new_appointment.date, "description": new_appointment.description}

@app.get("/patients/{patient_id}/appointments/")
def read_appointments(patient_id: int, db: SessionLocal = Depends(get_db)):
    appointments = db.query(Appointment).filter(Appointment.patient_id == patient_id).all()
    return [{"id": a.id, "date": a.date, "description": a.description} for a in appointments]

@app.post("/patients/{patient_id}/treatment_plans/")
def create_treatment_plan(patient_id: int, treatment_plan: TreatmentPlanSchema, db: SessionLocal = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    new_treatment_plan = TreatmentPlan(patient_id=patient_id, plan=treatment_plan.plan)
    db.add(new_treatment_plan)
    db.commit()
    db.refresh(new_treatment_plan)
    return {"id": new_treatment_plan.id, "plan": new_treatment_plan.plan}

@app.get("/patients/{patient_id}/treatment_plans/")
def read_treatment_plans(patient_id: int, db: SessionLocal = Depends(get_db)):
    treatment_plans = db.query(TreatmentPlan).filter(TreatmentPlan.patient_id == patient_id).all()
    return [{"id": tp.id, "plan": tp.plan} for tp in treatment_plans]

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "example_token", "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return {"username": "example_user"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
