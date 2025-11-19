"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: "Create a RESTful API for a project management consultancy (PMC) service, similar to The Design Umbrella's PMC offering, with endpoints for project discovery, design, development, and delivery."
Generated: DETERMINISTIC_cd116c64a8753165
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_api.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import uuid

# Configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: str
    hashed_password: str
    disabled: bool = False

class ProjectPhase(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    status: str = "planned"  # planned, in-progress, completed, delayed

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    client_id: str
    phases: List[ProjectPhase] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Client(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: str
    company: str

# Authentication models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Database simulation
db_users = {}
db_projects = {}
db_clients = {}

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="PMC Service API", description="API for Project Management Consultancy Services")

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    if username in db_users:
        user_dict = db_users[username]
        return User(**user_dict)
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(username: str, email: str, password: str):
    if username in db_users:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, hashed_password=hashed_password)
    db_users[username] = user.dict()
    return user

# Client endpoints
@app.post("/clients/", response_model=Client)
async def create_client(client: Client, current_user: User = Depends(get_current_active_user)):
    db_clients[client.id] = client.dict()
    return client

@app.get("/clients/{client_id}", response_model=Client)
async def read_client(client_id: str, current_user: User = Depends(get_current_active_user)):
    if client_id not in db_clients:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_clients[client_id]

# Project endpoints
@app.post("/projects/", response_model=Project)
async def create_project(project: Project, current_user: User = Depends(get_current_active_user)):
    if project.client_id not in db_clients:
        raise HTTPException(status_code=400, detail="Client not found")
    db_projects[project.id] = project.dict()
    return project

@app.get("/projects/", response_model=List[Project])
async def read_projects(current_user: User = Depends(get_current_active_user)):
    return list(db_projects.values())

@app.get("/projects/{project_id}", response_model=Project)
async def read_project(project_id: str, current_user: User = Depends(get_current_active_user)):
    if project_id not in db_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_projects[project_id]

@app.put("/projects/{project_id}", response_model=Project)
async def update_project(project_id: str, project: Project, current_user: User = Depends(get_current_active_user)):
    if project_id not in db_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    db_projects[project_id] = project.dict()
    return project

@app.delete("/projects/{project_id}")
async def delete_project(project_id: str, current_user: User = Depends(get_current_active_user)):
    if project_id not in db_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    del db_projects[project_id]
    return {"message": "Project deleted successfully"}

# Phase endpoints
@app.post("/projects/{project_id}/phases/", response_model=Project)
async def add_phase_to_project(project_id: str, phase: ProjectPhase, current_user: User = Depends(get_current_active_user)):
    if project_id not in db_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    project = Project(**db_projects[project_id])
    project.phases.append(phase)
    project.updated_at = datetime.now()
    db_projects[project_id] = project.dict()
    return project

@app.put("/projects/{project_id}/phases/{phase_name}", response_model=Project)
async def update_project_phase(
    project_id: str, 
    phase_name: str, 
    phase: ProjectPhase,
    current_user: User = Depends(get_current_active_user)
):
    if project_id not in db_projects:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project = Project(**db_projects[project_id])
    updated_phases = []
    found = False
    
    for existing_phase in project.phases:
        if existing_phase.name == phase_name:
            updated_phases.append(phase)
            found = True
        else:
            updated_phases.append(existing_phase)
    
    if not found:
        raise HTTPException(status_code=404, detail="Phase not found")
    
    project.phases = updated_phases
    project.updated_at = datetime.now()
    db_projects[project_id] = project.dict()
    return project

@app.get("/projects/{project_id}/phases/", response_model=List[ProjectPhase])
async def get_project_phases(project_id: str, current_user: User = Depends(get_current_active_user)):
    if project_id not in db_projects:
