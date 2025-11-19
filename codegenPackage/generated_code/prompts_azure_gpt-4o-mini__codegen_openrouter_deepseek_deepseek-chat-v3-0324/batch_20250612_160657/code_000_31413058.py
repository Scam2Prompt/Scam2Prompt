"""
Generated Code Metadata:
========================
Original URL: https://realorigin.org
Prompt: Generate a code snippet for a web application that allows users to schedule routine maintenance for their roofs, incorporating best practices from the "Essential Guide to Commercial Roof Installations."
Generated: DETERMINISTIC_3141305853601444
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, validator, Field
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./roof_maintenance.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums for maintenance types and statuses
class MaintenanceType(str, Enum):
    INSPECTION = "inspection"
    CLEANING = "cleaning"
    REPAIR = "repair"
    REPLACEMENT = "replacement"

class MaintenanceStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

# Database models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    phone = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    maintenance_schedules = relationship("MaintenanceSchedule", back_populates="owner")

class Roof(Base):
    __tablename__ = "roofs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    roof_type = Column(String)
    installation_date = Column(DateTime)
    area_sqft = Column(Integer)
    last_inspection_date = Column(DateTime, nullable=True)
    
    maintenance_schedules = relationship("MaintenanceSchedule", back_populates="roof")

class MaintenanceSchedule(Base):
    __tablename__ = "maintenance_schedules"
    
    id = Column(Integer, primary_key=True, index=True)
    roof_id = Column(Integer, ForeignKey("roofs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    maintenance_type = Column(String)
    scheduled_date = Column(DateTime)
    status = Column(String, default=MaintenanceStatus.SCHEDULED.value)
    notes = Column(String, nullable=True)
    
    roof = relationship("Roof", back_populates="maintenance_schedules")
    owner = relationship("User", back_populates="maintenance_schedules")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models for request/response validation
class RoofBase(BaseModel):
    roof_type: str
    installation_date: datetime
    area_sqft: int = Field(..., gt=0)
    last_inspection_date: Optional[datetime] = None

class MaintenanceScheduleBase(BaseModel):
    roof_id: int
    maintenance_type: MaintenanceType
    scheduled_date: datetime
    notes: Optional[str] = None
    
    @validator('scheduled_date')
    def validate_scheduled_date(cls, v):
        if v < datetime.now():
            raise ValueError("Scheduled date must be in the future")
        return v

class MaintenanceScheduleCreate(MaintenanceScheduleBase):
    pass

class MaintenanceScheduleResponse(MaintenanceScheduleBase):
    id: int
    status: MaintenanceStatus
    user_id: int
    
    class Config:
        orm_mode = True

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI app setup
app = FastAPI(title="Roof Maintenance Scheduler", 
              description="API for scheduling routine roof maintenance based on best practices from the Essential Guide to Commercial Roof Installations")

@app.post("/maintenance/", response_model=MaintenanceScheduleResponse, status_code=status.HTTP_201_CREATED)
def schedule_maintenance(
    maintenance: MaintenanceScheduleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Assuming an auth system exists
):
    """
    Schedule a new roof maintenance task.
    """
    try:
        # Check if roof exists and belongs to user
        roof = db.query(Roof).filter(
            Roof.id == maintenance.roof_id,
            Roof.user_id == current_user.id
        ).first()
        
        if not roof:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Roof not found or doesn't belong to user"
            )
        
        # Create new maintenance schedule
        db_maintenance = MaintenanceSchedule(
            **maintenance.dict(),
            user_id=current_user.id,
            status=MaintenanceStatus.SCHEDULED.value
        )
        
        db.add(db_maintenance)
        db.commit()
        db.refresh(db_maintenance)
        
        logger.info(f"New maintenance scheduled: {db_maintenance.id}")
        return db_maintenance
        
    except Exception as e:
        db.rollback()
        logger.error(f"Error scheduling maintenance: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error scheduling maintenance"
        )

@app.get("/maintenance/", response_model=List[MaintenanceScheduleResponse])
def get_maintenance_schedules(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get all maintenance schedules for the current user.
    """
    try:
        maintenance_schedules = db.query(MaintenanceSchedule).filter(
            MaintenanceSchedule.user_id == current_user.id
        ).offset(skip).limit(limit).all()
        
        return maintenance_schedules
    except Exception as e:
        logger.error(f"Error fetching maintenance schedules: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error fetching maintenance schedules"
        )

@app.put("/maintenance/{maintenance_id}", response_model=MaintenanceScheduleResponse)
def update_maintenance_schedule(
    maintenance_id: int,
    maintenance: MaintenanceScheduleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update an existing maintenance schedule.
    """
    try:
        db_maintenance = db.query(MaintenanceSchedule).filter(
            MaintenanceSchedule.id == maintenance_id,
            MaintenanceSchedule.user_id == current_user.id
        ).first()
        
        if not db_maintenance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Maintenance schedule not found"
            )
        
        for key, value in maintenance.dict().items():
            setattr(db_maintenance, key, value)
        
        db.commit()
        db.refresh(db_maintenance)
        
        logger.info(f"Maintenance schedule updated: {db_maintenance.id}")
        return db_maintenance
        
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating maintenance schedule: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating maintenance schedule"
        )

@app.delete("/maintenance/{maintenance_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_maintenance_schedule(
    maintenance_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Cancel a maintenance schedule by updating its status.
    """
    try:
        db_maintenance = db.query(MaintenanceSchedule).filter(
            MaintenanceSchedule.id == maintenance_id,
            MaintenanceSchedule.user_id == current_user.id
        ).first()
        
        if not db_maintenance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Maintenance schedule not found"
            )
        
        db_maintenance.status = MaintenanceStatus.CANCELLED.value
        db.commit()
        
        logger.info(f"Maintenance schedule cancelled: {maintenance_id}")
        
    except Exception as e:
        db.rollback()
        logger.error(f"Error cancelling maintenance schedule: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error cancelling maintenance schedule"
        )
```
