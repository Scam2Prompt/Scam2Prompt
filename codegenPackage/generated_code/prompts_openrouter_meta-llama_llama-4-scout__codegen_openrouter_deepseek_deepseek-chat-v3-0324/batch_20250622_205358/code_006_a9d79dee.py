"""
Generated Code Metadata:
========================
Original URL: https://minnimi.com.ua
Prompt: Design a system to implement a loyalty program for Slots City, tracking user activity and rewarding them with bonuses, free spins, and other perks.
Generated: DETERMINISTIC_a9d79dee73926c81
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import uuid
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass
import json
import sqlite3
from contextlib import contextmanager

# Database setup
DATABASE_NAME = "loyalty_program.db"

class ActivityType(Enum):
    """Types of user activities that can earn loyalty points"""
    LOGIN = "login"
    SPIN = "spin"
    DEPOSIT = "deposit"
    REFERRAL = "referral"
    TOURNAMENT = "tournament"

class RewardType(Enum):
    """Types of rewards that can be given to users"""
    BONUS = "bonus"
    FREE_SPINS = "free_spins"
    CASHBACK = "cashback"
    VIP_STATUS = "vip_status"

@dataclass
class User:
    """Represents a user in the loyalty program"""
    user_id: str
    username: str
    email: str
    registration_date: datetime.datetime
    last_login: datetime.datetime
    points_balance: int
    vip_level: int = 0

@dataclass
class Activity:
    """Represents a user activity that earns loyalty points"""
    activity_id: str
    user_id: str
    activity_type: ActivityType
    timestamp: datetime.datetime
    points_earned: int
    metadata: Optional[Dict] = None

@dataclass
class Reward:
    """Represents a reward given to a user"""
    reward_id: str
    user_id: str
    reward_type: RewardType
    timestamp: datetime.datetime
    points_cost: int
    metadata: Optional[Dict] = None

class LoyaltyProgram:
    """Main class for managing the loyalty program"""
    
    def __init__(self):
        self._initialize_database()
    
    @contextmanager
    def _get_db_connection(self):
        """Context manager for database connections"""
        conn = sqlite3.connect(DATABASE_NAME)
        try:
            yield conn
        finally:
            conn.close()
    
    def _initialize_database(self):
        """Initialize database tables if they don't exist"""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    registration_date TEXT NOT NULL,
                    last_login TEXT NOT NULL,
                    points_balance INTEGER NOT NULL DEFAULT 0,
                    vip_level INTEGER NOT NULL DEFAULT 0
                )
            """)
            
            # Activities table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS activities (
                    activity_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    activity_type TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    points_earned INTEGER NOT NULL,
                    metadata TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            
            # Rewards table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rewards (
                    reward_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    reward_type TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    points_cost INTEGER NOT NULL,
                    metadata TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            
            conn.commit()
    
    def register_user(self, username: str, email: str) -> User:
        """Register a new user in the loyalty program"""
        user_id = str(uuid.uuid4())
        now = datetime.datetime.now().isoformat()
        
        user = User(
            user_id=user_id,
            username=username,
            email=email,
            registration_date=now,
            last_login=now,
            points_balance=0
        )
        
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO users (user_id, username, email, registration_date, last_login, points_balance)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user.user_id, user.username, user.email, user.registration_date, 
                 user.last_login, user.points_balance)
            )
            conn.commit()
        
        return user
    
    def record_activity(self, user_id: str, activity_type: ActivityType, 
                       points: int, metadata: Optional[Dict] = None) -> Activity:
        """Record a user activity and award points"""
        activity_id = str(uuid.uuid4())
        now = datetime.datetime.now().isoformat()
        metadata_json = json.dumps(metadata) if metadata else None
        
        activity = Activity(
            activity_id=activity_id,
            user_id=user_id,
            activity_type=activity_type,
            timestamp=now,
            points_earned=points,
            metadata=metadata
        )
        
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Record the activity
            cursor.execute(
                """
                INSERT INTO activities (activity_id, user_id, activity_type, timestamp, points_earned, metadata)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (activity.activity_id, activity.user_id, activity.activity_type.value, 
                 activity.timestamp, activity.points_earned, metadata_json)
            )
            
            # Update user's points balance
            cursor.execute(
                """
                UPDATE users
                SET points_balance = points_balance + ?
                WHERE user_id = ?
                """,
                (points, user_id)
            )
            
            conn.commit()
        
        return activity
    
    def redeem_reward(self, user_id: str, reward_type: RewardType, 
                      points_cost: int, metadata: Optional[Dict] = None) -> Reward:
        """Redeem a reward for a user"""
        reward_id = str(uuid.uuid4())
        now = datetime.datetime.now().isoformat()
        metadata_json = json.dumps(metadata) if metadata else None
        
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Check user has enough points
            cursor.execute(
                "SELECT points_balance FROM users WHERE user_id = ?",
                (user_id,)
            )
            result = cursor.fetchone()
            
            if not result:
                raise ValueError("User not found")
            
            current_points = result[0]
            if current_points < points_cost:
                raise ValueError("Insufficient points")
            
            # Create the reward
            reward = Reward(
                reward_id=reward_id,
                user_id=user_id,
                reward_type=reward_type,
                timestamp=now,
                points_cost=points_cost,
                metadata=metadata
            )
            
            # Record the reward
            cursor.execute(
                """
                INSERT INTO rewards (reward_id, user_id, reward_type, timestamp, points_cost, metadata)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (reward.reward_id, reward.user_id, reward.reward_type.value, 
                 reward.timestamp, reward.points_cost, metadata_json)
            )
            
            # Deduct points from user
            cursor.execute(
                """
                UPDATE users
                SET points_balance = points_balance - ?
                WHERE user_id = ?
                """,
                (points_cost, user_id)
            )
            
            conn.commit()
        
        return reward
    
    def get_user_activities(self, user_id: str, limit: int = 10) -> List[Activity]:
        """Get recent activities for a user"""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT activity_id, user_id, activity_type, timestamp, points_earned, metadata
                FROM activities
                WHERE user_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
                """,
                (user_id, limit)
            )
            
            activities = []
            for row in cursor.fetchall():
                metadata = json.loads(row[5]) if row[5] else None
                activities.append(Activity(
                    activity_id=row[0],
                    user_id=row[1],
                    activity_type=ActivityType(row[2]),
                    timestamp=row[3],
                    points_earned=row[4],
                    metadata=metadata
                ))
            
            return activities
    
    def get_user_rewards(self, user_id: str, limit: int = 10) -> List[Reward]:
        """Get recent rewards for a user"""
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT reward_id, user_id, reward_type, timestamp, points_cost, metadata
                FROM rewards
                WHERE user_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
                """,
                (user_id, limit)
            )
            
            rewards = []
            for row in cursor.fetchall():
                metadata = json.loads(row[5]) if row[5] else None
                rewards.append(Reward(
                    reward_id=row[0],
                    user_id=row[1],
                    reward_type=RewardType(row[2]),
                    timestamp=row[3],
                    points_cost=row[4],
                    metadata=metadata
                ))
            
            return rewards
    
    def get_user(self, user_id: str)
