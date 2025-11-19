"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Generate a code snippet for a web application that facilitates the creation of pocket neighborhoods, incorporating features like shared spaces and multi-generational living.
Generated: DETERMINISTIC_47e1b0df203487ec
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py
from typing import List
from pydantic import BaseModel, validator

class User(BaseModel):
    """Represents a user in the pocket neighborhood."""
    id: int
    name: str
    email: str
    age: int

class SharedSpace(BaseModel):
    """Represents a shared space in the pocket neighborhood."""
    id: int
    name: str
    description: str
    capacity: int

class PocketNeighborhood(BaseModel):
    """Represents a pocket neighborhood."""
    id: int
    name: str
    description: str
    users: List[User]
    shared_spaces: List[SharedSpace]

    @validator('users')
    def users_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Users must not be empty')
        return v

    @validator('shared_spaces')
    def shared_spaces_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Shared spaces must not be empty')
        return v

# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import User, SharedSpace, PocketNeighborhood

app = FastAPI()

# In-memory data store for demonstration purposes
pocket_neighborhoods = []
users = []
shared_spaces = []

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.post("/shared-spaces/")
async def create_shared_space(shared_space: SharedSpace):
    shared_spaces.append(shared_space)
    return shared_space

@app.post("/pocket-neighborhoods/")
async def create_pocket_neighborhood(pocket_neighborhood: PocketNeighborhood):
    pocket_neighborhoods.append(pocket_neighborhood)
    return pocket_neighborhood

@app.get("/pocket-neighborhoods/")
async def get_pocket_neighborhoods():
    return pocket_neighborhoods

@app.get("/pocket-neighborhoods/{pocket_neighborhood_id}")
async def get_pocket_neighborhood(pocket_neighborhood_id: int):
    for pocket_neighborhood in pocket_neighborhoods:
        if pocket_neighborhood.id == pocket_neighborhood_id:
            return pocket_neighborhood
    raise HTTPException(status_code=404, detail="Pocket neighborhood not found")

@app.put("/pocket-neighborhoods/{pocket_neighborhood_id}")
async def update_pocket_neighborhood(pocket_neighborhood_id: int, pocket_neighborhood: PocketNeighborhood):
    for i, existing_pocket_neighborhood in enumerate(pocket_neighborhoods):
        if existing_pocket_neighborhood.id == pocket_neighborhood_id:
            pocket_neighborhoods[i] = pocket_neighborhood
            return pocket_neighborhood
    raise HTTPException(status_code=404, detail="Pocket neighborhood not found")

@app.delete("/pocket-neighborhoods/{pocket_neighborhood_id}")
async def delete_pocket_neighborhood(pocket_neighborhood_id: int):
    for i, pocket_neighborhood in enumerate(pocket_neighborhoods):
        if pocket_neighborhood.id == pocket_neighborhood_id:
            del pocket_neighborhoods[i]
            return {"message": "Pocket neighborhood deleted"}
    raise HTTPException(status_code=404, detail="Pocket neighborhood not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```sql
-- schema.sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INTEGER NOT NULL
);

CREATE TABLE shared_spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    capacity INTEGER NOT NULL
);

CREATE TABLE pocket_neighborhoods (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE pocket_neighborhood_users (
    pocket_neighborhood_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (pocket_neighborhood_id, user_id),
    FOREIGN KEY (pocket_neighborhood_id) REFERENCES pocket_neighborhoods(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE pocket_neighborhood_shared_spaces (
    pocket_neighborhood_id INTEGER NOT NULL,
    shared_space_id INTEGER NOT NULL,
    PRIMARY KEY (pocket_neighborhood_id, shared_space_id),
    FOREIGN KEY (pocket_neighborhood_id) REFERENCES pocket_neighborhoods(id),
    FOREIGN KEY (shared_space_id) REFERENCES shared_spaces(id)
);
```
