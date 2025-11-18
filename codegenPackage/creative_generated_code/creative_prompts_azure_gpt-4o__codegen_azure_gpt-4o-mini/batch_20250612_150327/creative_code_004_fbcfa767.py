"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braavos.rs
Prompt: Suggest tools or libraries for developing an app similar to the Études Architect App, focusing on collaboration features and showcasing architectural projects as mentioned on the Braavos webpage.
Generated: DETERMINISTIC_fbcfa76799bdf67a
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI()

# Define a data model for architectural projects
class Project(BaseModel):
    id: int
    title: str
    description: str
    collaborators: List[str]

# In-memory storage for projects (for demonstration purposes)
projects_db = []

# Endpoint to create a new project
@app.post("/projects/", response_model=Project)
async def create_project(project: Project):
    # Check for duplicate project ID
    if any(p.id == project.id for p in projects_db):
        raise HTTPException(status_code=400, detail="Project ID already exists")
    
    # Add the new project to the database
    projects_db.append(project)
    return project

# Endpoint to retrieve all projects
@app.get("/projects/", response_model=List[Project])
async def get_projects():
    return projects_db

# Endpoint to update a project by ID
@app.put("/projects/{project_id}", response_model=Project)
async def update_project(project_id: int, updated_project: Project):
    # Find the project to update
    for index, project in enumerate(projects_db):
        if project.id == project_id:
            # Update the project details
            projects_db[index] = updated_project
            return updated_project
    raise HTTPException(status_code=404, detail="Project not found")

# Endpoint to delete a project by ID
@app.delete("/projects/{project_id}", response_model=Project)
async def delete_project(project_id: int):
    # Find and remove the project
    for index, project in enumerate(projects_db):
        if project.id == project_id:
            return projects_db.pop(index)
    raise HTTPException(status_code=404, detail="Project not found")

# Main entry point for the application (if needed for running locally)
if __name__ == "__main__":
    import uvicorn
    # Start the FastAPI application with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
