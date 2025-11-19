"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Develop a Python API to retrieve and display the promotion list of students for a school like Param Gyan Niketan, following the CBSE and State Government guidelines.
Generated: DETERMINISTIC_c42baf601e2e4f49
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Student Promotion API",
    description="API to retrieve and display promotion list of students following CBSE and State Government guidelines",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database simulation
class Student(BaseModel):
    id: int
    name: str
    roll_number: str
    class_name: str = Field(..., alias="class")
    section: str
    academic_year: str
    marks: dict
    attendance_percentage: float
    promotion_status: Optional[str] = None

    @validator('attendance_percentage')
    def validate_attendance(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Attendance percentage must be between 0 and 100")
        return v

# In-memory database
students_db = []

def load_sample_data():
    """Load sample student data"""
    global students_db
    try:
        with open('sample_students.json', 'r') as f:
            students_db = json.load(f)
        logger.info("Sample data loaded successfully")
    except FileNotFoundError:
        logger.warning("Sample data file not found, starting with empty database")
        students_db = []

# Promotion criteria
class PromotionCriteria(BaseModel):
    min_attendance: float = 75.0
    min_marks: dict
    cbse_guidelines: bool = True
    state_guidelines: bool = True

# Load sample data on startup
load_sample_data()

def check_promotion(student: Student, criteria: PromotionCriteria) -> str:
    """Check if student meets promotion criteria"""
    # Check attendance
    if student.attendance_percentage < criteria.min_attendance:
        return "Not Promoted (Attendance)"

    # Check marks based on CBSE guidelines
    if criteria.cbse_guidelines:
        for subject, min_mark in criteria.min_marks.items():
            if student.marks.get(subject, 0) < min_mark:
                return f"Not Promoted ({subject} marks)"

    # Additional state-specific checks can be added here
    if criteria.state_guidelines:
        pass  # Placeholder for state-specific checks

    return "Promoted"

@app.get("/students/", response_model=List[Student])
async def get_all_students():
    """Get all students"""
    return students_db

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    """Get student by ID"""
    student = next((s for s in students_db if s["id"] == student_id), None)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/promotion-list/", response_model=List[Student])
async def get_promotion_list(
    class_name: Optional[str] = Query(None, description="Filter by class"),
    section: Optional[str] = Query(None, description="Filter by section"),
    academic_year: Optional[str] = Query(None, description="Filter by academic year")
):
    """Get promotion list with filters"""
    filtered_students = students_db
    
    if class_name:
        filtered_students = [s for s in filtered_students if s["class"] == class_name]
    if section:
        filtered_students = [s for s in filtered_students if s["section"] == section]
    if academic_year:
        filtered_students = [s for s in filtered_students if s["academic_year"] == academic_year]

    # Default promotion criteria (can be customized)
    criteria = PromotionCriteria(
        min_attendance=75.0,
        min_marks={"Math": 33, "Science": 33, "English": 33, "Social Studies": 33}
    )

    # Evaluate promotion status for each student
    for student in filtered_students:
        student["promotion_status"] = check_promotion(Student(**student), criteria)

    return filtered_students

@app.post("/students/", response_model=Student, status_code=201)
async def add_student(student: Student):
    """Add a new student"""
    if any(s["id"] == student.id for s in students_db):
        raise HTTPException(status_code=400, detail="Student ID already exists")
    
    student_dict = student.dict(by_alias=True)
    students_db.append(student_dict)
    logger.info(f"Added new student: {student.name} (ID: {student.id})")
    return student_dict

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student: Student):
    """Update student information"""
    index = next((i for i, s in enumerate(students_db) if s["id"] == student_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    if student_id != student.id:
        raise HTTPException(status_code=400, detail="Student ID cannot be changed")
    
    student_dict = student.dict(by_alias=True)
    students_db[index] = student_dict
    logger.info(f"Updated student: {student.name} (ID: {student.id})")
    return student_dict

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "student_count": len(students_db)
    }
```
