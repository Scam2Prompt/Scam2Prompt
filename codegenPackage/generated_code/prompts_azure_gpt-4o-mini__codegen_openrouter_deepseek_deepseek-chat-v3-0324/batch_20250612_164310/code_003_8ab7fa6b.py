"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Develop a REST API endpoint that allows users to fetch details about the "Diplomado de Auditoria Gubernamental" course from AulaContable.
Generated: DETERMINISTIC_8ab7fa6b9f65683f
Batch ID: 20250612_164310
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
from typing import Optional
import httpx

app = FastAPI(
    title="AulaContable Course API",
    description="API to fetch details about 'Diplomado de Auditoria Gubernamental' course",
    version="1.0.0"
)


class CourseDetails(BaseModel):
    title: str
    description: str
    duration: str
    price: float
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    instructor: Optional[str] = None
    syllabus: Optional[list[str]] = None


# Mock data - in a real application, this would be fetched from a database or external API
COURSE_DATA = {
    "diplomado-auditoria-gubernamental": {
        "title": "Diplomado de Auditoria Gubernamental",
        "description": "Programa especializado en auditoría para el sector público.",
        "duration": "6 meses",
        "price": 1200.00,
        "start_date": "2023-10-15",
        "end_date": "2024-04-15",
        "instructor": "Lic. Juan Pérez",
        "syllabus": [
            "Introducción a la auditoría gubernamental",
            "Normativas y regulaciones",
            "Procedimientos de auditoría",
            "Informes y documentación",
            "Casos prácticos"
        ]
    }
}


@app.get(
    "/courses/diplomado-auditoria-gubernamental",
    response_model=CourseDetails,
    summary="Get Diplomado de Auditoria Gubernamental details",
    tags=["Courses"]
)
async def get_course_details():
    """
    Fetch detailed information about the 'Diplomado de Auditoria Gubernamental' course.

    Returns:
        CourseDetails: An object containing all course details including:
            - title
            - description
            - duration
            - price
            - start_date (optional)
            - end_date (optional)
            - instructor (optional)
            - syllabus (optional)
    """
    try:
        course = COURSE_DATA.get("diplomado-auditoria-gubernamental")
        if not course:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )
        return course
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching course details: {str(e)}"
        )


@app.get("/health", include_in_schema=False)
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"}


# For production, you would typically add:
# - Proper logging
# - Authentication/Authorization
# - Rate limiting
# - Caching
# - Database integration
# - Environment configuration
```
