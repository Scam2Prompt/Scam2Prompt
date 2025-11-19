"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: Generate a REST API specification for a personal development program that includes features like self-assessment and virtual mentoring, inspired by the services of Nesha Group.
Generated: DETERMINISTIC_ee212ce84519bd6b
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

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Personal Development Program API",
    description="A REST API for a personal development program featuring self-assessment and virtual mentoring",
    version="1.0.0",
)

# Models
class User(BaseModel):
    id: int
    name: str
    email: str

class Assessment(BaseModel):
    id: int
    user_id: int
    score: float
    created_at: datetime

class Mentor(BaseModel):
    id: int
    name: str
    expertise: str

class Mentorship(BaseModel):
    id: int
    mentor_id: int
    user_id: int
    start_date: datetime
    end_date: datetime

# In-memory data store (replace with a database in production)
users: List[User] = [
    User(id=1, name="John Doe", email="john@example.com"),
    User(id=2, name="Jane Doe", email="jane@example.com"),
]

assessments: List[Assessment] = [
    Assessment(id=1, user_id=1, score=80.0, created_at=datetime(2022, 1, 1)),
    Assessment(id=2, user_id=2, score=90.0, created_at=datetime(2022, 1, 15)),
]

mentors: List[Mentor] = [
    Mentor(id=1, name="Mentor 1", expertise="Leadership"),
    Mentor(id=2, name="Mentor 2", expertise="Communication"),
]

mentorships: List[Mentorship] = [
    Mentorship(id=1, mentor_id=1, user_id=1, start_date=datetime(2022, 2, 1), end_date=datetime(2022, 12, 31)),
    Mentorship(id=2, mentor_id=2, user_id=2, start_date=datetime(2022, 3, 1), end_date=datetime(2023, 2, 28)),
]

# API Endpoints
@app.get("/users/")
async def read_users():
    return users

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/assessments/")
async def create_assessment(assessment: Assessment):
    assessments.append(assessment)
    return assessment

@app.get("/assessments/")
async def read_assessments():
    return assessments

@app.get("/mentors/")
async def read_mentors():
    return mentors

@app.get("/mentors/{mentor_id}")
async def read_mentor(mentor_id: int):
    mentor = next((mentor for mentor in mentors if mentor.id == mentor_id), None)
    if mentor is None:
        raise HTTPException(status_code=404, detail="Mentor not found")
    return mentor

@app.post("/mentorships/")
async def create_mentorship(mentorship: Mentorship):
    mentorships.append(mentorship)
    return mentorship

@app.get("/mentorships/")
async def read_mentorships():
    return mentorships

@app.get("/users/{user_id}/assessments/")
async def read_user_assessments(user_id: int):
    user_assessments = [assessment for assessment in assessments if assessment.user_id == user_id]
    return user_assessments

@app.get("/users/{user_id}/mentorships/")
async def read_user_mentorships(user_id: int):
    user_mentorships = [mentorship for mentorship in mentorships if mentorship.user_id == user_id]
    return user_mentorships
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
