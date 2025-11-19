"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: "Design a system architecture for a multidisciplinary team to manage patient data and therapy plans, considering outcome-based mindset and holistic assessment, as described in ICON's approach."
Generated: DETERMINISTIC_e488d0b9af35a183
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Patient Data and Therapy Plan Management System
Architecture for multidisciplinary teams with outcome-based mindset
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Optional
import uuid
import json
from enum import Enum, auto
import logging
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, String, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./patient_data.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums
class TherapyStatus(Enum):
    PLANNED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class AssessmentDomain(Enum):
    PHYSICAL = auto()
    PSYCHOLOGICAL = auto()
    SOCIAL = auto()
    ENVIRONMENTAL = auto()

# Database Models
class DBPatient(Base):
    __tablename__ = "patients"
    
    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    assessments = relationship("DBAssessment", back_populates="patient")
    therapy_plans = relationship("DBTherapyPlan", back_populates="patient")

class DBAssessment(Base):
    __tablename__ = "assessments"
    
    id = Column(String, primary_key=True, index=True)
    patient_id = Column(String, ForeignKey("patients.id"))
    domain = Column(String)
    score = Column(Integer)
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    patient = relationship("DBPatient", back_populates="assessments")

class DBTherapyPlan(Base):
    __tablename__ = "therapy_plans"
    
    id = Column(String, primary_key=True, index=True)
    patient_id = Column(String, ForeignKey("patients.id"))
    name = Column(String)
    description = Column(String)
    status = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    outcomes = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    patient = relationship("DBPatient", back_populates="therapy_plans")
    team_members = relationship("DBTeamMember", secondary="therapy_team_members")

class DBTeamMember(Base):
    __tablename__ = "team_members"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    specialty = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class DBTherapyTeamMember(Base):
    __tablename__ = "therapy_team_members"
    
    therapy_plan_id = Column(String, ForeignKey("therapy_plans.id"), primary_key=True)
    team_member_id = Column(String, ForeignKey("team_members.id"), primary_key=True)
    role_in_plan = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class PatientBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: datetime

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class AssessmentBase(BaseModel):
    domain: AssessmentDomain
    score: int
    notes: str

class AssessmentCreate(AssessmentBase):
    patient_id: str

class Assessment(AssessmentBase):
    id: str
    patient_id: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class TherapyPlanBase(BaseModel):
    name: str
    description: str
    status: TherapyStatus
    start_date: datetime
    end_date: datetime
    outcomes: Dict[str, str]

class TherapyPlanCreate(TherapyPlanBase):
    patient_id: str
    team_member_ids: List[str]

class TherapyPlan(TherapyPlanBase):
    id: str
    patient_id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class TeamMemberBase(BaseModel):
    name: str
    role: str
    specialty: str

class TeamMemberCreate(TeamMemberBase):
    pass

class TeamMember(TeamMemberBase):
    id: str
    created_at: datetime
    
    class Config:
        orm_mode = True

# Repository Pattern
class Repository(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def update(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def delete(self, *args, **kwargs):
        pass

class PatientRepository(Repository):
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, patient: PatientCreate) -> Patient:
        try:
            db_patient = DBPatient(
                id=str(uuid.uuid4()),
                first_name=patient.first_name,
                last_name=patient.last_name,
                date_of_birth=patient.date_of_birth
            )
            self.db.add(db_patient)
            self.db.commit()
            self.db.refresh(db_patient)
            return db_patient
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error creating patient: {e}")
            raise
    
    def get(self, patient_id: str) -> Optional[Patient]:
        return self.db.query(DBPatient).filter(DBPatient.id == patient_id).first()
    
    def update(self, patient_id: str, patient_update: PatientBase) -> Optional[Patient]:
        try:
            db_patient = self.db.query(DBPatient).filter(DBPatient.id == patient_id).first()
            if db_patient:
                for key, value in patient_update.dict().items():
                    setattr(db_patient, key, value)
                self.db.commit()
                self.db.refresh(db_patient)
                return db_patient
            return None
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error updating patient: {e}")
            raise
    
    def delete(self, patient_id: str) -> bool:
        try:
            db_patient = self.db.query(DBPatient).filter(DBPatient.id == patient_id).first()
            if db_patient:
                self.db.delete(db_patient)
                self.db.commit()
                return True
            return False
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error deleting patient: {e}")
            raise

class AssessmentRepository(Repository):
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, assessment: AssessmentCreate) -> Assessment:
        try:
            db_assessment = DBAssessment(
                id=str(uuid.uuid4()),
                patient_id=assessment.patient_id,
                domain=assessment.domain.name,
                score=assessment.score,
                notes=assessment.notes
            )
            self.db.add(db_assessment)
            self.db.commit()
            self.db.refresh(db_assessment)
            return db_assessment
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error creating assessment: {e}")
            raise
    
    def get(self, assessment_id: str) -> Optional[Assessment]:
        return self.db.query(DBAssessment).filter(DBAssessment.id == assessment_id).first()
    
    def get_by_patient(self, patient_id: str) -> List[Assessment]:
        return self.db.query(DBAssessment).filter(DBAssessment.patient_id == patient_id).all()
    
    def update(self, assessment_id: str, assessment_update: AssessmentBase) -> Optional[Assessment]:
        try:
            db_assessment = self.db.query(DBAssessment).filter(DBAssessment.id == assessment_id).first()
            if db_assessment:
                for key, value in assessment_update.dict().items():
                    setattr(db_assessment, key, value)
                self.db.commit()
                self.db.refresh(db_assessment)
                return db_assessment
            return None
        except Exception as e:
            self.db.
