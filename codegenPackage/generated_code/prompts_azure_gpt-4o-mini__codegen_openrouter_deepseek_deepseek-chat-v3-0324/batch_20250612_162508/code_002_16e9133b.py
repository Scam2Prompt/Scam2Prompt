"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Create an API endpoint that allows coaches to input training data and receive feedback on how to enhance both athletic performance and life skills, based on the principles outlined by Team DGA.
Generated: DETERMINISTIC_16e9133b08750973
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import Optional, List
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Team DGA Coaching Feedback API",
    description="API for coaches to input training data and receive performance enhancement feedback",
    version="1.0.0"
)

# Database mock (in production, use a real database)
feedback_db = []

class TrainingData(BaseModel):
    """Model for training data input by coaches"""
    coach_id: str = Field(..., description="Unique identifier for the coach")
    athlete_id: str = Field(..., description="Unique identifier for the athlete")
    session_date: datetime = Field(..., description="Date and time of the training session")
    physical_performance: dict = Field(
        ...,
        description="Metrics related to physical performance (e.g., speed, strength)"
    )
    life_skills_assessment: dict = Field(
        ...,
        description="Assessment of life skills (e.g., leadership, communication)"
    )
    session_notes: Optional[str] = Field(
        None,
        description="Additional notes about the training session"
    )

class FeedbackResponse(BaseModel):
    """Model for the feedback response"""
    physical_feedback: List[str] = Field(
        ...,
        description="Suggestions for improving physical performance"
    )
    life_skills_feedback: List[str] = Field(
        ...,
        description="Suggestions for improving life skills"
    )
    overall_recommendations: List[str] = Field(
        ...,
        description="Overall recommendations for the athlete"
    )

def analyze_physical_performance(data: dict) -> List[str]:
    """Analyze physical performance metrics and generate feedback"""
    feedback = []
    
    if data.get('speed', 0) < 8:
        feedback.append("Consider incorporating more speed drills in training.")
    if data.get('strength', 0) < 7:
        feedback.append("Add progressive overload strength training sessions.")
    if data.get('endurance', 0) < 6:
        feedback.append("Include longer duration cardio sessions to build endurance.")
    
    return feedback or ["Physical performance metrics are on track. Maintain current training regimen."]

def analyze_life_skills(data: dict) -> List[str]:
    """Analyze life skills assessment and generate feedback"""
    feedback = []
    
    if data.get('leadership', 0) < 4:
        feedback.append("Assign team captain responsibilities to develop leadership.")
    if data.get('communication', 0) < 5:
        feedback.append("Practice active listening exercises and team discussions.")
    if data.get('resilience', 0) < 6:
        feedback.append("Implement mental toughness training and reflection exercises.")
    
    return feedback or ["Life skills development is progressing well. Continue current approach."]

def generate_overall_recommendations(physical: List[str], life: List[str]) -> List[str]:
    """Generate overall recommendations based on all feedback"""
    recommendations = []
    
    if "speed drills" in " ".join(physical).lower():
        recommendations.append("Schedule weekly speed-focused sessions.")
    if "strength training" in " ".join(physical).lower():
        recommendations.append("Implement bi-weekly strength assessments.")
    if "leadership" in " ".join(life).lower():
        recommendations.append("Organize monthly leadership workshops.")
    
    return recommendations or ["Continue balanced training program with current focus areas."]

@app.post("/submit-training-data/", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
async def submit_training_data(data: TrainingData):
    """
    Submit training data and receive performance enhancement feedback.
    
    Args:
        data: TrainingData object containing session details and metrics
    
    Returns:
        FeedbackResponse with suggestions for improvement
    """
    try:
        # Validate input data
        if not data.physical_performance or not data.life_skills_assessment:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Both physical performance and life skills assessments are required"
            )
        
        # Generate feedback
        physical_feedback = analyze_physical_performance(data.physical_performance)
        life_skills_feedback = analyze_life_skills(data.life_skills_assessment)
        overall_recommendations = generate_overall_recommendations(
            physical_feedback, life_skills_feedback
        )
        
        # Store the data (in production, this would be a database operation)
        feedback_db.append(data.dict())
        
        logger.info(f"Training data submitted for athlete {data.athlete_id} by coach {data.coach_id}")
        
        return FeedbackResponse(
            physical_feedback=physical_feedback,
            life_skills_feedback=life_skills_feedback,
            overall_recommendations=overall_recommendations
        )
        
    except Exception as e:
        logger.error(f"Error processing training data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request"
        )

@app.get("/training-sessions/", response_model=List[TrainingData])
async def get_training_sessions(coach_id: Optional[str] = None, athlete_id: Optional[str] = None):
    """
    Retrieve training sessions data with optional filtering by coach or athlete.
    
    Args:
        coach_id: Filter sessions by coach ID
        athlete_id: Filter sessions by athlete ID
    
    Returns:
        List of training sessions matching the criteria
    """
    try:
        filtered_sessions = feedback_db
        
        if coach_id:
            filtered_sessions = [s for s in filtered_sessions if s['coach_id'] == coach_id]
        if athlete_id:
            filtered_sessions = [s for s in filtered_sessions if s['athlete_id'] == athlete_id]
            
        return filtered_sessions
        
    except Exception as e:
        logger.error(f"Error retrieving training sessions: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving training sessions"
        )
```
