"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Create a RESTful API endpoint for a construction management system that handles data related to mining and road construction projects.
Generated: DETERMINISTIC_6676918e0818a1f1
Batch ID: 20250612_155223
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
from datetime import date
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(
    title="Construction Management API",
    description="API for managing mining and road construction projects",
    version="1.0.0"
)

# Database simulation
db = {
    "projects": [],
    "equipment": [],
    "workers": []
}

# Enums and Models
class ProjectType(str, Enum):
    MINING = "mining"
    ROAD_CONSTRUCTION = "road_construction"

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class EquipmentType(str, Enum):
    EXCAVATOR = "excavator"
    BULLDOZER = "bulldozer"
    DUMP_TRUCK = "dump_truck"
    ROAD_ROLLER = "road_roller"

class WorkerPosition(str, Enum):
    ENGINEER = "engineer"
    OPERATOR = "operator"
    LABORER = "laborer"
    SUPERVISOR = "supervisor"

class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    type: ProjectType
    status: ProjectStatus = ProjectStatus.PLANNING
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: float
    location: str

class Equipment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: EquipmentType
    project_id: UUID
    status: str = "available"
    last_maintenance: Optional[date] = None

class Worker(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    position: WorkerPosition
    project_id: UUID
    contact: str

# Helper functions
def get_project(project_id: UUID):
    for project in db["projects"]:
        if project.id == project_id:
            return project
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project with id {project_id} not found"
    )

# Project Endpoints
@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(project: Project):
    db["projects"].append(project)
    return project

@app.get("/projects/", response_model=List[Project])
def list_projects(type: Optional[ProjectType] = None, status: Optional[ProjectStatus] = None):
    projects = db["projects"]
    if type:
        projects = [p for p in projects if p.type == type]
    if status:
        projects = [p for p in projects if p.status == status]
    return projects

@app.get("/projects/{project_id}", response_model=Project)
def get_project_by_id(project_id: UUID):
    return get_project(project_id)

@app.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: UUID, project_update: Project):
    project = get_project(project_id)
    for key, value in project_update.dict().items():
        setattr(project, key, value)
    return project

@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: UUID):
    project = get_project(project_id)
    db["projects"].remove(project)
    return None

# Equipment Endpoints
@app.post("/equipment/", response_model=Equipment, status_code=status.HTTP_201_CREATED)
def create_equipment(equipment: Equipment):
    get_project(equipment.project_id)  # Validate project exists
    db["equipment"].append(equipment)
    return equipment

@app.get("/equipment/", response_model=List[Equipment])
def list_equipment(project_id: Optional[UUID] = None, type: Optional[EquipmentType] = None):
    equipment = db["equipment"]
    if project_id:
        equipment = [e for e in equipment if e.project_id == project_id]
    if type:
        equipment = [e for e in equipment if e.type == type]
    return equipment

# Worker Endpoints
@app.post("/workers/", response_model=Worker, status_code=status.HTTP_201_CREATED)
def create_worker(worker: Worker):
    get_project(worker.project_id)  # Validate project exists
    db["workers"].append(worker)
    return worker

@app.get("/workers/", response_model=List[Worker])
def list_workers(project_id: Optional[UUID] = None, position: Optional[WorkerPosition] = None):
    workers = db["workers"]
    if project_id:
        workers = [w for w in workers if w.project_id == project_id]
    if position:
        workers = [w for w in workers if w.position == position]
    return workers

@app.get("/workers/{worker_id}", response_model=Worker)
def get_worker(worker_id: UUID):
    for worker in db["workers"]:
        if worker.id == worker_id:
            return worker
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Worker with id {worker_id} not found"
    )
```
