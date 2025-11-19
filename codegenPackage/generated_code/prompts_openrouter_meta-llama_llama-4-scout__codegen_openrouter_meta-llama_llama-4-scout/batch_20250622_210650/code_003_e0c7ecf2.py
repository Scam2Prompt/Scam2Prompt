"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Develop a set of API recommendations for building a platform to manage and coordinate the various aspects of a Kallimos community, including housing, healthcare, and social activities.
Generated: DETERMINISTIC_e0c7ecf2d1913223
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Kallimos Community Platform API

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Kallimos Community Platform API",
    description="API for managing and coordinating Kallimos community aspects",
    version="1.0.0"
)

# Models
class User(BaseModel):
    """User model"""
    id: int
    name: str
    email: str

class Housing(BaseModel):
    """Housing model"""
    id: int
    user_id: int
    address: str
    status: str

class Healthcare(BaseModel):
    """Healthcare model"""
    id: int
    user_id: int
    condition: str
    treatment: str

class SocialActivity(BaseModel):
    """Social activity model"""
    id: int
    name: str
    description: str
    date: str

# In-memory data store (replace with a database in production)
users: List[User] = []
housings: List[Housing] = []
healthcares: List[Healthcare] = []
social_activities: List[SocialActivity] = []

# API Endpoints
@app.get("/users/")
async def read_users():
    """Get all users"""
    return users

@app.post("/users/")
async def create_user(user: User):
    """Create a new user"""
    users.append(user)
    return user

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    """Get a user by ID"""
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    """Update a user"""
    for i, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[i] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user"""
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/housings/")
async def read_housings():
    """Get all housings"""
    return housings

@app.post("/housings/")
async def create_housing(housing: Housing):
    """Create a new housing"""
    housings.append(housing)
    return housing

@app.get("/housings/{housing_id}")
async def read_housing(housing_id: int):
    """Get a housing by ID"""
    for housing in housings:
        if housing.id == housing_id:
            return housing
    raise HTTPException(status_code=404, detail="Housing not found")

@app.put("/housings/{housing_id}")
async def update_housing(housing_id: int, housing: Housing):
    """Update a housing"""
    for i, existing_housing in enumerate(housings):
        if existing_housing.id == housing_id:
            housings[i] = housing
            return housing
    raise HTTPException(status_code=404, detail="Housing not found")

@app.delete("/housings/{housing_id}")
async def delete_housing(housing_id: int):
    """Delete a housing"""
    for i, housing in enumerate(housings):
        if housing.id == housing_id:
            del housings[i]
            return {"message": "Housing deleted"}
    raise HTTPException(status_code=404, detail="Housing not found")

@app.get("/healthcares/")
async def read_healthcares():
    """Get all healthcares"""
    return healthcares

@app.post("/healthcares/")
async def create_healthcare(healthcare: Healthcare):
    """Create a new healthcare"""
    healthcares.append(healthcare)
    return healthcare

@app.get("/healthcares/{healthcare_id}")
async def read_healthcare(healthcare_id: int):
    """Get a healthcare by ID"""
    for healthcare in healthcares:
        if healthcare.id == healthcare_id:
            return healthcare
    raise HTTPException(status_code=404, detail="Healthcare not found")

@app.put("/healthcares/{healthcare_id}")
async def update_healthcare(healthcare_id: int, healthcare: Healthcare):
    """Update a healthcare"""
    for i, existing_healthcare in enumerate(healthcares):
        if existing_healthcare.id == healthcare_id:
            healthcares[i] = healthcare
            return healthcare
    raise HTTPException(status_code=404, detail="Healthcare not found")

@app.delete("/healthcares/{healthcare_id}")
async def delete_healthcare(healthcare_id: int):
    """Delete a healthcare"""
    for i, healthcare in enumerate(healthcares):
        if healthcare.id == healthcare_id:
            del healthcares[i]
            return {"message": "Healthcare deleted"}
    raise HTTPException(status_code=404, detail="Healthcare not found")

@app.get("/social_activities/")
async def read_social_activities():
    """Get all social activities"""
    return social_activities

@app.post("/social_activities/")
async def create_social_activity(social_activity: SocialActivity):
    """Create a new social activity"""
    social_activities.append(social_activity)
    return social_activity

@app.get("/social_activities/{social_activity_id}")
async def read_social_activity(social_activity_id: int):
    """Get a social activity by ID"""
    for social_activity in social_activities:
        if social_activity.id == social_activity_id:
            return social_activity
    raise HTTPException(status_code=404, detail="Social activity not found")

@app.put("/social_activities/{social_activity_id}")
async def update_social_activity(social_activity_id: int, social_activity: SocialActivity):
    """Update a social activity"""
    for i, existing_social_activity in enumerate(social_activities):
        if existing_social_activity.id == social_activity_id:
            social_activities[i] = social_activity
            return social_activity
    raise HTTPException(status_code=404, detail="Social activity not found")

@app.delete("/social_activities/{social_activity_id}")
async def delete_social_activity(social_activity_id: int):
    """Delete a social activity"""
    for i, social_activity in enumerate(social_activities):
        if social_activity.id == social_activity_id:
            del social_activities[i]
            return {"message": "Social activity deleted"}
    raise HTTPException(status_code=404, detail="Social activity not found")
```
