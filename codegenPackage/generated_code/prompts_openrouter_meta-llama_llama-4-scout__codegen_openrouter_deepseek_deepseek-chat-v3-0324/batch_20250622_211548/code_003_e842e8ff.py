"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Design a simple API for a racing game that features unlocking new tracks and achievements, using the gameplay mechanics of Rally Racer Dirt as a reference.
Generated: DETERMINISTIC_e842e8ff198bd3de
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Racing Game API",
    description="API for a racing game featuring tracks and achievements",
    version="1.0.0"
)

# Database simulation (in-memory for simplicity)
tracks_db = {}
achievements_db = {}
players_db = {}

# Models
class Track(BaseModel):
    id: str
    name: str
    description: str
    difficulty: str  # easy, medium, hard
    is_locked: bool
    unlock_condition: Optional[str] = None

class Achievement(BaseModel):
    id: str
    name: str
    description: str
    reward: int  # points or credits
    is_unlocked: bool

class Player(BaseModel):
    id: str
    username: str
    unlocked_tracks: List[str]
    unlocked_achievements: List[str]
    credits: int

# Helper functions
def get_track(track_id: str) -> Track:
    if track_id not in tracks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Track not found"
        )
    return tracks_db[track_id]

def get_achievement(achievement_id: str) -> Achievement:
    if achievement_id not in achievements_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Achievement not found"
        )
    return achievements_db[achievement_id]

def get_player(player_id: str) -> Player:
    if player_id not in players_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    return players_db[player_id]

# API Endpoints
@app.post("/tracks/", response_model=Track, status_code=status.HTTP_201_CREATED)
def create_track(track: Track):
    """Create a new track"""
    if track.id in tracks_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Track with this ID already exists"
        )
    tracks_db[track.id] = track
    return track

@app.get("/tracks/", response_model=List[Track])
def list_tracks():
    """List all available tracks"""
    return list(tracks_db.values())

@app.get("/tracks/{track_id}", response_model=Track)
def get_track_by_id(track_id: str):
    """Get a specific track by ID"""
    return get_track(track_id)

@app.post("/achievements/", response_model=Achievement, status_code=status.HTTP_201_CREATED)
def create_achievement(achievement: Achievement):
    """Create a new achievement"""
    if achievement.id in achievements_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Achievement with this ID already exists"
        )
    achievements_db[achievement.id] = achievement
    return achievement

@app.get("/achievements/", response_model=List[Achievement])
def list_achievements():
    """List all available achievements"""
    return list(achievements_db.values())

@app.post("/players/", response_model=Player, status_code=status.HTTP_201_CREATED)
def create_player(username: str):
    """Create a new player"""
    player_id = str(uuid.uuid4())
    new_player = Player(
        id=player_id,
        username=username,
        unlocked_tracks=[],
        unlocked_achievements=[],
        credits=0
    )
    players_db[player_id] = new_player
    return new_player

@app.get("/players/{player_id}", response_model=Player)
def get_player_by_id(player_id: str):
    """Get player by ID"""
    return get_player(player_id)

@app.post("/players/{player_id}/unlock_track/{track_id}", response_model=Player)
def unlock_track(player_id: str, track_id: str):
    """Unlock a track for a player"""
    player = get_player(player_id)
    track = get_track(track_id)
    
    if track.id in player.unlocked_tracks:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Track already unlocked"
        )
    
    player.unlocked_tracks.append(track.id)
    players_db[player_id] = player
    return player

@app.post("/players/{player_id}/unlock_achievement/{achievement_id}", response_model=Player)
def unlock_achievement(player_id: str, achievement_id: str):
    """Unlock an achievement for a player"""
    player = get_player(player_id)
    achievement = get_achievement(achievement_id)
    
    if achievement.id in player.unlocked_achievements:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Achievement already unlocked"
        )
    
    player.unlocked_achievements.append(achievement.id)
    player.credits += achievement.reward
    players_db[player_id] = player
    return player

@app.get("/players/{player_id}/progress", response_model=dict)
def get_player_progress(player_id: str):
    """Get player progress (tracks and achievements unlocked)"""
    player = get_player(player_id)
    return {
        "unlocked_tracks": len(player.unlocked_tracks),
        "total_tracks": len(tracks_db),
        "unlocked_achievements": len(player.unlocked_achievements),
        "total_achievements": len(achievements_db),
        "credits": player.credits
    }

# Sample data initialization
def initialize_sample_data():
    """Initialize sample data for testing"""
    # Sample tracks
    tracks_db["track1"] = Track(
        id="track1",
        name="Forest Rally",
        description="Race through dense forests with tight turns",
        difficulty="medium",
        is_locked=False
    )
    
    tracks_db["track2"] = Track(
        id="track2",
        name="Mountain Pass",
        description="High altitude racing with steep drops",
        difficulty="hard",
        is_locked=True,
        unlock_condition="Complete Forest Rally 3 times"
    )
    
    # Sample achievements
    achievements_db["ach1"] = Achievement(
        id="ach1",
        name="First Win",
        description="Win your first race",
        reward=100,
        is_unlocked=False
    )
    
    achievements_db["ach2"] = Achievement(
        id="ach2",
        name="Speed Demon",
        description="Complete any track under par time",
        reward=200,
        is_unlocked=False
    )

# Initialize sample data when starting
initialize_sample_data()
```
