"""
Generated Code Metadata:
========================
Original URL: https://everyworld-started.pages.dev
Prompt: Create an API endpoint that allows users to submit their points and check their eligibility for the Everyworld drawings.
Generated: DETERMINISTIC_2d7baf81df743bc5
Batch ID: 20250612_142517
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
    title="Everyworld Drawings API",
    description="API for checking eligibility for Everyworld drawings",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
drawings_db = {
    "current_drawing": {
        "id": "drawing_2023_11",
        "name": "November 2023 Drawing",
        "min_points": 100,
        "start_date": "2023-11-01",
        "end_date": "2023-11-30",
        "is_active": True
    },
    "user_points": {}  # user_id: points
}

class PointsSubmission(BaseModel):
    user_id: str
    points: int
    source: Optional[str] = None

class EligibilityResponse(BaseModel):
    is_eligible: bool
    current_points: int
    required_points: int
    drawing_id: str
    drawing_name: str
    message: Optional[str] = None

@app.post("/submit-points/", status_code=status.HTTP_200_OK)
async def submit_points(points_data: PointsSubmission):
    """
    Submit user points to the system.
    """
    try:
        # Validate points are positive
        if points_data.points <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Points must be a positive integer"
            )

        # Update user points in the database
        current_points = drawings_db["user_points"].get(points_data.user_id, 0)
        drawings_db["user_points"][points_data.user_id] = current_points + points_data.points

        logger.info(f"User {points_data.user_id} submitted {points_data.points} points")

        return {
            "status": "success",
            "user_id": points_data.user_id,
            "total_points": drawings_db["user_points"][points_data.user_id]
        }
    except Exception as e:
        logger.error(f"Error submitting points: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@app.get("/check-eligibility/{user_id}", response_model=EligibilityResponse)
async def check_eligibility(user_id: str):
    """
    Check if a user is eligible for the current drawing.
    """
    try:
        current_drawing = drawings_db["current_drawing"]
        
        # Check if drawing is active
        if not current_drawing["is_active"]:
            return EligibilityResponse(
                is_eligible=False,
                current_points=0,
                required_points=current_drawing["min_points"],
                drawing_id=current_drawing["id"],
                drawing_name=current_drawing["name"],
                message="No active drawing at this time"
            )

        user_points = drawings_db["user_points"].get(user_id, 0)
        is_eligible = user_points >= current_drawing["min_points"]

        return EligibilityResponse(
            is_eligible=is_eligible,
            current_points=user_points,
            required_points=current_drawing["min_points"],
            drawing_id=current_drawing["id"],
            drawing_name=current_drawing["name"],
            message="Eligible" if is_eligible else f"Need {current_drawing['min_points'] - user_points} more points"
        )
    except Exception as e:
        logger.error(f"Error checking eligibility: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@app.get("/current-drawing/")
async def get_current_drawing():
    """
    Get information about the current active drawing.
    """
    try:
        return drawings_db["current_drawing"]
    except Exception as e:
        logger.error(f"Error getting current drawing: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
```
