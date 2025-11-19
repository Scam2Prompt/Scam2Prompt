"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Create a simple API that analyzes user interactions with AI, inspired by the discussions in "KI und Gesellschaft" about automation and human engagement.
Generated: DETERMINISTIC_82fe9adf0e88b664
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import datetime
import uuid
import logging
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Interaction Analyzer API",
    description="API for analyzing user interactions with AI systems",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database for demonstration purposes
# In production, replace with a proper database
interaction_db = []

class Interaction(BaseModel):
    user_id: str
    ai_system: str
    interaction_type: str
    duration_seconds: float
    sentiment_score: Optional[float] = None
    additional_metadata: Optional[dict] = None

class InteractionResponse(BaseModel):
    interaction_id: str
    timestamp: datetime.datetime
    user_id: str
    ai_system: str
    interaction_type: str
    duration_seconds: float
    sentiment_score: Optional[float] = None
    additional_metadata: Optional[dict] = None

class AnalysisResult(BaseModel):
    total_interactions: int
    average_duration: float
    most_common_interaction: str
    sentiment_distribution: dict
    user_engagement_score: float

@app.post("/interactions/", response_model=InteractionResponse, status_code=201)
async def log_interaction(interaction: Interaction):
    """
    Log a new user-AI interaction.
    
    Args:
        interaction: Interaction data including user_id, AI system, and interaction details
    
    Returns:
        InteractionResponse: The logged interaction with generated metadata
    """
    try:
        interaction_id = str(uuid.uuid4())
        timestamp = datetime.datetime.now()
        
        interaction_record = {
            "interaction_id": interaction_id,
            "timestamp": timestamp,
            **interaction.dict()
        }
        
        interaction_db.append(interaction_record)
        logger.info(f"Logged interaction {interaction_id} for user {interaction.user_id}")
        
        return interaction_record
    except Exception as e:
        logger.error(f"Error logging interaction: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/interactions/{user_id}", response_model=List[InteractionResponse])
async def get_user_interactions(user_id: str, limit: int = 100):
    """
    Retrieve all interactions for a specific user.
    
    Args:
        user_id: The user ID to filter interactions
        limit: Maximum number of interactions to return
    
    Returns:
        List[InteractionResponse]: List of interactions for the specified user
    """
    try:
        user_interactions = [
            interaction for interaction in interaction_db 
            if interaction["user_id"] == user_id
        ][:limit]
        
        if not user_interactions:
            raise HTTPException(status_code=404, detail="No interactions found for this user")
            
        return user_interactions
    except Exception as e:
        logger.error(f"Error retrieving interactions for user {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/analyze/{user_id}", response_model=AnalysisResult)
async def analyze_interactions(user_id: str):
    """
    Analyze interactions for a specific user.
    
    Args:
        user_id: The user ID to analyze
    
    Returns:
        AnalysisResult: Statistical analysis of the user's interactions
    """
    try:
        user_interactions = [
            interaction for interaction in interaction_db 
            if interaction["user_id"] == user_id
        ]
        
        if not user_interactions:
            raise HTTPException(status_code=404, detail="No interactions found for this user")
        
        # Calculate basic statistics
        total_interactions = len(user_interactions)
        average_duration = sum(
            i["duration_seconds"] for i in user_interactions
        ) / total_interactions
        
        # Find most common interaction type
        interaction_types = [i["interaction_type"] for i in user_interactions]
        most_common = max(set(interaction_types), key=interaction_types.count)
        
        # Calculate sentiment distribution
        sentiments = [i.get("sentiment_score", 0) for i in user_interactions]
        sentiment_distribution = {
            "positive": len([s for s in sentiments if s > 0.5]),
            "neutral": len([s for s in sentiments if -0.5 <= s <= 0.5]),
            "negative": len([s for s in sentiments if s < -0.5])
        }
        
        # Simple engagement score calculation
        engagement_score = min(
            100, 
            (total_interactions * average_duration) / 10
        )
        
        return {
            "total_interactions": total_interactions,
            "average_duration": round(average_duration, 2),
            "most_common_interaction": most_common,
            "sentiment_distribution": sentiment_distribution,
            "user_engagement_score": round(engagement_score, 2)
        }
    except Exception as e:
        logger.error(f"Error analyzing interactions for user {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log all incoming requests.
    """
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Request completed with status {response.status_code}")
    return response
```
