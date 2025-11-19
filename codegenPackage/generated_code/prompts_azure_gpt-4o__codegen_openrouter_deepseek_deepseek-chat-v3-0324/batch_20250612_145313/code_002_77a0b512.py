"""
Generated Code Metadata:
========================
Original URL: https://playember-57a.pages.dev
Prompt: Generate code to implement a leaderboard system for a blockchain-based mobile game, considering PlayEmber's experience with hit IP games and global brands.
Generated: DETERMINISTIC_77a0b512b536cdca
Batch ID: 20250612_145313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import redis
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Blockchain Game Leaderboard API",
    description="API for managing leaderboards in a blockchain-based mobile game",
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

# Redis connection pool
redis_pool = redis.ConnectionPool(
    host='redis',
    port=6379,
    db=0,
    decode_responses=True
)

# Models
class PlayerScore(BaseModel):
    player_id: str
    wallet_address: str
    score: int
    timestamp: datetime = None
    
    @validator('score')
    def score_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Score must be positive')
        return v

class LeaderboardEntry(BaseModel):
    rank: int
    player_id: str
    wallet_address: str
    score: int
    timestamp: datetime

class LeaderboardResponse(BaseModel):
    leaderboard_id: str
    entries: List[LeaderboardEntry]
    total_players: int
    time_range: Optional[str] = None

# Helper functions
def get_redis_connection():
    return redis.Redis(connection_pool=redis_pool)

def generate_leaderboard_key(leaderboard_id: str, time_range: str = None) -> str:
    if time_range:
        return f"leaderboard:{leaderboard_id}:{time_range}"
    return f"leaderboard:{leaderboard_id}"

def get_current_time_range() -> str:
    now = datetime.utcnow()
    return now.strftime("%Y-%m-%d")

# API Endpoints
@app.post("/leaderboards/{leaderboard_id}/scores", status_code=status.HTTP_201_CREATED)
async def submit_score(leaderboard_id: str, player_score: PlayerScore):
    """
    Submit a player's score to the leaderboard.
    """
    redis_conn = get_redis_connection()
    
    if not player_score.timestamp:
        player_score.timestamp = datetime.utcnow()
    
    # Store in main leaderboard
    main_key = generate_leaderboard_key(leaderboard_id)
    redis_conn.zadd(main_key, {player_score.player_id: player_score.score})
    
    # Store in daily leaderboard
    daily_key = generate_leaderboard_key(leaderboard_id, get_current_time_range())
    redis_conn.zadd(daily_key, {player_score.player_id: player_score.score})
    
    # Store player metadata
    player_data = {
        "wallet_address": player_score.wallet_address,
        "timestamp": player_score.timestamp.isoformat()
    }
    redis_conn.hset(f"player:{player_score.player_id}", mapping=player_data)
    
    return {"message": "Score submitted successfully"}

@app.get("/leaderboards/{leaderboard_id}", response_model=LeaderboardResponse)
async def get_leaderboard(
    leaderboard_id: str,
    limit: int = 100,
    offset: int = 0,
    time_range: Optional[str] = None
):
    """
    Retrieve leaderboard entries with pagination.
    """
    if limit > 1000 or limit < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Limit must be between 1 and 1000"
        )
    
    redis_conn = get_redis_connection()
    leaderboard_key = generate_leaderboard_key(leaderboard_id, time_range)
    
    if not redis_conn.exists(leaderboard_key):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Leaderboard not found"
        )
    
    # Get total players
    total_players = redis_conn.zcard(leaderboard_key)
    
    # Get ranked entries
    entries = []
    ranked_players = redis_conn.zrevrange(
        leaderboard_key,
        offset,
        offset + limit - 1,
        withscores=True
    )
    
    for rank, (player_id, score) in enumerate(ranked_players, start=offset + 1):
        player_data = redis_conn.hgetall(f"player:{player_id}")
        entries.append(LeaderboardEntry(
            rank=rank,
            player_id=player_id,
            wallet_address=player_data.get("wallet_address", ""),
            score=int(score),
            timestamp=datetime.fromisoformat(player_data.get("timestamp", datetime.utcnow().isoformat()))
        ))
    
    return LeaderboardResponse(
        leaderboard_id=leaderboard_id,
        entries=entries,
        total_players=total_players,
        time_range=time_range
    )

@app.get("/leaderboards/{leaderboard_id}/players/{player_id}", response_model=LeaderboardEntry)
async def get_player_rank(leaderboard_id: str, player_id: str, time_range: Optional[str] = None):
    """
    Get a specific player's rank and score from the leaderboard.
    """
    redis_conn = get_redis_connection()
    leaderboard_key = generate_leaderboard_key(leaderboard_id, time_range)
    
    if not redis_conn.exists(leaderboard_key):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Leaderboard not found"
        )
    
    score = redis_conn.zscore(leaderboard_key, player_id)
    if score is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found in leaderboard"
        )
    
    rank = redis_conn.zrevrank(leaderboard_key, player_id)
    if rank is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found in leaderboard"
        )
    
    player_data = redis_conn.hgetall(f"player:{player_id}")
    
    return LeaderboardEntry(
        rank=rank + 1,
        player_id=player_id,
        wallet_address=player_data.get("wallet_address", ""),
        score=int(score),
        timestamp=datetime.fromisoformat(player_data.get("timestamp", datetime.utcnow().isoformat()))
    )

# Periodic tasks
def cleanup_old_leaderboards():
    """
    Clean up old time-based leaderboards (e.g., daily leaderboards older than 30 days).
    """
    redis_conn = get_redis_connection()
    cutoff_date = datetime.utcnow() - timedelta(days=30)
    
    # Scan for old leaderboards
    for key in redis_conn.scan_iter("leaderboard:*:*"):
        parts = key.split(":")
        if len(parts) == 3:
            try:
                date_part = parts[2]
                leaderboard_date = datetime.strptime(date_part, "%Y-%m-%d")
                if leaderboard_date < cutoff_date:
                    redis_conn.delete(key)
            except ValueError:
                continue

# Startup event
@app.on_event("startup")
async def startup_event():
    # Initialize cleanup task
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(periodic_cleanup())

async def periodic_cleanup():
    import asyncio
    while True:
        cleanup_old_leaderboards()
        await asyncio.sleep(86400)  # Run daily
```
