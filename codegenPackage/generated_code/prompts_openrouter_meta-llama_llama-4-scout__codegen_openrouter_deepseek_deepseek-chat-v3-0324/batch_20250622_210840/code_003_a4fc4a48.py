"""
Generated Code Metadata:
========================
Original URL: https://agora-ai.market
Prompt: Design a rating system for AI agents on Agora AI, incorporating community-driven ratings and metrics to ensure high-quality AI solutions.
Generated: DETERMINISTIC_a4fc4a48144bf3ae
Batch ID: 20250622_210840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Agora AI Rating System
This module implements a community-driven rating system for AI agents on Agora AI.
"""

from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, validator
from enum import Enum
import uuid
import math

class RatingCategory(str, Enum):
    ACCURACY = "accuracy"
    PERFORMANCE = "performance"
    RELIABILITY = "reliability"
    USABILITY = "usability"
    ETHICS = "ethics"

class Rating(BaseModel):
    """
    Represents a single rating given by a user for an AI agent.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    ai_agent_id: str
    category: RatingCategory
    score: float = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('score')
    def round_score(cls, v):
        """Round score to nearest 0.5"""
        return round(v * 2) / 2

class AIAgentRatingSummary(BaseModel):
    """
    Summary of ratings for an AI agent across all categories.
    """
    ai_agent_id: str
    ratings_count: int
    average_rating: float
    category_breakdown: Dict[RatingCategory, float]
    weighted_score: float

class RatingSystem:
    """
    Main rating system class that handles rating operations and calculations.
    """
    
    def __init__(self):
        self.ratings: Dict[str, List[Rating]] = {}  # ai_agent_id -> list of ratings
    
    def add_rating(self, rating: Rating) -> None:
        """
        Add a new rating for an AI agent.
        """
        if rating.ai_agent_id not in self.ratings:
            self.ratings[rating.ai_agent_id] = []
        self.ratings[rating.ai_agent_id].append(rating)
    
    def get_ratings(self, ai_agent_id: str) -> List[Rating]:
        """
        Retrieve all ratings for a specific AI agent.
        """
        return self.ratings.get(ai_agent_id, [])
    
    def calculate_agent_summary(self, ai_agent_id: str) -> AIAgentRatingSummary:
        """
        Calculate and return a summary of ratings for an AI agent.
        """
        ratings = self.get_ratings(ai_agent_id)
        if not ratings:
            raise ValueError("No ratings found for this AI agent")
        
        # Calculate average rating
        total_score = sum(r.score for r in ratings)
        average_rating = total_score / len(ratings)
        
        # Calculate category breakdown
        category_scores: Dict[RatingCategory, List[float]] = {
            category: [] for category in RatingCategory
        }
        
        for rating in ratings:
            category_scores[rating.category].append(rating.score)
        
        category_breakdown = {
            category: sum(scores) / len(scores) if scores else 0
            for category, scores in category_scores.items()
        }
        
        # Calculate weighted score (more recent ratings have higher weight)
        weighted_scores = []
        max_time = max(r.created_at for r in ratings)
        
        for rating in ratings:
            time_diff = (max_time - rating.created_at).total_seconds()
            weight = math.exp(-time_diff / (30 * 24 * 3600))  # 30-day half-life
            weighted_scores.append(rating.score * weight)
        
        weighted_score = sum(weighted_scores) / sum(
            math.exp(-(max_time - r.created_at).total_seconds() / (30 * 24 * 3600))
            for r in ratings
        )
        
        return AIAgentRatingSummary(
            ai_agent_id=ai_agent_id,
            ratings_count=len(ratings),
            average_rating=round(average_rating, 2),
            category_breakdown={
                k: round(v, 2) for k, v in category_breakdown.items()
            },
            weighted_score=round(weighted_score, 2)
        )
    
    def get_top_agents(self, limit: int = 10) -> List[AIAgentRatingSummary]:
        """
        Get top-rated AI agents based on weighted score.
        """
        summaries = []
        for ai_agent_id in self.ratings:
            try:
                summary = self.calculate_agent_summary(ai_agent_id)
                summaries.append(summary)
            except ValueError:
                continue
        
        return sorted(
            summaries,
            key=lambda x: x.weighted_score,
            reverse=True
        )[:limit]

class RatingAPI:
    """
    API layer for interacting with the rating system.
    """
    
    def __init__(self):
        self.rating_system = RatingSystem()
    
    def submit_rating(self, rating_data: Dict) -> Rating:
        """
        Submit a new rating to the system.
        """
        try:
            rating = Rating(**rating_data)
            self.rating_system.add_rating(rating)
            return rating
        except Exception as e:
            raise ValueError(f"Invalid rating data: {str(e)}")
    
    def get_agent_ratings(self, ai_agent_id: str) -> List[Rating]:
        """
        Retrieve all ratings for a specific AI agent.
        """
        return self.rating_system.get_ratings(ai_agent_id)
    
    def get_agent_summary(self, ai_agent_id: str) -> AIAgentRatingSummary:
        """
        Get the rating summary for a specific AI agent.
        """
        try:
            return self.rating_system.calculate_agent_summary(ai_agent_id)
        except ValueError as e:
            raise ValueError(str(e))
    
    def get_top_rated_agents(self, limit: int = 10) -> List[AIAgentRatingSummary]:
        """
        Get the top-rated AI agents.
        """
        return self.rating_system.get_top_agents(limit)
```
