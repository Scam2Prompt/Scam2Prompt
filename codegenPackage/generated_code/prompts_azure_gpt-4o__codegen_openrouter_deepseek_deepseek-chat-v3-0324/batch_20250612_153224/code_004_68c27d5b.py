"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a REST API for managing data related to "Hogar Transitorio Trampolín," including endpoints for adding new cases, updating progress reports, and retrieving statistics about program outcomes.
Generated: DETERMINISTIC_68c27d5b4d5d73da
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
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from uuid import UUID, uuid4
import uvicorn

app = FastAPI(
    title="Hogar Transitorio Trampolín API",
    description="API for managing transitional home cases and progress reports",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
db = {
    "cases": [],
    "progress_reports": []
}

# Models
class Case(BaseModel):
    case_id: UUID = Field(default_factory=uuid4)
    child_name: str
    age: int
    admission_date: date
    background: str
    current_status: str = "active"
    social_worker: str

class ProgressReport(BaseModel):
    report_id: UUID = Field(default_factory=uuid4)
    case_id: UUID
    report_date: date
    progress_notes: str
    challenges: Optional[str] = None
    next_steps: Optional[str] = None

class StatisticsResponse(BaseModel):
    total_cases: int
    active_cases: int
    closed_cases: int
    average_case_duration_days: float
    most_common_background: str

# Endpoints
@app.post("/cases/", status_code=status.HTTP_201_CREATED, response_model=Case)
async def create_case(case: Case):
    """Create a new case record"""
    db["cases"].append(case)
    return case

@app.get("/cases/", response_model=List[Case])
async def get_all_cases(status_filter: Optional[str] = None):
    """Get all cases, optionally filtered by status"""
    if status_filter:
        return [case for case in db["cases"] if case.current_status.lower() == status_filter.lower()]
    return db["cases"]

@app.get("/cases/{case_id}", response_model=Case)
async def get_case(case_id: UUID):
    """Get a specific case by ID"""
    for case in db["cases"]:
        if case.case_id == case_id:
            return case
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Case not found"
    )

@app.put("/cases/{case_id}", response_model=Case)
async def update_case_status(case_id: UUID, new_status: str):
    """Update a case's status"""
    for case in db["cases"]:
        if case.case_id == case_id:
            case.current_status = new_status
            return case
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Case not found"
    )

@app.post("/progress-reports/", status_code=status.HTTP_201_CREATED, response_model=ProgressReport)
async def create_progress_report(report: ProgressReport):
    """Create a new progress report for a case"""
    # Verify case exists
    if not any(case.case_id == report.case_id for case in db["cases"]):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case not found"
        )
    db["progress_reports"].append(report)
    return report

@app.get("/progress-reports/{case_id}", response_model=List[ProgressReport])
async def get_case_progress_reports(case_id: UUID):
    """Get all progress reports for a specific case"""
    return [report for report in db["progress_reports"] if report.case_id == case_id]

@app.get("/statistics/", response_model=StatisticsResponse)
async def get_statistics():
    """Get program statistics and metrics"""
    if not db["cases"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No cases found"
        )
    
    total_cases = len(db["cases"])
    active_cases = len([case for case in db["cases"] if case.current_status.lower() == "active"])
    closed_cases = total_cases - active_cases
    
    # Calculate average case duration (mock calculation)
    today = date.today()
    durations = [(today - case.admission_date).days for case in db["cases"]]
    avg_duration = sum(durations) / total_cases if total_cases > 0 else 0
    
    # Find most common background (mock implementation)
    backgrounds = [case.background for case in db["cases"]]
    most_common = max(set(backgrounds), key=backgrounds.count) if backgrounds else "N/A"
    
    return StatisticsResponse(
        total_cases=total_cases,
        active_cases=active_cases,
        closed_cases=closed_cases,
        average_case_duration_days=avg_duration,
        most_common_background=most_common
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
