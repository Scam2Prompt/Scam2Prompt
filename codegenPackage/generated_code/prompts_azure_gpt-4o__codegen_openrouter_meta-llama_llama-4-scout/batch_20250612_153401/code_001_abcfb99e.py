"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate an API recommendation for managing student enrollment and certification in vocational education programs, specifically tailored for courses like the Graduate Diploma of Management (Learning): BSB80120 offered by Global Healthcare Management College.
Generated: DETERMINISTIC_abcfb99e37c5d38e
Batch ID: 20250612_153401
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///vocational_education.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the database models
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String, unique=True)

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    is_certified = Column(Boolean, default=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic models for API request and response validation
class StudentCreate(BaseModel):
    name: str
    email: str

class CourseCreate(BaseModel):
    name: str
    code: str

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

class CourseResponse(BaseModel):
    id: int
    name: str
    code: str

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    is_certified: bool

# FastAPI Application
app = FastAPI()

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints
@app.post("/students/")
def create_student(student: StudentCreate, db: SessionLocal = Depends(get_db)):
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return StudentResponse(id=new_student.id, name=new_student.name, email=new_student.email)

@app.get("/students/")
def read_students(db: SessionLocal = Depends(get_db)):
    students = db.query(Student).all()
    return [StudentResponse(id=s.id, name=s.name, email=s.email) for s in students]

@app.post("/courses/")
def create_course(course: CourseCreate, db: SessionLocal = Depends(get_db)):
    new_course = Course(name=course.name, code=course.code)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return CourseResponse(id=new_course.id, name=new_course.name, code=new_course.code)

@app.get("/courses/")
def read_courses(db: SessionLocal = Depends(get_db)):
    courses = db.query(Course).all()
    return [CourseResponse(id=c.id, name=c.name, code=c.code) for c in courses]

@app.post("/enrollments/")
def create_enrollment(enrollment: EnrollmentCreate, db: SessionLocal = Depends(get_db)):
    new_enrollment = Enrollment(student_id=enrollment.student_id, course_id=enrollment.course_id)
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return EnrollmentResponse(id=new_enrollment.id, student_id=new_enrollment.student_id, course_id=new_enrollment.course_id, is_certified=new_enrollment.is_certified)

@app.get("/enrollments/")
def read_enrollments(db: SessionLocal = Depends(get_db)):
    enrollments = db.query(Enrollment).all()
    return [EnrollmentResponse(id=e.id, student_id=e.student_id, course_id=e.course_id, is_certified=e.is_certified) for e in enrollments]

@app.put("/enrollments/{enrollment_id}/certify")
def certify_enrollment(enrollment_id: int, db: SessionLocal = Depends(get_db)):
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    enrollment.is_certified = True
    db.commit()
    db.refresh(enrollment)
    return EnrollmentResponse(id=enrollment.id, student_id=enrollment.student_id, course_id=enrollment.course_id, is_certified=enrollment.is_certified)

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
