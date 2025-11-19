"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Design a RESTful API for managing Agile course enrollments, including endpoints for subscribing to courses and tracking student progress.
Generated: DETERMINISTIC_c3c04853b759cd34
Batch ID: 20250622_210655
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
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(
    title="Agile Course Enrollment API",
    description="A RESTful API for managing Agile course enrollments",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
class Database:
    def __init__(self):
        self.courses = []
        self.enrollments = []
        self.students = []
        self.progress = []

db = Database()

# Models
class CourseLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class Course(BaseModel):
    id: UUID
    title: str
    description: str
    instructor: str
    duration_hours: int
    level: CourseLevel
    created_at: datetime
    updated_at: datetime

class CourseCreate(BaseModel):
    title: str
    description: str
    instructor: str
    duration_hours: int
    level: CourseLevel

class Student(BaseModel):
    id: UUID
    name: str
    email: str
    created_at: datetime

class StudentCreate(BaseModel):
    name: str
    email: str

class Enrollment(BaseModel):
    id: UUID
    student_id: UUID
    course_id: UUID
    enrolled_at: datetime
    completed: bool = False

class EnrollmentCreate(BaseModel):
    student_id: UUID
    course_id: UUID

class ProgressStatus(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class ProgressUpdate(BaseModel):
    status: ProgressStatus
    current_module: str
    percent_complete: float
    last_updated: datetime

class Progress(BaseModel):
    id: UUID
    enrollment_id: UUID
    status: ProgressStatus
    current_module: str
    percent_complete: float
    last_updated: datetime

class ProgressCreate(BaseModel):
    enrollment_id: UUID
    status: ProgressStatus
    current_module: str
    percent_complete: float

# Helper functions
def get_course(course_id: UUID) -> Optional[Course]:
    for course in db.courses:
        if course.id == course_id:
            return course
    return None

def get_student(student_id: UUID) -> Optional[Student]:
    for student in db.students:
        if student.id == student_id:
            return student
    return None

def get_enrollment(enrollment_id: UUID) -> Optional[Enrollment]:
    for enrollment in db.enrollments:
        if enrollment.id == enrollment_id:
            return enrollment
    return None

def get_progress_for_enrollment(enrollment_id: UUID) -> Optional[Progress]:
    for progress in db.progress:
        if progress.enrollment_id == enrollment_id:
            return progress
    return None

# Endpoints
@app.get("/courses", response_model=List[Course], tags=["Courses"])
def list_courses():
    """List all available courses."""
    return db.courses

@app.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED, tags=["Courses"])
def create_course(course: CourseCreate):
    """Create a new course."""
    new_course = Course(
        id=uuid4(),
        title=course.title,
        description=course.description,
        instructor=course.instructor,
        duration_hours=course.duration_hours,
        level=course.level,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.courses.append(new_course)
    return new_course

@app.get("/courses/{course_id}", response_model=Course, tags=["Courses"])
def get_course_by_id(course_id: UUID):
    """Get details of a specific course."""
    course = get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED, tags=["Students"])
def create_student(student: StudentCreate):
    """Register a new student."""
    new_student = Student(
        id=uuid4(),
        name=student.name,
        email=student.email,
        created_at=datetime.now()
    )
    db.students.append(new_student)
    return new_student

@app.get("/students/{student_id}", response_model=Student, tags=["Students"])
def get_student_by_id(student_id: UUID):
    """Get details of a specific student."""
    student = get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/enrollments", response_model=Enrollment, status_code=status.HTTP_201_CREATED, tags=["Enrollments"])
def create_enrollment(enrollment: EnrollmentCreate):
    """Enroll a student in a course."""
    student = get_student(enrollment.student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    course = get_course(enrollment.course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    new_enrollment = Enrollment(
        id=uuid4(),
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        enrolled_at=datetime.now()
    )
    db.enrollments.append(new_enrollment)
    return new_enrollment

@app.get("/enrollments/{enrollment_id}", response_model=Enrollment, tags=["Enrollments"])
def get_enrollment_by_id(enrollment_id: UUID):
    """Get details of a specific enrollment."""
    enrollment = get_enrollment(enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@app.post("/progress", response_model=Progress, status_code=status.HTTP_201_CREATED, tags=["Progress"])
def create_progress(progress: ProgressCreate):
    """Create or update progress for an enrollment."""
    enrollment = get_enrollment(progress.enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    
    existing_progress = get_progress_for_enrollment(progress.enrollment_id)
    
    if existing_progress:
        # Update existing progress
        existing_progress.status = progress.status
        existing_progress.current_module = progress.current_module
        existing_progress.percent_complete = progress.percent_complete
        existing_progress.last_updated = datetime.now()
        return existing_progress
    else:
        # Create new progress
        new_progress = Progress(
            id=uuid4(),
            enrollment_id=progress.enrollment_id,
            status=progress.status,
            current_module=progress.current_module,
            percent_complete=progress.percent_complete,
            last_updated=datetime.now()
        )
        db.progress.append(new_progress)
        return new_progress

@app.get("/progress/{enrollment_id}", response_model=Progress, tags=["Progress"])
def get_progress(enrollment_id: UUID):
    """Get progress for a specific enrollment."""
    progress = get_progress_for_enrollment(enrollment_id)
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress

@app.get("/students/{student_id}/enrollments", response_model=List[Enrollment], tags=["Students"])
def get_student_enrollments(student_id: UUID):
    """Get all enrollments for a specific student."""
    student = get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return [e for e in db.enrollments if e.student_id == student_id]

@app.get("/courses/{course_id}/enrollments", response_model=List[Enrollment], tags=["Courses"])
def get_course_enrollments(course_id: UUID):
    """Get all enrollments for a specific course."""
    course = get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return [e for e in db.enrollments if e.course_id == course_id]

@app.patch("/enrollments/{enrollment_id}/complete", response_model=Enrollment, tags=["Enrollments"])
def mark_enrollment_complete(enrollment_id: UUID):
    """Mark an enrollment as completed."""
    enrollment = get_enrollment(enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    
    enrollment.completed = True
    return enrollment
```
