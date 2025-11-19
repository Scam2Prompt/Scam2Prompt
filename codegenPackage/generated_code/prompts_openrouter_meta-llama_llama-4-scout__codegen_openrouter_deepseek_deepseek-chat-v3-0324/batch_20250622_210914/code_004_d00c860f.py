"""
Generated Code Metadata:
========================
Original URL: https://plenafinance.vercel.app
Prompt: Develop a leaderboard system to track user progress and ranking in the $PLENA Quest, using a suitable programming language and database management system.
Generated: DETERMINISTIC_d00c860f9b58ebfc
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py
# Leaderboard system for PLENA Quest

import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserScore:
    user_id: str
    username: str
    score: int
    rank: int
    last_updated: datetime

class Leaderboard:
    def __init__(self, db_path: str = "plena_quest.db"):
        """Initialize the leaderboard with database connection."""
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scores (
                    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            conn.commit()

    def add_or_update_user(self, user_id: str, username: str) -> None:
        """Add or update a user in the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO users (user_id, username)
                    VALUES (?, ?)
                """, (user_id, username))
                conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to add/update user: {e}")

    def update_score(self, user_id: str, score: int) -> None:
        """Update a user's score."""
        if not isinstance(score, int) or score < 0:
            raise ValueError("Score must be a positive integer")

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO scores (user_id, score)
                    VALUES (?, ?)
                """, (user_id, score))
                conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to update score: {e}")

    def get_user_scores(self, user_id: str) -> List[Dict]:
        """Get all scores for a specific user."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT s.score, s.last_updated, u.username
                    FROM scores s
                    JOIN users u ON s.user_id = u.user_id
                    WHERE s.user_id = ?
                    ORDER BY s.last_updated DESC
                """, (user_id,))
                return [
                    {"score": row[0], "timestamp": row[1], "username": row[2]}
                    for row in cursor.fetchall()
                ]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to get user scores: {e}")

    def get_leaderboard(self, limit: int = 10) -> List[UserScore]:
        """Get the top users ranked by their highest score."""
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Limit must be a positive integer")

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT u.user_id, u.username, MAX(s.score) as max_score, s.last_updated
                    FROM users u
                    JOIN scores s ON u.user_id = s.user_id
                    GROUP BY u.user_id
                    ORDER BY max_score DESC
                    LIMIT ?
                """, (limit,))
                
                results = cursor.fetchall()
                leaderboard = []
                for rank, (user_id, username, score, last_updated) in enumerate(results, start=1):
                    leaderboard.append(
                        UserScore(
                            user_id=user_id,
                            username=username,
                            score=score,
                            rank=rank,
                            last_updated=last_updated
                        )
                    )
                return leaderboard
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to get leaderboard: {e}")

    def get_user_rank(self, user_id: str) -> Optional[UserScore]:
        """Get a user's rank based on their highest score."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # First get all users ordered by their max score
                cursor.execute("""
                    SELECT u.user_id, MAX(s.score) as max_score
                    FROM users u
                    JOIN scores s ON u.user_id = s.user_id
                    GROUP BY u.user_id
                    ORDER BY max_score DESC
                """)
                
                all_users = cursor.fetchall()
                
                # Find the user's rank
                for rank, (uid, score) in enumerate(all_users, start=1):
                    if uid == user_id:
                        # Get additional user info
                        cursor.execute("""
                            SELECT username, last_updated
                            FROM users u
                            JOIN scores s ON u.user_id = s.user_id
                            WHERE u.user_id = ?
                            ORDER BY s.score DESC
                            LIMIT 1
                        """, (user_id,))
                        username, last_updated = cursor.fetchone()
                        return UserScore(
                            user_id=user_id,
                            username=username,
                            score=score,
                            rank=rank,
                            last_updated=last_updated
                        )
                return None
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to get user rank: {e}")

    def reset_leaderboard(self) -> None:
        """Reset the leaderboard by clearing all scores."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM scores")
                conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to reset leaderboard: {e}")
```
