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
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import date

app = FastAPI(
    title="Green Credit Builder API",
    description="A RESTful API for a Green Credit Builder-like platform",
    version="1.0.0",
)

# Define an enumeration for activity types
class ActivityType(str, Enum):
    """Enumeration for climate-positive activity types"""
    CARBON_OFFSET = "carbon_offset"
    RENEWABLE_ENERGY = "renewable_energy"
    RECYCLING = "recycling"
    SUSTAINABLE_TRANSPORT = "sustainable_transport"

# Define a Pydantic model for activity data
class ActivityData(BaseModel):
    """Pydantic model for climate-positive activity data"""
    activity_type: ActivityType
    amount: float
    date: date
    description: Optional[str] = None

# Define a Pydantic model for credit score response
class CreditScoreResponse(BaseModel):
    """Pydantic model for credit score response"""
    credit_score: float
    recommendations: Optional[list[str]] = []

# In-memory storage for demonstration purposes
# Replace with a proper database in production
activity_data_storage = []

# API endpoint to submit climate-positive activity data
@app.post("/activities/")
async def create_activity(activity_data: ActivityData):
    """Submit climate-positive activity data"""
    try:
        # Validate and store activity data
        activity_data_storage.append(activity_data.dict())
        return {"message": "Activity data submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to retrieve credit score and recommendations
@app.get("/credit-score/")
async def get_credit_score():
    """Retrieve credit score and recommendations"""
    try:
        # Calculate credit score based on stored activity data
        total_carbon_offset = sum(
            activity["amount"]
            for activity in activity_data_storage
            if activity["activity_type"] == ActivityType.CARBON_OFFSET.value
        )
        credit_score = total_carbon_offset * 0.1  # Simple calculation for demonstration

        # Generate recommendations based on activity data
        recommendations = []
        if credit_score < 10:
            recommendations.append("Consider increasing carbon offset activities")
        elif credit_score < 50:
            recommendations.append("Maintain current activity level")

        return CreditScoreResponse(credit_score=credit_score, recommendations=recommendations)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to retrieve activity data
@app.get("/activities/")
async def get_activities():
    """Retrieve all submitted activity data"""
    try:
        return activity_data_storage
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
