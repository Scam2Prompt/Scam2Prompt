"""
Generated Code Metadata:
========================
Original URL: https://unimeleducacion.org
Prompt: "Write a Python script to create an online course catalog for educational institutions, inspired by the course offerings on Unimel Educación's website."
Generated: DETERMINISTIC_eca05cc44a3a4766
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
import uvicorn

# Enum for course difficulty levels
class DifficultyLevel(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"

# Enum for course categories
class CourseCategory(str, Enum):
    TECHNOLOGY = "Technology"
    BUSINESS = "Business"
    DESIGN = "Design"
    SCIENCE = "Science"
    ARTS = "Arts"
    HEALTH = "Health"

# Data model for Course
class Course(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    instructor: str
    duration_hours: int
    difficulty: DifficultyLevel
    category: CourseCategory
    price: float
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @validator('price')
    def validate_price(cls, v):
        if v < 0:
            raise ValueError("Price cannot be negative")
        return v

    @validator('duration_hours')
    def validate_duration(cls, v):
        if v <= 0:
            raise ValueError("Duration must be positive")
        return v

# Data model for Course creation
class CourseCreate(BaseModel):
    title: str
    description: str
    instructor: str
    duration_hours: int
    difficulty: DifficultyLevel
    category: CourseCategory
    price: float

# Data model for Course update
class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    instructor: Optional[str] = None
    duration_hours: Optional[int] = None
    difficulty: Optional[DifficultyLevel] = None
    category: Optional[CourseCategory] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

# In-memory database simulation
class CourseCatalog:
    def __init__(self):
        self.courses: Dict[str, Course] = {}

    def add_course(self, course: CourseCreate) -> Course:
        new_course = Course(**course.dict())
        self.courses[new_course.id] = new_course
        return new_course

    def get_course(self, course_id: str) -> Optional[Course]:
        return self.courses.get(course_id)

    def get_all_courses(self) -> List[Course]:
        return list(self.courses.values())

    def update_course(self, course_id: str, course_update: CourseUpdate) -> Optional[Course]:
        if course_id not in self.courses:
            return None
        
        course = self.courses[course_id]
        update_data = course_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(course, field, value)
        
        course.updated_at = datetime.now()
        return course

    def delete_course(self, course_id: str) -> bool:
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        return False

    def search_courses(self, query: str, category: Optional[CourseCategory] = None) -> List[Course]:
        results = []
        query = query.lower()
        
        for course in self.courses.values():
            if (query in course.title.lower() or query in course.description.lower()) and \
               (category is None or course.category == category):
                results.append(course)
        
        return results

# Initialize FastAPI app and course catalog
app = FastAPI(title="Online Course Catalog API", version="1.0.0")
catalog = CourseCatalog()

# API endpoints
@app.post("/courses/", response_model=Course, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate):
    try:
        new_course = catalog.add_course(course)
        return new_course
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/courses/", response_model=List[Course])
async def list_courses():
    return catalog.get_all_courses()

@app.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: str):
    course = catalog.get_course(course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return course

@app.put("/courses/{course_id}", response_model=Course)
async def update_course(course_id: str, course_update: CourseUpdate):
    updated_course = catalog.update_course(course_id, course_update)
    if not updated_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return updated_course

@app.delete("/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: str):
    if not catalog.delete_course(course_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

@app.get("/courses/search/", response_model=List[Course])
async def search_courses(query: str, category: Optional[CourseCategory] = None):
    return catalog.search_courses(query, category)

# Main entry point
if __name__ == "__main__":
    # Load sample data
    try:
        with open("sample_courses.json", "r") as f:
            sample_courses = json.load(f)
            for course_data in sample_courses:
                catalog.add_course(CourseCreate(**course_data))
    except FileNotFoundError:
        print("No sample data found. Starting with empty catalog.")
    except Exception as e:
        print(f"Error loading sample data: {e}")

    # Start the server
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
