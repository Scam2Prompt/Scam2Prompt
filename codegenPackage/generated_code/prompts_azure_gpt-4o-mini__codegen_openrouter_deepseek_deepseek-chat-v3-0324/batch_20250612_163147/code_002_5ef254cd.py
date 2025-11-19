"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Create an API that provides information about the different occupational medical exams available at Medicid IPS, including details on exams for high-altitude work and confined spaces.
Generated: DETERMINISTIC_5ef254cdc9b6acad
Batch ID: 20250612_163147
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
from typing import List, Optional

app = FastAPI(
    title="Medicid IPS Occupational Medical Exams API",
    description="API providing information about occupational medical exams available at Medicid IPS",
    version="1.0.0"
)

class Exam(BaseModel):
    id: int
    name: str
    description: str
    duration_minutes: int
    special_requirements: Optional[str] = None
    recommended_for: List[str]

# In-memory database of exams
EXAMS_DATABASE = [
    {
        "id": 1,
        "name": "High-Altitude Work Exam",
        "description": "Comprehensive medical evaluation for workers in high-altitude environments",
        "duration_minutes": 90,
        "special_requirements": "Must be performed at least 24 hours after arriving at altitude",
        "recommended_for": ["Mountain guides", "Mining workers", "Telecommunication tower workers"]
    },
    {
        "id": 2,
        "name": "Confined Spaces Exam",
        "description": "Medical assessment for workers who operate in confined spaces",
        "duration_minutes": 60,
        "special_requirements": "Claustrophobia screening included",
        "recommended_for": ["Construction workers", "Tunnel workers", "Sewage system workers"]
    },
    {
        "id": 3,
        "name": "General Occupational Health Exam",
        "description": "Standard medical examination for all types of workers",
        "duration_minutes": 45,
        "recommended_for": ["All workers"]
    }
]

@app.get("/exams", response_model=List[Exam], summary="Get all available exams")
async def get_all_exams():
    """
    Retrieve a list of all occupational medical exams available at Medicid IPS.
    """
    return EXAMS_DATABASE

@app.get("/exams/{exam_id}", response_model=Exam, summary="Get exam by ID")
async def get_exam_by_id(exam_id: int):
    """
    Retrieve detailed information about a specific occupational medical exam.

    - **exam_id**: The unique identifier of the exam
    """
    exam = next((exam for exam in EXAMS_DATABASE if exam["id"] == exam_id), None)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam

@app.get("/exams/category/{category}", response_model=List[Exam], summary="Get exams by category")
async def get_exams_by_category(category: str):
    """
    Retrieve exams recommended for a specific work category.

    - **category**: Work category (e.g., "Construction workers", "Mining workers")
    """
    category_lower = category.lower()
    exams = [
        exam for exam in EXAMS_DATABASE
        if any(category_lower in rec.lower() for rec in exam["recommended_for"])
    ]
    if not exams:
        raise HTTPException(
            status_code=404,
            detail=f"No exams found for category '{category}'"
        )
    return exams

@app.get("/special-exams", response_model=List[Exam], summary="Get exams with special requirements")
async def get_special_exams():
    """
    Retrieve exams that have special requirements (e.g., high-altitude, confined spaces).
    """
    special_exams = [exam for exam in EXAMS_DATABASE if exam.get("special_requirements")]
    return special_exams
```
