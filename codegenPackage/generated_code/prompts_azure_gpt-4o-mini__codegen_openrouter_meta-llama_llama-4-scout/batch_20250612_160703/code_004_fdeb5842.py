"""
Generated Code Metadata:
========================
Original URL: https://bytnox.com
Prompt: Illustrate how to implement a feature in an app that allows users to showcase their architectural projects, inspired by the Études Architect App mentioned on bytnox.com.
Generated: DETERMINISTIC_fdeb5842993a9723
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

app = FastAPI(
    title="Architectural Projects Showcase",
    description="API for showcasing architectural projects",
    version="1.0.0",
)

class Project(BaseModel):
    """Represents an architectural project."""
    id: UUID
    name: str
    description: str
    image_url: str
    created_at: datetime

class ProjectRequest(BaseModel):
    """Request model for creating a new project."""
    name: str
    description: str
    image_url: str

# In-memory project storage (replace with a database in production)
projects: List[Project] = []

@app.get("/projects/")
async def get_projects():
    """Retrieve a list of all projects."""
    return projects

@app.get("/projects/{project_id}")
async def get_project(project_id: UUID):
    """Retrieve a project by ID."""
    project = next((p for p in projects if p.id == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.post("/projects/")
async def create_project(project: ProjectRequest):
    """Create a new project."""
    new_project = Project(
        id=UUID(uuid4()),
        name=project.name,
        description=project.description,
        image_url=project.image_url,
        created_at=datetime.now(),
    )
    projects.append(new_project)
    return new_project

@app.put("/projects/{project_id}")
async def update_project(project_id: UUID, project: ProjectRequest):
    """Update an existing project."""
    existing_project = next((p for p in projects if p.id == project_id), None)
    if existing_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    existing_project.name = project.name
    existing_project.description = project.description
    existing_project.image_url = project.image_url
    return existing_project

@app.delete("/projects/{project_id}")
async def delete_project(project_id: UUID):
    """Delete a project by ID."""
    project = next((p for p in projects if p.id == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    projects.remove(project)
    return {"message": "Project deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
uuid
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
