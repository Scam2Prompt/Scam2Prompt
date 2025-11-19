"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Write code to implement a leaderboard system for competitive games like "Bắn Cá" or "Nổ Hũ," inspired by the features on S666.
Generated: DETERMINISTIC_26eff32fdf09d700
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from datetime import datetime, timedelta

# Initialize FastAPI app
app = FastAPI(title="Game Leaderboard API", version="1.0.0")

# Redis connection
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

# Models
class PlayerScore(BaseModel):
    player_id: str
    score: int
    timestamp: Optional[float] = None

    @validator('score')
    def score_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Score must be positive')
        return v

class LeaderboardResponse(BaseModel):
    player_id: str
    score: int
    rank: int

# Constants
LEADERBOARD_EXPIRE_DAYS = 30
SCORE_PRECISION = 1000

# Helper functions
def get_leaderboard_key(game_id: str, date: str) -> str:
    return f"leaderboard:{game_id}:{date}"

def get_current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")

def get_previous_dates(days: int) -> List[str]:
    return [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") 
            for i in range(days)]

def round_score(score: int) -> int:
    return (score // SCORE_PRECISION) * SCORE_PRECISION

# API Endpoints
@app.post("/{game_id}/submit_score", response_model=LeaderboardResponse)
async def submit_score(game_id: str, player_score: PlayerScore):
    """Submit a player's score to the leaderboard"""
    try:
        date = get_current_date()
        key = get_leaderboard_key(game_id, date)
        
        # Set timestamp if not provided
        if player_score.timestamp is None:
            player_score.timestamp = time.time()
        
        rounded_score = round_score(player_score.score)
        
        # Add to sorted set with timestamp as tie-breaker
        redis_client.zadd(
            key,
            {player_score.player_id: f"{rounded_score}.{player_score.timestamp}"}
        )
        
        # Set expiration for the key
        redis_client.expire(key, LEADERBOARD_EXPIRE_DAYS * 24 * 3600)
        
        # Get player's rank
        rank = redis_client.zrevrank(key, player_score.player_id)
        
        return LeaderboardResponse(
            player_id=player_score.player_id,
            score=rounded_score,
            rank=rank + 1 if rank is not None else 0
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/{game_id}/leaderboard", response_model=List[LeaderboardResponse])
async def get_leaderboard(
    game_id: str, 
    date: Optional[str] = None, 
    limit: int = 100
):
    """Get the leaderboard for a specific game and date"""
    try:
        if date is None:
            date = get_current_date()
            
        key = get_leaderboard_key(game_id, date)
        
        # Get top players with scores
        leaderboard = redis_client.zrevrange(
            key, 0, limit - 1, withscores=True
        )
        
        response = []
        for rank, (player_id, score_data) in enumerate(leaderboard, start=1):
            # Extract the rounded score (before the decimal)
            score = int(float(score_data))
            response.append(LeaderboardResponse(
                player_id=player_id,
                score=score,
                rank=rank
            ))
            
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/{game_id}/player_rank", response_model=LeaderboardResponse)
async def get_player_rank(
    game_id: str, 
    player_id: str, 
    date: Optional[str] = None
):
    """Get a player's rank and score for a specific game and date"""
    try:
        if date is None:
            date = get_current_date()
            
        key = get_leaderboard_key(game_id, date)
        
        # Get player's score
        score_data = redis_client.zscore(key, player_id)
        if score_data is None:
            raise HTTPException(status_code=404, detail="Player not found")
        
        # Get player's rank
        rank = redis_client.zrevrank(key, player_id)
        if rank is None:
            raise HTTPException(status_code=404, detail="Player not found")
        
        # Extract the rounded score (before the decimal)
        score = int(float(score_data))
        
        return LeaderboardResponse(
            player_id=player_id,
            score=score,
            rank=rank + 1
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/{game_id}/weekly_leaderboard", response_model=Dict[str, List[LeaderboardResponse]])
async def get_weekly_leaderboard(game_id: str, limit: int = 100):
    """Get weekly leaderboards for the past 7 days"""
    try:
        dates = get_previous_dates(7)
        response = {}
        
        for date in dates:
            key = get_leaderboard_key(game_id, date)
            leaderboard = redis_client.zrevrange(
                key, 0, limit - 1, withscores=True
            )
            
            daily_leaderboard = []
            for rank, (player_id, score_data) in enumerate(leaderboard, start=1):
                score = int(float(score_data))
                daily_leaderboard.append(LeaderboardResponse(
                    player_id=player_id,
                    score=score,
                    rank=rank
                ))
            
            response[date] = daily_leaderboard
            
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/{game_id}/top_players", response_model=List[LeaderboardResponse])
async def get_top_players(game_id: str, days: int = 7, limit: int = 100):
    """Get top players across multiple days"""
    try:
        if days < 1 or days > 30:
            raise HTTPException(
                status_code=400, 
                detail="Days must be between 1 and 30"
            )
            
        dates = get_previous_dates(days)
        player_scores = defaultdict(int)
        
        # Aggregate scores across all specified days
        for date in dates:
            key = get_leaderboard_key(game_id, date)
            leaderboard = redis_client.zrevrange(
                key, 0, -1, withscores=True
            )
            
            for player_id, score_data in leaderboard:
                score = int(float(score_data))
                player_scores[player_id] += score
        
        # Sort players by aggregated score
        sorted_players = sorted(
            player_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]
        
        # Prepare response
        response = []
        for rank, (player_id, score) in enumerate(sorted_players, start=1):
            response.append(LeaderboardResponse(
                player_id=player_id,
                score=score,
                rank=rank
            ))
            
        return response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
