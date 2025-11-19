"""
Generated Code Metadata:
========================
Original URL: https://ggew.pages.dev
Prompt: Generate code for a leaderboard system that tracks user activity and rewards them with points, as described in Blum's rewarding crypto experience.
Generated: DETERMINISTIC_ce35cfcf5905047d
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class LeaderboardSystem:
    """
    A leaderboard system that tracks user activity and rewards points.
    Supports adding users, recording activities, calculating rewards, and displaying leaderboards.
    """
    
    def __init__(self, db_path: str = "leaderboard.db"):
        """
        Initialize the leaderboard system with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self._initialize_database()
        
    def _initialize_database(self) -> None:
        """Initialize database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Activities table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS activities (
                    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    activity_type TEXT NOT NULL,
                    points_earned INTEGER NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            
            # Points table (denormalized for performance)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_points (
                    user_id TEXT PRIMARY KEY,
                    total_points INTEGER NOT NULL DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            
            conn.commit()
    
    def add_user(self, user_id: str, username: str) -> bool:
        """
        Add a new user to the system.
        
        Args:
            user_id: Unique identifier for the user
            username: Display name for the user
            
        Returns:
            True if user was added successfully, False if user already exists
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (user_id, username) VALUES (?, ?)",
                    (user_id, username)
                )
                cursor.execute(
                    "INSERT INTO user_points (user_id, total_points) VALUES (?, 0)",
                    (user_id,)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def record_activity(self, user_id: str, activity_type: str) -> bool:
        """
        Record a user activity and update their points.
        
        Args:
            user_id: ID of the user performing the activity
            activity_type: Type of activity being performed
            
        Returns:
            True if activity was recorded successfully, False otherwise
        """
        # Define point values for different activities
        activity_points = {
            "login": 10,
            "post": 50,
            "comment": 20,
            "like": 5,
            "share": 30,
            "referral": 100
        }
        
        points = activity_points.get(activity_type.lower(), 0)
        if points == 0:
            return False
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Record the activity
                cursor.execute(
                    """INSERT INTO activities 
                    (user_id, activity_type, points_earned) 
                    VALUES (?, ?, ?)""",
                    (user_id, activity_type, points)
                )
                
                # Update user's total points
                cursor.execute(
                    """UPDATE user_points 
                    SET total_points = total_points + ?, 
                    last_updated = CURRENT_TIMESTAMP 
                    WHERE user_id = ?""",
                    (points, user_id)
                )
                
                conn.commit()
                return True
        except sqlite3.Error:
            return False
    
    def get_user_points(self, user_id: str) -> Optional[int]:
        """
        Get the total points for a user.
        
        Args:
            user_id: ID of the user to query
            
        Returns:
            Total points for the user, or None if user doesn't exist
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT total_points FROM user_points WHERE user_id = ?",
                (user_id,)
            )
            result = cursor.fetchone()
            return result[0] if result else None
    
    def get_leaderboard(self, limit: int = 10) -> List[Tuple[str, str, int]]:
        """
        Get the current leaderboard ranked by total points.
        
        Args:
            limit: Number of top users to return
            
        Returns:
            List of tuples containing (user_id, username, total_points)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.user_id, u.username, up.total_points
                FROM users u
                JOIN user_points up ON u.user_id = up.user_id
                ORDER BY up.total_points DESC
                LIMIT ?
            """, (limit,))
            return cursor.fetchall()
    
    def get_user_activities(self, user_id: str, limit: int = 10) -> List[Tuple[str, int, str]]:
        """
        Get recent activities for a user.
        
        Args:
            user_id: ID of the user to query
            limit: Number of activities to return
            
        Returns:
            List of tuples containing (activity_type, points_earned, timestamp)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT activity_type, points_earned, timestamp
                FROM activities
                WHERE user_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
            """, (user_id, limit))
            return cursor.fetchall()
    
    def get_activity_stats(self) -> Dict[str, int]:
        """
        Get statistics about all activities recorded in the system.
        
        Returns:
            Dictionary mapping activity types to total occurrences
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT activity_type, COUNT(*) as count
                FROM activities
                GROUP BY activity_type
            """)
            return dict(cursor.fetchall())
    
    def reset_leaderboard(self) -> None:
        """
        Reset all points in the system (for testing purposes).
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE user_points SET total_points = 0")
            cursor.execute("DELETE FROM activities")
            conn.commit()
```
