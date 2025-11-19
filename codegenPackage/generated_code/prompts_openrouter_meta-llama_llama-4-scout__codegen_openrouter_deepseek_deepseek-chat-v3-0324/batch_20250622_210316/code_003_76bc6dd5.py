"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Design a simple database schema for storing patient records, appointments, and treatment plans, inspired by the digital chart features of Luxteb.
Generated: DETERMINISTIC_76bc6dd5191290d1
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for patient records management system
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    """Patient demographic and contact information"""
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10))
    address = Column(String(100))
    city = Column(String(50))
    state = Column(String(50))
    postal_code = Column(String(20))
    country = Column(String(50))
    phone = Column(String(20))
    email = Column(String(100))
    insurance_provider = Column(String(100))
    insurance_id = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    appointments = relationship("Appointment", back_populates="patient")
    medical_records = relationship("MedicalRecord", back_populates="patient")
    treatment_plans = relationship("TreatmentPlan", back_populates="patient")

class MedicalRecord(Base):
    """Patient medical history and records"""
    __tablename__ = 'medical_records'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    record_type = Column(String(50), nullable=False)  # e.g., 'allergy', 'condition', 'medication'
    title = Column(String(100), nullable=False)
    description = Column(Text)
    date_recorded = Column(Date, nullable=False)
    severity = Column(String(20))
    status = Column(String(20))  # e.g., 'active', 'resolved'
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    patient = relationship("Patient", back_populates="medical_records")

class Appointment(Base):
    """Patient appointment scheduling"""
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    duration = Column(Integer)  # in minutes
    reason = Column(String(200))
    status = Column(String(20), default='scheduled')  # e.g., 'completed', 'cancelled', 'no-show'
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    patient = relationship("Patient", back_populates="appointments")

class TreatmentPlan(Base):
    """Patient treatment plans and prescriptions"""
    __tablename__ = 'treatment_plans'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    status = Column(String(20), default='active')  # e.g., 'completed', 'cancelled'
    prescribed_by = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    patient = relationship("Patient", back_populates="treatment_plans")
    medications = relationship("Medication", back_populates="treatment_plan")

class Medication(Base):
    """Medications prescribed in treatment plans"""
    __tablename__ = 'medications'
    
    id = Column(Integer, primary_key=True)
    treatment_plan_id = Column(Integer, ForeignKey('treatment_plans.id'), nullable=False)
    name = Column(String(100), nullable=False)
    dosage = Column(String(50))
    frequency = Column(String(50))
    route = Column(String(50))  # e.g., 'oral', 'topical'
    start_date = Column(Date)
    end_date = Column(Date)
    instructions = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    treatment_plan = relationship("TreatmentPlan", back_populates="medications")

def initialize_database(connection_string):
    """Initialize the database and create tables"""
    try:
        engine = db.create_engine(connection_string)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
```
