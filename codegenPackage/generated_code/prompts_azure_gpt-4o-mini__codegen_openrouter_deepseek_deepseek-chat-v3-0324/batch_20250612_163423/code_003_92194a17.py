"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Create an API endpoint for a virtual training platform that allows users to enroll in courses focused on personal and organizational change, as highlighted by Virtual5.
Generated: DETERMINISTIC_92194a17179dd69d
Batch ID: 20250612_163423
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
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Virtual5 Training Platform API",
    description="API for enrolling in personal and organizational change courses",
    version="1.0.0"
)

# Database mock (in-memory for demonstration)
class CourseDB:
    def __init__(self):
        self.courses = []
        self.enrollments = []

db = CourseDB()

# Pydantic models for request/response validation
class Course(BaseModel):
    id: UUID
    title: str
    description: str
    instructor: str
    duration_hours: int
    created_at: datetime
    updated_at: datetime

class CourseCreate(BaseModel):
    title: str
    description: str
    instructor: str
    duration_hours: int

class Enrollment(BaseModel):
    id: UUID
    user_id: UUID
    course_id: UUID
    enrolled_at: datetime
    status: str = "active"

class EnrollmentCreate(BaseModel):
    user_id: UUID
    course_id: UUID

# Utility functions
def get_course_by_id(course_id: UUID) -> Optional[Course]:
    for course in db.courses:
        if course.id == course_id:
            return course
    return None

def get_user_enrollment(user_id: UUID, course_id: UUID) -> Optional[Enrollment]:
    for enrollment in db.enrollments:
        if enrollment.user_id == user_id and enrollment.course_id == course_id:
            return enrollment
    return None

# API Endpoints
@app.post("/courses/", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate):
    """Create a new course (admin functionality)"""
    course_id = uuid4()
    now = datetime.now()
    new_course = Course(
        id=course_id,
        title=course.title,
        description=course.description,
        instructor=course.instructor,
        duration_hours=course.duration_hours,
        created_at=now,
        updated_at=now
    )
    db.courses.append(new_course)
    return new_course

@app.get("/courses/", response_model=List[Course])
def list_courses():
    """List all available courses"""
    return db.courses

@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: UUID):
    """Get details for a specific course"""
    course = get_course_by_id(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return course

@app.post("/enrollments/", response_model=Enrollment, status_code=status.HTTP_201_CREATED)
def enroll_user(enrollment: EnrollmentCreate):
    """Enroll a user in a course"""
    # Verify course exists
    course = get_course_by_id(enrollment.course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    
    # Check if user is already enrolled
    existing_enrollment = get_user_enrollment(enrollment.user_id, enrollment.course_id)
    if existing_enrollment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already enrolled in this course"
        )
    
    # Create new enrollment
    enrollment_id = uuid4()
    new_enrollment = Enrollment(
        id=enrollment_id,
        user_id=enrollment.user_id,
        course_id=enrollment.course_id,
        enrolled_at=datetime.now()
    )
    db.enrollments.append(new_enrollment)
    
    return new_enrollment

@app.get("/enrollments/{user_id}", response_model=List[Enrollment])
def get_user_enrollments(user_id: UUID):
    """Get all enrollments for a specific user"""
    user_enrollments = [e for e in db.enrollments if e.user_id == user_id]
    return user_enrollments

@app.delete("/enrollments/{enrollment_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_enrollment(enrollment_id: UUID):
    """Cancel a user's enrollment"""
    for i, enrollment in enumerate(db.enrollments):
        if enrollment.id == enrollment_id:
            db.enrollments.pop(i)
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Enrollment not found"
    )

# Example startup data for demonstration
@app.on_event("startup")
async def startup_event():
    """Initialize demo data"""
    now = datetime.now()
    demo_courses = [
        Course(
            id=uuid4(),
            title="Leading Organizational Change",
            description="Strategies for driving successful organizational transformations",
            instructor="Dr. Sarah Johnson",
            duration_hours=12,
            created_at=now,
            updated_at=now
        ),
        Course(
            id=uuid4(),
            title="Personal Transformation Workshop",
            description="Tools and techniques for personal growth and change",
            instructor="Michael Chen",
            duration_hours=8,
            created_at=now,
            updated_at=now
        )
    ]
    
    db.courses.extend(demo_courses)
```
