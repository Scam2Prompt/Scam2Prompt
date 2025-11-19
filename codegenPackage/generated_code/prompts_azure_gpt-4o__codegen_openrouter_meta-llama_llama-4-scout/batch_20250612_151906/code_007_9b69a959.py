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
# user_profile.py

from typing import List, Dict
from enum import Enum
from datetime import datetime

class AchievementType(str, Enum):
    """Types of achievements"""
    GAMING = "gaming"
    EMPLOYMENT = "employment"

class RewardType(str, Enum):
    """Types of rewards"""
    VIRTUAL_ITEM = "virtual_item"
    CURRENCY = "currency"

class EmploymentOpportunity:
    """Employment opportunity"""
    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

class Achievement:
    """Achievement"""
    def __init__(self, id: int, name: str, achievement_type: AchievementType):
        self.id = id
        self.name = name
        self.achievement_type = achievement_type
        self.unlocked = False

class Reward:
    """Reward"""
    def __init__(self, id: int, name: str, reward_type: RewardType):
        self.id = id
        self.name = name
        self.reward_type = reward_type

class UserProfile:
    """User profile"""
    def __init__(self, id: int, username: str):
        self.id = id
        self.username = username
        self.achievements: List[Achievement] = []
        self.rewards: List[Reward] = []
        self.employment_opportunities: List[EmploymentOpportunity] = []

    def add_achievement(self, achievement: Achievement):
        """Add achievement to user profile"""
        self.achievements.append(achievement)

    def unlock_achievement(self, achievement_id: int):
        """Unlock achievement"""
        for achievement in self.achievements:
            if achievement.id == achievement_id:
                achievement.unlocked = True
                break
        else:
            raise ValueError("Achievement not found")

    def add_reward(self, reward: Reward):
        """Add reward to user profile"""
        self.rewards.append(reward)

    def add_employment_opportunity(self, opportunity: EmploymentOpportunity):
        """Add employment opportunity to user profile"""
        self.employment_opportunities.append(opportunity)

class UserProfileSystem:
    """User profile system"""
    def __init__(self):
        self.user_profiles: Dict[int, UserProfile] = {}

    def create_user_profile(self, id: int, username: str):
        """Create user profile"""
        if id in self.user_profiles:
            raise ValueError("User profile already exists")
        self.user_profiles[id] = UserProfile(id, username)

    def get_user_profile(self, id: int):
        """Get user profile"""
        return self.user_profiles.get(id)

def main():
    # Create user profile system
    system = UserProfileSystem()

    # Create user profile
    system.create_user_profile(1, "example_user")

    # Get user profile
    user_profile = system.get_user_profile(1)

    # Create achievement
    achievement = Achievement(1, "Example Achievement", AchievementType.GAMING)

    # Add achievement to user profile
    user_profile.add_achievement(achievement)

    # Unlock achievement
    user_profile.unlock_achievement(1)

    # Create reward
    reward = Reward(1, "Example Reward", RewardType.VIRTUAL_ITEM)

    # Add reward to user profile
    user_profile.add_reward(reward)

    # Create employment opportunity
    opportunity = EmploymentOpportunity(1, "Example Opportunity", "This is an example opportunity")

    # Add employment opportunity to user profile
    user_profile.add_employment_opportunity(opportunity)

    # Print user profile information
    print(f"Username: {user_profile.username}")
    print("Achievements:")
    for achievement in user_profile.achievements:
        print(f"- {achievement.name} ({achievement.achievement_type.value}): {'Unlocked' if achievement.unlocked else 'Locked'}")
    print("Rewards:")
    for reward in user_profile.rewards:
        print(f"- {reward.name} ({reward.reward_type.value})")
    print("Employment Opportunities:")
    for opportunity in user_profile.employment_opportunities:
        print(f"- {opportunity.title}: {opportunity.description}")

if __name__ == "__main__":
    main()
```
