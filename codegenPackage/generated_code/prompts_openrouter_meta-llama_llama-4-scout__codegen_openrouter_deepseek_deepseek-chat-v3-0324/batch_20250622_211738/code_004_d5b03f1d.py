"""
Generated Code Metadata:
========================
Original URL: https://tropadavivi.site
Prompt: "Create a simple API recommendation system for a platform that offers free and VIP signal services, inspired by the features on https://tropadavivi.site."
Generated: DETERMINISTIC_d5b03f1dd48ca88f
Batch ID: 20250622_211738
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Signal Recommendation API",
    description="API for recommending free and VIP signal services",
    version="1.0.0"
)

class SignalType(str, Enum):
    FREE = "free"
    VIP = "vip"

class Signal(BaseModel):
    id: int
    name: str
    type: SignalType
    description: str
    success_rate: float
    last_updated: datetime
    popularity: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Gold Trader",
                "type": "vip",
                "description": "High accuracy gold trading signals",
                "success_rate": 85.5,
                "last_updated": "2023-01-15T10:30:00",
                "popularity": 150
            }
        }

class RecommendationRequest(BaseModel):
    user_id: Optional[int] = None
    signal_type: Optional[SignalType] = None
    limit: int = 5

    class Config:
        schema_extra = {
            "example": {
                "user_id": 123,
                "signal_type": "free",
                "limit": 3
            }
        }

# Mock database
signals_db = [
    Signal(
        id=1,
        name="Gold Trader",
        type=SignalType.VIP,
        description="High accuracy gold trading signals",
        success_rate=85.5,
        last_updated=datetime(2023, 1, 15, 10, 30),
        popularity=150
    ),
    Signal(
        id=2,
        name="Crypto Pro",
        type=SignalType.VIP,
        description="Premium cryptocurrency signals",
        success_rate=78.2,
        last_updated=datetime(2023, 2, 20, 14, 15),
        popularity=200
    ),
    Signal(
        id=3,
        name="Forex Beginner",
        type=SignalType.FREE,
        description="Basic forex signals for beginners",
        success_rate=65.0,
        last_updated=datetime(2023, 3, 5, 9, 0),
        popularity=300
    ),
    Signal(
        id=4,
        name="Stock Master",
        type=SignalType.VIP,
        description="Expert stock market signals",
        success_rate=82.0,
        last_updated=datetime(2023, 1, 30, 11, 45),
        popularity=120
    ),
    Signal(
        id=5,
        name="Crypto Free",
        type=SignalType.FREE,
        description="Free cryptocurrency signals",
        success_rate=60.5,
        last_updated=datetime(2023, 2, 10, 16, 20),
        popularity=250
    )
]

def get_recommendations(signal_type: Optional[SignalType] = None, limit: int = 5) -> List[Signal]:
    """
    Get recommended signals based on type and limit
    """
    filtered_signals = signals_db
    
    if signal_type:
        filtered_signals = [s for s in filtered_signals if s.type == signal_type]
    
    # Sort by popularity and success rate
    sorted_signals = sorted(
        filtered_signals,
        key=lambda x: (x.popularity, x.success_rate),
        reverse=True
    )
    
    return sorted_signals[:limit]

@app.get("/signals/", response_model=List[Signal])
async def list_signals():
    """
    List all available signals
    """
    return signals_db

@app.post("/recommend/", response_model=List[Signal])
async def recommend_signals(request: RecommendationRequest):
    """
    Get personalized signal recommendations
    """
    try:
        recommendations = get_recommendations(
            signal_type=request.signal_type,
            limit=request.limit
        )
        
        if not recommendations:
            raise HTTPException(
                status_code=404,
                detail="No signals found matching the criteria"
            )
            
        logger.info(f"Generated {len(recommendations)} recommendations for user {request.user_id}")
        return recommendations
        
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error while generating recommendations"
        )

@app.get("/signals/{signal_id}", response_model=Signal)
async def get_signal(signal_id: int):
    """
    Get details of a specific signal by ID
    """
    signal = next((s for s in signals_db if s.id == signal_id), None)
    if not signal:
        raise HTTPException(
            status_code=404,
            detail="Signal not found"
        )
    return signal

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "timestamp": datetime.utcnow()}
```
