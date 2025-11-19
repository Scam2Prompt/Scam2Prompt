"""
Generated Code Metadata:
========================
Original URL: https://metacade-co.pages.dev
Prompt: Develop a system for distributing rewards to users based on their contributions to game development and community engagement, inspired by Metacade's reward mechanisms.
Generated: DETERMINISTIC_ca165a768278df92
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum
import hashlib
import uuid
import sqlite3
from dataclasses import dataclass

# Database setup constants
DB_NAME = "metacade_rewards.db"

class ContributionType(Enum):
    """Enum representing different types of user contributions"""
    GAME_DEVELOPMENT = "game_development"
    BUG_REPORT = "bug_report"
    COMMUNITY_MODERATION = "community_moderation"
    CONTENT_CREATION = "content_creation"
    TESTING = "testing"
    OTHER = "other"

@dataclass
class User:
    """Data class representing a user"""
    user_id: str
    username: str
    email: str
    join_date: datetime
    reputation: int = 0

@dataclass
class Contribution:
    """Data class representing a user contribution"""
    contribution_id: str
    user_id: str
    contribution_type: ContributionType
    description: str
    timestamp: datetime
    points_awarded: int
    verified: bool = False

@dataclass
class Reward:
    """Data class representing a reward"""
    reward_id: str
    name: str
    description: str
    point_cost: int
    available_quantity: int
    expiry_date: Optional[datetime] = None

@dataclass
class RewardRedemption:
    """Data class representing a reward redemption"""
    redemption_id: str
    user_id: str
    reward_id: str
    redemption_date: datetime
    points_spent: int

class RewardSystem:
    """Main class handling the reward distribution system"""
    
    def __init__(self):
        """Initialize the reward system and database connection"""
        self.conn = sqlite3.connect(DB_NAME)
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist"""
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            join_date TEXT NOT NULL,
            reputation INTEGER DEFAULT 0
        )
        """)
        
        # Contributions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contributions (
            contribution_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            contribution_type TEXT NOT NULL,
            description TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            points_awarded INTEGER NOT NULL,
            verified INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        """)
        
        # Rewards table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rewards (
            reward_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            point_cost INTEGER NOT NULL,
            available_quantity INTEGER NOT NULL,
            expiry_date TEXT
        )
        """)
        
        # Reward redemptions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reward_redemptions (
            redemption_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            reward_id TEXT NOT NULL,
            redemption_date TEXT NOT NULL,
            points_spent INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (reward_id) REFERENCES rewards (reward_id)
        )
        """)
        
        self.conn.commit()
    
    def add_user(self, username: str, email: str) -> User:
        """Add a new user to the system"""
        user_id = str(uuid.uuid4())
        join_date = datetime.utcnow().isoformat()
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?)",
            (user_id, username, email, join_date, 0)
        )
        self.conn.commit()
        
        return User(user_id, username, email, datetime.fromisoformat(join_date))
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve a user by their ID"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        
        if row:
            return User(
                user_id=row[0],
                username=row[1],
                email=row[2],
                join_date=datetime.fromisoformat(row[3]),
                reputation=row[4]
            )
        return None
    
    def record_contribution(
        self,
        user_id: str,
        contribution_type: ContributionType,
        description: str,
        points: int
    ) -> Contribution:
        """Record a user contribution and award points"""
        contribution_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO contributions VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                contribution_id,
                user_id,
                contribution_type.value,
                description,
                timestamp,
                points,
                False  # Not verified by default
            )
        )
        
        # Update user reputation
        cursor.execute(
            "UPDATE users SET reputation = reputation + ? WHERE user_id = ?",
            (points, user_id)
        )
        
        self.conn.commit()
        
        return Contribution(
            contribution_id=contribution_id,
            user_id=user_id,
            contribution_type=contribution_type,
            description=description,
            timestamp=datetime.fromisoformat(timestamp),
            points_awarded=points
        )
    
    def verify_contribution(self, contribution_id: str) -> bool:
        """Verify a contribution and make points permanent"""
        cursor = self.conn.cursor()
        
        # Check if contribution exists and is not already verified
        cursor.execute(
            "SELECT user_id, points_awarded FROM contributions WHERE contribution_id = ? AND verified = 0",
            (contribution_id,)
        )
        result = cursor.fetchone()
        
        if not result:
            return False
        
        user_id, points = result
        
        # Mark as verified
        cursor.execute(
            "UPDATE contributions SET verified = 1 WHERE contribution_id = ?",
            (contribution_id,)
        )
        self.conn.commit()
        return True
    
    def add_reward(
        self,
        name: str,
        description: str,
        point_cost: int,
        available_quantity: int,
        expiry_date: Optional[datetime] = None
    ) -> Reward:
        """Add a new reward to the system"""
        reward_id = str(uuid.uuid4())
        expiry_str = expiry_date.isoformat() if expiry_date else None
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO rewards VALUES (?, ?, ?, ?, ?, ?)",
            (reward_id, name, description, point_cost, available_quantity, expiry_str)
        )
        self.conn.commit()
        
        return Reward(
            reward_id=reward_id,
            name=name,
            description=description,
            point_cost=point_cost,
            available_quantity=available_quantity,
            expiry_date=expiry_date
        )
    
    def get_available_rewards(self) -> List[Reward]:
        """Get all available rewards that haven't expired and have quantity left"""
        cursor = self.conn.cursor()
        current_time = datetime.utcnow().isoformat()
        
        cursor.execute("""
        SELECT * FROM rewards 
        WHERE (expiry_date IS NULL OR expiry_date > ?) 
        AND available_quantity > 0
        """, (current_time,))
        
        rewards = []
        for row in cursor.fetchall():
            expiry_date = datetime.fromisoformat(row[5]) if row[5] else None
            rewards.append(Reward(
                reward_id=row[0],
                name=row[1],
                description=row[2],
                point_cost=row[3],
                available_quantity=row[4],
                expiry_date=expiry_date
            ))
        
        return rewards
    
    def redeem_reward(self, user_id: str, reward_id: str) -> Optional[RewardRedemption]:
        """Redeem a reward for a user"""
        cursor = self.conn.cursor()
        
        # Check user reputation points
        cursor.execute("SELECT reputation FROM users WHERE user_id = ?", (user_id,))
        user_reputation = cursor.fetchone()
        if not user_reputation:
            return None
        
        user_points = user_reputation[0]
        
        # Check reward availability
        cursor.execute("""
        SELECT point_cost, available_quantity FROM rewards 
        WHERE reward_id = ? AND (expiry_date IS NULL OR expiry_date > ?)
        """, (reward_id, datetime.utcnow().isoformat()))
        
        reward_info = cursor.fetchone()
        if not reward_info or reward_info[1] <= 0:
            return None
        
        point_cost, available_quantity = reward_info
        
        if user_points < point_cost:
            return None
        
        # Create redemption record
        redemption_id = str(uuid.uuid4())
        redemption_date = datetime.utcnow().isoformat()
