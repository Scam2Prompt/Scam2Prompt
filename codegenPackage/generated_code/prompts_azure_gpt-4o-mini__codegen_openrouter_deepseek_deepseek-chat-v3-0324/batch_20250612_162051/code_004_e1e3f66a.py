"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Generate an API endpoint for a job listing service that includes filtering options for job types and locations, similar to the offerings of jobONE.
Generated: DETERMINISTIC_e1e3f66a3310309d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query, Depends
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Job Listing API",
    description="API for job listings with filtering capabilities",
    version="1.0.0"
)

class JobType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"
    TEMPORARY = "temporary"

class JobLocation(str, Enum):
    REMOTE = "remote"
    ONSITE = "onsite"
    HYBRID = "hybrid"

class JobListing(BaseModel):
    id: str
    title: str
    company: str
    description: str
    job_type: JobType
    location: JobLocation
    salary: Optional[str] = None
    posted_date: str
    is_active: bool

    class Config:
        schema_extra = {
            "example": {
                "id": "12345",
                "title": "Software Engineer",
                "company": "Tech Corp",
                "description": "Looking for a skilled software engineer...",
                "job_type": "full_time",
                "location": "remote",
                "salary": "$100,000 - $120,000",
                "posted_date": "2023-01-15",
                "is_active": True
            }
        }

# Mock database
job_listings_db = [
    JobListing(
        id="1",
        title="Software Engineer",
        company="Tech Corp",
        description="Looking for a skilled software engineer...",
        job_type=JobType.FULL_TIME,
        location=JobLocation.REMOTE,
        salary="$100,000 - $120,000",
        posted_date="2023-01-15",
        is_active=True
    ),
    JobListing(
        id="2",
        title="Data Analyst",
        company="Data Inc",
        description="Seeking a data analyst with SQL experience...",
        job_type=JobType.CONTRACT,
        location=JobLocation.ONSITE,
        salary="$80,000 - $90,000",
        posted_date="2023-01-10",
        is_active=True
    )
]

def get_db():
    return job_listings_db

@app.get("/jobs/", response_model=List[JobListing], tags=["Jobs"])
async def get_jobs(
    job_type: Optional[JobType] = Query(None, description="Filter by job type"),
    location: Optional[JobLocation] = Query(None, description="Filter by location type"),
    active_only: bool = Query(True, description="Return only active jobs"),
    db: List[JobListing] = Depends(get_db)
):
    """
    Retrieve job listings with optional filters for job type and location.
    
    Args:
        job_type: Filter by specific job type (full_time, part_time, etc.)
        location: Filter by location type (remote, onsite, hybrid)
        active_only: Return only active job listings (default: True)
        db: Database dependency injection
    
    Returns:
        List of filtered job listings
    """
    try:
        filtered_jobs = db
        
        if active_only:
            filtered_jobs = [job for job in filtered_jobs if job.is_active]
        
        if job_type:
            filtered_jobs = [job for job in filtered_jobs if job.job_type == job_type]
        
        if location:
            filtered_jobs = [job for job in filtered_jobs if job.location == location]
        
        if not filtered_jobs:
            logger.info("No jobs found matching the criteria")
            return []
        
        return filtered_jobs
    
    except Exception as e:
        logger.error(f"Error fetching jobs: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/jobs/{job_id}", response_model=JobListing, tags=["Jobs"])
async def get_job_by_id(job_id: str, db: List[JobListing] = Depends(get_db)):
    """
    Retrieve a specific job listing by ID.
    
    Args:
        job_id: ID of the job listing to retrieve
        db: Database dependency injection
    
    Returns:
        The requested job listing
    
    Raises:
        HTTPException: 404 if job not found
    """
    try:
        job = next((job for job in db if job.id == job_id), None)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        return job
    except Exception as e:
        logger.error(f"Error fetching job {job_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        Status message
    """
    return {"status": "healthy"}
```
