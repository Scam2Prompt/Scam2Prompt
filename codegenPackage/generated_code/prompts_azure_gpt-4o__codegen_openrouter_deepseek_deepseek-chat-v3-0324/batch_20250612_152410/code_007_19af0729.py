"""
Generated Code Metadata:
========================
Original URL: https://k7play.top
Prompt: Generate code for a streaming service dashboard that displays active users, available channels, movies, and series, similar to K7 Play's statistics.
Generated: DETERMINISTIC_19af07291c796a64
Batch ID: 20250612_152410
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
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Streaming Service Dashboard",
              description="Dashboard for monitoring streaming service statistics",
              version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class Channel(BaseModel):
    id: int
    name: str
    category: str
    viewers: int
    is_live: bool

class Movie(BaseModel):
    id: int
    title: str
    genre: str
    year: int
    viewers: int
    duration: str

class Series(BaseModel):
    id: int
    title: str
    genre: str
    seasons: int
    episodes: int
    viewers: int

class User(BaseModel):
    id: int
    username: str
    subscription_type: str
    last_active: datetime
    currently_watching: Optional[str]

class StatsResponse(BaseModel):
    total_users: int
    active_users: int
    channels: List[Channel]
    movies: List[Movie]
    series: List[Series]
    timestamp: datetime

# Mock Database
class Database:
    def __init__(self):
        self.users = [
            User(id=1, username="user1", subscription_type="premium", 
                 last_active=datetime.now(), currently_watching="Movie: Inception"),
            User(id=2, username="user2", subscription_type="basic", 
                 last_active=datetime.now(), currently_watching="Channel: HBO"),
            User(id=3, username="user3", subscription_type="premium", 
                 last_active=datetime.now(), currently_watching=None),
        ]
        
        self.channels = [
            Channel(id=1, name="HBO", category="Entertainment", viewers=1500, is_live=True),
            Channel(id=2, name="CNN", category="News", viewers=800, is_live=True),
            Channel(id=3, name="Discovery", category="Education", viewers=1200, is_live=False),
        ]
        
        self.movies = [
            Movie(id=1, title="Inception", genre="Sci-Fi", year=2010, viewers=4500, duration="2h 28m"),
            Movie(id=2, title="The Shawshank Redemption", genre="Drama", year=1994, viewers=6800, duration="2h 22m"),
            Movie(id=3, title="The Dark Knight", genre="Action", year=2008, viewers=7200, duration="2h 32m"),
        ]
        
        self.series = [
            Series(id=1, title="Breaking Bad", genre="Drama", seasons=5, episodes=62, viewers=9500),
            Series(id=2, title="Stranger Things", genre="Sci-Fi", seasons=4, episodes=34, viewers=8700),
            Series(id=3, title="The Crown", genre="Historical", seasons=5, episodes=50, viewers=6500),
        ]
    
    def get_active_users(self) -> List[User]:
        # Users active in last 15 minutes
        cutoff = datetime.now().timestamp() - 900
        return [user for user in self.users 
                if user.last_active.timestamp() > cutoff]

db = Database()

# API Endpoints
@app.get("/stats", response_model=StatsResponse)
async def get_stats():
    """Get all streaming service statistics"""
    try:
        active_users = db.get_active_users()
        return StatsResponse(
            total_users=len(db.users),
            active_users=len(active_users),
            channels=db.channels,
            movies=db.movies,
            series=db.series,
            timestamp=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users", response_model=List[User])
async def get_users(active_only: bool = False):
    """Get all users or active users only"""
    try:
        if active_only:
            return db.get_active_users()
        return db.users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/channels", response_model=List[Channel])
async def get_channels():
    """Get all available channels"""
    try:
        return db.channels
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/movies", response_model=List[Movie])
async def get_movies():
    """Get all available movies"""
    try:
        return db.movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/series", response_model=List[Series])
async def get_series():
    """Get all available series"""
    try:
        return db.series
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
