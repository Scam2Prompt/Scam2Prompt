"""
Generated Code Metadata:
========================
Original URL: https://searchhr.com.ar
Prompt: Suggest an API for integrating vocational guidance tools into an HR platform, similar to the "Orientación Vocacional-Ocupacional" services offered by Search HR.
Generated: DETERMINISTIC_6ed133004e8faefa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vocational_guidance_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Vocational Guidance API",
    description="API for integrating vocational guidance tools into an HR platform",
    version="1.0.0"
)

# Define a model for the user input
class UserProfile(BaseModel):
    """User profile model"""
    age: int
    interests: List[str]
    skills: List[str]
    career_goals: List[str]

# Define a model for the vocational guidance assessment
class VocationalGuidanceAssessment(BaseModel):
    """Vocational guidance assessment model"""
    recommended_careers: List[str]
    suggested_skills: List[str]
    recommended_interests: List[str]

# In-memory database for demonstration purposes
vocational_guidance_data = {
    "careers": [
        {"name": "Software Engineer", "interests": ["programming", "technology"], "skills": ["python", "java"]},
        {"name": "Data Scientist", "interests": ["data analysis", "machine learning"], "skills": ["python", "r"]},
    ]
}

# API endpoint to get vocational guidance assessment
@app.post("/assessment", response_model=VocationalGuidanceAssessment)
async def get_vocational_guidance_assessment(user_profile: UserProfile):
    try:
        # Simulate a vocational guidance assessment based on user input
        recommended_careers = []
        suggested_skills = []
        recommended_interests = []

        for career in vocational_guidance_data["careers"]:
            if any(interest in career["interests"] for interest in user_profile.interests):
                recommended_careers.append(career["name"])
                suggested_skills.extend([skill for skill in career["skills"] if skill not in suggested_skills])
                recommended_interests.extend([interest for interest in career["interests"] if interest not in recommended_interests])

        if not recommended_careers:
            raise HTTPException(status_code=404, detail="No matching careers found")

        return VocationalGuidanceAssessment(
            recommended_careers=recommended_careers,
            suggested_skills=suggested_skills,
            recommended_interests=recommended_interests
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get careers
@app.get("/careers", response_model=List[dict])
async def get_careers():
    try:
        return vocational_guidance_data["careers"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get skills
@app.get("/skills", response_model=List[str])
async def get_skills():
    try:
        skills = set()
        for career in vocational_guidance_data["careers"]:
            skills.update(career["skills"])
        return list(skills)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to get interests
@app.get("/interests", response_model=List[str])
async def get_interests():
    try:
        interests = set()
        for career in vocational_guidance_data["careers"]:
            interests.update(career["interests"])
        return list(interests)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

```python
# main.py
from vocational_guidance_api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
