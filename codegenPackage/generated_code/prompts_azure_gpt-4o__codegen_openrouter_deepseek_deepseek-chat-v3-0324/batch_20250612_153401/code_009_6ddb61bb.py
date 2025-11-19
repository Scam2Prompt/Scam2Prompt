"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Provide an example of a REST API design for managing construction projects, with endpoints for adding new projects, updating milestones, and retrieving statistics like apartments built and hours worked, as described by INARO S.A.S.
Generated: DETERMINISTIC_6ddb61bb09ec781b
Batch ID: 20250612_153401
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
import uvicorn

app = FastAPI(
    title="INARO S.A.S Construction Projects API",
    description="REST API for managing construction projects, milestones, and statistics",
    version="1.0.0"
)

# Database simulation
class Database:
    def __init__(self):
        self.projects = []
        self.milestones = []
    
    def get_project(self, project_id: UUID):
        for project in self.projects:
            if project.id == project_id:
                return project
        return None
    
    def get_milestones_for_project(self, project_id: UUID):
        return [m for m in self.milestones if m.project_id == project_id]

db = Database()

# Models
class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    location: str
    start_date: date
    end_date: Optional[date] = None
    total_apartments: int
    budget: float
    status: str = "planned"  # planned, in_progress, completed, delayed

class Milestone(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    name: str
    description: str
    target_date: date
    completed: bool = False
    completion_date: Optional[date] = None
    apartments_built: int = 0
    hours_worked: int = 0

class ProjectStats(BaseModel):
    project_id: UUID
    project_name: str
    total_apartments: int
    apartments_completed: int
    total_hours_worked: int
    milestones_completed: int
    total_milestones: int
    completion_percentage: float

class ProjectCreate(BaseModel):
    name: str
    location: str
    start_date: date
    end_date: Optional[date] = None
    total_apartments: int
    budget: float

class MilestoneCreate(BaseModel):
    project_id: UUID
    name: str
    description: str
    target_date: date

class MilestoneUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    target_date: Optional[date] = None
    completed: Optional[bool] = None
    completion_date: Optional[date] = None
    apartments_built: Optional[int] = None
    hours_worked: Optional[int] = None

# Helper functions
def calculate_project_stats(project_id: UUID) -> ProjectStats:
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    milestones = db.get_milestones_for_project(project_id)
    completed_milestones = [m for m in milestones if m.completed]
    
    apartments_completed = sum(m.apartments_built for m in completed_milestones)
    hours_worked = sum(m.hours_worked for m in milestones)
    
    completion_percentage = (len(completed_milestones) / len(milestones)) * 100 if milestones else 0
    
    return ProjectStats(
        project_id=project.id,
        project_name=project.name,
        total_apartments=project.total_apartments,
        apartments_completed=apartments_completed,
        total_hours_worked=hours_worked,
        milestones_completed=len(completed_milestones),
        total_milestones=len(milestones),
        completion_percentage=completion_percentage
    )

# Endpoints
@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate):
    """
    Create a new construction project
    """
    new_project = Project(**project.dict())
    db.projects.append(new_project)
    return new_project

@app.get("/projects/", response_model=List[Project])
def list_projects():
    """
    Get all construction projects
    """
    return db.projects

@app.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: UUID):
    """
    Get details of a specific project
    """
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project

@app.post("/projects/{project_id}/milestones", response_model=Milestone, status_code=status.HTTP_201_CREATED)
def create_milestone(project_id: UUID, milestone: MilestoneCreate):
    """
    Add a new milestone to a project
    """
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    new_milestone = Milestone(**milestone.dict())
    db.milestones.append(new_milestone)
    return new_milestone

@app.get("/projects/{project_id}/milestones", response_model=List[Milestone])
def list_milestones(project_id: UUID):
    """
    Get all milestones for a project
    """
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    return db.get_milestones_for_project(project_id)

@app.patch("/milestones/{milestone_id}", response_model=Milestone)
def update_milestone(milestone_id: UUID, milestone_update: MilestoneUpdate):
    """
    Update a milestone (partial update)
    """
    milestone = next((m for m in db.milestones if m.id == milestone_id), None)
    if not milestone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Milestone not found"
        )
    
    update_data = milestone_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(milestone, field, value)
    
    return milestone

@app.get("/projects/{project_id}/stats", response_model=ProjectStats)
def get_project_stats(project_id: UUID):
    """
    Get statistics for a project (apartments built, hours worked, etc.)
    """
    return calculate_project_stats(project_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
