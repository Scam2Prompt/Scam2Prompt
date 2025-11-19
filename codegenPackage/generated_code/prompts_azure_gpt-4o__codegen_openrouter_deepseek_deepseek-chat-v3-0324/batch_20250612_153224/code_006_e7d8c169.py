"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a RESTful API endpoint for submitting healthcare job applications, including fields for personal details, qualifications, and preferred job type (e.g., temporary, permanent, contract).
Generated: DETERMINISTIC_e7d8c1690b6de270
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, validator
from typing import List, Optional
from datetime import date
from enum import Enum
import uuid

app = FastAPI(
    title="Healthcare Job Application API",
    description="API for submitting healthcare job applications",
    version="1.0.0"
)

class JobType(str, Enum):
    TEMPORARY = "temporary"
    PERMANENT = "permanent"
    CONTRACT = "contract"

class Qualification(BaseModel):
    degree: str = Field(..., min_length=1, max_length=100)
    institution: str = Field(..., min_length=1, max_length=100)
    year_completed: int = Field(..., gt=1900, le=date.today().year)

class JobApplication(BaseModel):
    application_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    phone: str = Field(..., regex=r"^\+?[0-9\s\-]+$")
    address: str = Field(..., min_length=1, max_length=200)
    date_of_birth: date
    qualifications: List[Qualification]
    preferred_job_type: JobType
    years_of_experience: int = Field(..., ge=0)
    additional_notes: Optional[str] = Field(None, max_length=500)

    @validator("date_of_birth")
    def validate_date_of_birth(cls, v):
        if v > date.today():
            raise ValueError("Date of birth cannot be in the future")
        return v

# In-memory storage for demo purposes (replace with database in production)
applications_db = {}

@app.post("/applications/", 
          status_code=status.HTTP_201_CREATED,
          response_model=JobApplication,
          summary="Submit a new job application",
          response_description="The created job application")
async def submit_application(application: JobApplication):
    """
    Submit a healthcare job application with:
    - Personal details
    - Qualifications
    - Preferred job type
    """
    if application.application_id in applications_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Application ID already exists"
        )
    
    applications_db[application.application_id] = application
    return application

@app.get("/applications/{application_id}",
         response_model=JobApplication,
         summary="Retrieve a job application",
         response_description="The requested job application")
async def get_application(application_id: str):
    """
    Retrieve a submitted job application by its ID.
    """
    if application_id not in applications_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found"
        )
    return applications_db[application_id]

@app.get("/applications/",
         response_model=List[JobApplication],
         summary="List all job applications",
         response_description="List of all job applications")
async def list_applications():
    """
    Retrieve all submitted job applications.
    """
    return list(applications_db.values())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
