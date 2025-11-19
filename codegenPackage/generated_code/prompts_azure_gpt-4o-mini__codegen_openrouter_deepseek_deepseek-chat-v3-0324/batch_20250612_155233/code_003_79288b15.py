"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Develop a RESTful API endpoint that lists all available aviation security courses, including the Avsec Management Course and Risk Management Course, as offered by Welwitschia Aviation.
Generated: DETERMINISTIC_79288b154b00f025
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(
    title="Welwitschia Aviation Security Courses API",
    description="API for listing available aviation security courses offered by Welwitschia Aviation",
    version="1.0.0"
)

class Course(BaseModel):
    id: int
    name: str
    description: str
    duration: str
    certification: str

# Mock database of courses
COURSES_DB = [
    {
        "id": 1,
        "name": "Avsec Management Course",
        "description": "Comprehensive training in aviation security management principles and practices.",
        "duration": "5 days",
        "certification": "ICAO compliant"
    },
    {
        "id": 2,
        "name": "Risk Management Course",
        "description": "Training in identifying, assessing, and mitigating risks in aviation security.",
        "duration": "3 days",
        "certification": "ICAO compliant"
    }
]

@app.get("/courses", response_model=List[Course], tags=["Courses"])
def list_courses():
    """
    Retrieve a list of all available aviation security courses.
    
    Returns:
        List[Course]: A list of all available courses with their details.
    """
    try:
        return COURSES_DB
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving courses: {str(e)}"
        )

@app.get("/courses/{course_id}", response_model=Course, tags=["Courses"])
def get_course(course_id: int):
    """
    Retrieve details of a specific course by ID.
    
    Args:
        course_id (int): The ID of the course to retrieve.
    
    Returns:
        Course: The course details if found.
    
    Raises:
        HTTPException: If the course is not found.
    """
    try:
        course = next((course for course in COURSES_DB if course["id"] == course_id), None)
        if not course:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )
        return course
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving the course: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
