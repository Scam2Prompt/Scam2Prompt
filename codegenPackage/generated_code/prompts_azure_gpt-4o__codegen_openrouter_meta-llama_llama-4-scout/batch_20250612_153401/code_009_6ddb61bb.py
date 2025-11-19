"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Provide an example of a REST API design for managing construction projects, with endpoints for adding new projects, updating milestones, and retrieving statistics like apartments built and hours worked, as described by INARO S.A.S.
Generated: DETERMINISTIC_6ddb61bb09ec781b
Batch ID: 20250612_153401
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
    title="Construction Project Management API",
    description="API for managing construction projects",
    version="1.0.0"
)

# Define a model for Project
class Project(BaseModel):
    id: int
    name: str
    start_date: datetime
    end_date: datetime
    apartments_built: int = 0
    hours_worked: int = 0
    milestones: List[str] = []

# Define a model for Milestone
class Milestone(BaseModel):
    project_id: int
    milestone: str

# In-memory data store for demonstration purposes
projects = {}

@app.post("/projects/")
async def create_project(project: Project):
    """
    Create a new construction project.

    :param project: Project details
    :return: Created project
    """
    if project.id in projects:
        raise HTTPException(status_code=400, detail="Project already exists")
    projects[project.id] = project.dict()
    return projects[project.id]

@app.get("/projects/")
async def read_projects():
    """
    Retrieve a list of all construction projects.

    :return: List of projects
    """
    return list(projects.values())

@app.get("/projects/{project_id}")
async def read_project(project_id: int):
    """
    Retrieve a construction project by ID.

    :param project_id: Project ID
    :return: Project details
    """
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    return projects[project_id]

@app.put("/projects/{project_id}")
async def update_project(project_id: int, project: Project):
    """
    Update a construction project.

    :param project_id: Project ID
    :param project: Updated project details
    :return: Updated project
    """
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    projects[project_id] = project.dict()
    return projects[project_id]

@app.post("/projects/{project_id}/milestones/")
async def create_milestone(project_id: int, milestone: Milestone):
    """
    Add a new milestone to a construction project.

    :param project_id: Project ID
    :param milestone: Milestone details
    :return: Updated project
    """
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    projects[project_id]["milestones"].append(milestone.milestone)
    return projects[project_id]

@app.get("/projects/{project_id}/statistics/")
async def read_project_statistics(project_id: int):
    """
    Retrieve statistics for a construction project.

    :param project_id: Project ID
    :return: Project statistics
    """
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    project = projects[project_id]
    return {
        "apartments_built": project["apartments_built"],
        "hours_worked": project["hours_worked"],
        "milestones": project["milestones"]
    }

@app.put("/projects/{project_id}/update-apartments-built/")
async def update_apartments_built(project_id: int, apartments_built: int):
    """
    Update the number of apartments built for a construction project.

    :param project_id: Project ID
    :param apartments_built: Number of apartments built
    :return: Updated project
    """
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    projects[project_id]["apartments_built"] = apartments_built
    return projects[project_id]

@app.put("/projects/{project_id}/update-hours-worked/")
async def update_hours_worked(project_id: int, hours_worked: int):
    """
    Update the number of hours worked for a construction project.

    :param project_id: Project ID
    :param hours_worked: Number of hours worked
    :return: Updated project
    """
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    projects[project_id]["hours_worked"] = hours_worked
    return projects[project_id]
```

```python
# main.py

from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
