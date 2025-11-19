"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Create an API that provides personalized course recommendations for students based on their admission exam preparation needs, inspired by the offerings at Educar Comitán.
Generated: DETERMINISTIC_f315b4d18a6c27dc
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Educar Comitán Course Recommendation API",
    description="API for personalized course recommendations based on admission exam preparation needs",
    version="1.0.0"
)

# Database mock (in a real application, this would be a proper database)
COURSES_DB = {
    "math": [
        {"id": 1, "name": "Basic Algebra", "level": "beginner", "duration": "4 weeks", "price": 500},
        {"id": 2, "name": "Advanced Calculus", "level": "advanced", "duration": "8 weeks", "price": 800},
        {"id": 3, "name": "Geometry Fundamentals", "level": "beginner", "duration": "6 weeks", "price": 600},
    ],
    "spanish": [
        {"id": 4, "name": "Grammar Essentials", "level": "beginner", "duration": "5 weeks", "price": 550},
        {"id": 5, "name": "Advanced Composition", "level": "advanced", "duration": "7 weeks", "price": 750},
    ],
    "science": [
        {"id": 6, "name": "Biology Basics", "level": "beginner", "duration": "6 weeks", "price": 600},
        {"id": 7, "name": "Chemistry Concepts", "level": "intermediate", "duration": "8 weeks", "price": 800},
    ]
}

class StudentProfile(BaseModel):
    name: str
    subjects: List[str]
    skill_level: str
    budget: Optional[float] = None
    preferred_duration: Optional[str] = None

class CourseRecommendation(BaseModel):
    id: int
    name: str
    subject: str
    level: str
    duration: str
    price: float

@app.get("/courses", response_model=List[CourseRecommendation])
def get_all_courses():
    """Get all available courses from the database."""
    try:
        recommendations = []
        for subject, courses in COURSES_DB.items():
            for course in courses:
                recommendations.append({
                    "id": course["id"],
                    "name": course["name"],
                    "subject": subject,
                    "level": course["level"],
                    "duration": course["duration"],
                    "price": course["price"]
                })
        return recommendations
    except Exception as e:
        logger.error(f"Error fetching all courses: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/recommendations", response_model=List[CourseRecommendation])
def get_recommendations(profile: StudentProfile):
    """Get personalized course recommendations based on student profile."""
    try:
        recommendations = []
        
        for subject in profile.subjects:
            if subject not in COURSES_DB:
                continue
            
            for course in COURSES_DB[subject]:
                # Basic matching based on skill level
                if course["level"] == profile.skill_level:
                    # Additional filters if provided
                    if profile.budget and course["price"] > profile.budget:
                        continue
                    if (profile.preferred_duration and 
                        int(course["duration"].split()[0]) > int(profile.preferred_duration.split()[0])):
                        continue
                    
                    recommendations.append({
                        "id": course["id"],
                        "name": course["name"],
                        "subject": subject,
                        "level": course["level"],
                        "duration": course["duration"],
                        "price": course["price"]
                    })
        
        if not recommendations:
            raise HTTPException(
                status_code=404,
                detail="No courses found matching your criteria. Try adjusting your filters."
            )
            
        return recommendations
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/courses/{subject}", response_model=List[CourseRecommendation])
def get_courses_by_subject(subject: str):
    """Get all courses for a specific subject."""
    try:
        if subject not in COURSES_DB:
            raise HTTPException(
                status_code=404,
                detail=f"No courses found for subject: {subject}"
            )
            
        recommendations = []
        for course in COURSES_DB[subject]:
            recommendations.append({
                "id": course["id"],
                "name": course["name"],
                "subject": subject,
                "level": course["level"],
                "duration": course["duration"],
                "price": course["price"]
            })
            
        return recommendations
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching courses for subject {subject}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
