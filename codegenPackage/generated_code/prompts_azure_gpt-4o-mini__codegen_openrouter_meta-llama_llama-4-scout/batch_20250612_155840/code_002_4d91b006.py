"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: Create a RESTful API design for a construction company that highlights architectural design and project planning, reflecting the services offered by Albatros SPA.
Generated: DETERMINISTIC_4d91b006d5d6836f
Batch ID: 20250612_155840
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
    title="Albatros SPA Construction Company API",
    description="API for architectural design and project planning services",
    version="1.0.0",
)

# Define a model for Project
class Project(BaseModel):
    id: int
    name: str
    description: str
    status: str

# Define a model for Service
class Service(BaseModel):
    id: int
    name: str
    description: str

# In-memory data store for demonstration purposes
projects: List[Project] = [
    Project(id=1, name="Project 1", description="Description 1", status="In Progress"),
    Project(id=2, name="Project 2", description="Description 2", status="Completed"),
]

services: List[Service] = [
    Service(id=1, name="Architectural Design", description="Design services for buildings"),
    Service(id=2, name="Project Planning", description="Planning services for construction projects"),
]

# GET /
@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    return {"message": "Welcome to Albatros SPA Construction Company API"}

# GET /projects
@app.get("/projects/", status_code=status.HTTP_200_OK, response_model=List[Project])
async def read_projects():
    return projects

# GET /projects/{project_id}
@app.get("/projects/{project_id}", status_code=status.HTTP_200_OK, response_model=Project)
async def read_project(project_id: int):
    for project in projects:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

# POST /projects
@app.post("/projects/", status_code=status.HTTP_201_CREATED, response_model=Project)
async def create_project(project: Project):
    projects.append(project)
    return project

# PUT /projects/{project_id}
@app.put("/projects/{project_id}", status_code=status.HTTP_200_OK, response_model=Project)
async def update_project(project_id: int, project: Project):
    for i, existing_project in enumerate(projects):
        if existing_project.id == project_id:
            projects[i] = project
            return project
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

# DELETE /projects/{project_id}
@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int):
    for i, project in enumerate(projects):
        if project.id == project_id:
            del projects[i]
            return {"message": "Project deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

# GET /services
@app.get("/services/", status_code=status.HTTP_200_OK, response_model=List[Service])
async def read_services():
    return services

# GET /services/{service_id}
@app.get("/services/{service_id}", status_code=status.HTTP_200_OK, response_model=Service)
async def read_service(service_id: int):
    for service in services:
        if service.id == service_id:
            return service
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
