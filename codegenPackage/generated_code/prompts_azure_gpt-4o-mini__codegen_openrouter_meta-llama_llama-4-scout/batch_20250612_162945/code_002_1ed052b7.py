"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Create an API endpoint for a consultancy service that allows users to submit project ideas and request tailored solutions, reflecting the custom consultancy approach of Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_1ed052b79a7aa1af
Batch ID: 20250612_162945
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
from typing import Optional
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Dusanto Consultancy Trading OU API",
    description="API for submitting project ideas and requesting tailored solutions",
    version="1.0.0",
)

# Define the project idea model
class ProjectIdea(BaseModel):
    """Project idea model"""
    title: str
    description: str
    goals: Optional[str]
    requirements: Optional[str]

# In-memory project idea storage (replace with a database in production)
project_ideas = []

@app.post("/project-ideas/")
async def create_project_idea(project_idea: ProjectIdea):
    """Create a new project idea"""
    try:
        # Validate the project idea
        if not project_idea.title or not project_idea.description:
            raise HTTPException(status_code=400, detail="Title and description are required")

        # Store the project idea
        project_ideas.append(project_idea.dict())
        logger.info("Project idea created")

        return {"message": "Project idea created successfully"}
    except Exception as e:
        logger.error(f"Error creating project idea: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/project-ideas/")
async def get_project_ideas():
    """Get all project ideas"""
    try:
        return project_ideas
    except Exception as e:
        logger.error(f"Error getting project ideas: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/project-ideas/{project_idea_id}")
async def get_project_idea(project_idea_id: int):
    """Get a project idea by ID"""
    try:
        project_idea = project_ideas[project_idea_id]
        return project_idea
    except IndexError:
        raise HTTPException(status_code=404, detail="Project idea not found")
    except Exception as e:
        logger.error(f"Error getting project idea: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.put("/project-ideas/{project_idea_id}")
async def update_project_idea(project_idea_id: int, project_idea: ProjectIdea):
    """Update a project idea"""
    try:
        if project_idea_id >= len(project_ideas):
            raise HTTPException(status_code=404, detail="Project idea not found")

        project_ideas[project_idea_id] = project_idea.dict()
        logger.info("Project idea updated")
        return {"message": "Project idea updated successfully"}
    except Exception as e:
        logger.error(f"Error updating project idea: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/project-ideas/{project_idea_id}")
async def delete_project_idea(project_idea_id: int):
    """Delete a project idea"""
    try:
        if project_idea_id >= len(project_ideas):
            raise HTTPException(status_code=404, detail="Project idea not found")

        del project_ideas[project_idea_id]
        logger.info("Project idea deleted")
        return {"message": "Project idea deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting project idea: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

```python
# main.py

import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
