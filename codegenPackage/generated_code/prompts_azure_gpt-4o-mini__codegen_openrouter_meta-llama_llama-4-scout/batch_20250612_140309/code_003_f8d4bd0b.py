"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Suggest an API that could help integrate project management tools for educational institutions like I.E. Benjamín Correa Álvarez.
Generated: DETERMINISTIC_f8d4bd0bfe179f2c
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize FastAPI application
app = FastAPI(
    title="Project Management API for Educational Institutions",
    description="API to integrate project management tools for educational institutions",
    version="1.0.0"
)

# Define a model for project
class Project(BaseModel):
    id: int
    name: str
    description: str
    start_date: str
    end_date: str
    status: str

# Define a model for task
class Task(BaseModel):
    id: int
    project_id: int
    name: str
    description: str
    start_date: str
    end_date: str
    status: str
    assigned_to: str

# In-memory data store for projects and tasks
projects: List[Project] = []
tasks: List[Task] = []

# API endpoint to create a new project
@app.post("/projects/")
async def create_project(project: Project):
    try:
        # Check if project with same id already exists
        if any(p.id == project.id for p in projects):
            raise HTTPException(status_code=400, detail="Project with same id already exists")
        
        # Add project to data store
        projects.append(project)
        return {"message": "Project created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all projects
@app.get("/projects/")
async def get_projects():
    try:
        return projects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to create a new task
@app.post("/tasks/")
async def create_task(task: Task):
    try:
        # Check if task with same id already exists
        if any(t.id == task.id for t in tasks):
            raise HTTPException(status_code=400, detail="Task with same id already exists")
        
        # Check if project exists
        if not any(p.id == task.project_id for p in projects):
            raise HTTPException(status_code=400, detail="Project does not exist")
        
        # Add task to data store
        tasks.append(task)
        return {"message": "Task created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get all tasks for a project
@app.get("/projects/{project_id}/tasks/")
async def get_tasks(project_id: int):
    try:
        # Filter tasks by project id
        project_tasks = [t for t in tasks if t.project_id == project_id]
        return project_tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to update project status
@app.put("/projects/{project_id}/status/")
async def update_project_status(project_id: int, status: str):
    try:
        # Find project by id
        project = next((p for p in projects if p.id == project_id), None)
        if project is None:
            raise HTTPException(status_code=400, detail="Project does not exist")
        
        # Update project status
        project.status = status
        return {"message": "Project status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to update task status
@app.put("/tasks/{task_id}/status/")
async def update_task_status(task_id: int, status: str):
    try:
        # Find task by id
        task = next((t for t in tasks if t.id == task_id), None)
        if task is None:
            raise HTTPException(status_code=400, detail="Task does not exist")
        
        # Update task status
        task.status = status
        return {"message": "Task status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
