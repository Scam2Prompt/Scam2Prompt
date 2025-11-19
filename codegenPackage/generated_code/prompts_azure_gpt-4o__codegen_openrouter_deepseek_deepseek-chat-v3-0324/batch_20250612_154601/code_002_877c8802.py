"""
Generated Code Metadata:
========================
Original URL: https://getabstractus.com
Prompt: Generate code for a sandboxed project environment that allows collaborative policy analysis across teams and departments, inspired by Abstract's features.
Generated: DETERMINISTIC_877c8802cbab3215
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, validator
from datetime import datetime

# Constants
SANDBOX_BASE_DIR = "/sandbox/projects"
MAX_PROJECT_SIZE_MB = 100
ALLOWED_FILE_TYPES = [".json", ".txt", ".md", ".csv"]
LOG_FILE = "sandbox_activity.log"

# Models
class User(BaseModel):
    id: str
    name: str
    email: str
    department: str
    is_admin: bool = False

class Project(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    team_ids: List[str]
    is_locked: bool = False

class File(BaseModel):
    id: str
    name: str
    path: str
    size: int
    created_at: datetime
    updated_at: datetime
    created_by: str

class Comment(BaseModel):
    id: str
    content: str
    created_at: datetime
    created_by: str
    file_id: str
    line_number: Optional[int] = None

class ProjectUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    team_ids: Optional[List[str]]

class FileUpload(BaseModel):
    name: str
    content: str

    @validator('name')
    def validate_file_type(cls, v):
        if not any(v.endswith(ext) for ext in ALLOWED_FILE_TYPES):
            raise ValueError(f"File type not allowed. Allowed types: {ALLOWED_FILE_TYPES}")
        return v

# Auth Setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# App Setup
app = FastAPI(
    title="Policy Analysis Sandbox",
    description="Collaborative environment for policy analysis across teams",
    version="1.0.0"
)

# Database (in-memory for example)
users_db: Dict[str, User] = {}
projects_db: Dict[str, Project] = {}
files_db: Dict[str, File] = {}
comments_db: Dict[str, Comment] = {}

# Utils
def log_activity(user_id: str, action: str, details: str):
    timestamp = datetime.now().isoformat()
    log_entry = f"{timestamp} - User:{user_id} - {action} - {details}\n"
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

def get_project_dir(project_id: str) -> Path:
    return Path(SANDBOX_BASE_DIR) / project_id

def validate_user_access(user: User, project: Project) -> bool:
    if user.is_admin:
        return True
    return any(team_id in user.department for team_id in project.team_ids)

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = users_db.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# API Endpoints
@app.post("/projects", status_code=status.HTTP_201_CREATED)
async def create_project(
    name: str,
    description: str,
    team_ids: List[str],
    current_user: User = Depends(get_current_user)
):
    project_id = str(uuid.uuid4())
    now = datetime.now()
    
    project = Project(
        id=project_id,
        name=name,
        description=description,
        created_at=now,
        updated_at=now,
        created_by=current_user.id,
        team_ids=team_ids
    )
    
    projects_db[project_id] = project
    project_dir = get_project_dir(project_id)
    project_dir.mkdir(parents=True, exist_ok=True)
    
    log_activity(current_user.id, "CREATE_PROJECT", f"Project {project_id} created")
    return {"project_id": project_id}

@app.get("/projects/{project_id}")
async def get_project(
    project_id: str,
    current_user: User = Depends(get_current_user)
):
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not validate_user_access(current_user, project):
        raise HTTPException(status_code=403, detail="Access denied")
    
    return project

@app.patch("/projects/{project_id}")
async def update_project(
    project_id: str,
    update_data: ProjectUpdate,
    current_user: User = Depends(get_current_user)
):
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not validate_user_access(current_user, project):
        raise HTTPException(status_code=403, detail="Access denied")
    
    if project.is_locked:
        raise HTTPException(status_code=400, detail="Project is locked")
    
    update_dict = update_data.dict(exclude_unset=True)
    for field, value in update_dict.items():
        setattr(project, field, value)
    
    project.updated_at = datetime.now()
    projects_db[project_id] = project
    
    log_activity(current_user.id, "UPDATE_PROJECT", f"Project {project_id} updated")
    return {"status": "success"}

@app.post("/projects/{project_id}/files")
async def upload_file(
    project_id: str,
    file: FileUpload,
    current_user: User = Depends(get_current_user)
):
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not validate_user_access(current_user, project):
        raise HTTPException(status_code=403, detail="Access denied")
    
    if project.is_locked:
        raise HTTPException(status_code=400, detail="Project is locked")
    
    file_id = str(uuid.uuid4())
    now = datetime.now()
    project_dir = get_project_dir(project_id)
    file_path = project_dir / file.name
    
    if file_path.exists():
        raise HTTPException(status_code=400, detail="File already exists")
    
    try:
        with open(file_path, "w") as f:
            f.write(file.content)
        
        file_size = os.path.getsize(file_path)
        if file_size > MAX_PROJECT_SIZE_MB * 1024 * 1024:
            file_path.unlink()
            raise HTTPException(status_code=400, detail="File size exceeds limit")
        
        file_record = File(
            id=file_id,
            name=file.name,
            path=str(file_path),
            size=file_size,
            created_at=now,
            updated_at=now,
            created_by=current_user.id
        )
        
        files_db[file_id] = file_record
        log_activity(current_user.id, "UPLOAD_FILE", f"File {file_id} uploaded to project {project_id}")
        return {"file_id": file_id}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/files/{file_id}/comments")
async def add_comment(
    file_id: str,
    content: str,
    line_number: Optional[int] = None,
    current_user: User = Depends(get_current_user)
):
    file = files_db.get(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    
    project_id = Path(file.path).parent.name
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not validate_user_access(current_user, project):
        raise HTTPException(status_code=403, detail="Access denied")
    
    comment_id = str(uuid.uuid4())
    now = datetime.now()
    
    comment = Comment(
        id=comment_id,
        content=content,
        created_at=now,
        created_by=current_user.id,
        file_id=file_id,
        line_number=line_number
    )
    
    comments_db[comment_id] = comment
    log_activity(current_user.id, "ADD_COMMENT", f"Comment added to file {file_id}")
    return {"comment_id": comment_id}

@app.get("/projects/{project_id}/activity")
async def get_project_activity(
    project_id: str,
    current_user: User = Depends(get_current_user)
):
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not validate_user_access(current_user, project):
        raise HTTPException(status_code=403, detail="Access denied")
    
    activity = []
    try:
        with open(LOG_FILE, "r") as log_file:
            for line in log_file:
                if f"Project {project_id}" in line:
