"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Generate code for a game leaderboard system that tracks player scores and supports social interaction features, as described in SCATTER HITAM.
Generated: DETERMINISTIC_546efc3b07cf2b39
Batch ID: 20250612_151525
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
from datetime import datetime
from typing import List, Dict, Optional
import uuid
import sqlite3
from sqlite3 import Error

# Database setup and connection
class Database:
    def __init__(self, db_file: str = "leaderboard.db"):
        """Initialize database connection."""
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            self._create_tables()
        except Error as e:
            print(f"Database error: {e}")

    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        sql_players = """
        CREATE TABLE IF NOT EXISTS players (
            player_id TEXT PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            email TEXT UNIQUE,
            created_at TEXT NOT NULL
        );
        """
        
        sql_scores = """
        CREATE TABLE IF NOT EXISTS scores (
            score_id TEXT PRIMARY KEY,
            player_id TEXT NOT NULL,
            score INTEGER NOT NULL,
            game_mode TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players (player_id)
        );
        """
        
        sql_friends = """
        CREATE TABLE IF NOT EXISTS friends (
            relationship_id TEXT PRIMARY KEY,
            player_id TEXT NOT NULL,
            friend_id TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players (player_id),
            FOREIGN KEY (friend_id) REFERENCES players (player_id),
            UNIQUE(player_id, friend_id)
        );
        """
        
        sql_messages = """
        CREATE TABLE IF NOT EXISTS messages (
            message_id TEXT PRIMARY KEY,
            sender_id TEXT NOT NULL,
            receiver_id TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            is_read INTEGER DEFAULT 0,
            FOREIGN KEY (sender_id) REFERENCES players (player_id),
            FOREIGN KEY (receiver_id) REFERENCES players (player_id)
        );
        """
        
        cursor = self.conn.cursor()
        cursor.execute(sql_players)
        cursor.execute(sql_scores)
        cursor.execute(sql_friends)
        cursor.execute(sql_messages)
        self.conn.commit()

    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()

# Player model
class Player:
    def __init__(self, username: str, email: Optional[str] = None):
        self.player_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {
            "player_id": self.player_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at
        }

# Score model
class Score:
    def __init__(self, player_id: str, score: int, game_mode: str):
        self.score_id = str(uuid.uuid4())
        self.player_id = player_id
        self.score = score
        self.game_mode = game_mode
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {
            "score_id": self.score_id,
            "player_id": self.player_id,
            "score": self.score,
            "game_mode": self.game_mode,
            "timestamp": self.timestamp
        }

# Friend relationship model
class FriendRelationship:
    def __init__(self, player_id: str, friend_id: str, status: str = "pending"):
        self.relationship_id = str(uuid.uuid4())
        self.player_id = player_id
        self.friend_id = friend_id
        self.status = status  # pending, accepted, rejected
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {
            "relationship_id": self.relationship_id,
            "player_id": self.player_id,
            "friend_id": self.friend_id,
            "status": self.status,
            "created_at": self.created_at
        }

# Message model
class Message:
    def __init__(self, sender_id: str, receiver_id: str, content: str):
        self.message_id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = datetime.now().isoformat()
        self.is_read = False

    def to_dict(self) -> Dict:
        return {
            "message_id": self.message_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "content": self.content,
            "timestamp": self.timestamp,
            "is_read": self.is_read
        }

# Leaderboard system
class LeaderboardSystem:
    def __init__(self):
        self.db = Database()
    
    def __del__(self):
        self.db.close()

    def register_player(self, username: str, email: Optional[str] = None) -> Optional[Player]:
        """Register a new player."""
        player = Player(username, email)
        try:
            cursor = self.db.conn.cursor()
            cursor.execute(
                "INSERT INTO players VALUES (?, ?, ?, ?)",
                (player.player_id, player.username, player.email, player.created_at)
            )
            self.db.conn.commit()
            return player
        except Error as e:
            print(f"Error registering player: {e}")
            return None

    def submit_score(self, player_id: str, score: int, game_mode: str) -> Optional[Score]:
        """Submit a new score for a player."""
        score_obj = Score(player_id, score, game_mode)
        try:
            cursor = self.db.conn.cursor()
            cursor.execute(
                "INSERT INTO scores VALUES (?, ?, ?, ?, ?)",
                (score_obj.score_id, score_obj.player_id, score_obj.score, 
                 score_obj.game_mode, score_obj.timestamp)
            )
            self.db.conn.commit()
            return score_obj
        except Error as e:
            print(f"Error submitting score: {e}")
            return None

    def get_leaderboard(self, game_mode: str, limit: int = 10) -> List[Dict]:
        """Get top scores for a game mode."""
        try:
            cursor = self.db.conn.cursor()
            cursor.execute(
                """
                SELECT p.username, s.score, s.timestamp 
                FROM scores s
                JOIN players p ON s.player_id = p.player_id
                WHERE s.game_mode = ?
                ORDER BY s.score DESC
                LIMIT ?
                """,
                (game_mode, limit)
            )
            rows = cursor.fetchall()
            return [{"username": row[0], "score": row[1], "timestamp": row[2]} for row in rows]
        except Error as e:
            print(f"Error getting leaderboard: {e}")
            return []

    def send_friend_request(self, player_id: str, friend_username: str) -> Optional[FriendRelationship]:
        """Send a friend request to another player."""
        try:
            cursor = self.db.conn.cursor()
            
            # Get friend's player_id
            cursor.execute("SELECT player_id FROM players WHERE username = ?", (friend_username,))
            friend_row = cursor.fetchone()
            if not friend_row:
                return None
            
            friend_id = friend_row[0]
            
            # Check if relationship already exists
            cursor.execute(
                "SELECT * FROM friends WHERE player_id = ? AND friend_id = ?",
                (player_id, friend_id)
            )
            if cursor.fetchone():
                return None
            
            # Create new relationship
            relationship = FriendRelationship(player_id, friend_id)
            cursor.execute(
                "INSERT INTO friends VALUES (?, ?, ?, ?, ?)",
                (relationship.relationship_id, relationship.player_id, 
                 relationship.friend_id, relationship.status, relationship.created_at)
            )
            
            # Create reciprocal relationship
            reciprocal = FriendRelationship(friend_id, player_id, "pending")
            cursor.execute(
                "INSERT INTO friends VALUES (?, ?, ?, ?, ?)",
                (reciprocal.relationship_id, reciprocal.player_id, 
                 reciprocal.friend_id, reciprocal.status, reciprocal.created_at)
            )
            
            self.db.conn.commit()
            return relationship
        except Error as e:
            print(f"Error sending friend request: {e}")
            return None

    def accept_friend_request(self, player_id: str, friend_id: str) -> bool:
        """Accept a friend request."""
        try:
            cursor = self.db.conn.cursor()
            
            # Update both relationships
            cursor.execute(
                "UPDATE friends SET status = 'accepted' WHERE player_id = ? AND friend_id = ?",
                (player_id, friend_id)
            )
            cursor.execute(
                "UPDATE friends SET status = 'accepted' WHERE player_id = ? AND friend_id = ?",
                (friend_id, player_id)
            )
            
            self.db.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error accepting friend request: {e}")
            return False

    def get_friends(self, player_id: str) -> List[Dict]:
        """Get list of friends for a player."""
        try:
            cursor = self.db.conn.cursor()
