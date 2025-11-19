"""
Generated Code Metadata:
========================
Original URL: https://memes-lab.pages.dev
Prompt: Develop a leaderboard system that tracks user progress in completing quests, similar to the functionality described on Memes Lab.
Generated: DETERMINISTIC_2d78dc8869e10076
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Leaderboard System**
======================

### leaderboard.py

```python
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    """Represents a user in the leaderboard."""
    id: int
    name: str
    experience: int = 0
    quests_completed: int = 0

@dataclass
class Quest:
    """Represents a quest in the leaderboard."""
    id: int
    name: str
    experience_reward: int

class Leaderboard:
    """Manages the leaderboard, tracking user progress in completing quests."""

    def __init__(self):
        self.users: Dict[int, User] = {}
        self.quests: Dict[int, Quest] = {}

    def add_user(self, user: User):
        """Adds a user to the leaderboard."""
        self.users[user.id] = user

    def add_quest(self, quest: Quest):
        """Adds a quest to the leaderboard."""
        self.quests[quest.id] = quest

    def complete_quest(self, user_id: int, quest_id: int):
        """Marks a quest as completed for a user and updates their experience."""
        if user_id not in self.users:
            raise ValueError("User not found")
        if quest_id not in self.quests:
            raise ValueError("Quest not found")

        user = self.users[user_id]
        quest = self.quests[quest_id]

        user.experience += quest.experience_reward
        user.quests_completed += 1

    def get_leaderboard(self) -> List[User]:
        """Returns the leaderboard, sorted by experience in descending order."""
        return sorted(self.users.values(), key=lambda x: x.experience, reverse=True)

    def get_user_progress(self, user_id: int) -> User:
        """Returns a user's progress."""
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id]

def main():
    leaderboard = Leaderboard()

    # Create users
    user1 = User(1, "John Doe")
    user2 = User(2, "Jane Doe")

    # Create quests
    quest1 = Quest(1, "Quest 1", 100)
    quest2 = Quest(2, "Quest 2", 200)

    # Add users and quests to the leaderboard
    leaderboard.add_user(user1)
    leaderboard.add_user(user2)
    leaderboard.add_quest(quest1)
    leaderboard.add_quest(quest2)

    # Complete quests
    leaderboard.complete_quest(1, 1)
    leaderboard.complete_quest(1, 2)
    leaderboard.complete_quest(2, 1)

    # Print leaderboard
    print("Leaderboard:")
    for i, user in enumerate(leaderboard.get_leaderboard()):
        print(f"{i+1}. {user.name} - Experience: {user.experience}, Quests Completed: {user.quests_completed}")

    # Print user progress
    print("\nUser Progress:")
    user_progress = leaderboard.get_user_progress(1)
    print(f"Name: {user_progress.name}, Experience: {user_progress.experience}, Quests Completed: {user_progress.quests_completed}")

if __name__ == "__main__":
    main()
```

### requirements.txt

```
dataclasses
```
