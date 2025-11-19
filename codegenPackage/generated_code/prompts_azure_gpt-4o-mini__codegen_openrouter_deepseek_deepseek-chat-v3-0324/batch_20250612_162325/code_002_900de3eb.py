"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Create a RESTful API endpoint for a professional development program, like the outplacement services provided by Videtis Consultores, that allows users to submit their career goals and receive tailored advice.
Generated: DETERMINISTIC_900de3eb3fb6bfd5
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Professional Development API",
    description="API for career goal submission and tailored advice",
    version="1.0.0"
)

# Database mock (in production, replace with actual database)
career_goals_db = []
advice_db = []

class CareerGoal(BaseModel):
    user_id: str
    current_position: str
    desired_position: str
    skills: list[str]
    experience_years: int
    timeline_months: int
    additional_info: Optional[str] = None

class CareerAdvice(BaseModel):
    advice_id: str
    user_id: str
    advice_text: str
    resources: list[str]
    generated_at: datetime

def generate_advice(goal: CareerGoal) -> CareerAdvice:
    """Generate tailored career advice based on user's goals"""
    # In production, this would use more sophisticated logic or ML models
    advice_text = f"""
    Based on your goal to move from {goal.current_position} to {goal.desired_position}:
    1. Focus on developing these key skills: {', '.join(goal.skills[:3])}
    2. With your {goal.experience_years} years of experience, consider networking opportunities
    3. Your timeline of {goal.timeline_months} months is {'realistic' if goal.timeline_months >= 6 else 'ambitious'}
    """
    
    resources = [
        "Professional networking events",
        "Online courses for skill development",
        "Mentorship programs"
    ]
    
    return CareerAdvice(
        advice_id=str(len(advice_db) + 1),
        user_id=goal.user_id,
        advice_text=advice_text,
        resources=resources,
        generated_at=datetime.now()
    )

@app.post("/submit-goal/", status_code=status.HTTP_201_CREATED)
async def submit_career_goal(goal: CareerGoal):
    """Submit career goals and receive tailored advice"""
    try:
        # Validate input
        if not goal.skills:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one skill is required"
            )
        
        if goal.experience_years < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Experience years cannot be negative"
            )
        
        # Store the goal
        career_goals_db.append(goal)
        logger.info(f"New career goal submitted by user {goal.user_id}")
        
        # Generate and store advice
        advice = generate_advice(goal)
        advice_db.append(advice)
        
        return {
            "message": "Career goal submitted successfully",
            "advice_id": advice.advice_id
        }
    except Exception as e:
        logger.error(f"Error submitting career goal: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request"
        )

@app.get("/get-advice/{advice_id}", response_model=CareerAdvice)
async def get_career_advice(advice_id: str):
    """Retrieve previously generated career advice"""
    try:
        advice = next((a for a in advice_db if a.advice_id == advice_id), None)
        if not advice:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Advice not found"
            )
        return advice
    except Exception as e:
        logger.error(f"Error retrieving advice {advice_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving advice"
        )

@app.get("/user-goals/{user_id}", response_model=list[CareerGoal])
async def get_user_goals(user_id: str):
    """Retrieve all career goals for a specific user"""
    try:
        user_goals = [g for g in career_goals_db if g.user_id == user_id]
        if not user_goals:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No goals found for this user"
            )
        return user_goals
    except Exception as e:
        logger.error(f"Error retrieving goals for user {user_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving user goals"
        )
```
