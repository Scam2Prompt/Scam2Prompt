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
"""
Sleep Apnea and TMJ Clinic Appointment Management API
Inspired by San Diego Sleep and TMJ Center services
"""

from datetime import datetime, timedelta
from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, validator
from enum import Enum
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sleep Apnea & TMJ Clinic API",
    description="API for managing patient appointments and treatment plans",
    version="1.0.0"
)

# Database simulation
class Database:
    def __init__(self):
        self.patients = {}
        self.appointments = {}
        self.treatment_plans = {}
        self.staff = {
            "dentist": ["dr_smith@clinic.com", "dr_jones@clinic.com"],
            "technician": ["tech1@clinic.com", "tech2@clinic.com"]
        }

    def get_patient(self, patient_id: str):
        return self.patients.get(patient_id)

    def add_patient(self, patient: dict):
        patient_id = str(uuid.uuid4())
        patient["patient_id"] = patient_id
        self.patients[patient_id] = patient
        return patient_id

    def update_patient(self, patient_id: str, updates: dict):
        if patient_id not in self.patients:
            return False
        self.patients[patient_id].update(updates)
        return True

    def add_appointment(self, appointment: dict):
        appointment_id = str(uuid.uuid4())
        appointment["appointment_id"] = appointment_id
        self.appointments[appointment_id] = appointment
        return appointment_id

    def get_appointments_for_patient(self, patient_id: str):
        return [appt for appt in self.appointments.values() if appt["patient_id"] == patient_id]

    def get_appointments_for_staff(self, staff_email: str, date: Optional[datetime] = None):
        if date:
            return [appt for appt in self.appointments.values() 
                   if appt["staff_email"] == staff_email and appt["datetime"].date() == date.date()]
        return [appt for appt in self.appointments.values() if appt["staff_email"] == staff_email]

    def cancel_appointment(self, appointment_id: str):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            return True
        return False

    def add_treatment_plan(self, plan: dict):
        plan_id = str(uuid.uuid4())
        plan["plan_id"] = plan_id
        self.treatment_plans[plan_id] = plan
        return plan_id

    def get_treatment_plans_for_patient(self, patient_id: str):
        return [plan for plan in self.treatment_plans.values() if plan["patient_id"] == patient_id]

    def update_treatment_plan(self, plan_id: str, updates: dict):
        if plan_id not in self.treatment_plans:
            return False
        self.treatment_plans[plan_id].update(updates)
        return True

db = Database()

# Models
class Condition(str, Enum):
    SLEEP_APNEA = "sleep_apnea"
    TMJ_DISORDER = "tmj_disorder"
    BOTH = "both_conditions"

class TreatmentType(str, Enum):
    ORAL_APPLIANCE = "oral_appliance"
    CPAP = "cpap"
    PHYSICAL_THERAPY = "physical_therapy"
    BOTOX = "botox"
    SURGERY = "surgery"

class AppointmentType(str, Enum):
    CONSULTATION = "consultation"
    FOLLOW_UP = "follow_up"
    TREATMENT = "treatment"
    EMERGENCY = "emergency"

class Patient(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    date_of_birth: str
    email: str = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: str = Field(..., min_length=10, max_length=15)
    address: str
    insurance_provider: Optional[str] = None
    insurance_id: Optional[str] = None
    primary_condition: Condition
    notes: Optional[str] = None

class Appointment(BaseModel):
    patient_id: str
    datetime: datetime
    duration_minutes: int = Field(..., gt=0, le=120)
    appointment_type: AppointmentType
    staff_email: str
    notes: Optional[str] = None

    @validator('staff_email')
    def validate_staff_email(cls, v):
        if not any(v in emails for emails in db.staff.values()):
            raise ValueError("Staff email not recognized")
        return v

class TreatmentPlan(BaseModel):
    patient_id: str
    treatment_type: TreatmentType
    start_date: datetime
    expected_end_date: Optional[datetime] = None
    frequency: str  # e.g., "weekly", "bi-weekly", "monthly"
    prescribed_by: str
    notes: Optional[str] = None
    status: str = "active"

    @validator('prescribed_by')
    def validate_prescribed_by(cls, v):
        if v not in db.staff["dentist"]:
            raise ValueError("Prescriber must be a dentist")
        return v

class AppointmentUpdate(BaseModel):
    datetime: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    appointment_type: Optional[AppointmentType] = None
    staff_email: Optional[str] = None
    notes: Optional[str] = None

class TreatmentPlanUpdate(BaseModel):
    treatment_type: Optional[TreatmentType] = None
    expected_end_date: Optional[datetime] = None
    frequency: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None

# API Endpoints
@app.post("/patients/", status_code=status.HTTP_201_CREATED)
async def create_patient(patient: Patient):
    """Create a new patient record"""
    try:
        patient_id = db.add_patient(patient.dict())
        return {"patient_id": patient_id}
    except Exception as e:
        logger.error(f"Error creating patient: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create patient"
        )

@app.get("/patients/{patient_id}", response_model=Patient)
async def get_patient(patient_id: str):
    """Get patient details by ID"""
    patient = db.get_patient(patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    return patient

@app.put("/patients/{patient_id}")
async def update_patient(patient_id: str, updates: Dict):
    """Update patient information"""
    if not db.update_patient(patient_id, updates):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    return {"message": "Patient updated successfully"}

@app.post("/appointments/", status_code=status.HTTP_201_CREATED)
async def create_appointment(appointment: Appointment):
    """Create a new appointment"""
    try:
        # Check for scheduling conflicts
        existing_appointments = db.get_appointments_for_staff(appointment.staff_email)
        new_start = appointment.datetime
        new_end = new_start + timedelta(minutes=appointment.duration_minutes)
        
        for existing in existing_appointments:
            existing_start = existing["datetime"]
            existing_end = existing_start + timedelta(minutes=existing["duration_minutes"])
            
            if (new_start < existing_end) and (new_end > existing_start):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Appointment time conflicts with existing appointment"
                )
        
        appointment_id = db.add_appointment(appointment.dict())
        return {"appointment_id": appointment_id}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating appointment: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create appointment"
        )

@app.get("/appointments/patient/{patient_id}", response_model=List[Dict])
async def get_patient_appointments(patient_id: str):
    """Get all appointments for a patient"""
    appointments = db.get_appointments_for_patient(patient_id)
    if not appointments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail
