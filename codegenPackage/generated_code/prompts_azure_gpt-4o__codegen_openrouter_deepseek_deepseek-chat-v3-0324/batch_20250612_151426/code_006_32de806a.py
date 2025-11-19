"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Create a Python script that incorporates gamification elements, such as leaderboards and challenges, to encourage users to stay on track with their weight loss goals, as described on myneel.com.
Generated: DETERMINISTIC_32de806af13aba2e
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class User:
    """Represents a user with weight loss goals and progress."""
    
    def __init__(self, user_id: str, name: str, initial_weight: float, target_weight: float):
        """Initialize a user with their details and goals."""
        self.user_id = user_id
        self.name = name
        self.initial_weight = initial_weight
        self.current_weight = initial_weight
        self.target_weight = target_weight
        self.points = 0
        self.streak_days = 0
        self.last_checkin = datetime.now().date()
        self.challenges_completed = []
    
    def update_weight(self, new_weight: float) -> Tuple[bool, str]:
        """Update the user's current weight and calculate points."""
        if new_weight <= 0:
            return False, "Weight must be positive"
        
        weight_loss = self.current_weight - new_weight
        if weight_loss < 0:
            return False, "Weight cannot increase"
        
        self.current_weight = new_weight
        points_earned = int(weight_loss * 100)  # 1 point per 0.01 kg lost
        self.points += points_earned
        
        # Update streak
        today = datetime.now().date()
        if (today - self.last_checkin).days == 1:
            self.streak_days += 1
        elif (today - self.last_checkin).days > 1:
            self.streak_days = 0
        self.last_checkin = today
        
        return True, f"Updated weight! Earned {points_earned} points."
    
    def complete_challenge(self, challenge_id: str, points: int) -> bool:
        """Mark a challenge as completed and award points."""
        if challenge_id in self.challenges_completed:
            return False
        self.challenges_completed.append(challenge_id)
        self.points += points
        return True
    
    def to_dict(self) -> Dict:
        """Convert user data to a dictionary for storage."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "initial_weight": self.initial_weight,
            "current_weight": self.current_weight,
            "target_weight": self.target_weight,
            "points": self.points,
            "streak_days": self.streak_days,
            "last_checkin": self.last_checkin.isoformat(),
            "challenges_completed": self.challenges_completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create a User instance from a dictionary."""
        user = cls(
            data["user_id"],
            data["name"],
            data["initial_weight"],
            data["target_weight"]
        )
        user.current_weight = data["current_weight"]
        user.points = data["points"]
        user.streak_days = data["streak_days"]
        user.last_checkin = datetime.fromisoformat(data["last_checkin"]).date()
        user.challenges_completed = data["challenges_completed"]
        return user

class Challenge:
    """Represents a weight loss challenge."""
    
    def __init__(self, challenge_id: str, name: str, description: str, points: int, duration_days: int):
        """Initialize a challenge with its details."""
        self.challenge_id = challenge_id
        self.name = name
        self.description = description
        self.points = points
        self.duration_days = duration_days
        self.start_date = datetime.now().date()
        self.end_date = self.start_date + timedelta(days=duration_days)
    
    def is_active(self) -> bool:
        """Check if the challenge is still active."""
        return datetime.now().date() <= self.end_date
    
    def to_dict(self) -> Dict:
        """Convert challenge data to a dictionary for storage."""
        return {
            "challenge_id": self.challenge_id,
            "name": self.name,
            "description": self.description,
            "points": self.points,
            "duration_days": self.duration_days,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Challenge':
        """Create a Challenge instance from a dictionary."""
        challenge = cls(
            data["challenge_id"],
            data["name"],
            data["description"],
            data["points"],
            data["duration_days"]
        )
        challenge.start_date = datetime.fromisoformat(data["start_date"]).date()
        challenge.end_date = datetime.fromisoformat(data["end_date"]).date()
        return challenge

class WeightLossTracker:
    """Main class for managing weight loss gamification."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the tracker with data storage directory."""
        self.data_dir = data_dir
        self.users: Dict[str, User] = {}
        self.challenges: Dict[str, Challenge] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load user and challenge data from files."""
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load users
        users_file = os.path.join(self.data_dir, "users.json")
        if os.path.exists(users_file):
            with open(users_file, "r") as f:
                users_data = json.load(f)
                for user_data in users_data.values():
                    user = User.from_dict(user_data)
                    self.users[user.user_id] = user
        
        # Load challenges
        challenges_file = os.path.join(self.data_dir, "challenges.json")
        if os.path.exists(challenges_file):
            with open(challenges_file, "r") as f:
                challenges_data = json.load(f)
                for challenge_data in challenges_data.values():
                    challenge = Challenge.from_dict(challenge_data)
                    self.challenges[challenge.challenge_id] = challenge
    
    def _save_data(self) -> None:
        """Save user and challenge data to files."""
        # Save users
        users_file = os.path.join(self.data_dir, "users.json")
        users_data = {user_id: user.to_dict() for user_id, user in self.users.items()}
        with open(users_file, "w") as f:
            json.dump(users_data, f, indent=2)
        
        # Save challenges
        challenges_file = os.path.join(self.data_dir, "challenges.json")
        challenges_data = {challenge_id: challenge.to_dict() for challenge_id, challenge in self.challenges.items()}
        with open(challenges_file, "w") as f:
            json.dump(challenges_data, f, indent=2)
    
    def register_user(self, user_id: str, name: str, initial_weight: float, target_weight: float) -> bool:
        """Register a new user."""
        if user_id in self.users:
            return False
        if initial_weight <= 0 or target_weight <= 0:
            return False
        if target_weight >= initial_weight:
            return False
        
        self.users[user_id] = User(user_id, name, initial_weight, target_weight)
        self._save_data()
        return True
    
    def update_user_weight(self, user_id: str, new_weight: float) -> Tuple[bool, str]:
        """Update a user's weight and calculate points."""
        if user_id not in self.users:
            return False, "User not found"
        
        success, message = self.users[user_id].update_weight(new_weight)
        if success:
            self._save_data()
        return success, message
    
    def create_challenge(self, challenge_id: str, name: str, description: str, points: int, duration_days: int) -> bool:
        """Create a new challenge."""
        if challenge_id in self.challenges:
            return False
        if points <= 0 or duration_days <= 0:
            return False
        
        self.challenges[challenge_id] = Challenge(challenge_id, name, description, points, duration_days)
        self._save_data()
        return True
    
    def complete_challenge(self, user_id: str, challenge_id: str) -> Tuple[bool, str]:
        """Mark a challenge as completed for a user."""
        if user_id not in self.users:
            return False, "User not found"
        if challenge_id not in self.challenges:
            return False, "Challenge not found"
        
        challenge = self.challenges[challenge_id]
        if not challenge.is_active():
            return False, "Challenge is no longer active"
        
        success = self.users[user_id].complete_challenge(challenge_id, challenge.points)
        if success:
            self._save_data()
            return True, f"Challenge completed! Earned {challenge.points} points."
        return False, "Challenge already completed"
    
    def get_leaderboard(self, top_n: int = 10) -> List[Dict]:
        """Get the top users by points."""
        sorted_users = sorted(
            self.users.values(),
            key=lambda u: u.points,
            reverse=True
