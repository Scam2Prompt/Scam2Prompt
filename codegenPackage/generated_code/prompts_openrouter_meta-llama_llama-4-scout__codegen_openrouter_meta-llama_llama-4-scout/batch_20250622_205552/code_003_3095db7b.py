"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: Design an API for managing Adventure Instances, including features like player participation, challenge completion, and reward distribution, inspired by Big Time's game mechanics.
Generated: DETERMINISTIC_3095db7bfc61cdb4
Batch ID: 20250622_205552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# adventure_instance_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

app = FastAPI()

# Data Models
class Player(BaseModel):
    """Player data model"""
    id: UUID
    name: str

class Challenge(BaseModel):
    """Challenge data model"""
    id: UUID
    name: str
    description: str

class Reward(BaseModel):
    """Reward data model"""
    id: UUID
    name: str
    description: str

class AdventureInstance(BaseModel):
    """Adventure Instance data model"""
    id: UUID
    name: str
    description: str
    challenges: List[Challenge]
    rewards: List[Reward]
    players: List[Player]

# In-Memory Data Store (Replace with a database in production)
adventure_instances = {}
players = {}
challenges = {}
rewards = {}

# API Endpoints
@app.post("/adventure-instances/")
async def create_adventure_instance(adventure_instance: AdventureInstance):
    """Create a new Adventure Instance"""
    if adventure_instance.id in adventure_instances:
        raise HTTPException(status_code=400, detail="Adventure Instance already exists")
    adventure_instances[adventure_instance.id] = adventure_instance
    return {"message": "Adventure Instance created successfully"}

@app.get("/adventure-instances/")
async def get_adventure_instances():
    """Get all Adventure Instances"""
    return list(adventure_instances.values())

@app.get("/adventure-instances/{adventure_instance_id}")
async def get_adventure_instance(adventure_instance_id: UUID):
    """Get an Adventure Instance by ID"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    return adventure_instances[adventure_instance_id]

@app.put("/adventure-instances/{adventure_instance_id}")
async def update_adventure_instance(adventure_instance_id: UUID, adventure_instance: AdventureInstance):
    """Update an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    adventure_instances[adventure_instance_id] = adventure_instance
    return {"message": "Adventure Instance updated successfully"}

@app.delete("/adventure-instances/{adventure_instance_id}")
async def delete_adventure_instance(adventure_instance_id: UUID):
    """Delete an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    del adventure_instances[adventure_instance_id]
    return {"message": "Adventure Instance deleted successfully"}

@app.post("/adventure-instances/{adventure_instance_id}/players/")
async def add_player_to_adventure_instance(adventure_instance_id: UUID, player: Player):
    """Add a player to an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    if player.id in [p.id for p in adventure_instances[adventure_instance_id].players]:
        raise HTTPException(status_code=400, detail="Player already participates in this Adventure Instance")
    adventure_instances[adventure_instance_id].players.append(player)
    return {"message": "Player added to Adventure Instance successfully"}

@app.delete("/adventure-instances/{adventure_instance_id}/players/{player_id}")
async def remove_player_from_adventure_instance(adventure_instance_id: UUID, player_id: UUID):
    """Remove a player from an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    adventure_instances[adventure_instance_id].players = [p for p in adventure_instances[adventure_instance_id].players if p.id != player_id]
    return {"message": "Player removed from Adventure Instance successfully"}

@app.post("/adventure-instances/{adventure_instance_id}/challenges/{challenge_id}/complete")
async def complete_challenge(adventure_instance_id: UUID, challenge_id: UUID):
    """Complete a challenge in an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    challenge = next((c for c in adventure_instances[adventure_instance_id].challenges if c.id == challenge_id), None)
    if challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found")
    # Distribute rewards
    reward = next((r for r in adventure_instances[adventure_instance_id].rewards), None)
    if reward:
        # Implement reward distribution logic here
        pass
    return {"message": "Challenge completed successfully"}

@app.get("/adventure-instances/{adventure_instance_id}/players/")
async def get_players_in_adventure_instance(adventure_instance_id: UUID):
    """Get players in an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    return adventure_instances[adventure_instance_id].players

@app.get("/adventure-instances/{adventure_instance_id}/challenges/")
async def get_challenges_in_adventure_instance(adventure_instance_id: UUID):
    """Get challenges in an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    return adventure_instances[adventure_instance_id].challenges

@app.get("/adventure-instances/{adventure_instance_id}/rewards/")
async def get_rewards_in_adventure_instance(adventure_instance_id: UUID):
    """Get rewards in an Adventure Instance"""
    if adventure_instance_id not in adventure_instances:
        raise HTTPException(status_code=404, detail="Adventure Instance not found")
    return adventure_instances[adventure_instance_id].rewards

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
