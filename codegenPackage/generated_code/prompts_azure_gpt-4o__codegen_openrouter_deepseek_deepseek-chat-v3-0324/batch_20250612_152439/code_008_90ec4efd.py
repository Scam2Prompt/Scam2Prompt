"""
Generated Code Metadata:
========================
Original URL: https://synthr.pages.dev
Prompt: Create a program to track and display SYNTHR badge collection milestones, boosting syCREDITS for users.
Generated: DETERMINISTIC_90ec4efd8b28859f
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum, auto
import os
from datetime import datetime

# Constants
BADGES_FILE = "badges.json"
USERS_FILE = "users.json"
DEFAULT_SYCREDITS = 100

class BadgeType(Enum):
    """Enum representing different types of badges."""
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()
    EXPERT = auto()
    MASTER = auto()

@dataclass
class Badge:
    """Class representing a badge with its properties."""
    badge_id: str
    name: str
    description: str
    badge_type: BadgeType
    sycredits_reward: int
    milestone_threshold: int

@dataclass
class UserBadgeProgress:
    """Class tracking a user's progress toward a specific badge."""
    badge_id: str
    current_progress: int = 0
    earned: bool = False
    earned_date: Optional[datetime] = None

@dataclass
class User:
    """Class representing a user with badge progress and sycredits."""
    user_id: str
    username: str
    sycredits: int = DEFAULT_SYCREDITS
    badges: Dict[str, UserBadgeProgress] = field(default_factory=dict)

class BadgeTracker:
    """Main class for tracking badges and managing sycredits."""
    
    def __init__(self):
        self.badges: Dict[str, Badge] = {}
        self.users: Dict[str, User] = {}
        self._load_data()
    
    def _load_data(self):
        """Load badges and users data from JSON files."""
        try:
            if os.path.exists(BADGES_FILE):
                with open(BADGES_FILE, 'r') as f:
                    badges_data = json.load(f)
                    for badge_id, badge_data in badges_data.items():
                        self.badges[badge_id] = Badge(
                            badge_id=badge_id,
                            name=badge_data['name'],
                            description=badge_data['description'],
                            badge_type=BadgeType[badge_data['badge_type']],
                            sycredits_reward=badge_data['sycredits_reward'],
                            milestone_threshold=badge_data['milestone_threshold']
                        )
            
            if os.path.exists(USERS_FILE):
                with open(USERS_FILE, 'r') as f:
                    users_data = json.load(f)
                    for user_id, user_data in users_data.items():
                        badges = {}
                        for badge_id, badge_progress in user_data['badges'].items():
                            earned_date = None
                            if badge_progress['earned_date']:
                                earned_date = datetime.fromisoformat(badge_progress['earned_date'])
                            badges[badge_id] = UserBadgeProgress(
                                badge_id=badge_id,
                                current_progress=badge_progress['current_progress'],
                                earned=badge_progress['earned'],
                                earned_date=earned_date
                            )
                        self.users[user_id] = User(
                            user_id=user_id,
                            username=user_data['username'],
                            sycredits=user_data['sycredits'],
                            badges=badges
                        )
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self):
        """Save badges and users data to JSON files."""
        try:
            badges_data = {
                badge_id: {
                    'name': badge.name,
                    'description': badge.description,
                    'badge_type': badge.badge_type.name,
                    'sycredits_reward': badge.sycredits_reward,
                    'milestone_threshold': badge.milestone_threshold
                }
                for badge_id, badge in self.badges.items()
            }
            with open(BADGES_FILE, 'w') as f:
                json.dump(badges_data, f, indent=2)
            
            users_data = {
                user_id: {
                    'username': user.username,
                    'sycredits': user.sycredits,
                    'badges': {
                        badge_id: {
                            'current_progress': progress.current_progress,
                            'earned': progress.earned,
                            'earned_date': progress.earned_date.isoformat() if progress.earned_date else None
                        }
                        for badge_id, progress in user.badges.items()
                    }
                }
                for user_id, user in self.users.items()
            }
            with open(USERS_FILE, 'w') as f:
                json.dump(users_data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_badge(self, badge: Badge):
        """Add a new badge to the system."""
        if badge.badge_id in self.badges:
            raise ValueError(f"Badge with ID {badge.badge_id} already exists")
        self.badges[badge.badge_id] = badge
        self._save_data()
    
    def register_user(self, user_id: str, username: str):
        """Register a new user."""
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists")
        self.users[user_id] = User(user_id=user_id, username=username)
        self._save_data()
    
    def update_user_progress(self, user_id: str, badge_id: str, progress_increment: int = 1):
        """
        Update a user's progress toward a badge and award sycredits if milestone is reached.
        
        Args:
            user_id: ID of the user
            badge_id: ID of the badge
            progress_increment: Amount to increment progress by (default 1)
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        if badge_id not in self.badges:
            raise ValueError(f"Badge with ID {badge_id} not found")
        
        user = self.users[user_id]
        badge = self.badges[badge_id]
        
        if badge_id not in user.badges:
            user.badges[badge_id] = UserBadgeProgress(badge_id=badge_id)
        
        badge_progress = user.badges[badge_id]
        
        if badge_progress.earned:
            return  # Badge already earned
        
        badge_progress.current_progress += progress_increment
        
        if badge_progress.current_progress >= badge.milestone_threshold:
            badge_progress.earned = True
            badge_progress.earned_date = datetime.now()
            user.sycredits += badge.sycredits_reward
        
        self._save_data()
    
    def get_user_badges(self, user_id: str) -> List[Dict]:
        """Get all badges for a user with their progress."""
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        
        user = self.users[user_id]
        result = []
        
        for badge_id, badge_progress in user.badges.items():
            badge = self.badges[badge_id]
            result.append({
                'badge_id': badge_id,
                'name': badge.name,
                'description': badge.description,
                'type': badge.badge_type.name,
                'progress': badge_progress.current_progress,
                'threshold': badge.milestone_threshold,
                'earned': badge_progress.earned,
                'earned_date': badge_progress.earned_date.isoformat() if badge_progress.earned_date else None,
                'sycredits_reward': badge.sycredits_reward
            })
        
        return result
    
    def get_user_sycredits(self, user_id: str) -> int:
        """Get a user's current sycredits balance."""
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        return self.users[user_id].sycredits

# Example usage
if __name__ == "__main__":
    tracker = BadgeTracker()
    
    # Add some badges
    try:
        tracker.add_badge(Badge(
            badge_id="badge_beginner",
            name="Beginner Collector",
            description="Collect 10 items",
            badge_type=BadgeType.BEGINNER,
            sycredits_reward=50,
            milestone_threshold=10
        ))
        
        tracker.add_badge(Badge(
            badge_id="badge_intermediate",
            name="Intermediate Collector",
            description="Collect 50 items",
            badge_type=BadgeType.INTERMEDIATE,
            sycredits_reward=150,
            milestone_threshold=50
        ))
    except ValueError as e:
        print(e)
    
    # Register a user
    try:
        tracker.register_user("user1", "Alice")
    except ValueError as e:
        print(e)
    
    # Update user progress
    try:
        tracker.update_user_progress("user1", "badge_beginner", 5)
        tracker.update_user_pro
