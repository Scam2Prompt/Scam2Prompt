"""
Generated Code Metadata:
========================
Original URL: https://tarileague.pages.dev
Prompt: Design a leaderboard system for the Tari Airdrop Game, tracking user scores and rewards, including gems, turtle shells, and sky hammers.
Generated: DETERMINISTIC_6c5910beecbce3d4
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import uuid
import datetime
import sqlite3
from contextlib import contextmanager

# Database connection manager
@contextmanager
def get_db_connection():
    conn = sqlite3.connect('leaderboard.db')
    try:
        yield conn
    finally:
        conn.close()

# Initialize database tables
def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                score_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                gems INTEGER NOT NULL DEFAULT 0,
                turtle_shells INTEGER NOT NULL DEFAULT 0,
                sky_hammers INTEGER NOT NULL DEFAULT 0,
                last_updated TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        conn.commit()

# Data classes
@dataclass
class User:
    user_id: str
    username: str
    created_at: str

@dataclass
class Score:
    score_id: str
    user_id: str
    gems: int
    turtle_shells: int
    sky_hammers: int
    last_updated: str

class LeaderboardSystem:
    def __init__(self):
        init_db()
    
    def add_user(self, username: str) -> User:
        """Add a new user to the system."""
        user_id = str(uuid.uuid4())
        created_at = datetime.datetime.now().isoformat()
        user = User(user_id, username, created_at)
        
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO users VALUES (?, ?, ?)',
                    (user.user_id, user.username, user.created_at)
                )
                conn.commit()
            return user
        except sqlite3.IntegrityError:
            raise ValueError(f"Username '{username}' already exists")
    
    def get_user(self, username: str) -> Optional[User]:
        """Retrieve a user by username."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT user_id, username, created_at FROM users WHERE username = ?',
                (username,)
            )
            row = cursor.fetchone()
            if row:
                return User(*row)
            return None
    
    def update_score(
        self,
        user_id: str,
        gems: int = 0,
        turtle_shells: int = 0,
        sky_hammers: int = 0
    ) -> Score:
        """Update user's score. Creates score if it doesn't exist."""
        last_updated = datetime.datetime.now().isoformat()
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Check if score exists
            cursor.execute(
                'SELECT score_id FROM scores WHERE user_id = ?',
                (user_id,)
            )
            existing_score = cursor.fetchone()
            
            if existing_score:
                score_id = existing_score[0]
                cursor.execute(
                    '''
                    UPDATE scores SET
                        gems = gems + ?,
                        turtle_shells = turtle_shells + ?,
                        sky_hammers = sky_hammers + ?,
                        last_updated = ?
                    WHERE score_id = ?
                    ''',
                    (gems, turtle_shells, sky_hammers, last_updated, score_id)
                )
            else:
                score_id = str(uuid.uuid4())
                cursor.execute(
                    'INSERT INTO scores VALUES (?, ?, ?, ?, ?, ?)',
                    (score_id, user_id, gems, turtle_shells, sky_hammers, last_updated)
                )
            
            conn.commit()
            
            # Return updated score
            cursor.execute(
                'SELECT * FROM scores WHERE score_id = ?',
                (score_id,)
            )
            return Score(*cursor.fetchone())
    
    def get_leaderboard(
        self,
        limit: int = 10,
        sort_by: str = 'gems'
    ) -> List[Dict]:
        """Get top users sorted by specified metric."""
        valid_sort_columns = {'gems', 'turtle_shells', 'sky_hammers'}
        if sort_by not in valid_sort_columns:
            raise ValueError(f"Invalid sort column. Must be one of {valid_sort_columns}")
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f'''
                SELECT u.username, s.gems, s.turtle_shells, s.sky_hammers
                FROM scores s
                JOIN users u ON s.user_id = u.user_id
                ORDER BY s.{sort_by} DESC
                LIMIT ?
                ''',
                (limit,)
            )
            
            leaderboard = []
            columns = [desc[0] for desc in cursor.description]
            for row in cursor.fetchall():
                leaderboard.append(dict(zip(columns, row)))
            
            return leaderboard
    
    def get_user_score(self, user_id: str) -> Optional[Score]:
        """Get a user's score by user_id."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM scores WHERE user_id = ?',
                (user_id,)
            )
            row = cursor.fetchone()
            if row:
                return Score(*row)
            return None
    
    def reset_leaderboard(self):
        """Reset all scores (for testing purposes)."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM scores')
            cursor.execute('DELETE FROM users')
            conn.commit()

# Example usage
if __name__ == '__main__':
    leaderboard = LeaderboardSystem()
    
    # Add some users
    try:
        user1 = leaderboard.add_user("player1")
        user2 = leaderboard.add_user("player2")
        user3 = leaderboard.add_user("player3")
    except ValueError as e:
        print(f"Error adding user: {e}")
    
    # Update scores
    leaderboard.update_score(user1.user_id, gems=100, turtle_shells=5, sky_hammers=2)
    leaderboard.update_score(user2.user_id, gems=150, turtle_shells=3, sky_hammers=1)
    leaderboard.update_score(user3.user_id, gems=75, turtle_shells=7, sky_hammers=3)
    
    # Get leaderboard
    print("Top players by gems:")
    for player in leaderboard.get_leaderboard(sort_by='gems'):
        print(json.dumps(player, indent=2))
```
