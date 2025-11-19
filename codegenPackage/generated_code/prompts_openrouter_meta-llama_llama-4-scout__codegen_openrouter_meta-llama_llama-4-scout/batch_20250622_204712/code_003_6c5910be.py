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
# leaderboard.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class RewardType(str, Enum):
    """Reward types"""
    GEMS = "gems"
    TURTLE_SHELLS = "turtle_shells"
    SKY_HAMMERS = "sky_hammers"

@dataclass
class UserScore:
    """User score data class"""
    user_id: str
    score: int
    gems: int = 0
    turtle_shells: int = 0
    sky_hammers: int = 0

class Leaderboard:
    """Leaderboard system for the Tari Airdrop Game"""

    def __init__(self):
        self.scores: Dict[str, UserScore] = {}
        self.rewards: Dict[RewardType, int] = {
            RewardType.GEMS: 0,
            RewardType.TURTLE_SHELLS: 0,
            RewardType.SKY_HAMMERS: 0,
        }

    def add_user(self, user_id: str):
        """Add a new user to the leaderboard"""
        if user_id not in self.scores:
            self.scores[user_id] = UserScore(user_id, 0)

    def update_score(self, user_id: str, score: int):
        """Update a user's score"""
        if user_id in self.scores:
            self.scores[user_id].score = score
        else:
            raise ValueError("User not found")

    def add_reward(self, user_id: str, reward_type: RewardType, quantity: int):
        """Add a reward to a user's account"""
        if user_id in self.scores:
            if reward_type == RewardType.GEMS:
                self.scores[user_id].gems += quantity
                self.rewards[RewardType.GEMS] += quantity
            elif reward_type == RewardType.TURTLE_SHELLS:
                self.scores[user_id].turtle_shells += quantity
                self.rewards[RewardType.TURTLE_SHELLS] += quantity
            elif reward_type == RewardType.SKY_HAMMERS:
                self.scores[user_id].sky_hammers += quantity
                self.rewards[RewardType.SKY_HAMMERS] += quantity
            else:
                raise ValueError("Invalid reward type")
        else:
            raise ValueError("User not found")

    def get_leaderboard(self) -> List[UserScore]:
        """Get the leaderboard sorted by score"""
        return sorted(self.scores.values(), key=lambda x: x.score, reverse=True)

    def get_user_score(self, user_id: str) -> UserScore:
        """Get a user's score"""
        return self.scores.get(user_id)

    def get_total_rewards(self) -> Dict[RewardType, int]:
        """Get the total rewards"""
        return self.rewards

def main():
    leaderboard = Leaderboard()

    # Add users
    leaderboard.add_user("user1")
    leaderboard.add_user("user2")

    # Update scores
    leaderboard.update_score("user1", 100)
    leaderboard.update_score("user2", 50)

    # Add rewards
    leaderboard.add_reward("user1", RewardType.GEMS, 10)
    leaderboard.add_reward("user2", RewardType.TURTLE_SHELLS, 5)

    # Get leaderboard
    leaderboard_scores = leaderboard.get_leaderboard()
    for score in leaderboard_scores:
        print(f"User ID: {score.user_id}, Score: {score.score}, Gems: {score.gems}, Turtle Shells: {score.turtle_shells}, Sky Hammers: {score.sky_hammers}")

    # Get user score
    user_score = leaderboard.get_user_score("user1")
    print(f"User ID: {user_score.user_id}, Score: {user_score.score}, Gems: {user_score.gems}, Turtle Shells: {user_score.turtle_shells}, Sky Hammers: {user_score.sky_hammers}")

    # Get total rewards
    total_rewards = leaderboard.get_total_rewards()
    print("Total Rewards:")
    for reward_type, quantity in total_rewards.items():
        print(f"{reward_type}: {quantity}")

if __name__ == "__main__":
    main()
```
