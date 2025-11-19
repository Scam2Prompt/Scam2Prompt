"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Develop an API that allows users to interact with Avatars in a growing colony simulation, inspired by the "Parallel Colony" concept on the website.
Generated: DETERMINISTIC_0bdcdee47fc1a906
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Avatar API for Parallel Colony Simulation

This API provides endpoints to interact with avatars in a colony simulation.
Features include creating avatars, retrieving avatar details, updating avatar states,
and performing actions within the colony.

API follows RESTful conventions and uses JSON for data exchange.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI(
    title="Parallel Colony Avatar API",
    description="API for managing avatars in a colony simulation",
    version="1.0.0"
)

# Database simulation (in-memory for this example)
avatars_db = {}
colony_db = {
    "resources": {
        "food": 1000,
        "energy": 500,
        "materials": 750
    },
    "stats": {
        "population": 0,
        "happiness": 75,
        "productivity": 60
    }
}

class Avatar(BaseModel):
    """Represents an avatar in the colony"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    role: str
    skills: List[str]
    energy: int = Field(100, ge=0, le=100)
    health: int = Field(100, ge=0, le=100)
    happiness: int = Field(80, ge=0, le=100)
    last_active: datetime = Field(default_factory=datetime.utcnow)
    location: str = "habitat"

class AvatarCreate(BaseModel):
    """Schema for creating a new avatar"""
    name: str
    role: str
    skills: List[str]

class AvatarUpdate(BaseModel):
    """Schema for updating avatar attributes"""
    name: Optional[str] = None
    role: Optional[str] = None
    skills: Optional[List[str]] = None
    energy: Optional[int] = None
    health: Optional[int] = None
    happiness: Optional[int] = None
    location: Optional[str] = None

class ColonyStatus(BaseModel):
    """Current status of the colony"""
    resources: dict
    stats: dict

class ActionRequest(BaseModel):
    """Request for an avatar to perform an action"""
    action_type: str
    target: Optional[str] = None
    duration: int = 1

@app.get("/avatars", response_model=List[Avatar], tags=["Avatars"])
def list_avatars():
    """List all avatars in the colony"""
    return list(avatars_db.values())

@app.post("/avatars", response_model=Avatar, status_code=status.HTTP_201_CREATED, tags=["Avatars"])
def create_avatar(avatar: AvatarCreate):
    """Create a new avatar in the colony"""
    new_avatar = Avatar(**avatar.dict())
    avatars_db[new_avatar.id] = new_avatar
    colony_db["stats"]["population"] += 1
    return new_avatar

@app.get("/avatars/{avatar_id}", response_model=Avatar, tags=["Avatars"])
def get_avatar(avatar_id: str):
    """Get details for a specific avatar"""
    if avatar_id not in avatars_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avatar not found"
        )
    return avatars_db[avatar_id]

@app.put("/avatars/{avatar_id}", response_model=Avatar, tags=["Avatars"])
def update_avatar(avatar_id: str, update: AvatarUpdate):
    """Update avatar attributes"""
    if avatar_id not in avatars_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avatar not found"
        )
    
    avatar = avatars_db[avatar_id]
    update_data = update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(avatar, field, value)
    
    avatar.last_active = datetime.utcnow()
    return avatar

@app.delete("/avatars/{avatar_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Avatars"])
def delete_avatar(avatar_id: str):
    """Remove an avatar from the colony"""
    if avatar_id not in avatars_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avatar not found"
        )
    del avatars_db[avatar_id]
    colony_db["stats"]["population"] -= 1

@app.post("/avatars/{avatar_id}/actions", response_model=Avatar, tags=["Actions"])
def perform_action(avatar_id: str, action: ActionRequest):
    """Have an avatar perform an action in the colony"""
    if avatar_id not in avatars_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Avatar not found"
        )
    
    avatar = avatars_db[avatar_id]
    
    # Simulate action effects
    if action.action_type == "work":
        avatar.energy = max(0, avatar.energy - 10 * action.duration)
        colony_db["resources"]["energy"] += 5 * action.duration
        colony_db["stats"]["productivity"] = min(100, colony_db["stats"]["productivity"] + 1)
    elif action.action_type == "rest":
        avatar.energy = min(100, avatar.energy + 20 * action.duration)
        avatar.health = min(100, avatar.health + 5 * action.duration)
    elif action.action_type == "socialize":
        avatar.happiness = min(100, avatar.happiness + 15 * action.duration)
        colony_db["stats"]["happiness"] = min(100, colony_db["stats"]["happiness"] + 2)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid action type"
        )
    
    avatar.last_active = datetime.utcnow()
    return avatar

@app.get("/colony/status", response_model=ColonyStatus, tags=["Colony"])
def get_colony_status():
    """Get current status of the colony"""
    return ColonyStatus(**colony_db)

@app.post("/colony/cycle", response_model=ColonyStatus, tags=["Colony"])
def advance_colony_cycle():
    """Advance the colony simulation by one cycle"""
    # Update all avatars
    for avatar in avatars_db.values():
        avatar.energy = max(0, avatar.energy - 5)
        avatar.happiness = max(0, avatar.happiness - 2)
    
    # Update colony resources
    colony_db["resources"]["food"] = max(0, colony_db["resources"]["food"] - len(avatars_db) * 2)
    colony_db["resources"]["energy"] = max(0, colony_db["resources"]["energy"] - len(avatars_db))
    
    # Update colony stats
    total_happiness = sum(avatar.happiness for avatar in avatars_db.values())
    if avatars_db:
        colony_db["stats"]["happiness"] = total_happiness // len(avatars_db)
    
    return ColonyStatus(**colony_db)
```
