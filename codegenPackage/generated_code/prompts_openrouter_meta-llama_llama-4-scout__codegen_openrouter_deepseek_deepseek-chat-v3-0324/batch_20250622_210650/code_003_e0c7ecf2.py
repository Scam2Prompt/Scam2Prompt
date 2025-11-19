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
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from uuid import uuid4

app = FastAPI(
    title="Kallimos Community Platform API",
    description="API for managing Kallimos community resources including housing, healthcare, and social activities",
    version="1.0.0"
)

# Database models (would typically be ORM models in production)
class User(BaseModel):
    id: str
    name: str
    email: str
    role: str  # resident, staff, admin
    join_date: datetime
    is_active: bool

class HousingUnit(BaseModel):
    id: str
    name: str
    type: str  # apartment, shared, etc.
    capacity: int
    current_occupants: List[str]  # user IDs
    amenities: List[str]

class HealthcareRecord(BaseModel):
    id: str
    user_id: str
    provider_id: str
    date: datetime
    notes: str
    medications: List[str]
    is_emergency: bool

class SocialActivity(BaseModel):
    id: str
    name: str
    description: str
    date: datetime
    location: str
    organizer_id: str
    attendees: List[str]  # user IDs
    max_participants: Optional[int]

# In-memory "database" for demo purposes
db = {
    "users": [],
    "housing": [],
    "healthcare": [],
    "activities": []
}

# Dependency to get current active user
async def get_current_user(token: str):
    # In production, this would validate JWT or session token
    user = next((u for u in db["users"] if u.id == token), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return user

# User Management Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    user.id = str(uuid4())
    user.join_date = datetime.now()
    user.is_active = True
    db["users"].append(user)
    return user

@app.get("/users/", response_model=List[User])
async def list_users():
    return db["users"]

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = next((u for u in db["users"] if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Housing Management Endpoints
@app.post("/housing/", response_model=HousingUnit, status_code=status.HTTP_201_CREATED)
async def create_housing_unit(unit: HousingUnit, current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can create housing units")
    unit.id = str(uuid4())
    db["housing"].append(unit)
    return unit

@app.get("/housing/", response_model=List[HousingUnit])
async def list_housing_units():
    return db["housing"]

@app.post("/housing/{unit_id}/assign/{user_id}", response_model=HousingUnit)
async def assign_to_housing(
    unit_id: str, 
    user_id: str,
    current_user: User = Depends(get_current_user)
):
    unit = next((u for u in db["housing"] if u.id == unit_id), None)
    if not unit:
        raise HTTPException(status_code=404, detail="Housing unit not found")
    
    user = next((u for u in db["users"] if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_id in unit.current_occupants:
        raise HTTPException(status_code=400, detail="User already assigned to this unit")
    
    unit.current_occupants.append(user_id)
    return unit

# Healthcare Endpoints
@app.post("/healthcare/", response_model=HealthcareRecord, status_code=status.HTTP_201_CREATED)
async def create_healthcare_record(
    record: HealthcareRecord,
    current_user: User = Depends(get_current_user)
):
    record.id = str(uuid4())
    record.date = datetime.now()
    
    # Validate user exists
    user = next((u for u in db["users"] if u.id == record.user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db["healthcare"].append(record)
    return record

@app.get("/healthcare/user/{user_id}", response_model=List[HealthcareRecord])
async def get_user_healthcare_records(user_id: str):
    return [r for r in db["healthcare"] if r.user_id == user_id]

# Social Activities Endpoints
@app.post("/activities/", response_model=SocialActivity, status_code=status.HTTP_201_CREATED)
async def create_activity(
    activity: SocialActivity,
    current_user: User = Depends(get_current_user)
):
    activity.id = str(uuid4())
    activity.organizer_id = current_user.id
    activity.attendees = []
    db["activities"].append(activity)
    return activity

@app.post("/activities/{activity_id}/register/{user_id}", response_model=SocialActivity)
async def register_for_activity(
    activity_id: str,
    user_id: str,
    current_user: User = Depends(get_current_user)
):
    activity = next((a for a in db["activities"] if a.id == activity_id), None)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    user = next((u for u in db["users"] if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_id in activity.attendees:
        raise HTTPException(status_code=400, detail="User already registered")
    
    if activity.max_participants and len(activity.attendees) >= activity.max_participants:
        raise HTTPException(status_code=400, detail="Activity is full")
    
    activity.attendees.append(user_id)
    return activity

@app.get("/activities/", response_model=List[SocialActivity])
async def list_activities():
    return db["activities"]
```
