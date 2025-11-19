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
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date
from uuid import UUID, uuid4
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///./vocational_education.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# SQLAlchemy models
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, index=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(50))
    last_name = sqlalchemy.Column(sqlalchemy.String(50))
    email = sqlalchemy.Column(sqlalchemy.String(100), unique=True, index=True)
    phone = sqlalchemy.Column(sqlalchemy.String(20))
    address = sqlalchemy.Column(sqlalchemy.String(200))
    date_of_birth = sqlalchemy.Column(sqlalchemy.Date)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, server_default=sqlalchemy.func.now())
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, onupdate=sqlalchemy.func.now())

class Course(Base):
    __tablename__ = "courses"
    
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, index=True)
    code = sqlalchemy.Column(sqlalchemy.String(20), unique=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    description = sqlalchemy.Column(sqlalchemy.Text)
    duration_weeks = sqlalchemy.Column(sqlalchemy.Integer)
    is_active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, server_default=sqlalchemy.func.now())

class Enrollment(Base):
    __tablename__ = "enrollments"
    
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, index=True)
    student_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("students.id"))
    course_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("courses.id"))
    enrollment_date = sqlalchemy.Column(sqlalchemy.Date)
    completion_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.String(20))  # e.g., "active", "completed", "withdrawn"
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, server_default=sqlalchemy.func.now())

class Certification(Base):
    __tablename__ = "certifications"
    
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, index=True)
    enrollment_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("enrollments.id"))
    certificate_number = sqlalchemy.Column(sqlalchemy.String(50), unique=True)
    issue_date = sqlalchemy.Column(sqlalchemy.Date)
    expiry_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    is_verified = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, server_default=sqlalchemy.func.now())

# Create tables
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="Vocational Education Management API",
    description="API for managing student enrollment and certification in vocational education programs",
    version="1.0.0"
)

# Pydantic models
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str
    date_of_birth: date

class StudentResponse(StudentCreate):
    id: UUID
    created_at: date

class CourseCreate(BaseModel):
    code: str
    name: str
    description: str
    duration_weeks: int
    is_active: bool = True

class CourseResponse(CourseCreate):
    id: UUID
    created_at: date

class EnrollmentCreate(BaseModel):
    student_id: UUID
    course_id: UUID
    enrollment_date: date
    status: str = "active"

class EnrollmentResponse(EnrollmentCreate):
    id: UUID
    created_at: date
    completion_date: Optional[date] = None

class CertificationCreate(BaseModel):
    enrollment_id: UUID
    certificate_number: str
    issue_date: date
    expiry_date: Optional[date] = None
    is_verified: bool = False

class CertificationResponse(CertificationCreate):
    id: UUID
    created_at: date

# Database dependency
async def get_db():
    async with database.transaction():
        yield database

# Startup and shutdown events
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# API endpoints
@app.post("/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate, db: databases.Database = Depends(get_db)):
    query = Student.__table__.insert().values(
        id=str(uuid4()),
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        phone=student.phone,
        address=student.address,
        date_of_birth=student.date_of_birth
    )
    student_id = await db.execute(query)
    return {**student.dict(), "id": student_id, "created_at": date.today()}

@app.get("/students/", response_model=List[StudentResponse])
async def get_students(db: databases.Database = Depends(get_db)):
    query = Student.__table__.select()
    return await db.fetch_all(query)

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: UUID, db: databases.Database = Depends(get_db)):
    query = Student.__table__.select().where(Student.id == str(student_id))
    student = await db.fetch_one(query)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: databases.Database = Depends(get_db)):
    query = Course.__table__.insert().values(
        id=str(uuid4()),
        code=course.code,
        name=course.name,
        description=course.description,
        duration_weeks=course.duration_weeks,
        is_active=course.is_active
    )
    course_id = await db.execute(query)
    return {**course.dict(), "id": course_id, "created_at": date.today()}

@app.get("/courses/", response_model=List[CourseResponse])
async def get_courses(db: databases.Database = Depends(get_db)):
    query = Course.__table__.select()
    return await db.fetch_all(query)

@app.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: UUID, db: databases.Database = Depends(get_db)):
    query = Course.__table__.select().where(Course.id == str(course_id))
    course = await db.fetch_one(query)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.post("/enrollments/", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
async def create_enrollment(enrollment: EnrollmentCreate, db: databases.Database = Depends(get_db)):
    # Check if student exists
    student_query = Student.__table__.select().where(Student.id == str(enrollment.student_id))
    student = await db.fetch_one(student_query)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check if course exists
    course_query = Course.__table__.select().where(Course.id == str(enrollment.course_id))
    course = await db.fetch_one(course_query)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    query = Enrollment.__table__.insert().values(
        id=str(uuid4()),
        student_id=str(enrollment.student_id),
        course_id=str(enrollment.course_id),
        enrollment_date=enrollment.enrollment_date,
        status=enrollment.status
    )
    enrollment_id = await db.execute(query)
    return {**enrollment.dict(), "id": enrollment_id, "created_at": date.today()}

@app.get("/enrollments/", response_model=List[EnrollmentResponse])
async def get_enrollments(db: databases.Database = Depends(get_db)):
    query = Enrollment.__table__.select()
    return await db.fetch_all(query)

@app.get("/enrollments/{enrollment_id
