"""
Generated Code Metadata:
========================
Original URL: https://trialsonicsolutions.com
Prompt: "Design a RESTful API for an industrial parts cleaning service, including endpoints for ultrasonic cleaning, jet washing, and vapour blasting, inspired by the services provided by Sonic Solutions Ltd."
Generated: DETERMINISTIC_9459b7ecb6fa8081
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from enum import Enum

app = FastAPI(
    title="Industrial Parts Cleaning Service API",
    description="API for industrial parts cleaning services",
    version="1.0.0",
)

# Define cleaning methods
class CleaningMethod(str, Enum):
    ultrasonic = "ultrasonic"
    jet_washing = "jet_washing"
    vapour_blasting = "vapour_blasting"

# Define request model for cleaning services
class CleaningRequest(BaseModel):
    parts: List[str]
    method: CleaningMethod
    duration: int  # in minutes

# Define response model for cleaning services
class CleaningResponse(BaseModel):
    job_id: str
    method: CleaningMethod
    parts: List[str]
    status: str

# In-memory job storage (replace with database in production)
jobs = {}

# Generate unique job ID
import uuid

# Ultrasonic cleaning endpoint
@app.post("/cleaning/ultrasonic", response_model=CleaningResponse)
async def ultrasonic_cleaning(request: CleaningRequest):
    if request.method != CleaningMethod.ultrasonic:
        raise HTTPException(status_code=400, detail="Invalid cleaning method")
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "method": request.method,
        "parts": request.parts,
        "status": "pending"
    }
    return CleaningResponse(
        job_id=job_id,
        method=request.method,
        parts=request.parts,
        status="pending"
    )

# Jet washing endpoint
@app.post("/cleaning/jet-washing", response_model=CleaningResponse)
async def jet_washing_cleaning(request: CleaningRequest):
    if request.method != CleaningMethod.jet_washing:
        raise HTTPException(status_code=400, detail="Invalid cleaning method")
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "method": request.method,
        "parts": request.parts,
        "status": "pending"
    }
    return CleaningResponse(
        job_id=job_id,
        method=request.method,
        parts=request.parts,
        status="pending"
    )

# Vapour blasting endpoint
@app.post("/cleaning/vapour-blasting", response_model=CleaningResponse)
async def vapour_blasting_cleaning(request: CleaningRequest):
    if request.method != CleaningMethod.vapour_blasting:
        raise HTTPException(status_code=400, detail="Invalid cleaning method")
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "method": request.method,
        "parts": request.parts,
        "status": "pending"
    }
    return CleaningResponse(
        job_id=job_id,
        method=request.method,
        parts=request.parts,
        status="pending"
    )

# Generic cleaning endpoint
@app.post("/cleaning", response_model=CleaningResponse)
async def generic_cleaning(request: CleaningRequest):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "method": request.method,
        "parts": request.parts,
        "status": "pending"
    }
    return CleaningResponse(
        job_id=job_id,
        method=request.method,
        parts=request.parts,
        status="pending"
    )

# Get job status endpoint
@app.get("/jobs/{job_id}")
async def get_job_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job_id": job_id, "status": jobs[job_id]["status"]}

# Update job status endpoint
@app.put("/jobs/{job_id}")
async def update_job_status(job_id: str, status: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    jobs[job_id]["status"] = status
    return {"job_id": job_id, "status": status}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
