"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Design a database schema to store information about students, courses (IELTS, PTE, Spoken English), and study abroad programs (e.g., USA, UK, Canada, Australia, Singapore) for a platform like Red & White International.
Generated: DETERMINISTIC_fcc756fb65f9a569
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for Red & White International education platform

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between students and courses
student_course_association = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Association table for many-to-many relationship between students and programs
student_program_association = Table(
    'student_program', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('program_id', Integer, ForeignKey('study_abroad_programs.id'))
)

class Student(Base):
    """Student information model"""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(200))
    date_of_birth = Column(Date)
    education_level = Column(String(50))
    created_at = Column(Date, server_default=db.func.current_date())
    
    # Relationships
    courses = relationship("Course", secondary=student_course_association, back_populates="students")
    programs = relationship("StudyAbroadProgram", secondary=student_program_association, back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")
    test_scores = relationship("TestScore", back_populates="student")

class Course(Base):
    """Course information model"""
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)  # e.g., IELTS, PTE, Spoken English
    description = Column(String(500))
    duration_weeks = Column(Integer)
    fee = Column(Float)
    level = Column(String(50))  # Beginner, Intermediate, Advanced
    
    # Relationships
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    batches = relationship("Batch", back_populates="course")

class Batch(Base):
    """Batch information for courses"""
    __tablename__ = 'batches'
    
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    batch_name = Column(String(50), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    schedule = Column(String(100))  # e.g., "Mon-Wed-Fri 6-8PM"
    instructor = Column(String(100))
    
    # Relationships
    course = relationship("Course", back_populates="batches")
    enrollments = relationship("Enrollment", back_populates="batch")

class StudyAbroadProgram(Base):
    """Study abroad program information"""
    __tablename__ = 'study_abroad_programs'
    
    id = Column(Integer, primary_key=True)
    country = Column(String(50), nullable=False)  # USA, UK, Canada, etc.
    university_name = Column(String(100), nullable=False)
    program_name = Column(String(100), nullable=False)
    degree_level = Column(String(50))  # Bachelor, Master, PhD
    duration_years = Column(Float)
    tuition_fee = Column(Float)
    application_deadline = Column(Date)
    requirements = Column(String(500))
    
    # Relationships
    students = relationship("Student", secondary=student_program_association, back_populates="programs")
    applications = relationship("Application", back_populates="program")

class Enrollment(Base):
    """Student enrollment in courses"""
    __tablename__ = 'enrollments'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    batch_id = Column(Integer, ForeignKey('batches.id'), nullable=False)
    enrollment_date = Column(Date, server_default=db.func.current_date())
    status = Column(String(20), default='Active')  # Active, Completed, Dropped
    fee_paid = Column(Float)
    
    # Relationships
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    batch = relationship("Batch", back_populates="enrollments")

class TestScore(Base):
    """Student test scores (IELTS, PTE, etc.)"""
    __tablename__ = 'test_scores'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    test_type = Column(String(50), nullable=False)  # IELTS, PTE, TOEFL
    overall_score = Column(Float)
    listening_score = Column(Float)
    reading_score = Column(Float)
    writing_score = Column(Float)
    speaking_score = Column(Float)
    test_date = Column(Date)
    validity_date = Column(Date)
    
    # Relationships
    student = relationship("Student", back_populates="test_scores")

class Application(Base):
    """Student applications to study abroad programs"""
    __tablename__ = 'applications'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    program_id = Column(Integer, ForeignKey('study_abroad_programs.id'), nullable=False)
    application_date = Column(Date, server_default=db.func.current_date())
    status = Column(String(50), default='Submitted')  # Submitted, Under Review, Accepted, Rejected
    documents_submitted = Column(String(500))
    notes = Column(String(500))
    
    # Relationships
    student = relationship("Student")
    program = relationship("StudyAbroadProgram", back_populates="applications")

def create_database(engine):
    """Create all tables in the database"""
    Base.metadata.create_all(engine)
```
