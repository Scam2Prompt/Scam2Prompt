"""
Generated Code Metadata:
========================
Original URL: https://www.cosmicrewards.com
Prompt: Generate code for a leaderboard system that tracks user interaction time and rewards accumulation, similar to Cosmic Rewards' "play longer, earn more Stardust" feature.
Generated: DETERMINISTIC_3f5e216401f1c324
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
import sqlite3
from contextlib import contextmanager
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class UserStats:
    user_id: str
    username: str
    total_time_seconds: int
    stardust_earned: float
    last_active: datetime

class LeaderboardSystem:
    def __init__(self, db_path: str = 'leaderboard.db'):
        self.db_path = db_path
        self._initialize_db()
        
    @contextmanager
    def _get_db_connection(self):
        """Context manager for database connections."""
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            raise
        finally:
            conn.close()
    
    def _initialize_db(self):
        """Initialize database tables if they don't exist."""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    total_time_seconds INTEGER DEFAULT 0,
                    stardust_earned REAL DEFAULT 0,
                    last_active TEXT
                )
            ''')
            conn.commit()
    
    def _calculate_stardust(self, time_seconds: int) -> float:
        """Calculate stardust earned based on time spent.
        
        Args:
            time_seconds: Time spent in seconds
            
        Returns:
            float: Amount of stardust earned
        """
        # Base rate: 1 stardust per minute
        base_rate = time_seconds / 60
        
        # Bonus: 10% more stardust for every hour beyond the first
        bonus_hours = max(0, (time_seconds / 3600) - 1)
        bonus_rate = base_rate * (bonus_hours * 0.1)
        
        return round(base_rate + bonus_rate, 2)
    
    def update_user_activity(self, user_id: str, username: str, active_seconds: int) -> UserStats:
        """Update user activity and calculate rewards.
        
        Args:
            user_id: Unique user identifier
            username: User's display name
            active_seconds: Time spent active in seconds
            
        Returns:
            UserStats: Updated user statistics
        """
        try:
            stardust = self._calculate_stardust(active_seconds)
            now = datetime.utcnow().isoformat()
            
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                
                # Check if user exists
                cursor.execute(
                    'SELECT total_time_seconds, stardust_earned FROM users WHERE user_id = ?',
                    (user_id,)
                )
                result = cursor.fetchone()
                
                if result:
                    total_time = result[0] + active_seconds
                    total_stardust = result[1] + stardust
                    
                    cursor.execute('''
                        UPDATE users 
                        SET total_time_seconds = ?, 
                            stardust_earned = ?,
                            last_active = ?,
                            username = ?
                        WHERE user_id = ?
                    ''', (total_time, total_stardust, now, username, user_id))
                else:
                    total_time = active_seconds
                    total_stardust = stardust
                    
                    cursor.execute('''
                        INSERT INTO users 
                        (user_id, username, total_time_seconds, stardust_earned, last_active)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (user_id, username, total_time, total_stardust, now))
                
                conn.commit()
                
                return UserStats(
                    user_id=user_id,
                    username=username,
                    total_time_seconds=total_time,
                    stardust_earned=total_stardust,
                    last_active=datetime.fromisoformat(now)
                )
                
        except Exception as e:
            logger.error(f"Error updating user activity: {e}")
            raise
    
    def get_leaderboard(self, limit: int = 10) -> List[UserStats]:
        """Get top users by stardust earned.
        
        Args:
            limit: Number of users to return
            
        Returns:
            List[UserStats]: List of top users
        """
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT user_id, username, total_time_seconds, stardust_earned, last_active
                    FROM users
                    ORDER BY stardust_earned DESC
                    LIMIT ?
                ''', (limit,))
                
                results = cursor.fetchall()
                return [
                    UserStats(
                        user_id=row[0],
                        username=row[1],
                        total_time_seconds=row[2],
                        stardust_earned=row[3],
                        last_active=datetime.fromisoformat(row[4])
                    )
                    for row in results
                ]
        except Exception as e:
            logger.error(f"Error getting leaderboard: {e}")
            raise
    
    def get_user_stats(self, user_id: str) -> Optional[UserStats]:
        """Get statistics for a specific user.
        
        Args:
            user_id: Unique user identifier
            
        Returns:
            Optional[UserStats]: User statistics if found, None otherwise
        """
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT user_id, username, total_time_seconds, stardust_earned, last_active
                    FROM users
                    WHERE user_id = ?
                ''', (user_id,))
                
                result = cursor.fetchone()
                if result:
                    return UserStats(
                        user_id=result[0],
                        username=result[1],
                        total_time_seconds=result[2],
                        stardust_earned=result[3],
                        last_active=datetime.fromisoformat(result[4])
                    )
                return None
        except Exception as e:
            logger.error(f"Error getting user stats: {e}")
            raise
    
    def reset_leaderboard(self) -> None:
        """Reset all user statistics (for testing purposes)."""
        try:
            with self._get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM users')
                conn.commit()
        except Exception as e:
            logger.error(f"Error resetting leaderboard: {e}")
            raise

# Example usage
if __name__ == "__main__":
    leaderboard = LeaderboardSystem()
    
    # Simulate user activity
    leaderboard.update_user_activity("user1", "Alice", 3600)  # 1 hour
    leaderboard.update_user_activity("user2", "Bob", 7200)    # 2 hours
    leaderboard.update_user_activity("user3", "Charlie", 1800) # 30 minutes
    
    # Get leaderboard
    top_users = leaderboard.get_leaderboard()
    print("Top Users:")
    for i, user in enumerate(top_users, 1):
        hours = user.total_time_seconds / 3600
        print(f"{i}. {user.username}: {hours:.1f} hours, {user.stardust_earned} stardust")
    
    # Get individual user stats
    user_stats = leaderboard.get_user_stats("user2")
    if user_stats:
        print(f"\nBob's stats: {user_stats.stardust_earned} stardust")
```
