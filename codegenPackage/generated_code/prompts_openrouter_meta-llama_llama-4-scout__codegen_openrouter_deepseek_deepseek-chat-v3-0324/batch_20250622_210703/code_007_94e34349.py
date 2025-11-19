"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Design a simple system to track student attendance and daily meals for a preschool, including a basic data model and potential API endpoints.
Generated: DETERMINISTIC_94e3434992e909fe
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# attendance_meal_tracker.py
from datetime import date
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="Preschool Attendance and Meal Tracker")

# Data Models
class Student(BaseModel):
    id: int
    name: str
    age: int
    classroom: str

class Attendance(BaseModel):
    id: int
    student_id: int
    date: date
    present: bool
    check_in_time: Optional[str] = None
    check_out_time: Optional[str] = None

class Meal(BaseModel):
    id: int
    student_id: int
    date: date
    meal_type: str  # e.g., "breakfast", "lunch", "snack"
    items_consumed: List[str]

# In-memory database (replace with actual database in production)
students_db = {}
attendance_db = {}
meals_db = {}

# Helper functions
def get_next_id(collection):
    return max(collection.keys(), default=0) + 1

# API Endpoints
@app.post("/students/", status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    if student.id in students_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student ID already exists"
        )
    students_db[student.id] = student
    return {"message": "Student created successfully"}

@app.get("/students/", response_model=List[Student])
async def list_students():
    return list(students_db.values())

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return students_db[student_id]

@app.post("/attendance/", status_code=status.HTTP_201_CREATED)
async def record_attendance(attendance: Attendance):
    if attendance.student_id not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    attendance.id = get_next_id(attendance_db)
    attendance_db[attendance.id] = attendance
    return {"message": "Attendance recorded successfully"}

@app.get("/attendance/{student_id}", response_model=List[Attendance])
async def get_student_attendance(student_id: int):
    if student_id not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return [att for att in attendance_db.values() if att.student_id == student_id]

@app.post("/meals/", status_code=status.HTTP_201_CREATED)
async def record_meal(meal: Meal):
    if meal.student_id not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    meal.id = get_next_id(meals_db)
    meals_db[meal.id] = meal
    return {"message": "Meal recorded successfully"}

@app.get("/meals/{student_id}", response_model=List[Meal])
async def get_student_meals(student_id: int):
    if student_id not in students_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return [meal for meal in meals_db.values() if meal.student_id == student_id]

@app.get("/daily-report/{report_date}", response_model=dict)
async def get_daily_report(report_date: date):
    attendance = [
        att for att in attendance_db.values() 
        if att.date == report_date
    ]
    meals = [
        meal for meal in meals_db.values()
        if meal.date == report_date
    ]
    
    return {
        "date": report_date,
        "total_students": len(students_db),
        "present_count": sum(1 for att in attendance if att.present),
        "absent_count": sum(1 for att in attendance if not att.present),
        "meals_served": len(meals),
        "attendance_records": attendance,
        "meal_records": meals
    }
```
