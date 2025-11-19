"""
Generated Code Metadata:
========================
Original URL: https://mammoth-cxk.pages.dev
Prompt: Develop a brief API documentation for a service that provides information on token rewards for conservation efforts, inspired by the $MAMAI token's mission.
Generated: DETERMINISTIC_c90f27193576739b
Batch ID: 20250622_210918
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
from enum import Enum

app = FastAPI(
    title="MAMAI Token Rewards API",
    description="API for tracking token rewards for conservation efforts",
    version="1.0.0",
    contact={
        "name": "MAMAI Support",
        "email": "support@mamai-token.org"
    },
    license_info={
        "name": "MIT",
    },
)

class ConservationActivity(str, Enum):
    TREE_PLANTING = "tree_planting"
    WILDLIFE_PROTECTION = "wildlife_protection"
    WATER_CONSERVATION = "water_conservation"
    EDUCATION = "education"

class RewardRequest(BaseModel):
    activity: ConservationActivity
    duration_hours: float
    location: str
    user_id: str

class RewardResponse(BaseModel):
    token_amount: float
    activity: ConservationActivity
    transaction_hash: Optional[str] = None
    status: str

@app.post("/calculate-rewards", response_model=RewardResponse, tags=["Rewards"])
async def calculate_rewards(request: RewardRequest):
    """
    Calculate token rewards for a conservation activity.
    
    Parameters:
    - activity: Type of conservation activity (tree_planting, wildlife_protection, etc.)
    - duration_hours: Duration of activity in hours
    - location: Geographic location of activity
    - user_id: Unique identifier for the user
    
    Returns:
    - Calculated token amount
    - Activity details
    - Transaction hash (if applicable)
    - Status of calculation
    """
    try:
        # Mock calculation - in production this would use actual business logic
        reward_multipliers = {
            ConservationActivity.TREE_PLANTING: 10,
            ConservationActivity.WILDLIFE_PROTECTION: 15,
            ConservationActivity.WATER_CONSERVATION: 12,
            ConservationActivity.EDUCATION: 8
        }
        
        token_amount = request.duration_hours * reward_multipliers[request.activity]
        
        return RewardResponse(
            token_amount=token_amount,
            activity=request.activity,
            status="success"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating rewards: {str(e)}"
        )

@app.get("/supported-activities", tags=["Reference"])
async def get_supported_activities():
    """
    Get list of supported conservation activities and their reward multipliers.
    
    Returns:
    - Dictionary of activities and their base reward rates (tokens per hour)
    """
    return {
        "tree_planting": 10,
        "wildlife_protection": 15,
        "water_conservation": 12,
        "education": 8
    }
```
