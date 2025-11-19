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
# app.py

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI(
    title="TWM Associates Architectural Project Management API",
    description="API for managing architectural projects",
    version="1.0.0",
)

# Project Status
class ProjectStatus(str):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    CANCELED = "canceled"

# Project Model
class Project(BaseModel):
    id: int
    name: str
    description: str
    status: ProjectStatus
    start_date: date
    end_date: date | None

# Client Model
class Client(BaseModel):
    id: int
    name: str
    email: str
    projects: List[Project]

# Project Request Model
class ProjectRequest(BaseModel):
    name: str
    description: str
    start_date: date

# Client Request Model
class ClientRequest(BaseModel):
    name: str
    email: str

# In-memory data store (replace with a database in production)
projects = [
    Project(id=1, name="Project 1", description="Description 1", status=ProjectStatus.IN_PROGRESS, start_date=date(2022, 1, 1), end_date=None),
    Project(id=2, name="Project 2", description="Description 2", status=ProjectStatus.COMPLETED, start_date=date(2022, 6, 1), end_date=date(2022, 12, 31)),
]

clients = [
    Client(id=1, name="Client 1", email="client1@example.com", projects=[projects[0]]),
    Client(id=2, name="Client 2", email="client2@example.com", projects=[projects[1]]),
]

# Get all projects
@app.get("/projects", response_model=List[Project])
def get_projects():
    """Get all projects"""
    return projects

# Get project by ID
@app.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: int):
    """Get project by ID"""
    project = next((p for p in projects if p.id == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# Create new project
@app.post("/projects", response_model=Project)
def create_project(project: ProjectRequest):
    """Create new project"""
    new_project_id = len(projects) + 1
    new_project = Project(id=new_project_id, name=project.name, description=project.description, status=ProjectStatus.IN_PROGRESS, start_date=project.start_date, end_date=None)
    projects.append(new_project)
    return new_project

# Update existing project
@app.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: int, project: ProjectRequest):
    """Update existing project"""
    existing_project = next((p for p in projects if p.id == project_id), None)
    if existing_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    existing_project.name = project.name
    existing_project.description = project.description
    existing_project.start_date = project.start_date
    return existing_project

# Delete project
@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    """Delete project"""
    global projects
    projects = [p for p in projects if p.id != project_id]
    return {"message": f"Project {project_id} deleted"}

# Get all clients
@app.get("/clients", response_model=List[Client])
def get_clients():
    """Get all clients"""
    return clients

# Get client by ID
@app.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int):
    """Get client by ID"""
    client = next((c for c in clients if c.id == client_id), None)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Create new client
@app.post("/clients", response_model=Client)
def create_client(client: ClientRequest):
    """Create new client"""
    new_client_id = len(clients) + 1
    new_client = Client(id=new_client_id, name=client.name, email=client.email, projects=[])
    clients.append(new_client)
    return new_client

# Update existing client
@app.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientRequest):
    """Update existing client"""
    existing_client = next((c for c in clients if c.id == client_id), None)
    if existing_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    existing_client.name = client.name
    existing_client.email = client.email
    return existing_client

# Delete client
@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    """Delete client"""
    global clients
    clients = [c for c in clients if c.id != client_id]
    return {"message": f"Client {client_id} deleted"}

# Add project to client
@app.post("/clients/{client_id}/projects", response_model=Client)
def add_project_to_client(client_id: int, project_id: int):
    """Add project to client"""
    client = next((c for c in clients if c.id == client_id), None)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    project = next((p for p in projects if p.id == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    client.projects.append(project)
    return client

# Remove project from client
@app.delete("/clients/{client_id}/projects/{project_id}")
def remove_project_from_client(client_id: int, project_id: int):
    """Remove project from client"""
    client = next((c for c in clients if c.id == client_id), None)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    client.projects = [p for p in client.projects if p.id != project_id]
    return {"message": f"Project {project_id} removed from client {client_id}"}
```
