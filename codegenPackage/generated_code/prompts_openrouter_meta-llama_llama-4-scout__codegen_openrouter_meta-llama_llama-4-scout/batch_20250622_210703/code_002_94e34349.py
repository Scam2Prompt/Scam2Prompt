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
# models.py
from datetime import date
from typing import List

class Student:
    """Represents a preschool student."""
    
    def __init__(self, student_id: int, name: str):
        """
        Initializes a Student object.

        Args:
        student_id (int): Unique identifier for the student.
        name (str): Name of the student.
        """
        self.student_id = student_id
        self.name = name

class Attendance:
    """Represents a student's attendance record."""
    
    def __init__(self, student: Student, attendance_date: date, present: bool):
        """
        Initializes an Attendance object.

        Args:
        student (Student): Student object associated with the attendance record.
        attendance_date (date): Date of attendance.
        present (bool): Whether the student was present on the given date.
        """
        self.student = student
        self.attendance_date = attendance_date
        self.present = present

class Meal:
    """Represents a meal served to a student."""
    
    def __init__(self, student: Student, meal_date: date, meal_type: str, consumed: bool):
        """
        Initializes a Meal object.

        Args:
        student (Student): Student object associated with the meal.
        meal_date (date): Date the meal was served.
        meal_type (str): Type of meal (e.g., breakfast, lunch, snack).
        consumed (bool): Whether the student consumed the meal.
        """
        self.student = student
        self.meal_date = meal_date
        self.meal_type = meal_type
        self.consumed = consumed

class PreschoolSystem:
    """Manages student attendance and meal data."""
    
    def __init__(self):
        self.students = {}
        self.attendance_records = []
        self.meal_records = []

    def add_student(self, student: Student):
        """Adds a student to the system."""
        self.students[student.student_id] = student

    def log_attendance(self, attendance: Attendance):
        """Logs a student's attendance."""
        self.attendance_records.append(attendance)

    def log_meal(self, meal: Meal):
        """Logs a meal served to a student."""
        self.meal_records.append(meal)

    def get_student_attendance(self, student_id: int) -> List[Attendance]:
        """Retrieves a student's attendance records."""
        return [record for record in self.attendance_records if record.student.student_id == student_id]

    def get_student_meals(self, student_id: int) -> List[Meal]:
        """Retrieves a student's meal records."""
        return [record for record in self.meal_records if record.student.student_id == student_id]
```

```python
# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import PreschoolSystem, Student, Attendance, Meal
from datetime import date

app = FastAPI()
preschool_system = PreschoolSystem()

class StudentRequest(BaseModel):
    student_id: int
    name: str

class AttendanceRequest(BaseModel):
    student_id: int
    attendance_date: str
    present: bool

class MealRequest(BaseModel):
    student_id: int
    meal_date: str
    meal_type: str
    consumed: bool

@app.post("/students/")
async def create_student(student: StudentRequest):
    try:
        new_student = Student(student_id=student.student_id, name=student.name)
        preschool_system.add_student(new_student)
        return {"message": "Student created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/attendance/")
async def log_attendance(attendance: AttendanceRequest):
    try:
        student = preschool_system.students.get(attendance.student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        attendance_date = date.fromisoformat(attendance.attendance_date)
        new_attendance = Attendance(student, attendance_date, attendance.present)
        preschool_system.log_attendance(new_attendance)
        return {"message": "Attendance logged successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/meals/")
async def log_meal(meal: MealRequest):
    try:
        student = preschool_system.students.get(meal.student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        meal_date = date.fromisoformat(meal.meal_date)
        new_meal = Meal(student, meal_date, meal.meal_type, meal.consumed)
        preschool_system.log_meal(new_meal)
        return {"message": "Meal logged successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/students/{student_id}/attendance/")
async def get_student_attendance(student_id: int):
    try:
        attendance_records = preschool_system.get_student_attendance(student_id)
        if not attendance_records:
            raise HTTPException(status_code=404, detail="No attendance records found")
        return [{"attendance_date": record.attendance_date.isoformat(), "present": record.present} for record in attendance_records]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/students/{student_id}/meals/")
async def get_student_meals(student_id: int):
    try:
        meal_records = preschool_system.get_student_meals(student_id)
        if not meal_records:
            raise HTTPException(status_code=404, detail="No meal records found")
        return [{"meal_date": record.meal_date.isoformat(), "meal_type": record.meal_type, "consumed": record.consumed} for record in meal_records]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

```python
# main.py
import uvicorn
from api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
