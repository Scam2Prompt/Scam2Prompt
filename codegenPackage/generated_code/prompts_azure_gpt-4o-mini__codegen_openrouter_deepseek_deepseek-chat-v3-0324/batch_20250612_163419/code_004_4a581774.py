"""
Generated Code Metadata:
========================
Original URL: https://milc-global.pages.dev
Prompt: Create a sample code snippet that demonstrates how to provide early audience feedback for video content within the MILC Community platform.
Generated: DETERMINISTIC_4a581774d482aaeb
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel, Field, validator
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="MILC Community Video Feedback API",
    description="API for collecting and retrieving early audience feedback for video content",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database simulation
video_feedback_db = []

# Models
class Feedback(BaseModel):
    """Model for individual feedback entry"""
    user_id: str = Field(..., description="ID of the user providing feedback")
    video_id: str = Field(..., description="ID of the video being reviewed")
    rating: int = Field(..., ge=1, le=5, description="Rating from 1 to 5 stars")
    comment: Optional[str] = Field(None, max_length=500, description="Optional comment")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Feedback submission time")

    @validator('comment')
    def validate_comment(cls, v):
        if v and len(v.strip()) == 0:
            raise ValueError("Comment cannot be empty or whitespace only")
        return v

class VideoFeedbackSummary(BaseModel):
    """Model for aggregated feedback data"""
    video_id: str
    average_rating: float
    total_feedbacks: int
    last_feedback_time: Optional[datetime]
    feedback_samples: List[Feedback]

# Routes
@app.post("/feedback/", status_code=status.HTTP_201_CREATED, response_model=Feedback)
async def submit_feedback(feedback: Feedback):
    """
    Submit feedback for a video.
    
    Args:
        feedback: Feedback object containing user_id, video_id, rating, and optional comment
    
    Returns:
        The submitted feedback with timestamp
    """
    try:
        video_feedback_db.append(feedback.dict())
        return feedback
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error submitting feedback: {str(e)}"
        )

@app.get("/feedback/{video_id}", response_model=VideoFeedbackSummary)
async def get_video_feedback(
    video_id: str,
    limit: int = Query(5, ge=1, le=100, description="Limit number of sample feedbacks")
):
    """
    Get aggregated feedback for a specific video.
    
    Args:
        video_id: ID of the video to get feedback for
        limit: Maximum number of sample feedbacks to return
    
    Returns:
        VideoFeedbackSummary with aggregated data and sample feedbacks
    """
    try:
        video_feedbacks = [f for f in video_feedback_db if f['video_id'] == video_id]
        
        if not video_feedbacks:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No feedback found for this video"
            )
        
        ratings = [f['rating'] for f in video_feedbacks]
        average_rating = sum(ratings) / len(ratings)
        
        # Sort by timestamp descending and get most recent
        sorted_feedbacks = sorted(
            video_feedbacks,
            key=lambda x: x['timestamp'],
            reverse=True
        )
        
        return VideoFeedbackSummary(
            video_id=video_id,
            average_rating=round(average_rating, 2),
            total_feedbacks=len(video_feedbacks),
            last_feedback_time=sorted_feedbacks[0]['timestamp'],
            feedback_samples=sorted_feedbacks[:limit]
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving feedback: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow()}
```
