"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Create an API that allows users to track the development of aerospace and defense projects in India, referencing Aanjaneya Aerodynamics' focus on joint ventures and partnerships.
Generated: DETERMINISTIC_3940c9a1f18b0359
Batch ID: 20250612_160656
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
from datetime import datetime

app = FastAPI(
    title="Aerospace and Defense Project Tracker",
    description="API to track development of aerospace and defense projects in India",
    version="1.0.0"
)

# Define a model for projects
class Project(BaseModel):
    id: int
    name: str
    description: str
    joint_venture: bool
    partnership: bool
    start_date: datetime
    end_date: datetime
    status: str

# In-memory data store for projects (replace with a database in production)
projects: List[Project] = [
    Project(
        id=1,
        name="Project Akash",
        description="Development of a new aircraft",
        joint_venture=True,
        partnership=False,
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2025, 1, 1),
        status="In Progress"
    ),
    Project(
        id=2,
        name="Project Raksha",
        description="Development of a new defense system",
        joint_venture=False,
        partnership=True,
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2026, 1, 1),
        status="Planning"
    )
]

# API endpoint to get all projects
@app.get("/projects/")
async def get_all_projects():
    """Returns a list of all projects"""
    return projects

# API endpoint to get a project by ID
@app.get("/projects/{project_id}")
async def get_project(project_id: int):
    """Returns a project by ID"""
    for project in projects:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="Project not found")

# API endpoint to create a new project
@app.post("/projects/")
async def create_project(project: Project):
    """Creates a new project"""
    # Check for duplicate project IDs
    for p in projects:
        if p.id == project.id:
            raise HTTPException(status_code=400, detail="Project ID already exists")
    projects.append(project)
    return project

# API endpoint to update a project
@app.put("/projects/{project_id}")
async def update_project(project_id: int, project: Project):
    """Updates a project"""
    for i, p in enumerate(projects):
        if p.id == project_id:
            # Validate updated project ID
            if project.id != project_id:
                raise HTTPException(status_code=400, detail="Project ID cannot be updated")
            projects[i] = project
            return project
    raise HTTPException(status_code=404, detail="Project not found")

# API endpoint to delete a project
@app.delete("/projects/{project_id}")
async def delete_project(project_id: int):
    """Deletes a project"""
    for i, project in enumerate(projects):
        if project.id == project_id:
            del projects[i]
            return {"message": "Project deleted successfully"}
    raise HTTPException(status_code=404, detail="Project not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt

fastapi
uvicorn
pydantic
```

```bash
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
