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
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator
from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import date

app = FastAPI(
    title="Healthcare Job Application API",
    description="API for submitting healthcare job applications",
    version="1.0.0",
)

class JobType(str, Enum):
    temporary = "temporary"
    permanent = "permanent"
    contract = "contract"

class HealthcareJobApplication(BaseModel):
    id: Optional[UUID]
    first_name: str
    last_name: str
    email: str
    phone_number: str
    qualifications: list[str]
    preferred_job_type: JobType
    additional_info: Optional[str]

    @validator("qualifications")
    def qualifications_not_empty(cls, v):
        if not v:
            raise ValueError("Qualifications cannot be empty")
        return v

    class Config:
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "phone_number": "+1 123 456 7890",
                "qualifications": ["RN", "BSc Nursing"],
                "preferred_job_type": "permanent",
                "additional_info": "Available for immediate hire"
            }
        }

# In-memory storage for demonstration purposes only.
# In a production application, use a proper database.

job_applications = {}

@app.post("/job-applications", status_code=status.HTTP_201_CREATED)
async def create_job_application(application: HealthcareJobApplication):
    try:
        application.id = application.id or UUID(int.from_bytes(bytes(16), 'big'))
        job_applications[str(application.id)] = application.dict()
        return application
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/job-applications", status_code=status.HTTP_200_OK)
async def get_all_job_applications():
    try:
        return list(job_applications.values())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/job-applications/{application_id}", status_code=status.HTTP_200_OK)
async def get_job_application(application_id: UUID):
    try:
        application = job_applications.get(str(application_id))
        if application is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
        return application
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.put("/job-applications/{application_id}", status_code=status.HTTP_200_OK)
async def update_job_application(application_id: UUID, application: HealthcareJobApplication):
    try:
        if str(application_id) not in job_applications:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
        application.id = application_id
        job_applications[str(application_id)] = application.dict()
        return application
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.delete("/job-applications/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_job_application(application_id: UUID):
    try:
        if str(application_id) not in job_applications:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
        del job_applications[str(application_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
