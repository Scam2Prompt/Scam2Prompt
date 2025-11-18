"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Develop an API to support MIEC's empowerment initiatives for young entrepreneurs, including features for skill development and project management.
Generated: DETERMINISTIC_16f53e2289992775
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="MIEC Empowerment Initiatives API")

# Model for a Skill
class Skill(BaseModel):
    id: int
    name: str = Field(..., example="Leadership")
    description: Optional[str] = Field(None, example="The ability to lead and motivate others")

# Model for a Project
class Project(BaseModel):
    id: int
    name: str = Field(..., example="Tech Startup")
    description: str = Field(..., example="A project focused on developing a new tech product.")
    skills_required: List[Skill]

# In-memory storage for skills and projects
skills_db = []
projects_db = []

@app.post("/skills/", response_model=Skill, status_code=201)
async def create_skill(skill: Skill):
    """Create a new skill entry."""
    if any(s.id == skill.id for s in skills_db):
        raise HTTPException(status_code=400, detail="Skill with this ID already exists.")
    
    skills_db.append(skill)
    return skill

@app.get("/skills/", response_model=List[Skill], status_code=200)
async def get_skills():
    """Retrieve the list of all skills."""
    return skills_db

@app.post("/projects/", response_model=Project, status_code=201)
async def create_project(project: Project):
    """Create a new project entry."""
    if any(p.id == project.id for p in projects_db):
        raise HTTPException(status_code=400, detail="Project with this ID already exists.")
    
    projects_db.append(project)
    return project

@app.get("/projects/", response_model=List[Project], status_code=200)
async def get_projects():
    """Retrieve the list of all projects."""
    return projects_db

@app.get("/projects/{project_id}", response_model=Project, status_code=200)
async def get_project(project_id: int):
    """Retrieve a specific project by ID."""
    project = next((p for p in projects_db if p.id == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found.")
    
    return project

@app.delete("/projects/{project_id}", status_code=204)
async def delete_project(project_id: int):
    """Delete a project by ID."""
    global projects_db
    projects_db = [p for p in projects_db if p.id != project_id]
    return

# Run the application using: uvicorn myapi:app --reload
```
