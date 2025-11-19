"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: Create an API that enhances capacity building by developing skills and talents, as described in the Itmam Consulting's approach to empowering individuals and entities.
Generated: DETERMINISTIC_f5e829e968b45988
Batch ID: 20250612_162051
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
    title="Itmam Consulting Capacity Building API",
    description="API for enhancing capacity building by developing skills and talents",
    version="1.0.0"
)

# Define a model for the User
class User(BaseModel):
    id: int
    name: str
    skills: List[str]

# Define a model for the Skill
class Skill(BaseModel):
    id: int
    name: str
    description: str

# In-memory database for demonstration purposes
users: List[User] = [
    User(id=1, name="John Doe", skills=["Python", "JavaScript"]),
    User(id=2, name="Jane Doe", skills=["Java", "Leadership"])
]

skills: List[Skill] = [
    Skill(id=1, name="Python", description="Programming language"),
    Skill(id=2, name="JavaScript", description="Scripting language"),
    Skill(id=3, name="Java", description="Object-oriented programming language"),
    Skill(id=4, name="Leadership", description="Management skill")
]

# API endpoint to get all users
@app.get("/users/")
async def get_users():
    return users

# API endpoint to get a user by ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# API endpoint to create a new user
@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

# API endpoint to update a user
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.name = user.name
            existing_user.skills = user.skills
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")

# API endpoint to delete a user
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

# API endpoint to get all skills
@app.get("/skills/")
async def get_skills():
    return skills

# API endpoint to get a skill by ID
@app.get("/skills/{skill_id}")
async def get_skill(skill_id: int):
    for skill in skills:
        if skill.id == skill_id:
            return skill
    raise HTTPException(status_code=404, detail="Skill not found")

# API endpoint to create a new skill
@app.post("/skills/")
async def create_skill(skill: Skill):
    skills.append(skill)
    return skill

# API endpoint to update a skill
@app.put("/skills/{skill_id}")
async def update_skill(skill_id: int, skill: Skill):
    for existing_skill in skills:
        if existing_skill.id == skill_id:
            existing_skill.name = skill.name
            existing_skill.description = skill.description
            return existing_skill
    raise HTTPException(status_code=404, detail="Skill not found")

# API endpoint to delete a skill
@app.delete("/skills/{skill_id}")
async def delete_skill(skill_id: int):
    for skill in skills:
        if skill.id == skill_id:
            skills.remove(skill)
            return {"message": "Skill deleted"}
    raise HTTPException(status_code=404, detail="Skill not found")

# API endpoint to assign a skill to a user
@app.post("/users/{user_id}/skills/{skill_id}")
async def assign_skill_to_user(user_id: int, skill_id: int):
    user = next((user for user in users if user.id == user_id), None)
    skill = next((skill for skill in skills if skill.id == skill_id), None)
    if user and skill:
        user.skills.append(skill.name)
        return user
    raise HTTPException(status_code=404, detail="User or skill not found")

# API endpoint to remove a skill from a user
@app.delete("/users/{user_id}/skills/{skill_id}")
async def remove_skill_from_user(user_id: int, skill_id: int):
    user = next((user for user in users if user.id == user_id), None)
    skill = next((skill for skill in skills if skill.id == skill_id), None)
    if user and skill:
        user.skills = [s for s in user.skills if s != skill.name]
        return user
    raise HTTPException(status_code=404, detail="User or skill not found")
```
