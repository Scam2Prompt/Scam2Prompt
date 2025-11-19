"""
Generated Code Metadata:
========================
Original URL: https://tronofficial.com
Prompt: Develop an API that provides real-time data on online betting odds, inspired by the information about online gambling practices found on tronofficial.com.
Generated: DETERMINISTIC_2fcb45bc4bfb6fb1
Batch ID: 20250612_164245
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
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from typing import List, Optional
import httpx
from cachetools import TTLCache

app = FastAPI(
    title="Real-Time Betting Odds API",
    description="API providing real-time data on online betting odds",
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

# Cache configuration (5 minutes TTL)
odds_cache = TTLCache(maxsize=1000, ttl=300)

# Models
class Odds(BaseModel):
    event_id: str
    event_name: str
    sport: str
    start_time: datetime
    home_team: str
    away_team: str
    home_odds: float
    draw_odds: Optional[float] = None
    away_odds: float
    provider: str
    last_updated: datetime

    @validator('home_odds', 'away_odds', 'draw_odds')
    def odds_must_be_positive(cls, v):
        if v is not None and v <= 1:
            raise ValueError('Odds must be greater than 1')
        return v

class OddsResponse(BaseModel):
    success: bool
    data: List[Odds]
    timestamp: datetime
    count: int

# Mock data provider (in production, replace with actual API calls)
async def fetch_odds_from_provider(sport: Optional[str] = None):
    # Simulate API delay
    await asyncio.sleep(0.1)
    
    mock_data = [
        {
            "event_id": "epl-123",
            "event_name": "Premier League: Man Utd vs Liverpool",
            "sport": "football",
            "start_time": "2023-12-15T20:00:00",
            "home_team": "Manchester United",
            "away_team": "Liverpool",
            "home_odds": 2.5,
            "draw_odds": 3.2,
            "away_odds": 2.8,
            "provider": "Bet365",
            "last_updated": datetime.utcnow().isoformat()
        },
        {
            "event_id": "nba-456",
            "event_name": "NBA: Lakers vs Warriors",
            "sport": "basketball",
            "start_time": "2023-12-16T03:30:00",
            "home_team": "LA Lakers",
            "away_team": "Golden State Warriors",
            "home_odds": 1.9,
            "away_odds": 1.95,
            "provider": "DraftKings",
            "last_updated": datetime.utcnow().isoformat()
        }
    ]
    
    if sport:
        return [item for item in mock_data if item['sport'] == sport]
    return mock_data

# API Endpoints
@app.get("/odds", response_model=OddsResponse)
async def get_odds(
    sport: Optional[str] = Query(None, description="Filter by sport type"),
    provider: Optional[str] = Query(None, description="Filter by odds provider")
):
    """
    Get current betting odds for all or filtered events
    """
    try:
        cache_key = f"odds_{sport or 'all'}_{provider or 'all'}"
        
        if cache_key in odds_cache:
            return odds_cache[cache_key]
            
        data = await fetch_odds_from_provider(sport)
        
        if provider:
            data = [item for item in data if item['provider'].lower() == provider.lower()]
        
        response = {
            "success": True,
            "data": data,
            "timestamp": datetime.utcnow(),
            "count": len(data)
        }
        
        odds_cache[cache_key] = response
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching odds data: {str(e)}"
        )

@app.get("/odds/{event_id}", response_model=OddsResponse)
async def get_odds_by_event(event_id: str):
    """
    Get betting odds for a specific event by ID
    """
    try:
        cache_key = f"odds_{event_id}"
        
        if cache_key in odds_cache:
            return odds_cache[cache_key]
            
        data = await fetch_odds_from_provider()
        event_data = [item for item in data if item['event_id'] == event_id]
        
        if not event_data:
            raise HTTPException(
                status_code=404,
                detail="Event not found"
            )
            
        response = {
            "success": True,
            "data": event_data,
            "timestamp": datetime.utcnow(),
            "count": len(event_data)
        }
        
        odds_cache[cache_key] = response
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching event odds: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "timestamp": datetime.utcnow()}

if __name__ == "__main__":
    import uvicorn
    import asyncio
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
