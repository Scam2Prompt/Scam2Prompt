"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-lab.pages.dev
Prompt: Suggest an architecture for implementing a gamified quest system with XP tracking and reward claiming, inspired by Memes Lab.
Generated: DETERMINISTIC_f0a6e88f0bc6c483
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Gamified Quest System with XP Tracking and Reward Claiming

This system implements the core architecture for a quest-based gamification system.
It includes tracking XP, completing quests, and claiming rewards.
"""

from typing import List, Dict, Optional


# --- Models ---
class User:
    """
    Represents a user in the gamified system.
    """
    def __init__(self, username: str):
        self.username = username
        self.xp = 0  # User's XP
        self.completed_quests = set()  # Set for tracking completed quest IDs
        self.claimed_rewards = set()  # Set for tracking claimed reward IDs


class Quest:
    """
    Represents a quest within the system.
    """
    def __init__(self, quest_id: str, description: str, xp_reward: int):
        self.quest_id = quest_id
        self.description = description
        self.xp_reward = xp_reward  # XP awarded upon quest completion


class Reward:
    """
    Represents a reward that can be claimed by the user based on XP.
    """
    def __init__(self, reward_id: str, description: str, xp_required: int):
        self.reward_id = reward_id
        self.description = description
        self.xp_required = xp_required  # XP required to claim the reward


# --- Service Layer ---
class GamifiedQuestSystem:
    """
    Core service class for the gamified quest system.
    """
    def __init__(self):
        self.users: Dict[str, User] = {}  # A dictionary of users by username
        self.quests: Dict[str, Quest] = {}  # A dictionary of quests by quest_id
        self.rewards: Dict[str, Reward] = {}  # A dictionary of rewards by reward_id

    # User management
    def register_user(self, username: str) -> User:
        """
        Registers a new user in the system.
        """
        if username in self.users:
            raise ValueError(f"Username '{username}' is already taken.")
        user = User(username)
        self.users[username] = user
        return user

    def get_user(self, username: str) -> Optional[User]:
        """
        Retrieves a user by username.
        """
        return self.users.get(username)

    # Quest management
    def add_quest(self, quest_id: str, description: str, xp_reward: int) -> Quest:
        """
        Adds a new quest to the system.
        """
        if quest_id in self.quests:
            raise ValueError(f"Quest ID '{quest_id}' already exists.")
        quest = Quest(quest_id, description, xp_reward)
        self.quests[quest_id] = quest
        return quest

    def complete_quest(self, username: str, quest_id: str) -> str:
        """
        Marks a quest as completed for a specific user and awards XP.
        """
        user = self.get_user(username)
        if not user:
            raise ValueError(f"User '{username}' does not exist.")
        quest = self.quests.get(quest_id)
        if not quest:
            raise ValueError(f"Quest ID '{quest_id}' does not exist.")
        if quest_id in user.completed_quests:
            raise ValueError(f"Quest '{quest_id}' has already been completed by the user.")
        
        # Award XP and mark quest as completed
        user.xp += quest.xp_reward
        user.completed_quests.add(quest_id)
        return f"Quest '{quest.description}' completed! {quest.xp_reward} XP awarded."

    # Reward claiming
    def add_reward(self, reward_id: str, description: str, xp_required: int) -> Reward:
        """
        Adds a new reward to the system.
        """
        if reward_id in self.rewards:
            raise ValueError(f"Reward ID '{reward_id}' already exists.")
        reward = Reward(reward_id, description, xp_required)
        self.rewards[reward_id] = reward
        return reward

    def claim_reward(self, username: str, reward_id: str) -> str:
        """
        Allows a user to claim a reward if they have enough XP.
        """
        user = self.get_user(username)
        if not user:
            raise ValueError(f"User '{username}' does not exist.")
        reward = self.rewards.get(reward_id)
        if not reward:
            raise ValueError(f"Reward ID '{reward_id}' does not exist.")
        if reward_id in user.claimed_rewards:
            raise ValueError(f"Reward '{reward_id}' has already been claimed by the user.")
        if user.xp < reward.xp_required:
            raise ValueError(f"User '{username}' does not have enough XP to claim this reward.")

        # Mark reward as claimed
        user.claimed_rewards.add(reward_id)
        return f"Reward '{reward.description}' claimed!"

    # System stats
    def user_summary(self, username: str) -> Dict[str, any]:
        """
        Retrieves a summary of a user's progress and stats.
        """
        user = self.get_user(username)
        if not user:
            raise ValueError(f"User '{username}' does not exist.")
        return {
            "username": user.username,
            "xp": user.xp,
            "completed_quests": list(user.completed_quests),
            "claimed_rewards": list(user.claimed_rewards)
        }


# --- Example Usage ---
if __name__ == "__main__":
    # Initialize the system
    system = GamifiedQuestSystem()

    # Add users
    system.register_user("player1")

    # Add quests
    system.add_quest("quest1", "Complete the first challenge", 100)
    system.add_quest("quest2", "Solve the riddle", 200)

    # Add rewards
    system.add_reward("reward1", "Bronze Trophy", 150)
    system.add_reward("reward2", "Silver Trophy", 300)

    # Player completes a quest
    print(system.complete_quest("player1", "quest1"))

    # Player claims a reward
    print(system.claim_reward("player1", "reward1"))

    # Display user summary
    print(system.user_summary("player1"))
```
