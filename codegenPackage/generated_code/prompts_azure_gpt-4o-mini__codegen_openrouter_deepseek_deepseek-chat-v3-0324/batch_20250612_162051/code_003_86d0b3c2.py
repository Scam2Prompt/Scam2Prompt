"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: Develop a REST API endpoint that allows users to fetch information about the different skill levels available for sewing courses at Workshop Granada, including beginner, intermediate, and professional options.
Generated: DETERMINISTIC_86d0b3c20e810dd3
Batch ID: 20250612_162051
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
from enum import Enum
from typing import List

app = FastAPI(
    title="Workshop Granada Sewing Courses API",
    description="API for fetching information about sewing course skill levels at Workshop Granada",
    version="1.0.0"
)

class SkillLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    PROFESSIONAL = "professional"

class CourseLevel(BaseModel):
    level: SkillLevel
    description: str
    prerequisites: List[str]
    duration_weeks: int
    max_participants: int

# Mock database of course levels
COURSE_LEVELS = {
    SkillLevel.BEGINNER: CourseLevel(
        level=SkillLevel.BEGINNER,
        description="Introduction to sewing techniques, basic patterns, and machine operation.",
        prerequisites=["No prior experience required"],
        duration_weeks=4,
        max_participants=12
    ),
    SkillLevel.INTERMEDIATE: CourseLevel(
        level=SkillLevel.INTERMEDIATE,
        description="Advanced patterns, garment construction, and fabric selection.",
        prerequisites=["Beginner course completion or equivalent experience"],
        duration_weeks=6,
        max_participants=10
    ),
    SkillLevel.PROFESSIONAL: CourseLevel(
        level=SkillLevel.PROFESSIONAL,
        description="Master-level techniques, couture sewing, and small business preparation.",
        prerequisites=["Intermediate course completion or professional experience"],
        duration_weeks=8,
        max_participants=8
    )
}

@app.get(
    "/levels/",
    response_model=List[CourseLevel],
    summary="Get all available skill levels",
    description="Returns information about all sewing course skill levels offered at Workshop Granada."
)
async def get_all_levels():
    """Fetch all available course skill levels."""
    return list(COURSE_LEVELS.values())

@app.get(
    "/levels/{level_name}",
    response_model=CourseLevel,
    summary="Get specific skill level details",
    description="Returns detailed information about a specific sewing course skill level.",
    responses={
        404: {"description": "Skill level not found"}
    }
)
async def get_level(level_name: SkillLevel):
    """Fetch details for a specific course skill level."""
    if level_name not in COURSE_LEVELS:
        raise HTTPException(
            status_code=404,
            detail=f"Skill level '{level_name}' not found"
        )
    return COURSE_LEVELS[level_name]

@app.get(
    "/levels/enum",
    response_model=List[str],
    summary="Get available skill level enum values",
    description="Returns the possible values for the skill level parameter."
)
async def get_level_enum():
    """Get all possible skill level enum values."""
    return [level.value for level in SkillLevel]
```
