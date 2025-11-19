"""
Generated Code Metadata:
========================
Original URL: https://greencreditbuilder.com
Prompt: "Design a RESTful API for a Green Credit Builder-like platform that accepts climate-positive activity data and returns credit scores or recommendations."
Generated: DETERMINISTIC_8c89b1bddf0f1683
Batch ID: 20250622_212850
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
from datetime import date
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Green Credit Builder API",
    description="A RESTful API for tracking climate-positive activities and calculating green credit scores",
    version="1.0.0"
)

# Database simulation (in production, replace with a real database)
class ActivityDB:
    def __init__(self):
        self.activities = {}
        self.users = {}

    def add_activity(self, activity):
        activity_id = str(uuid.uuid4())
        activity.id = activity_id
        self.activities[activity_id] = activity
        return activity_id

    def get_activities_by_user(self, user_id):
        return [act for act in self.activities.values() if act.user_id == user_id]

    def get_user(self, user_id):
        return self.users.get(user_id)

    def add_user(self, user):
        user_id = str(uuid.uuid4())
        user.id = user_id
        self.users[user_id] = user
        return user_id

db = ActivityDB()

# Models
class User(BaseModel):
    id: Optional[str] = None
    name: str = Field(..., example="Jane Doe")
    email: str = Field(..., example="jane@example.com")
    location: str = Field(..., example="New York, USA")

class Activity(BaseModel):
    id: Optional[str] = None
    user_id: str = Field(..., example="user123")
    activity_type: str = Field(..., example="recycling", description="Type of climate-positive activity")
    description: str = Field(..., example="Recycled 5kg of plastic")
    date: date = Field(..., example="2023-01-15")
    carbon_saved: float = Field(..., example=2.5, description="Amount of carbon saved in kg")
    verified: bool = Field(default=False, description="Whether the activity has been verified")

class CreditScoreResponse(BaseModel):
    user_id: str
    score: float = Field(..., ge=0, le=1000, description="Green credit score (0-1000)")
    level: str = Field(..., description="Credit level based on score")
    recommendations: List[str] = Field(..., description="List of recommended actions to improve score")

# Helper functions
def calculate_credit_score(activities: List[Activity]) -> CreditScoreResponse:
    """Calculate green credit score based on user's activities"""
    if not activities:
        return CreditScoreResponse(
            user_id=activities[0].user_id if activities else "",
            score=0,
            level="Beginner",
            recommendations=["Start logging your climate-positive activities!"]
        )

    total_carbon_saved = sum(act.carbon_saved for act in activities)
    verified_activities = sum(1 for act in activities if act.verified)
    
    # Simple scoring algorithm (in production, this would be more sophisticated)
    base_score = min(total_carbon_saved * 10, 800)
    verification_bonus = verified_activities * 5
    score = min(base_score + verification_bonus, 1000)
    
    if score >= 800:
        level = "Eco Champion"
    elif score >= 500:
        level = "Green Leader"
    elif score >= 200:
        level = "Eco Conscious"
    else:
        level = "Beginner"

    recommendations = []
    if verified_activities < len(activities) / 2:
        recommendations.append("Verify more activities to increase your score")
    if total_carbon_saved < 50:
        recommendations.append("Try to increase your carbon savings by exploring new activities")
    if "recycling" not in [act.activity_type for act in activities]:
        recommendations.append("Consider adding recycling to your activities")

    return CreditScoreResponse(
        user_id=activities[0].user_id,
        score=score,
        level=level,
        recommendations=recommendations
    )

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    """Create a new user"""
    try:
        user_id = db.add_user(user)
        created_user = db.get_user(user_id)
        logger.info(f"Created new user with ID: {user_id}")
        return created_user
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create user"
        )

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    """Get user details by ID"""
    user = db.get_user(user_id)
    if not user:
        logger.warning(f"User not found: {user_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@app.post("/activities/", response_model=Activity, status_code=status.HTTP_201_CREATED)
async def log_activity(activity: Activity):
    """Log a new climate-positive activity"""
    try:
        if not db.get_user(activity.user_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        activity_id = db.add_activity(activity)
        created_activity = db.activities[activity_id]
        logger.info(f"Logged new activity: {activity_id}")
        return created_activity
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error logging activity: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not log activity"
        )

@app.get("/activities/{user_id}", response_model=List[Activity])
async def get_user_activities(user_id: str):
    """Get all activities for a user"""
    try:
        activities = db.get_activities_by_user(user_id)
        if not activities:
            logger.info(f"No activities found for user: {user_id}")
        return activities
    except Exception as e:
        logger.error(f"Error fetching activities: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not fetch activities"
        )

@app.get("/creditscore/{user_id}", response_model=CreditScoreResponse)
async def get_credit_score(user_id: str):
    """Calculate and return the green credit score for a user"""
    try:
        user = db.get_user(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        activities = db.get_activities_by_user(user_id)
        return calculate_credit_score(activities)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating credit score: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not calculate credit score"
        )

@app.put("/activities/verify/{activity_id}", response_model=Activity)
async def verify_activity(activity_id: str):
    """Mark an activity as verified"""
    try:
        if activity_id not in db.activities:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Activity not found"
            )
        
        db.activities[activity_id].verified = True
        logger.info(f"Verified activity: {activity_id}")
        return db.activities[activity_id]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error verifying activity: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not verify activity"
        )
```
