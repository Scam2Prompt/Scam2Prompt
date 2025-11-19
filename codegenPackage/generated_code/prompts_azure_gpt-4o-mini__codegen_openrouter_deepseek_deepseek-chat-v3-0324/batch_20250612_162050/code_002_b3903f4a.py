"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate a sample API that provides resources and exercises for DBT skills training, targeting adolescents and adults with emotional regulation issues.
Generated: DETERMINISTIC_b3903f4a197d8ae9
Batch ID: 20250612_162050
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
from uuid import uuid4, UUID

app = FastAPI(
    title="DBT Skills Training API",
    description="API providing resources and exercises for DBT skills training targeting adolescents and adults with emotional regulation issues.",
    version="1.0.0",
    contact={
        "name": "Support Team",
        "email": "support@dbtskills.org"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in production, use a real database)
db = {
    "resources": [],
    "exercises": [],
    "users": []
}

# Models
class Resource(BaseModel):
    id: UUID
    title: str
    description: str
    content: str
    target_audience: str  # "adolescents" or "adults"
    skill_category: str  # e.g., "mindfulness", "distress_tolerance", etc.

class Exercise(BaseModel):
    id: UUID
    title: str
    description: str
    steps: List[str]
    target_audience: str
    skill_category: str
    duration_minutes: int

class User(BaseModel):
    id: UUID
    username: str
    age: int
    is_professional: bool

class ResourceCreate(BaseModel):
    title: str
    description: str
    content: str
    target_audience: str
    skill_category: str

class ExerciseCreate(BaseModel):
    title: str
    description: str
    steps: List[str]
    target_audience: str
    skill_category: str
    duration_minutes: int

class UserCreate(BaseModel):
    username: str
    age: int
    is_professional: bool

# Utility functions
def find_resource(resource_id: UUID):
    for resource in db["resources"]:
        if resource["id"] == resource_id:
            return resource
    return None

def find_exercise(exercise_id: UUID):
    for exercise in db["exercises"]:
        if exercise["id"] == exercise_id:
            return exercise
    return None

def find_user(user_id: UUID):
    for user in db["users"]:
        if user["id"] == user_id:
            return user
    return None

# Endpoints
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the DBT Skills Training API"}

# Resources endpoints
@app.post("/resources/", response_model=Resource, status_code=status.HTTP_201_CREATED, tags=["Resources"])
async def create_resource(resource: ResourceCreate):
    resource_data = resource.dict()
    resource_data["id"] = uuid4()
    db["resources"].append(resource_data)
    return resource_data

@app.get("/resources/", response_model=List[Resource], tags=["Resources"])
async def get_resources(target_audience: Optional[str] = None, skill_category: Optional[str] = None):
    resources = db["resources"]
    if target_audience:
        resources = [r for r in resources if r["target_audience"] == target_audience]
    if skill_category:
        resources = [r for r in resources if r["skill_category"] == skill_category]
    return resources

@app.get("/resources/{resource_id}", response_model=Resource, tags=["Resources"])
async def get_resource(resource_id: UUID):
    resource = find_resource(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

# Exercises endpoints
@app.post("/exercises/", response_model=Exercise, status_code=status.HTTP_201_CREATED, tags=["Exercises"])
async def create_exercise(exercise: ExerciseCreate):
    exercise_data = exercise.dict()
    exercise_data["id"] = uuid4()
    db["exercises"].append(exercise_data)
    return exercise_data

@app.get("/exercises/", response_model=List[Exercise], tags=["Exercises"])
async def get_exercises(target_audience: Optional[str] = None, skill_category: Optional[str] = None):
    exercises = db["exercises"]
    if target_audience:
        exercises = [e for e in exercises if e["target_audience"] == target_audience]
    if skill_category:
        exercises = [e for e in exercises if e["skill_category"] == skill_category]
    return exercises

@app.get("/exercises/{exercise_id}", response_model=Exercise, tags=["Exercises"])
async def get_exercise(exercise_id: UUID):
    exercise = find_exercise(exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise

# User endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED, tags=["Users"])
async def create_user(user: UserCreate):
    user_data = user.dict()
    user_data["id"] = uuid4()
    db["users"].append(user_data)
    return user_data

@app.get("/users/{user_id}", response_model=User, tags=["Users"])
async def get_user(user_id: UUID):
    user = find_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Recommendation endpoints
@app.get("/recommendations/resources/", response_model=List[Resource], tags=["Recommendations"])
async def recommend_resources(user_id: UUID):
    user = find_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    target = "adolescents" if user["age"] < 18 else "adults"
    return [r for r in db["resources"] if r["target_audience"] == target]

@app.get("/recommendations/exercises/", response_model=List[Exercise], tags=["Recommendations"])
async def recommend_exercises(user_id: UUID, max_duration: Optional[int] = None):
    user = find_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    target = "adolescents" if user["age"] < 18 else "adults"
    exercises = [e for e in db["exercises"] if e["target_audience"] == target]
    
    if max_duration:
        exercises = [e for e in exercises if e["duration_minutes"] <= max_duration]
    
    return exercises
```
