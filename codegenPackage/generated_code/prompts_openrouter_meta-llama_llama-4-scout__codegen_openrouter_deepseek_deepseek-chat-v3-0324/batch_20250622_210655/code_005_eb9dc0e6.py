"""
Generated Code Metadata:
========================
Original URL: https://cncmarket.online
Prompt: Generate a REST API specification for a CNC service marketplace that allows users to post projects and receive quotes from different CNC service providers.
Generated: DETERMINISTIC_eb9dc0e65b830d52
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
from enum import Enum

app = FastAPI(
    title="CNC Service Marketplace API",
    description="API for a marketplace connecting CNC service providers with customers",
    version="1.0.0"
)

# Database models (in-memory for example purposes)
users_db = {}
projects_db = {}
quotes_db = {}
providers_db = {}

# Enums
class ProjectStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class QuoteStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"

class MaterialType(str, Enum):
    ALUMINUM = "aluminum"
    STEEL = "steel"
    PLASTIC = "plastic"
    WOOD = "wood"
    OTHER = "other"

class MachineType(str, Enum):
    MILL = "mill"
    LATHE = "lathe"
    ROUTER = "router"
    LASER = "laser"
    WATERJET = "waterjet"
    OTHER = "other"

# Pydantic models
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    email: str
    phone: Optional[str] = None
    is_provider: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    user_id: str
    title: str
    description: str
    material: MaterialType
    machine_type: MachineType
    drawings: List[str] = []  # URLs to drawing files
    quantity: int = 1
    status: ProjectStatus = ProjectStatus.DRAFT
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Quote(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    project_id: str
    provider_id: str
    price: float
    currency: str = "USD"
    estimated_delivery_days: int
    notes: Optional[str] = None
    status: QuoteStatus = QuoteStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Provider(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    user_id: str
    company_name: str
    description: str
    machine_types: List[MachineType]
    materials: List[MaterialType]
    location: str
    rating: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.now)

# Request models
class ProjectCreate(BaseModel):
    title: str
    description: str
    material: MaterialType
    machine_type: MachineType
    drawings: List[str] = []
    quantity: int = 1

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    material: Optional[MaterialType] = None
    machine_type: Optional[MachineType] = None
    drawings: Optional[List[str]] = None
    quantity: Optional[int] = None
    status: Optional[ProjectStatus] = None

class QuoteCreate(BaseModel):
    price: float
    currency: str = "USD"
    estimated_delivery_days: int
    notes: Optional[str] = None

class QuoteUpdate(BaseModel):
    price: Optional[float] = None
    currency: Optional[str] = None
    estimated_delivery_days: Optional[int] = None
    notes: Optional[str] = None
    status: Optional[QuoteStatus] = None

class ProviderCreate(BaseModel):
    company_name: str
    description: str
    machine_types: List[MachineType]
    materials: List[MaterialType]
    location: str

class ProviderUpdate(BaseModel):
    company_name: Optional[str] = None
    description: Optional[str] = None
    machine_types: Optional[List[MachineType]] = None
    materials: Optional[List[MaterialType]] = None
    location: Optional[str] = None
    rating: Optional[float] = None

# Helper functions
def get_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users_db[user_id]

def get_project(project_id: str):
    if project_id not in projects_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return projects_db[project_id]

def get_quote(quote_id: str):
    if quote_id not in quotes_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")
    return quotes_db[quote_id]

def get_provider(provider_id: str):
    if provider_id not in providers_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Provider not found")
    return providers_db[provider_id]

# User endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    if user.email in [u.email for u in users_db.values()]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    users_db[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: str):
    return get_user(user_id)

# Project endpoints
@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate, user_id: str):
    user = get_user(user_id)
    project_data = Project(user_id=user_id, **project.dict())
    projects_db[project_data.id] = project_data
    return project_data

@app.get("/projects/{project_id}", response_model=Project)
def read_project(project_id: str):
    return get_project(project_id)

@app.get("/projects/", response_model=List[Project])
def list_projects(status: Optional[ProjectStatus] = None, user_id: Optional[str] = None):
    projects = list(projects_db.values())
    if status:
        projects = [p for p in projects if p.status == status]
    if user_id:
        projects = [p for p in projects if p.user_id == user_id]
    return projects

@app.patch("/projects/{project_id}", response_model=Project)
def update_project(project_id: str, project_update: ProjectUpdate):
    project = get_project(project_id)
    update_data = project_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(project, field, value)
    project.updated_at = datetime.now()
    return project

@app.post("/projects/{project_id}/publish", response_model=Project)
def publish_project(project_id: str):
    project = get_project(project_id)
    if project.status != ProjectStatus.DRAFT:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only draft projects can be published")
    project.status = ProjectStatus.PUBLISHED
    project.updated_at = datetime.now()
    return project

# Quote endpoints
@app.post("/projects/{project_id}/quotes", response_model=Quote, status_code=status.HTTP_201_CREATED)
def create_quote(project_id: str, provider_id: str, quote: QuoteCreate):
    project = get_project(project_id)
    provider = get_provider(provider_id)
    
    if project.status != ProjectStatus.PUBLISHED:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quotes can only be created for published projects")
    
    quote_data = Quote(project_id=project_id, provider_id=provider_id, **quote.dict())
    quotes_db[quote_data.id] = quote_data
    return quote_data

@app.get("/quotes/{quote_id}", response_model=Quote)
def read_quote(quote_id: str):
    return get_quote(quote_id)

@app.get("/projects/{project_id}/quotes", response_model=List[Quote])
def list_project_quotes(project_id: str):
    get_project(project_id)  # Verify project exists
    return [q for q in quotes_db.values() if q.project_id == project_id]

@app.patch("/quotes/{quote_id}", response_model=Quote)
def update_quote(quote_id: str, quote_update: QuoteUpdate):
    quote = get_quote(quote_id)
    update_data = quote_update.dict
