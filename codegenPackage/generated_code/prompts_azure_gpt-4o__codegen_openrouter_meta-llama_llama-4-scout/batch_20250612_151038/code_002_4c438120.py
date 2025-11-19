"""
Generated Code Metadata:
========================
Original URL: https://pacmoon-8ko.pages.dev
Prompt: Create a leaderboard system for tracking user activity in a cryptocurrency community, inspired by the "Pacmoon" leaderboard feature.
Generated: DETERMINISTIC_4c438120f48f220e
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Leaderboard System for Cryptocurrency Community**
=====================================================

**leaderboard.py**
```python
import datetime
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User:
    """Represents a user in the leaderboard."""
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.score = 0
        self.last_active = datetime.datetime.now()

    def update_score(self, score_change: int):
        """Updates the user's score."""
        self.score += score_change

    def update_last_active(self):
        """Updates the user's last active timestamp."""
        self.last_active = datetime.datetime.now()

class Leaderboard:
    """Manages the leaderboard data."""
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add_user(self, user_id: int, username: str):
        """Adds a new user to the leaderboard."""
        if user_id in self.users:
            logger.warning(f"User with ID {user_id} already exists.")
            return
        self.users[user_id] = User(user_id, username)

    def update_user_score(self, user_id: int, score_change: int):
        """Updates a user's score."""
        if user_id not in self.users:
            logger.error(f"User with ID {user_id} does not exist.")
            return
        self.users[user_id].update_score(score_change)

    def update_user_last_active(self, user_id: int):
        """Updates a user's last active timestamp."""
        if user_id not in self.users:
            logger.error(f"User with ID {user_id} does not exist.")
            return
        self.users[user_id].update_last_active()

    def get_leaderboard(self, limit: int = 10) -> List[Dict]:
        """Returns the leaderboard data, sorted by score."""
        sorted_users = sorted(self.users.values(), key=lambda x: x.score, reverse=True)
        leaderboard_data = []
        for user in sorted_users[:limit]:
            leaderboard_data.append({
                "user_id": user.user_id,
                "username": user.username,
                "score": user.score,
                "last_active": user.last_active.isoformat()
            })
        return leaderboard_data

def main():
    leaderboard = Leaderboard()

    # Example usage:
    leaderboard.add_user(1, "user1")
    leaderboard.add_user(2, "user2")

    leaderboard.update_user_score(1, 100)
    leaderboard.update_user_score(2, 50)

    leaderboard.update_user_last_active(1)

    print(leaderboard.get_leaderboard())

if __name__ == "__main__":
    main()
```

**database.py**
```python
import sqlite3
from typing import Dict, List

class Database:
    """Manages the leaderboard data in a SQLite database."""
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the leaderboard table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS leaderboard (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                score INTEGER DEFAULT 0,
                last_active TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.conn.commit()

    def add_user(self, user_id: int, username: str):
        """Adds a new user to the leaderboard."""
        self.cursor.execute("INSERT INTO leaderboard (user_id, username) VALUES (?, ?);", (user_id, username))
        self.conn.commit()

    def update_user_score(self, user_id: int, score_change: int):
        """Updates a user's score."""
        self.cursor.execute("UPDATE leaderboard SET score = score + ? WHERE user_id = ?;", (score_change, user_id))
        self.conn.commit()

    def update_user_last_active(self, user_id: int):
        """Updates a user's last active timestamp."""
        self.cursor.execute("UPDATE leaderboard SET last_active = CURRENT_TIMESTAMP WHERE user_id = ?;", (user_id,))
        self.conn.commit()

    def get_leaderboard(self, limit: int = 10) -> List[Dict]:
        """Returns the leaderboard data, sorted by score."""
        self.cursor.execute("""
            SELECT user_id, username, score, last_active
            FROM leaderboard
            ORDER BY score DESC
            LIMIT ?;
        """, (limit,))
        rows = self.cursor.fetchall()
        leaderboard_data = []
        for row in rows:
            leaderboard_data.append({
                "user_id": row[0],
                "username": row[1],
                "score": row[2],
                "last_active": row[3]
            })
        return leaderboard_data

    def close(self):
        """Closes the database connection."""
        self.conn.close()

def main():
    db = Database("leaderboard.db")

    # Example usage:
    db.add_user(1, "user1")
    db.add_user(2, "user2")

    db.update_user_score(1, 100)
    db.update_user_score(2, 50)

    db.update_user_last_active(1)

    print(db.get_leaderboard())

    db.close()

if __name__ == "__main__":
    main()
```

**leaderboard_api.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from leaderboard import Leaderboard
from database import Database

app = FastAPI()

class UserRequest(BaseModel):
    user_id: int
    username: str

class ScoreRequest(BaseModel):
    user_id: int
    score_change: int

leaderboard = Leaderboard()
db = Database("leaderboard.db")

@app.post("/users/")
async def create_user(user: UserRequest):
    leaderboard.add_user(user.user_id, user.username)
    db.add_user(user.user_id, user.username)
    return {"message": "User created"}

@app.post("/users/{user_id}/score")
async def update_user_score(user_id: int, score_request: ScoreRequest):
    leaderboard.update_user_score(user_id, score_request.score_change)
    db.update_user_score(user_id, score_request.score_change)
    return {"message": "Score updated"}

@app.get("/leaderboard/")
async def get_leaderboard(limit: int = 10):
    leaderboard_data = leaderboard.get_leaderboard(limit)
    return leaderboard_data

@app.get("/leaderboard/db/")
async def get_leaderboard_db(limit: int = 10):
    leaderboard_data = db.get_leaderboard(limit)
    return leaderboard_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
