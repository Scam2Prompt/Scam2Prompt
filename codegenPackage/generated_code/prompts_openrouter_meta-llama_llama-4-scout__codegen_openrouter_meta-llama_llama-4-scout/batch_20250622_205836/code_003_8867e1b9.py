"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Design an API for managing Adventure Instances, including creating, joining, and completing instances, in the Big Time game.
Generated: DETERMINISTIC_8867e1b960b8f4cd
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# adventure_instance_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4

app = FastAPI(
    title="Adventure Instance API",
    description="API for managing Adventure Instances in Big Time game",
    version="1.0.0"
)

# Data Store for Adventure Instances
adventure_instances = {}

class Player(BaseModel):
    """Player data model"""
    id: UUID
    name: str

class AdventureInstance(BaseModel):
    """Adventure Instance data model"""
    id: UUID
    name: str
    players: List[Player]
    completed: bool = False

class CreateAdventureInstanceRequest(BaseModel):
    """Request data model for creating an Adventure Instance"""
    name: str

class JoinAdventureInstanceRequest(BaseModel):
    """Request data model for joining an Adventure Instance"""
    instance_id: UUID
    player: Player

class CompleteAdventureInstanceRequest(BaseModel):
    """Request data model for completing an Adventure Instance"""
    instance_id: UUID

# API Endpoints

@app.post("/adventure-instances", response_model=AdventureInstance)
async def create_adventure_instance(request: CreateAdventureInstanceRequest):
    """Create a new Adventure Instance"""
    instance_id = uuid4()
    instance = AdventureInstance(
        id=instance_id,
        name=request.name,
        players=[]
    )
    adventure_instances[instance_id] = instance
    return instance

@app.get("/adventure-instances", response_model=List[AdventureInstance])
async def get_adventure_instances():
    """Get all Adventure Instances"""
    return list(adventure_instances.values())

@app.get("/adventure-instances/{instance_id}", response_model=AdventureInstance)
async def get_adventure_instance(instance_id: UUID):
    """Get an Adventure Instance by ID"""
    instance = adventure_instances.get(instance_id)
    if instance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instance not found")
    return instance

@app.post("/adventure-instances/{instance_id}/join", response_model=AdventureInstance)
async def join_adventure_instance(instance_id: UUID, request: JoinAdventureInstanceRequest):
    """Join an Adventure Instance"""
    instance = adventure_instances.get(instance_id)
    if instance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instance not found")
    if request.player in instance.players:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Player already joined")
    instance.players.append(request.player)
    adventure_instances[instance_id] = instance
    return instance

@app.post("/adventure-instances/{instance_id}/complete", response_model=AdventureInstance)
async def complete_adventure_instance(instance_id: UUID, request: CompleteAdventureInstanceRequest):
    """Complete an Adventure Instance"""
    instance = adventure_instances.get(instance_id)
    if instance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Instance not found")
    if instance.completed:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Instance already completed")
    instance.completed = True
    adventure_instances[instance_id] = instance
    return instance

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP Exceptions"""
    return exc

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    """Handle generic Exceptions"""
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
