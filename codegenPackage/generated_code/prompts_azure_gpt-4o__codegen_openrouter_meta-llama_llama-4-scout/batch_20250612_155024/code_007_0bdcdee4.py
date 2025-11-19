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
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Colony Simulation API",
    description="API for interacting with avatars in a colony simulation",
    version="1.0.0"
)

class Avatar(BaseModel):
    """Avatar model"""
    id: int
    name: str
    age: int
    hunger: int
    health: int

class Colony(BaseModel):
    """Colony model"""
    id: int
    name: str
    avatars: List[Avatar]

# In-memory data store for demonstration purposes
avatars: List[Avatar] = [
    Avatar(id=1, name="Avatar 1", age=20, hunger=50, health=100),
    Avatar(id=2, name="Avatar 2", age=30, hunger=70, health=80)
]

colonies: List[Colony] = [
    Colony(id=1, name="Colony 1", avatars=[avatars[0]]),
    Colony(id=2, name="Colony 2", avatars=[avatars[1]])
]

@app.get("/avatars/")
async def get_all_avatars():
    """Get all avatars"""
    return avatars

@app.get("/avatars/{avatar_id}")
async def get_avatar(avatar_id: int):
    """Get avatar by ID"""
    for avatar in avatars:
        if avatar.id == avatar_id:
            return avatar
    raise HTTPException(status_code=404, detail="Avatar not found")

@app.post("/avatars/")
async def create_avatar(avatar: Avatar):
    """Create a new avatar"""
    avatars.append(avatar)
    return avatar

@app.put("/avatars/{avatar_id}")
async def update_avatar(avatar_id: int, avatar: Avatar):
    """Update an existing avatar"""
    for existing_avatar in avatars:
        if existing_avatar.id == avatar_id:
            existing_avatar.name = avatar.name
            existing_avatar.age = avatar.age
            existing_avatar.hunger = avatar.hunger
            existing_avatar.health = avatar.health
            return existing_avatar
    raise HTTPException(status_code=404, detail="Avatar not found")

@app.delete("/avatars/{avatar_id}")
async def delete_avatar(avatar_id: int):
    """Delete an avatar"""
    for avatar in avatars:
        if avatar.id == avatar_id:
            avatars.remove(avatar)
            return {"message": f"Avatar {avatar_id} deleted"}
    raise HTTPException(status_code=404, detail="Avatar not found")

@app.get("/colonies/")
async def get_all_colonies():
    """Get all colonies"""
    return colonies

@app.get("/colonies/{colony_id}")
async def get_colony(colony_id: int):
    """Get colony by ID"""
    for colony in colonies:
        if colony.id == colony_id:
            return colony
    raise HTTPException(status_code=404, detail="Colony not found")

@app.post("/colonies/")
async def create_colony(colony: Colony):
    """Create a new colony"""
    colonies.append(colony)
    return colony

@app.put("/colonies/{colony_id}")
async def update_colony(colony_id: int, colony: Colony):
    """Update an existing colony"""
    for existing_colony in colonies:
        if existing_colony.id == colony_id:
            existing_colony.name = colony.name
            existing_colony.avatars = colony.avatars
            return existing_colony
    raise HTTPException(status_code=404, detail="Colony not found")

@app.delete("/colonies/{colony_id}")
async def delete_colony(colony_id: int):
    """Delete a colony"""
    for colony in colonies:
        if colony.id == colony_id:
            colonies.remove(colony)
            return {"message": f"Colony {colony_id} deleted"}
    raise HTTPException(status_code=404, detail="Colony not found")

@app.post("/avatars/{avatar_id}/feed")
async def feed_avatar(avatar_id: int):
    """Feed an avatar"""
    for avatar in avatars:
        if avatar.id == avatar_id:
            avatar.hunger -= 10
            if avatar.hunger < 0:
                avatar.hunger = 0
            return avatar
    raise HTTPException(status_code=404, detail="Avatar not found")

@app.post("/avatars/{avatar_id}/heal")
async def heal_avatar(avatar_id: int):
    """Heal an avatar"""
    for avatar in avatars:
        if avatar.id == avatar_id:
            avatar.health += 10
            if avatar.health > 100:
                avatar.health = 100
            return avatar
    raise HTTPException(status_code=404, detail="Avatar not found")
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
