"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Generate a REST API specification for a consulting service that manages architectural projects, inspired by the consulting services offered by TWM Associates.
Generated: DETERMINISTIC_ba3315165fcc5375
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Architectural Project Management API",
    description="REST API for managing architectural projects, inspired by TWM Associates consulting services.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@archprojects.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in production, replace with actual database)
projects_db = []
clients_db = []
consultants_db = []

# Models
class Address(BaseModel):
    street: str
    city: str
    state: str
    postal_code: str
    country: str = "USA"

class Client(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    contact_person: str
    email: str
    phone: str
    address: Address
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Consultant(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    specialization: str
    email: str
    phone: str
    hire_date: datetime
    is_active: bool = True

class ProjectPhase(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    status: str = "planned"  # planned, in_progress, completed, delayed

class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    client_id: UUID
    lead_consultant_id: UUID
    phases: List[ProjectPhase] = []
    start_date: datetime
    estimated_end_date: datetime
    actual_end_date: Optional[datetime] = None
    status: str = "draft"  # draft, active, on_hold, completed, cancelled
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

# Helper functions
def get_project(project_id: UUID):
    for project in projects_db:
        if project.id == project_id:
            return project
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project with ID {project_id} not found"
    )

def get_client(client_id: UUID):
    for client in clients_db:
        if client.id == client_id:
            return client
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Client with ID {client_id} not found"
    )

def get_consultant(consultant_id: UUID):
    for consultant in consultants_db:
        if consultant.id == consultant_id:
            return consultant
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Consultant with ID {consultant_id} not found"
    )

# Client endpoints
@app.post("/clients/", response_model=Client, status_code=status.HTTP_201_CREATED)
def create_client(client: Client):
    clients_db.append(client)
    return client

@app.get("/clients/", response_model=List[Client])
def list_clients():
    return clients_db

@app.get("/clients/{client_id}", response_model=Client)
def read_client(client_id: UUID):
    return get_client(client_id)

@app.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: UUID, client: Client):
    existing_client = get_client(client_id)
    client.id = client_id
    client.created_at = existing_client.created_at
    client.updated_at = datetime.now()
    clients_db.remove(existing_client)
    clients_db.append(client)
    return client

@app.delete("/clients/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: UUID):
    client = get_client(client_id)
    clients_db.remove(client)
    return None

# Consultant endpoints
@app.post("/consultants/", response_model=Consultant, status_code=status.HTTP_201_CREATED)
def create_consultant(consultant: Consultant):
    consultants_db.append(consultant)
    return consultant

@app.get("/consultants/", response_model=List[Consultant])
def list_consultants(active_only: bool = True):
    if active_only:
        return [c for c in consultants_db if c.is_active]
    return consultants_db

@app.get("/consultants/{consultant_id}", response_model=Consultant)
def read_consultant(consultant_id: UUID):
    return get_consultant(consultant_id)

@app.put("/consultants/{consultant_id}", response_model=Consultant)
def update_consultant(consultant_id: UUID, consultant: Consultant):
    existing_consultant = get_consultant(consultant_id)
    consultant.id = consultant_id
    consultant.hire_date = existing_consultant.hire_date
    consultants_db.remove(existing_consultant)
    consultants_db.append(consultant)
    return consultant

@app.delete("/consultants/{consultant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_consultant(consultant_id: UUID):
    consultant = get_consultant(consultant_id)
    consultants_db.remove(consultant)
    return None

# Project endpoints
@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(project: Project):
    # Validate client and consultant exist
    get_client(project.client_id)
    get_consultant(project.lead_consultant_id)
    
    projects_db.append(project)
    return project

@app.get("/projects/", response_model=List[Project])
def list_projects(status_filter: Optional[str] = None):
    if status_filter:
        return [p for p in projects_db if p.status == status_filter]
    return projects_db

@app.get("/projects/{project_id}", response_model=Project)
def read_project(project_id: UUID):
    return get_project(project_id)

@app.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: UUID, project: Project):
    existing_project = get_project(project_id)
    # Validate client and consultant exist if they're being updated
    if project.client_id != existing_project.client_id:
        get_client(project.client_id)
    if project.lead_consultant_id != existing_project.lead_consultant_id:
        get_consultant(project.lead_consultant_id)
    
    project.id = project_id
    project.created_at = existing_project.created_at
    project.updated_at = datetime.now()
    projects_db.remove(existing_project)
    projects_db.append(project)
    return project

@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: UUID):
    project = get_project(project_id)
    projects_db.remove(project)
    return None

# Project Phase endpoints
@app.post("/projects/{project_id}/phases/", response_model=Project)
def add_project_phase(project_id: UUID, phase: ProjectPhase):
    project = get_project(project_id)
    project.phases.append(phase)
    project.updated_at = datetime.now()
    return project

@app.put("/projects/{project_id}/phases/{phase_index}", response_model=Project)
def update_project_phase(project_id: UUID, phase_index: int, phase: ProjectPhase):
    project = get_project(project_id)
    if phase_index >= len(project.phases):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Phase index {phase_index} not found in project"
        )
    project.phases[phase_index] = phase
    project.updated_at = datetime.now()
    return project

@app.delete("/projects/{project_id}/phases/{phase_index}", response_model=Project)
def delete_project_phase(project_id: UUID, phase_index: int):
    project = get_project(project_id)
    if phase_index >= len(project.phases):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Phase index {phase_index} not found in project"
        )
    project.phases.pop(phase_index)
    project.updated_at = datetime.now()
    return project
```
