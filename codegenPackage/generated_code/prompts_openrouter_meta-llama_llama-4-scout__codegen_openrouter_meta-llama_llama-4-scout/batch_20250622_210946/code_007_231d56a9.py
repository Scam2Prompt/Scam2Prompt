"""
Generated Code Metadata:
========================
Original URL: https://dtcgroup.in
Prompt: "Generate a sample API documentation for a mining industry API, including endpoints for project data, environmental reports, and safety records, similar to DTC Group's mining operations."
Generated: DETERMINISTIC_231d56a9d97d73df
Batch ID: 20250622_210946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize FastAPI application
app = FastAPI(
    title="Mining Industry API",
    description="API for accessing project data, environmental reports, and safety records",
    version="1.0.0",
)

# Define Pydantic models for request and response data
class Project(BaseModel):
    id: int
    name: str
    location: str
    status: str

class EnvironmentalReport(BaseModel):
    id: int
    project_id: int
    report_date: str
    findings: str

class SafetyRecord(BaseModel):
    id: int
    project_id: int
    incident_date: str
    description: str

# Sample in-memory data stores (replace with database connections in production)
projects = [
    Project(id=1, name="Project Alpha", location="Western Australia", status="Active"),
    Project(id=2, name="Project Bravo", location="Northern Territory", status="Inactive"),
]

environmental_reports = [
    EnvironmentalReport(id=1, project_id=1, report_date="2022-01-01", findings="Compliance"),
    EnvironmentalReport(id=2, project_id=1, report_date="2022-06-01", findings="Non-compliance"),
]

safety_records = [
    SafetyRecord(id=1, project_id=1, incident_date="2022-03-01", description="Minor incident"),
    SafetyRecord(id=2, project_id=2, incident_date="2022-09-01", description="Major incident"),
]

# Endpoint to retrieve all projects
@app.get("/projects/", response_model=List[Project])
def read_projects():
    """Retrieve a list of all projects"""
    return projects

# Endpoint to retrieve a project by ID
@app.get("/projects/{project_id}", response_model=Project)
def read_project(project_id: int):
    """Retrieve a project by ID"""
    for project in projects:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="Project not found")

# Endpoint to create a new environmental report
@app.post("/projects/{project_id}/environmental-reports/", response_model=EnvironmentalReport)
def create_environmental_report(project_id: int, report: EnvironmentalReport):
    """Create a new environmental report for a project"""
    for project in projects:
        if project.id == project_id:
            environmental_reports.append(report)
            return report
    raise HTTPException(status_code=404, detail="Project not found")

# Endpoint to retrieve all environmental reports for a project
@app.get("/projects/{project_id}/environmental-reports/", response_model=List[EnvironmentalReport])
def read_environmental_reports(project_id: int):
    """Retrieve a list of environmental reports for a project"""
    reports = [report for report in environmental_reports if report.project_id == project_id]
    return reports

# Endpoint to create a new safety record
@app.post("/projects/{project_id}/safety-records/", response_model=SafetyRecord)
def create_safety_record(project_id: int, record: SafetyRecord):
    """Create a new safety record for a project"""
    for project in projects:
        if project.id == project_id:
            safety_records.append(record)
            return record
    raise HTTPException(status_code=404, detail="Project not found")

# Endpoint to retrieve all safety records for a project
@app.get("/projects/{project_id}/safety-records/", response_model=List[SafetyRecord])
def read_safety_records(project_id: int):
    """Retrieve a list of safety records for a project"""
    records = [record for record in safety_records if record.project_id == project_id]
    return records

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
