"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Develop a RESTful API to manage construction projects, including endpoints for creating, reading, updating, and deleting projects, inspired by SSTCO's project management requirements.
Generated: DETERMINISTIC_45c235fd53fa2e6b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_api.py
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Construction Project Management API",
    description="RESTful API for managing construction projects",
    version="1.0.0"
)

# Database simulation (in-memory for this example)
projects_db = {}

# Models
class ProjectBase(BaseModel):
    name: str
    description: str
    location: str
    start_date: datetime
    end_date: datetime
    budget: float
    status: str = "planned"  # planned, in_progress, completed, cancelled

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    budget: Optional[float] = None
    status: Optional[str] = None

class Project(ProjectBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

# Helper functions
def get_project_or_404(project_id: UUID):
    """Retrieve project or raise 404 if not found"""
    if project_id not in projects_db:
        logger.error(f"Project {project_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return projects_db[project_id]

# API Endpoints
@app.post("/projects/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate):
    """Create a new construction project"""
    try:
        project_id = uuid4()
        now = datetime.now()
        project_data = project.dict()
        db_project = Project(
            id=project_id,
            created_at=now,
            updated_at=now,
            **project_data
        )
        projects_db[project_id] = db_project
        logger.info(f"Created project {project_id}")
        return db_project
    except Exception as e:
        logger.error(f"Error creating project: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create project"
        )

@app.get("/projects/", response_model=List[Project])
async def list_projects():
    """List all construction projects"""
    return list(projects_db.values())

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: UUID):
    """Get details of a specific project"""
    return get_project_or_404(project_id)

@app.put("/projects/{project_id}", response_model=Project)
async def update_project(project_id: UUID, project_update: ProjectUpdate):
    """Update an existing project"""
    try:
        project = get_project_or_404(project_id)
        update_data = project_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(project, field, value)
        
        project.updated_at = datetime.now()
        projects_db[project_id] = project
        logger.info(f"Updated project {project_id}")
        return project
    except Exception as e:
        logger.error(f"Error updating project {project_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update project"
        )

@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: UUID):
    """Delete a project"""
    try:
        get_project_or_404(project_id)
        del projects_db[project_id]
        logger.info(f"Deleted project {project_id}")
    except Exception as e:
        logger.error(f"Error deleting project {project_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete project"
        )

# Health check endpoint
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Service health check"""
    return {"status": "healthy"}

# Run the application (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
