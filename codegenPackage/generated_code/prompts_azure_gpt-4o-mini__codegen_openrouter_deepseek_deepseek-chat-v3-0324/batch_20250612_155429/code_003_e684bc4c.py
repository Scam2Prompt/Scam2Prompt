"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Create a function that allows users to submit their interior design project ideas, inspired by the client collaboration process at Zirciulit.
Generated: DETERMINISTIC_e684bc4ccd0625dc
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status
import uuid

app = FastAPI()

class DesignProject(BaseModel):
    """Represents an interior design project submission."""
    project_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique project identifier")
    title: str = Field(..., min_length=3, max_length=100, description="Project title")
    description: str = Field(..., min_length=10, max_length=1000, description="Detailed project description")
    style: str = Field(..., description="Design style (e.g., Modern, Rustic, Minimalist)")
    room_type: str = Field(..., description="Type of room (e.g., Living Room, Kitchen, Bedroom)")
    budget_range: str = Field(..., description="Budget range (e.g., $1k-$5k, $5k-$10k)")
    color_palette: List[str] = Field(default_factory=list, description="Preferred color palette")
    inspiration_images: Optional[List[str]] = Field(default_factory=list, description="URLs to inspiration images")
    submitted_by: str = Field(..., min_length=2, description="Name of the person submitting")
    email: str = Field(..., description="Contact email")
    submission_date: datetime = Field(default_factory=datetime.now, description="Date of submission")
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()

# In-memory storage for projects (replace with database in production)
projects_db: Dict[str, DesignProject] = {}

@app.post("/projects/", 
          response_model=DesignProject,
          status_code=status.HTTP_201_CREATED,
          summary="Submit a new interior design project",
          description="Allows users to submit their interior design project ideas for collaboration.")
async def submit_project(project: DesignProject):
    """Submit a new interior design project."""
    if project.project_id in projects_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project ID already exists"
        )
    
    projects_db[project.project_id] = project
    return project

@app.get("/projects/{project_id}",
         response_model=DesignProject,
         summary="Get project details",
         description="Retrieve details of a specific interior design project.")
async def get_project(project_id: str):
    """Retrieve a specific project by ID."""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return projects_db[project_id]

@app.get("/projects/",
         response_model=List[DesignProject],
         summary="List all projects",
         description="Retrieve a list of all submitted interior design projects.")
async def list_projects():
    """Retrieve all submitted projects."""
    return list(projects_db.values())

@app.delete("/projects/{project_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Delete a project",
            description="Remove a specific interior design project.")
async def delete_project(project_id: str):
    """Delete a project by ID."""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    del projects_db[project_id]
    return None
```
