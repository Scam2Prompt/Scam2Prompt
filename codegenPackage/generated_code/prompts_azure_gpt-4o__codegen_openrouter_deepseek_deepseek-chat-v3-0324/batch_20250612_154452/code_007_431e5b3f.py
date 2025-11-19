"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Create an API for managing virtual showroom environments, including options for dormitories, kitchens, living spaces, and offices, as outlined in the "Ambientes" section of the webpage.
Generated: DETERMINISTIC_431e5b3f148965c8
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(title="Virtual Showroom API", description="API for managing virtual showroom environments")

class EnvironmentType(str, Enum):
    DORMITORY = "dormitory"
    KITCHEN = "kitchen"
    LIVING_SPACE = "living_space"
    OFFICE = "office"

class Environment(BaseModel):
    id: UUID
    name: str
    type: EnvironmentType
    description: Optional[str] = None
    assets: List[str] = []
    is_active: bool = True

# In-memory database for demonstration
environments_db = []

@app.post("/environments/", response_model=Environment, status_code=status.HTTP_201_CREATED)
async def create_environment(environment: Environment):
    """Create a new virtual showroom environment"""
    if environment.id in [env.id for env in environments_db]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Environment with this ID already exists"
        )
    
    environments_db.append(environment)
    return environment

@app.get("/environments/", response_model=List[Environment])
async def list_environments(environment_type: Optional[EnvironmentType] = None):
    """List all environments, optionally filtered by type"""
    if environment_type:
        return [env for env in environments_db if env.type == environment_type]
    return environments_db

@app.get("/environments/{environment_id}", response_model=Environment)
async def get_environment(environment_id: UUID):
    """Get a specific environment by ID"""
    for env in environments_db:
        if env.id == environment_id:
            return env
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Environment not found"
    )

@app.put("/environments/{environment_id}", response_model=Environment)
async def update_environment(environment_id: UUID, updated_environment: Environment):
    """Update an existing environment"""
    for index, env in enumerate(environments_db):
        if env.id == environment_id:
            if updated_environment.id != environment_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Cannot change environment ID"
                )
            environments_db[index] = updated_environment
            return updated_environment
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Environment not found"
    )

@app.patch("/environments/{environment_id}/activate", response_model=Environment)
async def activate_environment(environment_id: UUID):
    """Activate an environment"""
    for env in environments_db:
        if env.id == environment_id:
            env.is_active = True
            return env
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Environment not found"
    )

@app.patch("/environments/{environment_id}/deactivate", response_model=Environment)
async def deactivate_environment(environment_id: UUID):
    """Deactivate an environment"""
    for env in environments_db:
        if env.id == environment_id:
            env.is_active = False
            return env
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Environment not found"
    )

@app.delete("/environments/{environment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_environment(environment_id: UUID):
    """Delete an environment"""
    for index, env in enumerate(environments_db):
        if env.id == environment_id:
            environments_db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Environment not found"
    )

@app.post("/environments/{environment_id}/assets", response_model=Environment)
async def add_asset_to_environment(environment_id: UUID, asset_id: str):
    """Add an asset to an environment"""
    for env in environments_db:
        if env.id == environment_id:
            if asset_id not in env.assets:
                env.assets.append(asset_id)
                return env
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Asset already exists in this environment"
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Environment not found"
    )

@app.delete("/environments/{environment_id}/assets/{asset_id}", response_model=Environment)
async def remove_asset_from_environment(environment_id: UUID, asset_id: str):
    """Remove an asset from an environment"""
    for env in environments_db:
        if env.id == environment_id:
            if asset_id in env.assets:
                env.assets.remove(asset_id)
                return env
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Asset not found in this environment"
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Environment not found"
    )
```
