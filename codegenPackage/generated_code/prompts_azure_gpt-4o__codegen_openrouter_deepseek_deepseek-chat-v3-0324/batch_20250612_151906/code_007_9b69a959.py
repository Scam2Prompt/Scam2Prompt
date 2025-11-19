"""
Generated Code Metadata:
========================
Original URL: https://metacade-web.pages.dev
Prompt: Generate code for a user profile system that tracks gaming achievements, rewards, and employment opportunities, inspired by Metacade's digital pass functionality.
Generated: DETERMINISTIC_9b69a95932076b91
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
from pydantic import BaseModel, validator, Field


class AchievementLevel(Enum):
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    PLATINUM = auto()


class Achievement(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    level: AchievementLevel
    points: int
    unlocked: bool = False
    unlock_date: Optional[datetime] = None

    @validator('points')
    def validate_points(cls, v):
        if v < 0:
            raise ValueError("Points cannot be negative")
        return v


class RewardType(Enum):
    DIGITAL = auto()
    PHYSICAL = auto()
    IN_GAME = auto()


class Reward(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    reward_type: RewardType
    claimed: bool = False
    claim_date: Optional[datetime] = None


class EmploymentOpportunity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    company: str
    description: str
    requirements: List[str]
    applied: bool = False
    application_date: Optional[datetime] = None


class UserProfile(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: str
    total_points: int = 0
    achievements: List[Achievement] = []
    rewards: List[Reward] = []
    employment_opportunities: List[EmploymentOpportunity] = []

    def add_achievement(self, achievement: Achievement) -> None:
        """Add an achievement to the user's profile."""
        self.achievements.append(achievement)
        self.total_points += achievement.points

    def unlock_achievement(self, achievement_id: str) -> bool:
        """Unlock an achievement by ID."""
        for achievement in self.achievements:
            if achievement.id == achievement_id:
                if not achievement.unlocked:
                    achievement.unlocked = True
                    achievement.unlock_date = datetime.now()
                    return True
        return False

    def add_reward(self, reward: Reward) -> None:
        """Add a reward to the user's profile."""
        self.rewards.append(reward)

    def claim_reward(self, reward_id: str) -> bool:
        """Claim a reward by ID."""
        for reward in self.rewards:
            if reward.id == reward_id:
                if not reward.claimed:
                    reward.claimed = True
                    reward.claim_date = datetime.now()
                    return True
        return False

    def add_employment_opportunity(self, opportunity: EmploymentOpportunity) -> None:
        """Add an employment opportunity to the user's profile."""
        self.employment_opportunities.append(opportunity)

    def apply_for_opportunity(self, opportunity_id: str) -> bool:
        """Apply for an employment opportunity by ID."""
        for opportunity in self.employment_opportunities:
            if opportunity.id == opportunity_id:
                if not opportunity.applied:
                    opportunity.applied = True
                    opportunity.application_date = datetime.now()
                    return True
        return False

    def get_unlocked_achievements(self) -> List[Achievement]:
        """Get all unlocked achievements."""
        return [ach for ach in self.achievements if ach.unlocked]

    def get_claimed_rewards(self) -> List[Reward]:
        """Get all claimed rewards."""
        return [reward for reward in self.rewards if reward.claimed]

    def get_applied_opportunities(self) -> List[EmploymentOpportunity]:
        """Get all applied employment opportunities."""
        return [opp for opp in self.employment_opportunities if opp.applied]


class UserProfileManager:
    def __init__(self):
        self.profiles: Dict[str, UserProfile] = {}

    def create_profile(self, username: str, email: str) -> UserProfile:
        """Create a new user profile."""
        if any(profile.username == username for profile in self.profiles.values()):
            raise ValueError("Username already exists")
        if any(profile.email == email for profile in self.profiles.values()):
            raise ValueError("Email already in use")
        
        profile = UserProfile(username=username, email=email)
        self.profiles[profile.user_id] = profile
        return profile

    def get_profile(self, user_id: str) -> Optional[UserProfile]:
        """Get a user profile by ID."""
        return self.profiles.get(user_id)

    def delete_profile(self, user_id: str) -> bool:
        """Delete a user profile by ID."""
        if user_id in self.profiles:
            del self.profiles[user_id]
            return True
        return False

    def update_profile_email(self, user_id: str, new_email: str) -> bool:
        """Update a user's email address."""
        profile = self.get_profile(user_id)
        if profile:
            if any(p.email == new_email for p in self.profiles.values() if p.user_id != user_id):
                raise ValueError("Email already in use")
            profile.email = new_email
            return True
        return False
```
