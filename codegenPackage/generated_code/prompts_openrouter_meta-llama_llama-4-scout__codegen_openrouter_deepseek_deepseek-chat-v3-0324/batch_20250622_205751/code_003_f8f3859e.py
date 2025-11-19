"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Write a Python API for retrieving patient appointment schedules and doctor details, similar to Dr. S Nagendra Boopathy's practice.
Generated: DETERMINISTIC_f8f3859e620f6836
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from typing import List, Optional, Dict
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

# MongoDB configuration
MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "clinic_db"

# Initialize FastAPI app
app = FastAPI(
    title="Clinic Appointment API",
    description="API for managing patient appointments and doctor details",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB client setup
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client[DB_NAME]

# Models
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Doctor(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(..., min_length=3)
    specialization: str
    contact_number: str = Field(..., regex=r"^[0-9]{10}$")
    email: str = Field(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    available_days: List[str]
    available_hours: Dict[str, List[str]]

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Dr. S Nagendra Boopathy",
                "specialization": "General Physician",
                "contact_number": "9876543210",
                "email": "doctor@example.com",
                "available_days": ["Monday", "Wednesday", "Friday"],
                "available_hours": {
                    "Monday": ["09:00-12:00", "14:00-17:00"],
                    "Wednesday": ["10:00-13:00"],
                    "Friday": ["09:00-11:00", "15:00-18:00"]
                }
            }
        }

class Patient(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(..., min_length=3)
    contact_number: str = Field(..., regex=r"^[0-9]{10}$")
    email: str = Field(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "John Doe",
                "contact_number": "9876543210",
                "email": "patient@example.com"
            }
        }

class Appointment(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    patient_id: PyObjectId
    doctor_id: PyObjectId
    date: str = Field(..., regex=r"^\d{4}-\d{2}-\d{2}$")
    time_slot: str = Field(..., regex=r"^\d{2}:\d{2}-\d{2}:\d{2}$")
    status: str = Field(default="scheduled", regex=r"^(scheduled|completed|cancelled)$")
    notes: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "patient_id": "507f1f77bcf86cd799439011",
                "doctor_id": "507f191e810c19729de860ea",
                "date": "2023-12-15",
                "time_slot": "10:00-11:00",
                "status": "scheduled",
                "notes": "Regular checkup"
            }
        }

class AppointmentCreate(BaseModel):
    patient_id: str
    doctor_id: str
    date: str
    time_slot: str
    notes: Optional[str] = None

# Helper functions
async def get_doctor_or_404(doctor_id: str):
    doctor = await db.doctors.find_one({"_id": ObjectId(doctor_id)})
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found"
        )
    return doctor

async def get_patient_or_404(patient_id: str):
    patient = await db.patients.find_one({"_id": ObjectId(patient_id)})
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    return patient

async def get_appointment_or_404(appointment_id: str):
    appointment = await db.appointments.find_one({"_id": ObjectId(appointment_id)})
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    return appointment

# Routes
@app.get("/doctors/", response_model=List[Doctor], tags=["Doctors"])
async def list_doctors():
    doctors = await db.doctors.find().to_list(1000)
    return doctors

@app.get("/doctors/{doctor_id}", response_model=Doctor, tags=["Doctors"])
async def get_doctor(doctor_id: str):
    doctor = await get_doctor_or_404(doctor_id)
    return doctor

@app.post("/doctors/", response_model=Doctor, status_code=status.HTTP_201_CREATED, tags=["Doctors"])
async def create_doctor(doctor: Doctor):
    existing_doctor = await db.doctors.find_one({"email": doctor.email})
    if existing_doctor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Doctor with this email already exists"
        )
    
    doctor_dict = doctor.dict(by_alias=True)
    await db.doctors.insert_one(doctor_dict)
    return doctor

@app.get("/patients/", response_model=List[Patient], tags=["Patients"])
async def list_patients():
    patients = await db.patients.find().to_list(1000)
    return patients

@app.get("/patients/{patient_id}", response_model=Patient, tags=["Patients"])
async def get_patient(patient_id: str):
    patient = await get_patient_or_404(patient_id)
    return patient

@app.post("/patients/", response_model=Patient, status_code=status.HTTP_201_CREATED, tags=["Patients"])
async def create_patient(patient: Patient):
    existing_patient = await db.patients.find_one({"email": patient.email})
    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Patient with this email already exists"
        )
    
    patient_dict = patient.dict(by_alias=True)
    await db.patients.insert_one(patient_dict)
    return patient

@app.get("/appointments/", response_model=List[Appointment], tags=["Appointments"])
async def list_appointments():
    appointments = await db.appointments.find().to_list(1000)
    return appointments

@app.get("/appointments/{appointment_id}", response_model=Appointment, tags=["Appointments"])
async def get_appointment(appointment_id: str):
    appointment = await get_appointment_or_404(appointment_id)
    return appointment

@app.post("/appointments/", response_model=Appointment, status_code=status.HTTP_201_CREATED, tags=["Appointments"])
async def create_appointment(appointment: AppointmentCreate):
    # Validate doctor exists
    doctor = await get_doctor_or_404(appointment.doctor_id)
    
    # Validate patient exists
    patient = await get_patient_or_404(appointment.patient_id)
    
    # Validate date format
    try:
        datetime.strptime(appointment.date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid date format. Use YYYY-MM-DD"
        )
    
    # Check if doctor is available at the requested time
    day_of_week = datetime.strptime(appointment.date, "%Y-%m-%d").strftime("%A")
    if day_of_week not in doctor["available_d
