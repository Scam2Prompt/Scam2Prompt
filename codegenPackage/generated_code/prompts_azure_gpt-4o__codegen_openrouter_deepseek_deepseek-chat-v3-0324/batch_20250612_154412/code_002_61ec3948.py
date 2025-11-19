"""
Generated Code Metadata:
========================
Original URL: https://jups.io
Prompt: Develop a leaderboard system for tracking top players in a crypto-based casino platform, inspired by the leaderboard functionality on Jups.io.
Generated: DETERMINISTIC_61ec3948bf055cc4
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Redis configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None  # Set in production

# Leaderboard constants
LEADERBOARD_KEY = "crypto_casino:leaderboard"
DAILY_LEADERBOARD_KEY = "crypto_casino:daily_leaderboard:{date}"
WEEKLY_LEADERBOARD_KEY = "crypto_casino:weekly_leaderboard:{week}"
ALL_TIME_LEADERBOARD_KEY = "crypto_casino:all_time_leaderboard"
TOP_PLAYERS_LIMIT = 100

# Models
class PlayerScore(BaseModel):
    player_id: str
    username: str
    score: float
    wallet_address: Optional[str] = None
    games_played: int = 0

    @validator('score')
    def score_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Score must be positive')
        return v

class LeaderboardResponse(BaseModel):
    leaderboard_type: str
    players: List[PlayerScore]
    updated_at: datetime

# Initialize Redis connection
try:
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
    redis_client.ping()  # Test connection
except redis.ConnectionError as e:
    logger.error(f"Failed to connect to Redis: {e}")
    raise

# Initialize FastAPI
app = FastAPI(
    title="Crypto Casino Leaderboard API",
    description="API for managing and retrieving leaderboard data for a crypto casino platform",
    version="1.0.0"
)

def get_current_date_key() -> str:
    """Get current date formatted as YYYY-MM-DD for daily leaderboard key."""
    return datetime.now().strftime("%Y-%m-%d")

def get_current_week_key() -> str:
    """Get current week formatted as YYYY-WW for weekly leaderboard key."""
    return datetime.now().strftime("%Y-%W")

def update_player_score(player: PlayerScore, leaderboard_key: str) -> None:
    """Update player score in the specified leaderboard."""
    try:
        player_data = json.dumps({
            "username": player.username,
            "wallet_address": player.wallet_address,
            "games_played": player.games_played
        })
        
        # Use Redis pipeline for atomic operations
        pipeline = redis_client.pipeline()
        pipeline.zadd(leaderboard_key, {player.player_id: player.score})
        pipeline.hset(f"{leaderboard_key}:metadata", player.player_id, player_data)
        pipeline.execute()
    except redis.RedisError as e:
        logger.error(f"Error updating player score: {e}")
        raise HTTPException(status_code=500, detail="Failed to update leaderboard")

def get_leaderboard(leaderboard_key: str, limit: int = TOP_PLAYERS_LIMIT) -> List[PlayerScore]:
    """Retrieve top players from a leaderboard."""
    try:
        # Get top player IDs with scores
        player_ids_with_scores = redis_client.zrevrange(
            leaderboard_key, 0, limit - 1, withscores=True
        )
        
        if not player_ids_with_scores:
            return []
        
        # Get player metadata
        player_ids = [player_id for player_id, _ in player_ids_with_scores]
        metadata = redis_client.hmget(f"{leaderboard_key}:metadata", player_ids)
        
        players = []
        for (player_id, score), meta in zip(player_ids_with_scores, metadata):
            if not meta:
                continue
                
            meta_data = json.loads(meta)
            players.append(PlayerScore(
                player_id=player_id,
                username=meta_data["username"],
                wallet_address=meta_data.get("wallet_address"),
                score=score,
                games_played=meta_data.get("games_played", 0)
            ))
        
        return players
    except redis.RedisError as e:
        logger.error(f"Error retrieving leaderboard: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve leaderboard")

@app.post("/update_score/", response_model=PlayerScore)
async def update_score(player: PlayerScore):
    """Update a player's score across all relevant leaderboards."""
    try:
        # Update all leaderboards
        update_player_score(player, ALL_TIME_LEADERBOARD_KEY)
        update_player_score(player, DAILY_LEADERBOARD_KEY.format(date=get_current_date_key()))
        update_player_score(player, WEEKLY_LEADERBOARD_KEY.format(week=get_current_week_key()))
        
        return player
    except Exception as e:
        logger.error(f"Error in update_score: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/leaderboard/all_time/", response_model=LeaderboardResponse)
async def get_all_time_leaderboard(limit: int = TOP_PLAYERS_LIMIT):
    """Get all-time leaderboard."""
    try:
        players = get_leaderboard(ALL_TIME_LEADERBOARD_KEY, limit)
        return LeaderboardResponse(
            leaderboard_type="all_time",
            players=players,
            updated_at=datetime.now()
        )
    except Exception as e:
        logger.error(f"Error in get_all_time_leaderboard: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/leaderboard/daily/", response_model=LeaderboardResponse)
async def get_daily_leaderboard(limit: int = TOP_PLAYERS_LIMIT):
    """Get daily leaderboard."""
    try:
        players = get_leaderboard(
            DAILY_LEADERBOARD_KEY.format(date=get_current_date_key()),
            limit
        )
        return LeaderboardResponse(
            leaderboard_type="daily",
            players=players,
            updated_at=datetime.now()
        )
    except Exception as e:
        logger.error(f"Error in get_daily_leaderboard: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/leaderboard/weekly/", response_model=LeaderboardResponse)
async def get_weekly_leaderboard(limit: int = TOP_PLAYERS_LIMIT):
    """Get weekly leaderboard."""
    try:
        players = get_leaderboard(
            WEEKLY_LEADERBOARD_KEY.format(week=get_current_week_key()),
            limit
        )
        return LeaderboardResponse(
            leaderboard_type="weekly",
            players=players,
            updated_at=datetime.now()
        )
    except Exception as e:
        logger.error(f"Error in get_weekly_leaderboard: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/{player_id}/", response_model=PlayerScore)
async def get_player_stats(player_id: str):
    """Get a player's stats across all leaderboards."""
    try:
        # Get all-time score
        score = redis_client.zscore(ALL_TIME_LEADERBOARD_KEY, player_id)
        if score is None:
            raise HTTPException(status_code=404, detail="Player not found")
        
        # Get metadata
        meta = redis_client.hget(f"{ALL_TIME_LEADERBOARD_KEY}:metadata", player_id)
        if not meta:
            raise HTTPException(status_code=404, detail="Player metadata not found")
            
        meta_data = json.loads(meta)
        
        return PlayerScore(
            player_id=player_id,
            username=meta_data["username"],
            wallet_address=meta_data.get("wallet_address"),
            score=score,
            games_played=meta_data.get("games_played", 0)
        )
    except Exception as e:
        logger.error(f"Error in get_player_stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def initialize_leaderboards():
    """Initialize leaderboard keys with appropriate TTLs."""
    try:
        # Set TTL for daily leaderboard (2 days to handle timezone differences)
        daily_key = DAILY_LEADERBOARD_KEY.format(date=get_current_date_key())
        redis_client.expire(daily_key, timedelta(days=2))
        
        # Set TTL for weekly leaderboard (10 days to handle week transitions)
        weekly_key = WEEKLY_LEADERBOARD_KEY.format(week=get_current_week_key())
        redis_client.expire(weekly_key, timedelta(days=10))
    except redis.RedisError as e:
        logger.error(f"Error initializing leaderboards: {e}")

# Initialize leaderboards on startup
initialize_leaderboards()
```
