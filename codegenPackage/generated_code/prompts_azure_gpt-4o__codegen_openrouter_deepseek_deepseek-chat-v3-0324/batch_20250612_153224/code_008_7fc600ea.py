"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Recommend tools or libraries for implementing a home restoration management system, including tracking repairs and material usage, as described in the "شمس المملكة" services.
Generated: DETERMINISTIC_7fc600eab23e9d34
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Home Restoration Management System for شمس المملكة Services

This module provides a foundation for tracking repairs, material usage, and project management
for home restoration services. It includes recommended tools and libraries for implementation.
"""

# Core Libraries
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging

# Database - SQLAlchemy for ORM, Alembic for migrations
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import alembic
from alembic.config import Config
from alembic import command

# Web Framework - FastAPI for REST API
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, validator

# Authentication - JWT
from jose import JWTError, jwt
from passlib.context import CryptContext

# Background Tasks - Celery
from celery import Celery

# File Storage - AWS S3
import boto3
from botocore.exceptions import ClientError

# Reporting - ReportLab for PDF generation
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# SMS Notifications - Twilio
from twilio.rest import Client

# Email Notifications - SendGrid
import sendgrid
from sendgrid.helpers.mail import Mail

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database Models
Base = declarative_base()

class Project(Base):
    """Represents a home restoration project"""
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    status = Column(String(20), default='pending')
    budget = Column(Float, nullable=False)
    
    repairs = relationship("Repair", back_populates="project")
    materials = relationship("MaterialUsage", back_populates="project")

class Repair(Base):
    """Represents a repair task in a project"""
    __tablename__ = 'repairs'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    description = Column(String(500), nullable=False)
    cost = Column(Float, nullable=False)
    status = Column(String(20), default='pending')
    completion_date = Column(DateTime, nullable=True)
    
    project = relationship("Project", back_populates="repairs")

class MaterialUsage(Base):
    """Tracks materials used in a project"""
    __tablename__ = 'material_usage'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    material_name = Column(String(100), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String(20), nullable=False)
    cost_per_unit = Column(Float, nullable=False)
    date_used = Column(DateTime, default=datetime.datetime.utcnow)
    
    project = relationship("Project", back_populates="materials")

# Pydantic Models for API
class ProjectCreate(BaseModel):
    name: str
    address: str
    budget: float

class RepairCreate(BaseModel):
    project_id: int
    description: str
    cost: float

class MaterialUsageCreate(BaseModel):
    project_id: int
    material_name: str
    quantity: float
    unit: str
    cost_per_unit: float

# Authentication Setup
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database Setup
DATABASE_URL = "sqlite:///./restoration.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize FastAPI
app = FastAPI(title="Home Restoration Management System")

# Initialize Celery
celery_app = Celery(
    'restoration_tasks',
    broker='pyamqp://guest@localhost//',
    backend='rpc://'
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints
@app.post("/projects/", status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate, db: SessionLocal = Depends(get_db)):
    """Create a new restoration project"""
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.post("/repairs/", status_code=status.HTTP_201_CREATED)
def create_repair(repair: RepairCreate, db: SessionLocal = Depends(get_db)):
    """Add a repair task to a project"""
    db_repair = Repair(**repair.dict())
    db.add(db_repair)
    db.commit()
    db.refresh(db_repair)
    return db_repair

@app.post("/materials/", status_code=status.HTTP_201_CREATED)
def record_material_usage(material: MaterialUsageCreate, db: SessionLocal = Depends(get_db)):
    """Record material usage for a project"""
    db_material = MaterialUsage(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

# Celery Tasks
@celery_app.task
def generate_project_report(project_id: int):
    """Background task to generate project report"""
    db = SessionLocal()
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise ValueError(f"Project {project_id} not found")
        
        # Generate PDF report
        filename = f"project_report_{project_id}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(100, 750, f"Project Report: {project.name}")
        c.drawString(100, 730, f"Address: {project.address}")
        c.save()
        
        return filename
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        raise
    finally:
        db.close()

# AWS S3 Helper Functions
def upload_file_to_s3(file_name: str, bucket: str, object_name: str = None):
    """Upload a file to an S3 bucket"""
    s3_client = boto3.client('s3')
    try:
        if object_name is None:
            object_name = file_name
        s3_client.upload_file(file_name, bucket, object_name)
        return True
    except ClientError as e:
        logger.error(f"S3 upload error: {e}")
        return False

# Twilio SMS Helper
def send_sms_notification(to: str, message: str):
    """Send SMS notification using Twilio"""
    try:
        client = Client("your_account_sid", "your_auth_token")
        message = client.messages.create(
            body=message,
            from_="+1234567890",
            to=to
        )
        return message.sid
    except Exception as e:
        logger.error(f"SMS sending failed: {e}")
        return None

# SendGrid Email Helper
def send_email_notification(to_email: str, subject: str, content: str):
    """Send email notification using SendGrid"""
    try:
        sg = sendgrid.SendGridAPIClient(api_key="your_sendgrid_api_key")
        mail = Mail(
            from_email="notifications@shams-al-mamlaka.com",
            to_emails=to_email,
            subject=subject,
            html_content=content
        )
        response = sg.send(mail)
        return response.status_code
    except Exception as e:
        logger.error(f"Email sending failed: {e}")
        return None

# Database Migration Configuration
def run_migrations():
    """Run database migrations using Alembic"""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

# Main Execution
if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Run migrations
    run_migrations()
    
    # Start the FastAPI app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
