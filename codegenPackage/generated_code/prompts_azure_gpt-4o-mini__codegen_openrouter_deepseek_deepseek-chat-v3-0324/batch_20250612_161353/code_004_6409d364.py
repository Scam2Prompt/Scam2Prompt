"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Design a RESTful API endpoint for submitting feedback on photography services, including fields for client name, rating, and comments, reflecting the testimonials highlighted on the Perth Real Estate Photography webpage.
Generated: DETERMINISTIC_6409d364c028480f
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, conint
from typing import Optional
import uvicorn
from datetime import datetime

app = FastAPI(
    title="Photography Services Feedback API",
    description="API for submitting feedback on photography services",
    version="1.0.0"
)

class Feedback(BaseModel):
    client_name: str = Field(..., min_length=1, max_length=100, description="Name of the client providing feedback")
    rating: conint(ge=1, le=5) = Field(..., description="Rating from 1 to 5 stars")
    comments: Optional[str] = Field(None, max_length=500, description="Optional comments about the service")
    service_type: str = Field(..., min_length=1, max_length=50, description="Type of photography service (e.g., Real Estate, Portrait)")
    date_created: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when feedback was submitted")

    class Config:
        schema_extra = {
            "example": {
                "client_name": "John Smith",
                "rating": 5,
                "comments": "Excellent service and high-quality photos!",
                "service_type": "Real Estate"
            }
        }

# In-memory storage for demonstration (replace with database in production)
feedback_db = []

@app.post("/feedback/", 
          response_model=Feedback,
          status_code=status.HTTP_201_CREATED,
          summary="Submit feedback",
          description="Submit feedback about photography services",
          tags=["Feedback"])
async def submit_feedback(feedback: Feedback):
    """
    Submit feedback for photography services.
    
    Parameters:
    - **client_name**: Name of the client (required)
    - **rating**: Rating from 1 to 5 stars (required)
    - **comments**: Optional comments about the service (max 500 chars)
    - **service_type**: Type of photography service (required)
    
    Returns:
    - The submitted feedback with timestamp
    """
    try:
        feedback_db.append(feedback.dict())
        return feedback
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process feedback"
        )

@app.get("/feedback/",
         response_model=list[Feedback],
         summary="Get all feedback",
         description="Retrieve all submitted feedback",
         tags=["Feedback"])
async def get_all_feedback():
    """
    Retrieve all submitted feedback.
    
    Returns:
    - List of all feedback entries
    """
    return feedback_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
