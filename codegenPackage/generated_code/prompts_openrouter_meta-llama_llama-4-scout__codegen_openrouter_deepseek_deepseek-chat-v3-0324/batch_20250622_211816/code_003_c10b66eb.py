"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Design an API for a property management system that integrates with financial planners, mortgage brokers, accountants, and solicitors, similar to Bebold Properties' network of trusted experts.
Generated: DETERMINISTIC_c10b66eb564f7240
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import uuid4
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Property Management System API",
    description="API for property management system integrating with financial planners, mortgage brokers, accountants, and solicitors.",
    version="1.0.0"
)

# Database models (in a real app, this would connect to a database)
class Database:
    def __init__(self):
        self.properties = []
        self.professionals = []
        self.users = []
        self.appointments = []

db = Database()

# Pydantic models for request/response validation
class ProfessionalBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    profession: str  # e.g., "accountant", "solicitor", etc.
    company: Optional[str] = None
    years_experience: Optional[int] = None

class ProfessionalCreate(ProfessionalBase):
    pass

class Professional(ProfessionalBase):
    id: str

    class Config:
        orm_mode = True

class PropertyBase(BaseModel):
    address: str
    postcode: str
    property_type: str
    bedrooms: int
    bathrooms: int
    owner_id: str

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    property_id: str
    professional_id: str
    user_id: str
    appointment_time: datetime
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str

    class Config:
        orm_mode = True

# Helper functions
def get_professional(professional_id: str):
    professional = next((p for p in db.professionals if p.id == professional_id), None)
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    return professional

def get_property(property_id: str):
    property = next((p for p in db.properties if p.id == property_id), None)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

def get_user(user_id: str):
    user = next((u for u in db.users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_appointment(appointment_id: str):
    appointment = next((a for a in db.appointments if a.id == appointment_id), None)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

# API endpoints
@app.post("/professionals/", response_model=Professional, status_code=status.HTTP_201_CREATED)
async def create_professional(professional: ProfessionalCreate):
    """
    Create a new professional (financial planner, mortgage broker, etc.)
    """
    try:
        db_professional = Professional(
            id=str(uuid4()),
            **professional.dict()
        )
        db.professionals.append(db_professional)
        logger.info(f"Created professional with ID: {db_professional.id}")
        return db_professional
    except Exception as e:
        logger.error(f"Error creating professional: {str(e)}")
        raise HTTPException(status_code=400, detail="Error creating professional")

@app.get("/professionals/", response_model=List[Professional])
async def get_professionals(profession: Optional[str] = None):
    """
    Get all professionals, optionally filtered by profession
    """
    try:
        if profession:
            return [p for p in db.professionals if p.profession.lower() == profession.lower()]
        return db.professionals
    except Exception as e:
        logger.error(f"Error retrieving professionals: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving professionals")

@app.post("/properties/", response_model=Property, status_code=status.HTTP_201_CREATED)
async def create_property(property: PropertyCreate):
    """
    Create a new property
    """
    try:
        now = datetime.now()
        db_property = Property(
            id=str(uuid4()),
            created_at=now,
            updated_at=now,
            **property.dict()
        )
        db.properties.append(db_property)
        logger.info(f"Created property with ID: {db_property.id}")
        return db_property
    except Exception as e:
        logger.error(f"Error creating property: {str(e)}")
        raise HTTPException(status_code=400, detail="Error creating property")

@app.get("/properties/{property_id}", response_model=Property)
async def get_property_by_id(property_id: str):
    """
    Get a property by ID
    """
    return get_property(property_id)

@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """
    Create a new user
    """
    try:
        db_user = User(
            id=str(uuid4()),
            **user.dict()
        )
        db.users.append(db_user)
        logger.info(f"Created user with ID: {db_user.id}")
        return db_user
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        raise HTTPException(status_code=400, detail="Error creating user")

@app.post("/appointments/", response_model=Appointment, status_code=status.HTTP_201_CREATED)
async def create_appointment(appointment: AppointmentCreate):
    """
    Create a new appointment with a professional
    """
    try:
        # Validate references
        get_property(appointment.property_id)
        get_professional(appointment.professional_id)
        get_user(appointment.user_id)

        db_appointment = Appointment(
            id=str(uuid4()),
            created_at=datetime.now(),
            **appointment.dict()
        )
        db.appointments.append(db_appointment)
        logger.info(f"Created appointment with ID: {db_appointment.id}")
        return db_appointment
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error creating appointment: {str(e)}")
        raise HTTPException(status_code=400, detail="Error creating appointment")

@app.get("/appointments/{appointment_id}", response_model=Appointment)
async def get_appointment_by_id(appointment_id: str):
    """
    Get an appointment by ID
    """
    return get_appointment(appointment_id)

@app.get("/appointments/property/{property_id}", response_model=List[Appointment])
async def get_appointments_by_property(property_id: str):
    """
    Get all appointments for a property
    """
    try:
        get_property(property_id)  # Validate property exists
        return [a for a in db.appointments if a.property_id == property_id]
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error retrieving appointments: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving appointments")

@app.get("/appointments/professional/{professional_id}", response_model=List[Appointment])
async def get_appointments_by_professional(professional_id: str):
    """
    Get all appointments for a professional
    """
    try:
        get_professional(professional_id)  # Validate professional exists
        return [a for a in db.appointments if a.professional_id == professional_id]
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error retrieving appointments: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving appointments")
```
