"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braindom.xyz
Prompt: Recommend tools or libraries for creating a mobile-friendly brain teaser game like Braindom, with features for tracking player progress and cognitive skill improvement.
Generated: DETERMINISTIC_577931bc7df632da
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is a Python-based example for creating a mobile-friendly game backend using FastAPI and SQLite. It tracks player progress and cognitive skill improvement. This can serve as the backend API for your brain teaser game.

```python
# Import required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from contextlib import closing

# Initialize the FastAPI app
app = FastAPI()

# Database setup: Create SQLite database for player progress and cognitive skill tracking
DB_NAME = "game.db"

def init_db():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        with conn.cursor() as cursor:
            # Create player table if it doesn't exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER DEFAULT 0,
                cognitive_skills TEXT DEFAULT '[]'
            )
            """)
            conn.commit()

init_db()

# Define Pydantic models for API requests and responses
class Player(BaseModel):
    id: Optional[int] = None
    name: str
    score: int = 0
    cognitive_skills: List[str] = []

class UpdateScore(BaseModel):
    score: int

class UpdateSkills(BaseModel):
    cognitive_skills: List[str]

# API endpoint to create a new player
@app.post("/players/", response_model=Player)
def create_player(player: Player):
    try:
        with closing(sqlite3.connect(DB_NAME)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO players (name, score, cognitive_skills)
                VALUES (?, ?, ?)
                """, (player.name, player.score, str(player.cognitive_skills)))
                conn.commit()
                player_id = cursor.lastrowid
                return {**player.dict(), "id": player_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating player: {str(e)}")

# API endpoint to get all players
@app.get("/players/", response_model=List[Player])
def get_players():
    try:
        with closing(sqlite3.connect(DB_NAME)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, score, cognitive_skills FROM players")
                players = cursor.fetchall()
                return [
                    Player(
                        id=row[0],
                        name=row[1],
                        score=row[2],
                        cognitive_skills=eval(row[3])  # Convert stored JSON-like string to list
                    )
                    for row in players
                ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching players: {str(e)}")

# API endpoint to update player score
@app.put("/players/{player_id}/score", response_model=Player)
def update_score(player_id: int, update: UpdateScore):
    try:
        with closing(sqlite3.connect(DB_NAME)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM players WHERE id = ?", (player_id,))
                player = cursor.fetchone()
                if not player:
                    raise HTTPException(status_code=404, detail="Player not found")
                
                new_score = update.score
                cursor.execute("UPDATE players SET score = ? WHERE id = ?", (new_score, player_id))
                conn.commit()
                return Player(
                    id=player_id,
                    name=player[1],
                    score=new_score,
                    cognitive_skills=eval(player[3])
                )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating score: {str(e)}")

# API endpoint to update cognitive skills
@app.put("/players/{player_id}/skills", response_model=Player)
def update_skills(player_id: int, update: UpdateSkills):
    try:
        with closing(sqlite3.connect(DB_NAME)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM players WHERE id = ?", (player_id,))
                player = cursor.fetchone()
                if not player:
                    raise HTTPException(status_code=404, detail="Player not found")
                
                new_skills = update.cognitive_skills
                cursor.execute("UPDATE players SET cognitive_skills = ? WHERE id = ?", (str(new_skills), player_id))
                conn.commit()
                return Player(
                    id=player_id,
                    name=player[1],
                    score=player[2],
                    cognitive_skills=new_skills
                )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating cognitive skills: {str(e)}")

# API endpoint to delete a player
@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    try:
        with closing(sqlite3.connect(DB_NAME)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM players WHERE id = ?", (player_id,))
                player = cursor.fetchone()
                if not player:
                    raise HTTPException(status_code=404, detail="Player not found")
                
                cursor.execute("DELETE FROM players WHERE id = ?", (player_id,))
                conn.commit()
                return {"detail": "Player deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting player: {str(e)}")
```

This code provides the backend API for managing players, scores, and skills. You can integrate this API with a mobile front-end built using frameworks like React Native, Flutter, or Swift (for iOS). Use this backend to store and retrieve player data, enabling features like progress tracking and cognitive skill improvement.
