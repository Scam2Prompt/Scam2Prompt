"""
Generated Code Metadata:
========================
Original URL: https://celestia.top
Prompt: Write Python code to integrate project management features into an architecture-focused app, inspired by the Études Architect App described on Celestia's website.
Generated: DETERMINISTIC_efc456991776ae34
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import uuid
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///./etudes_architect.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# SQLAlchemy models
projects = sqlalchemy.Table(
    "projects",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("start_date", sqlalchemy.DateTime),
    sqlalchemy.Column("end_date", sqlalchemy.DateTime),
    sqlalchemy.Column("client", sqlalchemy.String),
    sqlalchemy.Column("location", sqlalchemy.String),
    sqlalchemy.Column("budget", sqlalchemy.Float),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
)

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("project_id", sqlalchemy.String, sqlalchemy.ForeignKey("projects.id")),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("priority", sqlalchemy.String),
    sqlalchemy.Column("due_date", sqlalchemy.DateTime),
    sqlalchemy.Column("assigned_to", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
)

team_members = sqlalchemy.Table(
    "team_members",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("role", sqlalchemy.String),
    sqlalchemy.Column("specialization", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
)

# Pydantic models
class ProjectStatus(str, Enum):
    planning = "planning"
    in_progress = "in_progress"
    on_hold = "on_hold"
    completed = "completed"
    cancelled = "cancelled"

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    review = "review"
    done = "done"

class TeamMemberRole(str, Enum):
    architect = "architect"
    designer = "designer"
    engineer = "engineer"
    project_manager = "project_manager"
    intern = "intern"

class ProjectBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: ProjectStatus = ProjectStatus.planning
    start_date: datetime
    end_date: Optional[datetime] = None
    client: str = Field(..., max_length=100)
    location: str = Field(..., max_length=100)
    budget: Optional[float] = None

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: TaskStatus = TaskStatus.todo
    priority: TaskPriority = TaskPriority.medium
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = None

class TaskCreate(TaskBase):
    project_id: str

class Task(TaskBase):
    id: str
    project_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TeamMemberBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    role: TeamMemberRole
    specialization: Optional[str] = Field(None, max_length=100)

class TeamMemberCreate(TeamMemberBase):
    pass

class TeamMember(TeamMemberBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# FastAPI app setup
app = FastAPI(title="Études Architect Project Management API",
              description="API for managing architecture projects, tasks, and team members",
              version="1.0.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database connection
@app.on_event("startup")
async def startup():
    await database.connect()
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Helper functions
async def get_project_or_404(project_id: str):
    query = projects.select().where(projects.c.id == project_id)
    project = await database.fetch_one(query)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

async def get_task_or_404(task_id: str):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

async def get_team_member_or_404(member_id: str):
    query = team_members.select().where(team_members.c.id == member_id)
    member = await database.fetch_one(query)
    if member is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team member not found")
    return member

# Project endpoints
@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, token: str = Depends(oauth2_scheme)):
    project_id = str(uuid.uuid4())
    now = datetime.utcnow()
    query = projects.insert().values(
        id=project_id,
        name=project.name,
        description=project.description,
        status=project.status.value,
        start_date=project.start_date,
        end_date=project.end_date,
        client=project.client,
        location=project.location,
        budget=project.budget,
        created_at=now,
        updated_at=now
    )
    await database.execute(query)
    return await get_project_or_404(project_id)

@app.get("/projects/", response_model=List[Project])
async def list_projects(token: str = Depends(oauth2_scheme)):
    query = projects.select()
    return await database.fetch_all(query)

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str, token: str = Depends(oauth2_scheme)):
    return await get_project_or_404(project_id)

@app.put("/projects/{project_id}", response_model=Project)
async def update_project(project_id: str, project: ProjectCreate, token: str = Depends(oauth2_scheme)):
    await get_project_or_404(project_id)
    now = datetime.utcnow()
    query = (
        projects.update()
        .where(projects.c.id == project_id)
        .values(
            name=project.name,
            description=project.description,
            status=project.status.value,
            start_date=project.start_date,
            end_date=project.end_date,
            client=project.client,
            location=project.location,
            budget=project.budget,
            updated_at=now
        )
    )
    await database.execute(query)
    return await get_project_or_404(project_id)

@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: str, token: str =
