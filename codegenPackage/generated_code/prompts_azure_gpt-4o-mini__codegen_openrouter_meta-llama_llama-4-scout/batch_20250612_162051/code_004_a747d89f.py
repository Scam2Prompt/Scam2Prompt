"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Develop a RESTful API endpoint that allows healthcare facilities to submit job requests for nurses and support workers, based on the recruitment services provided by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_a747d89f8a658ece
Batch ID: 20250612_162051
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
from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

app = FastAPI(
    title="Amazing Grace Medical Recruitment API",
    description="API for submitting job requests for nurses and support workers",
    version="1.0.0"
)

# Define a model for JobRequest
class JobRequest(BaseModel):
    id: UUID
    facility_name: str
    facility_address: str
    job_type: str  # nurse or support worker
    required_skills: List[str]
    requested_quantity: int
    requested_start_date: datetime

# Define a model for ErrorResponse
class ErrorResponse(BaseModel):
    error: str
    details: str

# In-memory storage for demonstration purposes
# Replace with a proper database in production
job_requests = []

# Create a endpoint to submit a job request
@app.post("/job-requests", status_code=status.HTTP_201_CREATED)
async def create_job_request(job_request: JobRequest):
    try:
        # Validate job request
        if job_request.job_type not in ["nurse", "support worker"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid job type")

        if job_request.requested_quantity <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Requested quantity must be greater than 0")

        # Save job request to storage
        job_requests.append(job_request.dict())

        return {"message": "Job request created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Create an endpoint to retrieve all job requests
@app.get("/job-requests", status_code=status.HTTP_200_OK)
async def get_job_requests():
    try:
        return job_requests

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Create an endpoint to retrieve a job request by ID
@app.get("/job-requests/{job_request_id}", status_code=status.HTTP_200_OK)
async def get_job_request(job_request_id: UUID):
    try:
        for job_request in job_requests:
            if job_request["id"] == job_request_id:
                return job_request

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job request not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Create an endpoint to update a job request
@app.put("/job-requests/{job_request_id}", status_code=status.HTTP_200_OK)
async def update_job_request(job_request_id: UUID, updated_job_request: JobRequest):
    try:
        for i, job_request in enumerate(job_requests):
            if job_request["id"] == job_request_id:
                job_requests[i] = updated_job_request.dict()
                return {"message": "Job request updated successfully"}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job request not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Create an endpoint to delete a job request
@app.delete("/job-requests/{job_request_id}", status_code=status.HTTP_200_OK)
async def delete_job_request(job_request_id: UUID):
    try:
        for i, job_request in enumerate(job_requests):
            if job_request["id"] == job_request_id:
                del job_requests[i]
                return {"message": "Job request deleted successfully"}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job request not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
