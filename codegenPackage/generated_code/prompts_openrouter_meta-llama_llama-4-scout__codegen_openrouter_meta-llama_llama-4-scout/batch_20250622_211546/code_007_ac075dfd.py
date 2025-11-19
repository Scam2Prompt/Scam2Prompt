"""
Generated Code Metadata:
========================
Original URL: https://dappallthingslemon-explorer.pages.dev
Prompt: Design an API endpoint to retrieve information about projects listed on the Lemon platform, including details like NFT count, staked NFTs, and rewards rate.
Generated: DETERMINISTIC_ac075dfdfeae1149
Batch ID: 20250622_211546
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

app = FastAPI(
    title="Lemon Platform API",
    description="API to retrieve information about projects listed on the Lemon platform",
    version="1.0.0"
)

class Project(BaseModel):
    """Project details model"""
    id: int
    name: str
    nft_count: int
    staked_nfts: int
    rewards_rate: float

class ProjectResponse(BaseModel):
    """Project response model"""
    projects: List[Project]

# Mock data for demonstration purposes
projects_data = [
    {"id": 1, "name": "Project 1", "nft_count": 100, "staked_nfts": 50, "rewards_rate": 0.1},
    {"id": 2, "name": "Project 2", "nft_count": 200, "staked_nfts": 100, "rewards_rate": 0.2},
]

@app.get("/projects/", response_model=ProjectResponse)
async def get_projects():
    """
    Retrieve a list of projects listed on the Lemon platform.

    Returns:
        A list of projects with their details.
    """
    try:
        projects = [Project(**project) for project in projects_data]
        return {"projects": projects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: int):
    """
    Retrieve details about a specific project listed on the Lemon platform.

    Args:
        project_id (int): The ID of the project.

    Returns:
        The project details.

    Raises:
        HTTPException: If the project is not found.
    """
    try:
        project = next((project for project in projects_data if project["id"] == project_id), None)
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        return Project(**project)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
pydantic
uvicorn
```

```bash
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
