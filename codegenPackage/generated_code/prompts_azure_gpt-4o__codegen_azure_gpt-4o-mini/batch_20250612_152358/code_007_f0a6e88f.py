"""
Generated Code Metadata:
========================
Original URL: https://memes-lab.pages.dev
Prompt: Suggest an architecture for implementing a gamified quest system with XP tracking and reward claiming, inspired by Memes Lab.
Generated: DETERMINISTIC_f0a6e88f0bc6c483
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quest_system.py

class Quest:
    """
    Represents a quest in the gamified system.
    Each quest has a title, description, experience points (XP) reward, and a completion status.
    """
    def __init__(self, title: str, description: str, xp_reward: int):
        self.title = title
        self.description = description
        self.xp_reward = xp_reward
        self.completed = False

    def complete_quest(self):
        """Mark the quest as completed."""
        if not self.completed:
            self.completed = True
            return self.xp_reward
        raise ValueError("Quest already completed.")


class User:
    """
    Represents a user in the gamified system.
    Each user has a username, total XP, and a list of quests.
    """
    def __init__(self, username: str):
        self.username = username
        self.total_xp = 0
        self.quests = []

    def add_quest(self, quest: Quest):
        """Add a quest to the user's quest list."""
        self.quests.append(quest)

    def complete_quest(self, quest_title: str):
        """Complete a quest by its title and update the user's XP."""
        for quest in self.quests:
            if quest.title == quest_title:
                xp_gained = quest.complete_quest()
                self.total_xp += xp_gained
                return xp_gained
        raise ValueError("Quest not found or already completed.")


class Reward:
    """
    Represents a reward that can be claimed by the user.
    Each reward has a name, description, and the required XP to claim it.
    """
    def __init__(self, name: str, description: str, required_xp: int):
        self.name = name
        self.description = description
        self.required_xp = required_xp
        self.claimed = False

    def claim_reward(self, user: User):
        """Claim the reward if the user has enough XP."""
        if user.total_xp >= self.required_xp and not self.claimed:
            self.claimed = True
            return True
        raise ValueError("Not enough XP or reward already claimed.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a user
        user = User("Player1")

        # Create quests
        quest1 = Quest("First Quest", "Complete the first task.", 100)
        quest2 = Quest("Second Quest", "Complete the second task.", 200)

        # Add quests to user
        user.add_quest(quest1)
        user.add_quest(quest2)

        # Complete quests and track XP
        xp_gained = user.complete_quest("First Quest")
        print(f"{user.username} gained {xp_gained} XP. Total XP: {user.total_xp}")

        # Create a reward
        reward1 = Reward("Starter Pack", "A pack of useful items.", 150)

        # Attempt to claim the reward
        if reward1.claim_reward(user):
            print(f"{user.username} claimed the reward: {reward1.name}")

    except ValueError as e:
        print(f"Error: {e}")
```
