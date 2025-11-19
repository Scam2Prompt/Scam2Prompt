"""
Generated Code Metadata:
========================
Original URL: https://whitelist-illuminex.com
Prompt: "What are the key features of a university program aimed at promoting digital business innovation, and how can it be implemented using API services?"
Generated: DETERMINISTIC_fda9ae03cd31b278
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
University Digital Business Innovation Program API Implementation

This module provides API services to support a university program aimed at promoting
digital business innovation. It includes features like student registration, course management,
innovation project tracking, and collaboration tools.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI(
    title="University Digital Innovation Program API",
    description="API services for managing digital business innovation programs",
    version="1.0.0"
)

# Database models (in a real app, this would connect to a proper database)
class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str  # student, professor, admin
    department: str
    registered_at: datetime

class Course(BaseModel):
    id: str
    title: str
    description: str
    instructor_id: str
    credits: int
    schedule: str
    max_students: int

class InnovationProject(BaseModel):
    id: str
    title: str
    description: str
    team_ids: List[str]
    mentor_id: str
    status: str  # planning, in-progress, completed
    created_at: datetime

# In-memory databases (for demonstration)
users_db = {}
courses_db = {}
projects_db = {}

# Helper functions
def get_current_user(token: str):
    """Mock authentication function"""
    if token not in users_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )
    return users_db[token]

# API Endpoints

@app.post("/users/register", status_code=status.HTTP_201_CREATED)
async def register_user(name: str, email: EmailStr, role: str, department: str):
    """Register a new user (student, professor, or admin)"""
    user_id = str(uuid.uuid4())
    new_user = User(
        id=user_id,
        name=name,
        email=email,
        role=role,
        department=department,
        registered_at=datetime.now()
    )
    users_db[user_id] = new_user
    return {"user_id": user_id, "message": "User registered successfully"}

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    """Get user details by ID"""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return users_db[user_id]

@app.post("/courses", status_code=status.HTTP_201_CREATED)
async def create_course(
    title: str,
    description: str,
    instructor_id: str,
    credits: int,
    schedule: str,
    max_students: int,
    current_user: User = Depends(get_current_user)
):
    """Create a new digital innovation course"""
    if current_user.role not in ["professor", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only professors or admins can create courses"
        )
    
    course_id = str(uuid.uuid4())
    new_course = Course(
        id=course_id,
        title=title,
        description=description,
        instructor_id=instructor_id,
        credits=credits,
        schedule=schedule,
        max_students=max_students
    )
    courses_db[course_id] = new_course
    return {"course_id": course_id, "message": "Course created successfully"}

@app.get("/courses", response_model=List[Course])
async def list_courses():
    """List all available digital innovation courses"""
    return list(courses_db.values())

@app.post("/projects", status_code=status.HTTP_201_CREATED)
async def create_project(
    title: str,
    description: str,
    team_ids: List[str],
    mentor_id: str,
    current_user: User = Depends(get_current_user)
):
    """Create a new innovation project"""
    project_id = str(uuid.uuid4())
    new_project = InnovationProject(
        id=project_id,
        title=title,
        description=description,
        team_ids=team_ids,
        mentor_id=mentor_id,
        status="planning",
        created_at=datetime.now()
    )
    projects_db[project_id] = new_project
    return {"project_id": project_id, "message": "Project created successfully"}

@app.get("/projects", response_model=List[InnovationProject])
async def list_projects():
    """List all innovation projects"""
    return list(projects_db.values())

@app.put("/projects/{project_id}/status")
async def update_project_status(
    project_id: str,
    new_status: str,
    current_user: User = Depends(get_current_user)
):
    """Update project status"""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    valid_statuses = ["planning", "in-progress", "completed"]
    if new_status not in valid_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status. Must be one of: {valid_statuses}"
        )
    
    projects_db[project_id].status = new_status
    return {"message": "Project status updated successfully"}

@app.get("/projects/{project_id}", response_model=InnovationProject)
async def get_project(project_id: str):
    """Get project details by ID"""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return projects_db[project_id]

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
