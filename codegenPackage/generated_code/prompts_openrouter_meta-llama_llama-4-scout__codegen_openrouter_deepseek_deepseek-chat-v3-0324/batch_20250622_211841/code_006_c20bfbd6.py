"""
Generated Code Metadata:
========================
Original URL: https://yo-channel.com
Prompt: "Design an API for a wellness platform that integratesファスティング and self律神経 data to provide personalized recommendations."
Generated: DETERMINISTIC_c20bfbd6deb36911
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Wellness Platform API",
    description="API for integrating fasting and autonomic nervous system data to provide personalized recommendations",
    version="1.0.0"
)

# Database models (simulated with in-memory storage for demonstration)
class User(BaseModel):
    id: str
    name: str
    age: int
    weight: float
    height: float
    health_conditions: Optional[List[str]] = None

class FastingData(BaseModel):
    user_id: str
    start_time: datetime
    end_time: datetime
    duration_hours: float
    notes: Optional[str] = None

class ANSData(BaseModel):
    user_id: str
    timestamp: datetime
    heart_rate: float
    hrv: float  # Heart Rate Variability
    stress_level: float = Field(..., ge=0, le=100)

class Recommendation(BaseModel):
    user_id: str
    timestamp: datetime
    recommendation_type: str
    message: str
    priority: int = Field(..., ge=1, le=3)

# In-memory storage (replace with actual database in production)
users_db = {}
fasting_data_db = []
ans_data_db = []
recommendations_db = []

# Dependency to get user
def get_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/users/", response_model=User, status_code=201)
async def create_user(user: User):
    """Create a new user profile"""
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user
    logger.info(f"Created user: {user.id}")
    return user

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    """Get user profile by ID"""
    return get_user(user_id)

@app.post("/fasting/", response_model=FastingData, status_code=201)
async def add_fasting_data(data: FastingData):
    """Add fasting data for a user"""
    if data.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    fasting_data_db.append(data)
    logger.info(f"Added fasting data for user: {data.user_id}")
    return data

@app.post("/ans/", response_model=ANSData, status_code=201)
async def add_ans_data(data: ANSData):
    """Add autonomic nervous system data for a user"""
    if data.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    ans_data_db.append(data)
    logger.info(f"Added ANS data for user: {data.user_id}")
    return data

@app.get("/recommendations/{user_id}", response_model=List[Recommendation])
async def get_recommendations(user_id: str):
    """Get personalized recommendations based on user data"""
    get_user(user_id)  # Check user exists
    
    # Simulate recommendation logic
    fasting_data = [d for d in fasting_data_db if d.user_id == user_id]
    ans_data = [d for d in ans_data_db if d.user_id == user_id]
    
    if not fasting_data and not ans_data:
        raise HTTPException(status_code=404, detail="No data available for recommendations")
    
    recommendations = []
    current_time = datetime.now()
    
    # Example recommendation logic
    if fasting_data:
        latest_fast = max(fasting_data, key=lambda x: x.end_time)
        if latest_fast.duration_hours > 16:
            recommendations.append(Recommendation(
                user_id=user_id,
                timestamp=current_time,
                recommendation_type="fasting",
                message="Consider a shorter fasting window next time based on your stress levels",
                priority=2
            ))
    
    if ans_data:
        avg_stress = sum(d.stress_level for d in ans_data) / len(ans_data)
        if avg_stress > 70:
            recommendations.append(Recommendation(
                user_id=user_id,
                timestamp=current_time,
                recommendation_type="stress_management",
                message="High stress detected. Try breathing exercises or meditation",
                priority=1
            ))
    
    if not recommendations:
        recommendations.append(Recommendation(
            user_id=user_id,
            timestamp=current_time,
            recommendation_type="general",
            message="Your current regimen looks good. Keep it up!",
            priority=3
        ))
    
    recommendations_db.extend(recommendations)
    return recommendations

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.error(f"HTTP error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unexpected error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred"},
    )
```
