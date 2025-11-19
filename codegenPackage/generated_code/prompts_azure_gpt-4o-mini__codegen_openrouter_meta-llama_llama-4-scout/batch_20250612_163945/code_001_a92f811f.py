"""
Generated Code Metadata:
========================
Original URL: https://www.cloud-telephonie.net
Prompt: How can I implement an API to handle user project selection and urgency status in a telephony service application?
Generated: DETERMINISTIC_a92f811fba23b133
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Telephony Service API",
    description="API to handle user project selection and urgency status",
    version="1.0.0"
)

# Define Pydantic models for request and response bodies
class Project(BaseModel):
    id: int
    name: str

class UrgencyStatus(BaseModel):
    id: int
    status: str

class UserProject(BaseModel):
    user_id: int
    project_id: int
    urgency_status_id: int

class ProjectResponse(BaseModel):
    id: int
    name: str
    users: List[int]

class UrgencyStatusResponse(BaseModel):
    id: int
    status: str
    users: List[int]

# In-memory data store for demonstration purposes
projects = [
    Project(id=1, name="Project 1"),
    Project(id=2, name="Project 2")
]

urgency_statuses = [
    UrgencyStatus(id=1, status="Low"),
    UrgencyStatus(id=2, status="High")
]

user_projects = []

# API Endpoints
@app.get("/projects/", response_model=List[ProjectResponse])
def get_projects():
    """Retrieve a list of all projects"""
    project_responses = []
    for project in projects:
        user_ids = [user.user_id for user in user_projects if user.project_id == project.id]
        project_responses.append(ProjectResponse(id=project.id, name=project.name, users=user_ids))
    return project_responses

@app.get("/urgency-statuses/", response_model=List[UrgencyStatusResponse])
def get_urgency_statuses():
    """Retrieve a list of all urgency statuses"""
    urgency_status_responses = []
    for urgency_status in urgency_statuses:
        user_ids = [user.user_id for user in user_projects if user.urgency_status_id == urgency_status.id]
        urgency_status_responses.append(UrgencyStatusResponse(id=urgency_status.id, status=urgency_status.status, users=user_ids))
    return urgency_status_responses

@app.post("/users/{user_id}/projects/{project_id}/urgency-statuses/{urgency_status_id}")
def create_user_project(user_id: int, project_id: int, urgency_status_id: int):
    """Create a new user project with urgency status"""
    project = next((p for p in projects if p.id == project_id), None)
    urgency_status = next((u for u in urgency_statuses if u.id == urgency_status_id), None)
    
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    if not urgency_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Urgency status not found")
    
    existing_user_project = next((u for u in user_projects if u.user_id == user_id and u.project_id == project_id), None)
    if existing_user_project:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User project already exists")
    
    user_project = UserProject(user_id=user_id, project_id=project_id, urgency_status_id=urgency_status_id)
    user_projects.append(user_project)
    return {"message": "User project created successfully"}

@app.get("/users/{user_id}/projects/")
def get_user_projects(user_id: int):
    """Retrieve a list of projects for a user"""
    user_project_responses = []
    for user_project in user_projects:
        if user_project.user_id == user_id:
            project = next((p for p in projects if p.id == user_project.project_id), None)
            urgency_status = next((u for u in urgency_statuses if u.id == user_project.urgency_status_id), None)
            user_project_responses.append({"project": project.name, "urgency_status": urgency_status.status})
    return user_project_responses

@app.put("/users/{user_id}/projects/{project_id}/urgency-statuses/{urgency_status_id}")
def update_user_project_urgency_status(user_id: int, project_id: int, urgency_status_id: int):
    """Update the urgency status of a user project"""
    user_project = next((u for u in user_projects if u.user_id == user_id and u.project_id == project_id), None)
    if not user_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User project not found")
    
    urgency_status = next((u for u in urgency_statuses if u.id == urgency_status_id), None)
    if not urgency_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Urgency status not found")
    
    user_project.urgency_status_id = urgency_status_id
    return {"message": "Urgency status updated successfully"}

@app.delete("/users/{user_id}/projects/{project_id}")
def delete_user_project(user_id: int, project_id: int):
    """Delete a user project"""
    user_project = next((u for u in user_projects if u.user_id == user_id and u.project_id == project_id), None)
    if not user_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User project not found")
    
    user_projects.remove(user_project)
    return {"message": "User project deleted successfully"}
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
