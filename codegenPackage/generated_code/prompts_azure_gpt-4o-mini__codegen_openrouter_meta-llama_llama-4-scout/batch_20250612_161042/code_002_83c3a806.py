"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Create a RESTful API design for a construction company that includes endpoints for project tracking, based on the services offered by Sadad Engineering.
Generated: DETERMINISTIC_83c3a80688dc126f
Batch ID: 20250612_161042
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

app = FastAPI(
    title="Sadad Engineering Project Tracking API",
    description="A RESTful API for project tracking",
    version="1.0.0",
)

# Define Pydantic models
class Project(BaseModel):
    id: int
    name: str
    description: str
    status: str

class Service(BaseModel):
    id: int
    name: str
    description: str

class ProjectService(BaseModel):
    project_id: int
    service_id: int

# In-memory data store (replace with a database in production)
projects: List[Project] = [
    Project(id=1, name="Project 1", description="Description 1", status="In Progress"),
    Project(id=2, name="Project 2", description="Description 2", status="Completed"),
]

services: List[Service] = [
    Service(id=1, name="Design", description="Design services"),
    Service(id=2, name="Construction", description="Construction services"),
]

project_services: List[ProjectService] = [
    ProjectService(project_id=1, service_id=1),
    ProjectService(project_id=1, service_id=2),
    ProjectService(project_id=2, service_id=1),
]

# API Endpoints
@app.get("/projects/", response_model=List[Project])
def read_projects():
    """Retrieve a list of all projects"""
    return projects

@app.get("/projects/{project_id}", response_model=Project)
def read_project(project_id: int):
    """Retrieve a project by ID"""
    project = next((p for p in projects if p.id == project_id), None)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(project: Project):
    """Create a new project"""
    projects.append(project)
    return project

@app.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: int, project: Project):
    """Update an existing project"""
    existing_project = next((p for p in projects if p.id == project_id), None)
    if existing_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    existing_project.name = project.name
    existing_project.description = project.description
    existing_project.status = project.status
    return existing_project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    """Delete a project"""
    global projects
    projects = [p for p in projects if p.id != project_id]
    return {"message": "Project deleted"}

@app.get("/services/", response_model=List[Service])
def read_services():
    """Retrieve a list of all services"""
    return services

@app.get("/services/{service_id}", response_model=Service)
def read_service(service_id: int):
    """Retrieve a service by ID"""
    service = next((s for s in services if s.id == service_id), None)
    if service is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return service

@app.post("/projects/{project_id}/services/", response_model=ProjectService, status_code=status.HTTP_201_CREATED)
def add_service_to_project(project_id: int, service: Service):
    """Add a service to a project"""
    project = next((p for p in projects if p.id == project_id), None)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    existing_service = next((s for s in services if s.id == service.id), None)
    if existing_service is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    project_service = ProjectService(project_id=project_id, service_id=service.id)
    project_services.append(project_service)
    return project_service

@app.get("/projects/{project_id}/services/", response_model=List[Service])
def read_project_services(project_id: int):
    """Retrieve a list of services for a project"""
    project_services_for_project = [ps for ps in project_services if ps.project_id == project_id]
    services_for_project = []
    for ps in project_services_for_project:
        service = next((s for s in services if s.id == ps.service_id), None)
        services_for_project.append(service)
    return services_for_project
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
