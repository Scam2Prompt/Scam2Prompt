"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Generate an API specification for a daycare management system that includes functionalities for tracking child development and organizing parenting webinars, similar to those offered by Kiddoo Playway.
Generated: DETERMINISTIC_add4e536b16d1d5e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid

app = FastAPI(
    title="Daycare Management System API",
    description="API for managing daycare operations, child development tracking, and parenting webinars.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@daycareapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Enums
class ChildGender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class DevelopmentArea(str, Enum):
    cognitive = "cognitive"
    physical = "physical"
    social = "social"
    emotional = "emotional"
    language = "language"

class WebinarStatus(str, Enum):
    upcoming = "upcoming"
    ongoing = "ongoing"
    completed = "completed"
    cancelled = "cancelled"

# Models
class Child(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    first_name: str
    last_name: str
    date_of_birth: datetime
    gender: ChildGender
    parent_name: str
    parent_contact: str
    enrollment_date: datetime = Field(default_factory=datetime.now)
    allergies: Optional[List[str]] = None
    special_needs: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Emma",
                "last_name": "Johnson",
                "date_of_birth": "2020-05-15T00:00:00",
                "gender": "female",
                "parent_name": "Sarah Johnson",
                "parent_contact": "sarah@example.com",
                "allergies": ["peanuts"],
                "special_needs": "None"
            }
        }

class DevelopmentRecord(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    child_id: str
    date: datetime = Field(default_factory=datetime.now)
    area: DevelopmentArea
    observation: str
    educator_notes: Optional[str] = None
    next_steps: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "child_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "area": "cognitive",
                "observation": "Recognizes basic shapes and colors",
                "educator_notes": "Excelling in shape recognition",
                "next_steps": "Introduce more complex shapes"
            }
        }

class Webinar(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    scheduled_time: datetime
    duration_minutes: int
    presenter: str
    status: WebinarStatus = WebinarStatus.upcoming
    max_participants: int
    registered_participants: List[str] = Field(default_factory=list)

    class Config:
        schema_extra = {
            "example": {
                "title": "Positive Parenting Techniques",
                "description": "Learn effective strategies for positive parenting",
                "scheduled_time": "2023-12-15T18:00:00",
                "duration_minutes": 90,
                "presenter": "Dr. Jane Smith",
                "max_participants": 50
            }
        }

class WebinarRegistration(BaseModel):
    parent_email: str
    webinar_id: str

    class Config:
        schema_extra = {
            "example": {
                "parent_email": "parent@example.com",
                "webinar_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }

# In-memory database (replace with real database in production)
children_db = []
development_records_db = []
webinars_db = []

# Child Endpoints
@app.post("/children/", status_code=status.HTTP_201_CREATED, tags=["Children"])
async def register_child(child: Child):
    """Register a new child in the daycare system."""
    children_db.append(child)
    return {"message": "Child registered successfully", "child_id": child.id}

@app.get("/children/", response_model=List[Child], tags=["Children"])
async def get_all_children():
    """Get a list of all registered children."""
    return children_db

@app.get("/children/{child_id}", response_model=Child, tags=["Children"])
async def get_child(child_id: str):
    """Get details of a specific child."""
    for child in children_db:
        if child.id == child_id:
            return child
    raise HTTPException(status_code=404, detail="Child not found")

# Development Tracking Endpoints
@app.post("/development/", status_code=status.HTTP_201_CREATED, tags=["Development Tracking"])
async def add_development_record(record: DevelopmentRecord):
    """Add a new development observation for a child."""
    # Check if child exists
    if not any(child.id == record.child_id for child in children_db):
        raise HTTPException(status_code=404, detail="Child not found")
    
    development_records_db.append(record)
    return {"message": "Development record added successfully", "record_id": record.id}

@app.get("/development/{child_id}", response_model=List[DevelopmentRecord], tags=["Development Tracking"])
async def get_child_development_records(child_id: str):
    """Get all development records for a specific child."""
    return [record for record in development_records_db if record.child_id == child_id]

# Webinar Endpoints
@app.post("/webinars/", status_code=status.HTTP_201_CREATED, tags=["Parenting Webinars"])
async def create_webinar(webinar: Webinar):
    """Create a new parenting webinar."""
    webinars_db.append(webinar)
    return {"message": "Webinar created successfully", "webinar_id": webinar.id}

@app.get("/webinars/", response_model=List[Webinar], tags=["Parenting Webinars"])
async def get_all_webinars(status_filter: Optional[WebinarStatus] = None):
    """Get a list of all webinars, optionally filtered by status."""
    if status_filter:
        return [webinar for webinar in webinars_db if webinar.status == status_filter]
    return webinars_db

@app.post("/webinars/register/", status_code=status.HTTP_201_CREATED, tags=["Parenting Webinars"])
async def register_for_webinar(registration: WebinarRegistration):
    """Register a parent for a webinar."""
    webinar = next((w for w in webinars_db if w.id == registration.webinar_id), None)
    if not webinar:
        raise HTTPException(status_code=404, detail="Webinar not found")
    
    if len(webinar.registered_participants) >= webinar.max_participants:
        raise HTTPException(status_code=400, detail="Webinar is full")
    
    if registration.parent_email in webinar.registered_participants:
        raise HTTPException(status_code=400, detail="Already registered for this webinar")
    
    webinar.registered_participants.append(registration.parent_email)
    return {"message": "Registration successful"}

@app.put("/webinars/{webinar_id}/status", tags=["Parenting Webinars"])
async def update_webinar_status(webinar_id: str, new_status: WebinarStatus):
    """Update the status of a webinar."""
    webinar = next((w for w in webinars_db if w.id == webinar_id), None)
    if not webinar:
        raise HTTPException(status_code=404, detail="Webinar not found")
    
    webinar.status = new_status
    return {"message": "Webinar status updated successfully"}

# Health Check
@app.get("/health", tags=["System"])
async def health_check():
    """Check if the API is running."""
    return {"status": "healthy"}
```
