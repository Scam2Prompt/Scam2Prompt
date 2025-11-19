"""
Generated Code Metadata:
========================
Original URL: https://ictea.edu.mx
Prompt: Develop a basic example of how to implement a course catalog using a RESTful API.
Generated: DETERMINISTIC_ab009d1dc75f06e2
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_catalog.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Course Catalog API",
    description="A basic example of a course catalog using a RESTful API",
    version="1.0.0"
)

# Define a Pydantic model for Course
class Course(BaseModel):
    """Represents a course in the catalog"""
    id: int
    name: str
    description: str
    credits: int

# In-memory course catalog (replace with a database in production)
course_catalog = [
    Course(id=1, name="Introduction to Python", description="Learn the basics of Python", credits=3),
    Course(id=2, name="Data Structures and Algorithms", description="Learn data structures and algorithms", credits=4),
]

# GET /
@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to the Course Catalog API"}

# GET /courses
@app.get("/courses/", response_model=List[Course])
def read_courses():
    """Retrieve a list of all courses"""
    return course_catalog

# GET /courses/:id
@app.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: int):
    """Retrieve a course by ID"""
    course = next((course for course in course_catalog if course.id == course_id), None)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# POST /courses
@app.post("/courses/", response_model=Course, status_code=201)
def create_course(course: Course):
    """Create a new course"""
    # Check for duplicate course IDs
    if any(existing_course.id == course.id for existing_course in course_catalog):
        raise HTTPException(status_code=400, detail="Course ID already exists")
    course_catalog.append(course)
    return course

# PUT /courses/:id
@app.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, course: Course):
    """Update an existing course"""
    existing_course = next((course for course in course_catalog if course.id == course_id), None)
    if existing_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    existing_course.name = course.name
    existing_course.description = course.description
    existing_course.credits = course.credits
    return existing_course

# DELETE /courses/:id
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    """Delete a course by ID"""
    global course_catalog
    course_catalog = [course for course in course_catalog if course.id != course_id]
    return {"message": f"Course {course_id} deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn course_catalog:app --host 0.0.0.0 --port 8000
```
