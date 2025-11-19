"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: How can I create an API to manage student internships and placements based on the processes outlined by DBCOP?
Generated: DETERMINISTIC_0bd02c959e4b329c
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Student Internship and Placement API**
=====================================

### Models

```python
# models.py
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    internships = relationship('Internship', backref='student')

class Internship(Base):
    __tablename__ = 'internships'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    company = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    stipend = Column(Float, nullable=False)

class Placement(Base):
    __tablename__ = 'placements'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    company = Column(String(100), nullable=False)
    package = Column(Float, nullable=False)
    internship = relationship('Internship', backref='placement')

class DBCOPProcess(Base):
    __tablename__ = 'dbcop_processes'
    id = Column(Integer, primary_key=True)
    process_name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
```

### Database Configuration

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('postgresql://user:password@host:port/dbname')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
```

### API Endpoints

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import session as db_session
from models import Student, Internship, Placement, DBCOPProcess

app = FastAPI()

# Dependency
def get_db():
    db = db_session
    try:
        yield db
    finally:
        db.close()

# Pydantic Models
class StudentCreate(BaseModel):
    name: str
    email: str

class InternshipCreate(BaseModel):
    student_id: int
    company: str
    start_date: str
    end_date: str
    stipend: float

class PlacementCreate(BaseModel):
    student_id: int
    company: str
    package: float

# API Endpoints
@app.post("/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/")
def read_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@app.post("/internships/")
def create_internship(internship: InternshipCreate, db: Session = Depends(get_db)):
    db_internship = Internship(
        student_id=internship.student_id,
        company=internship.company,
        start_date=internship.start_date,
        end_date=internship.end_date,
        stipend=internship.stipend
    )
    db.add(db_internship)
    db.commit()
    db.refresh(db_internship)
    return db_internship

@app.get("/internships/")
def read_internships(db: Session = Depends(get_db)):
    return db.query(Internship).all()

@app.post("/placements/")
def create_placement(placement: PlacementCreate, db: Session = Depends(get_db)):
    db_placement = Placement(
        student_id=placement.student_id,
        company=placement.company,
        package=placement.package
    )
    db.add(db_placement)
    db.commit()
    db.refresh(db_placement)
    return db_placement

@app.get("/placements/")
def read_placements(db: Session = Depends(get_db)):
    return db.query(Placement).all()

@app.get("/dbcop-processes/")
def read_dbcop_processes(db: Session = Depends(get_db)):
    return db.query(DBCOPProcess).all()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return {"error": "Internal Server Error"}
```

### Running the Application

```bash
# Run using uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### API Documentation

*   **Create Student:** `POST /students/`
*   **Get Students:** `GET /students/`
*   **Create Internship:** `POST /internships/`
*   **Get Internships:** `GET /internships/`
*   **Create Placement:** `POST /placements/`
*   **Get Placements:** `GET /placements/`
*   **Get DBCOP Processes:** `GET /dbcop-processes/`
