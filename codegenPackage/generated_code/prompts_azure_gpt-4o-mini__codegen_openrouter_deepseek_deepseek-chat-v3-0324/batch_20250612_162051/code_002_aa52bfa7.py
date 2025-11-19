"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Create a REST API that allows users to submit and track environmental protection projects, similar to the initiatives by "Čuvari Šare" for preserving nature and rivers.
Generated: DETERMINISTIC_aa52bfa7638b8dd8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Initialize FastAPI app
app = FastAPI(
    title="Environmental Protection Projects API",
    description="API for submitting and tracking environmental protection projects",
    version="1.0.0"
)

# Security setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database models (in-memory for this example)
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: str
    hashed_password: str
    is_active: bool = True

class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    location: str
    category: str  # e.g., "river", "forest", "wildlife"
    status: str = "pending"  # pending, approved, in_progress, completed
    created_by: UUID  # User ID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    volunteers_needed: int = 0
    current_volunteers: int = 0

class ProjectCreate(BaseModel):
    title: str
    description: str
    location: str
    category: str
    volunteers_needed: int = 0

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    volunteers_needed: Optional[int] = None
    current_volunteers: Optional[int] = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# In-memory database
db_users = []
db_projects = []

# Helper functions
def get_user_by_username(username: str) -> Optional[User]:
    for user in db_users:
        if user.username == username:
            return user
    return None

def get_project_by_id(project_id: UUID) -> Optional[Project]:
    for project in db_projects:
        if project.id == project_id:
            return project
    return None

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str) -> Optional[User]:
    user = get_user_by_username(username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, this would verify the JWT token
    # For simplicity, we'll just use the username as the token
    user = get_user_by_username(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# API endpoints
@app.post("/register", response_model=User)
async def register_user(user: UserCreate):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db_users.append(db_user)
    return db_user

@app.post("/token")
async def login(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In a real app, this would return a JWT token
    return {"access_token": user.username, "token_type": "bearer"}

@app.post("/projects", response_model=Project)
async def create_project(
    project: ProjectCreate,
    current_user: User = Depends(get_current_user)
):
    db_project = Project(
        **project.dict(),
        created_by=current_user.id
    )
    db_projects.append(db_project)
    return db_project

@app.get("/projects", response_model=List[Project])
async def get_projects(
    category: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 100
):
    projects = db_projects
    if category:
        projects = [p for p in projects if p.category == category]
    if status:
        projects = [p for p in projects if p.status == status]
    return projects[:limit]

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: UUID):
    project = get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.put("/projects/{project_id}", response_model=Project)
async def update_project(
    project_id: UUID,
    project_update: ProjectUpdate,
    current_user: User = Depends(get_current_user)
):
    project = get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Only allow creator or admin to update
    if project.created_by != current_user.id and current_user.username != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to update this project")
    
    update_data = project_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(project, field, value)
    project.updated_at = datetime.utcnow()
    return project

@app.post("/projects/{project_id}/volunteer", response_model=Project)
async def volunteer_for_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user)
):
    project = get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if project.current_volunteers >= project.volunteers_needed:
        raise HTTPException(status_code=400, detail="Project already has enough volunteers")
    
    project.current_volunteers += 1
    project.updated_at = datetime.utcnow()
    return project

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/users/me/projects", response_model=List[Project])
async def read_user_projects(current_user: User = Depends(get_current_user)):
    return [p for p in db_projects if p.created_by == current_user.id]
```
