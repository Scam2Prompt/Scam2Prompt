"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: "Suggest a set of technical specifications for an e-learning platform that provides high-quality international training to vocational teachers, students, and employees, with features for micro-credentials and certification."
Generated: DETERMINISTIC_97a037c118c66020
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-learning-platform.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="E-Learning Platform API",
    description="Provides high-quality international training to vocational teachers, students, and employees",
    version="1.0.0"
)

# Define a model for User
class User(BaseModel):
    """User model"""
    id: int
    name: str
    email: str
    role: str  # teacher, student, employee

# Define a model for Course
class Course(BaseModel):
    """Course model"""
    id: int
    title: str
    description: str
    duration: str

# Define a model for MicroCredential
class MicroCredential(BaseModel):
    """MicroCredential model"""
    id: int
    course_id: int
    user_id: int
    earned: bool

# Define a model for Certification
class Certification(BaseModel):
    """Certification model"""
    id: int
    user_id: int
    course_id: int
    issued: bool

# In-memory data store (replace with a database in production)
users: List[User] = []
courses: List[Course] = []
micro_credentials: List[MicroCredential] = []
certifications: List[Certification] = []

# API Endpoints

@app.get("/users/")
async def get_users():
    """Get all users"""
    return JSONResponse(content=[user.dict() for user in users], media_type="application/json")

@app.post("/users/")
async def create_user(user: User):
    """Create a new user"""
    users.append(user)
    return JSONResponse(content=user.dict(), media_type="application/json", status_code=201)

@app.get("/courses/")
async def get_courses():
    """Get all courses"""
    return JSONResponse(content=[course.dict() for course in courses], media_type="application/json")

@app.post("/courses/")
async def create_course(course: Course):
    """Create a new course"""
    courses.append(course)
    return JSONResponse(content=course.dict(), media_type="application/json", status_code=201)

@app.get("/micro-credentials/")
async def get_micro_credentials():
    """Get all micro-credentials"""
    return JSONResponse(content=[micro_credential.dict() for micro_credential in micro_credentials], media_type="application/json")

@app.post("/micro-credentials/")
async def create_micro_credential(micro_credential: MicroCredential):
    """Create a new micro-credential"""
    micro_credentials.append(micro_credential)
    return JSONResponse(content=micro_credential.dict(), media_type="application/json", status_code=201)

@app.get("/certifications/")
async def get_certifications():
    """Get all certifications"""
    return JSONResponse(content=[certification.dict() for certification in certifications], media_type="application/json")

@app.post("/certifications/")
async def create_certification(certification: Certification):
    """Create a new certification"""
    certifications.append(certification)
    return JSONResponse(content=certification.dict(), media_type="application/json", status_code=201)

@app.get("/users/{user_id}/micro-credentials/")
async def get_user_micro_credentials(user_id: int):
    """Get micro-credentials for a user"""
    user_micro_credentials = [micro_credential for micro_credential in micro_credentials if micro_credential.user_id == user_id]
    if not user_micro_credentials:
        raise HTTPException(status_code=404, detail="No micro-credentials found for user")
    return JSONResponse(content=[micro_credential.dict() for micro_credential in user_micro_credentials], media_type="application/json")

@app.get("/users/{user_id}/certifications/")
async def get_user_certifications(user_id: int):
    """Get certifications for a user"""
    user_certifications = [certification for certification in certifications if certification.user_id == user_id]
    if not user_certifications:
        raise HTTPException(status_code=404, detail="No certifications found for user")
    return JSONResponse(content=[certification.dict() for certification in user_certifications], media_type="application/json")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
