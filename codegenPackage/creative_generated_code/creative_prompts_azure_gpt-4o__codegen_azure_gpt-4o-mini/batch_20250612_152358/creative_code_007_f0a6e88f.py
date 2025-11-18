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
# Import necessary libraries
from typing import List, Dict, Optional
import json
import uuid

# Define a class to represent a Quest
class Quest:
    def __init__(self, title: str, description: str, xp_reward: int):
        self.id = str(uuid.uuid4())  # Unique identifier for the quest
        self.title = title  # Title of the quest
        self.description = description  # Description of the quest
        self.xp_reward = xp_reward  # XP reward for completing the quest
        self.completed = False  # Status of the quest

    def complete(self):
        """Mark the quest as completed."""
        self.completed = True

# Define a class to represent a User
class User:
    def __init__(self, username: str):
        self.username = username  # Username of the user
        self.xp = 0  # Total XP the user has
        self.completed_quests: List[str] = []  # List of completed quests

    def complete_quest(self, quest: Quest):
        """Complete a quest and update XP."""
        if quest.id in self.completed_quests:
            raise ValueError("Quest already completed.")
        
        quest.complete()  # Mark the quest as completed
        self.xp += quest.xp_reward  # Add reward to the user's XP
        self.completed_quests.append(quest.id)  # Record completed quest

# Define a class to manage the Quest System
class QuestSystem:
    def __init__(self):
        self.quests: Dict[str, Quest] = {}  # Dictionary to store quests
        self.users: Dict[str, User] = {}  # Dictionary to store users

    def add_quest(self, title: str, description: str, xp_reward: int):
        """Add a new quest to the system."""
        if xp_reward < 0:
            raise ValueError("XP reward must be a non-negative integer.")
        
        new_quest = Quest(title, description, xp_reward)
        self.quests[new_quest.id] = new_quest

    def register_user(self, username: str):
        """Register a new user in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        
        new_user = User(username)
        self.users[username] = new_user

    def complete_quest_for_user(self, username: str, quest_id: str):
        """Allow a user to complete a quest by its ID."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        if quest_id not in self.quests:
            raise ValueError("Quest not found.")
        
        user = self.users[username]
        quest = self.quests[quest_id]
        user.complete_quest(quest)

    def get_user_info(self, username: str) -> Optional[Dict]:
        """Get the user's info including XP and completed quests."""
        if username not in self.users:
            return None
        
        user = self.users[username]
        return {
            "username": user.username,
            "xp": user.xp,
            "completed_quests": user.completed_quests
        }

# Example usage (Commented out to prevent execution on import)
if __name__ == "__main__":
    try:
        quest_system = QuestSystem()
        quest_system.register_user("player1")
        quest_system.add_quest("First Quest", "Complete your first task!", 100)
        
        # User completes a quest
        quest_id = list(quest_system.quests.keys())[0]  # Get the first quest ID
        quest_system.complete_quest_for_user("player1", quest_id)
        
        # Print user information
        user_info = quest_system.get_user_info("player1")
        print(json.dumps(user_info, indent=4))
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
