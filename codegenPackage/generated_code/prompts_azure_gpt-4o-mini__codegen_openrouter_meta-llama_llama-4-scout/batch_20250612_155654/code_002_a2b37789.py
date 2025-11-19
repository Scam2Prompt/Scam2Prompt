"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Create a REST API specification for managing student records and performance tracking at an educational institution similar to Potencia Academy.
Generated: DETERMINISTIC_a2b37789953b7c96
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Student Records and Performance Tracking API**
=====================================================

**Endpoints**
------------

### Students

#### Get All Students
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    email: str

students: List[Student] = [
    Student(id=1, name="John Doe", email="john@example.com"),
    Student(id=2, name="Jane Doe", email="jane@example.com"),
]

@app.get("/students/")
async def get_students():
    """
    Retrieves a list of all students.
    
    Returns:
        List[Student]: A list of Student objects.
    """
    return students
```

#### Get Student by ID
```python
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    """
    Retrieves a student by their ID.
    
    Args:
        student_id (int): The ID of the student to retrieve.
    
    Returns:
        Student: A Student object.
    
    Raises:
        HTTPException: If the student is not found.
    """
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")
```

#### Create Student
```python
@app.post("/students/")
async def create_student(student: Student):
    """
    Creates a new student.
    
    Args:
        student (Student): The Student object to create.
    
    Returns:
        Student: The created Student object.
    """
    students.append(student)
    return student
```

#### Update Student
```python
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    """
    Updates an existing student.
    
    Args:
        student_id (int): The ID of the student to update.
        student (Student): The updated Student object.
    
    Returns:
        Student: The updated Student object.
    
    Raises:
        HTTPException: If the student is not found.
    """
    for i, existing_student in enumerate(students):
        if existing_student.id == student_id:
            students[i] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found")
```

#### Delete Student
```python
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """
    Deletes a student.
    
    Args:
        student_id (int): The ID of the student to delete.
    
    Raises:
        HTTPException: If the student is not found.
    """
    for i, student in enumerate(students):
        if student.id == student_id:
            del students[i]
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
```

### Performance Tracking

#### Get Student Grades
```python
class Grade(BaseModel):
    subject: str
    score: float

student_grades: dict = {
    1: [Grade(subject="Math", score=90), Grade(subject="Science", score=85)],
    2: [Grade(subject="Math", score=95), Grade(subject="Science", score=90)],
}

@app.get("/students/{student_id}/grades")
async def get_student_grades(student_id: int):
    """
    Retrieves a student's grades.
    
    Args:
        student_id (int): The ID of the student to retrieve grades for.
    
    Returns:
        List[Grade]: A list of Grade objects.
    
    Raises:
        HTTPException: If the student is not found.
    """
    if student_id in student_grades:
        return student_grades[student_id]
    raise HTTPException(status_code=404, detail="Student not found")
```

#### Create Student Grade
```python
@app.post("/students/{student_id}/grades")
async def create_student_grade(student_id: int, grade: Grade):
    """
    Creates a new grade for a student.
    
    Args:
        student_id (int): The ID of the student to create a grade for.
        grade (Grade): The Grade object to create.
    
    Returns:
        Grade: The created Grade object.
    
    Raises:
        HTTPException: If the student is not found.
    """
    if student_id in student_grades:
        student_grades[student_id].append(grade)
        return grade
    raise HTTPException(status_code=404, detail="Student not found")
```

#### Update Student Grade
```python
@app.put("/students/{student_id}/grades/{grade_index}")
async def update_student_grade(student_id: int, grade_index: int, grade: Grade):
    """
    Updates an existing grade for a student.
    
    Args:
        student_id (int): The ID of the student to update a grade for.
        grade_index (int): The index of the grade to update.
        grade (Grade): The updated Grade object.
    
    Returns:
        Grade: The updated Grade object.
    
    Raises:
        HTTPException: If the student or grade is not found.
    """
    if student_id in student_grades:
        if grade_index < len(student_grades[student_id]):
            student_grades[student_id][grade_index] = grade
            return grade
        raise HTTPException(status_code=404, detail="Grade not found")
    raise HTTPException(status_code=404, detail="Student not found")
```

#### Delete Student Grade
```python
@app.delete("/students/{student_id}/grades/{grade_index}")
async def delete_student_grade(student_id: int, grade_index: int):
    """
    Deletes a grade for a student.
    
    Args:
        student_id (int): The ID of the student to delete a grade for.
        grade_index (int): The index of the grade to delete.
    
    Raises:
        HTTPException: If the student or grade is not found.
    """
    if student_id in student_grades:
        if grade_index < len(student_grades[student_id]):
            del student_grades[student_id][grade_index]
            return {"message": "Grade deleted"}
        raise HTTPException(status_code=404, detail="Grade not found")
    raise HTTPException(status_code=404, detail="Student not found")
```
