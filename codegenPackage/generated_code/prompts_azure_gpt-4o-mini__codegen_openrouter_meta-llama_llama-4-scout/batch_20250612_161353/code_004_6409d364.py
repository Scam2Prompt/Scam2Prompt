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
# feedback_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Photography Service Feedback API",
    description="Submit feedback on photography services",
    version="1.0.0",
)

class Feedback(BaseModel):
    """Feedback model"""
    client_name: str
    rating: int
    comments: Optional[str] = None

    class Config:
        """Model configuration"""
        schema_extra = {
            "example": {
                "client_name": "John Doe",
                "rating": 5,
                "comments": "Excellent service!"
            }
        }

@app.post("/feedback", status_code=201, response_model=Feedback)
async def create_feedback(feedback: Feedback):
    """
    Create a new feedback entry.

    Args:
    - feedback (Feedback): The feedback data.

    Returns:
    - The created feedback entry.

    Raises:
    - HTTPException: If the rating is out of range.
    """
    if not 1 <= feedback.rating <= 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")

    # In a real application, you would save the feedback to a database here
    # For demonstration purposes, we'll just return the feedback
    return feedback

@app.get("/feedback", status_code=200)
async def read_feedback():
    """
    Read all feedback entries.

    Returns:
    - A list of feedback entries.
    """
    # In a real application, you would fetch the feedback from a database here
    # For demonstration purposes, we'll return an empty list
    return []

@app.get("/feedback/{feedback_id}", status_code=200, response_model=Feedback)
async def read_feedback_by_id(feedback_id: int):
    """
    Read a feedback entry by ID.

    Args:
    - feedback_id (int): The ID of the feedback entry.

    Returns:
    - The feedback entry.

    Raises:
    - HTTPException: If the feedback entry is not found.
    """
    # In a real application, you would fetch the feedback from a database here
    # For demonstration purposes, we'll return a sample feedback
    if feedback_id == 1:
        return Feedback(client_name="Jane Doe", rating=4, comments="Good service!")
    else:
        raise HTTPException(status_code=404, detail="Feedback not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
