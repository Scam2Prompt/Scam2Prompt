"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Create a function that tracks user progress through quests and upgrades in a game, inspired by the mechanics of Hamster Kombat.
Generated: DETERMINISTIC_18858ee35e0ec5b5
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, List

class GameProgressTracker:
    """
    A class to track user progress through quests and upgrades in a game.
    """

    def __init__(self):
        """
        Initialize the tracker with empty progress data for quests and upgrades.
        """
        self.user_data: Dict[str, Dict[str, List[str]]] = {}

    def add_user(self, user_id: str):
        """
        Add a new user to the tracker.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.user_data:
            raise ValueError(f"User '{user_id}' already exists.")
        self.user_data[user_id] = {
            'quests_completed': [],
            'upgrades_purchased': []
        }

    def complete_quest(self, user_id: str, quest_name: str):
        """
        Mark a quest as completed for a user.
        :param user_id: Unique identifier for the user.
        :param quest_name: Name of the quest to mark as completed.
        """
        if user_id not in self.user_data:
            raise ValueError(f"User '{user_id}' does not exist.")
        if quest_name in self.user_data[user_id]['quests_completed']:
            raise ValueError(f"Quest '{quest_name}' already completed by user '{user_id}'.")
        self.user_data[user_id]['quests_completed'].append(quest_name)

    def purchase_upgrade(self, user_id: str, upgrade_name: str):
        """
        Record an upgrade purchase for a user.
        :param user_id: Unique identifier for the user.
        :param upgrade_name: Name of the upgrade to record.
        """
        if user_id not in self.user_data:
            raise ValueError(f"User '{user_id}' does not exist.")
        if upgrade_name in self.user_data[user_id]['upgrades_purchased']:
            raise ValueError(f"Upgrade '{upgrade_name}' already purchased by user '{user_id}'.")
        self.user_data[user_id]['upgrades_purchased'].append(upgrade_name)

    def get_user_progress(self, user_id: str) -> Dict[str, List[str]]:
        """
        Get the progress of a user (quests completed and upgrades purchased).
        :param user_id: Unique identifier for the user.
        :return: Dictionary containing the user's progress.
        """
        if user_id not in self.user_data:
            raise ValueError(f"User '{user_id}' does not exist.")
        return self.user_data[user_id]

    def reset_user_progress(self, user_id: str):
        """
        Reset a user's progress (clear completed quests and purchased upgrades).
        :param user_id: Unique identifier for the user.
        """
        if user_id not in self.user_data:
            raise ValueError(f"User '{user_id}' does not exist.")
        self.user_data[user_id] = {
            'quests_completed': [],
            'upgrades_purchased': []
        }

# Example usage
if __name__ == "__main__":
    tracker = GameProgressTracker()

    # Add a user
    tracker.add_user("user123")

    # Complete quests
    tracker.complete_quest("user123", "Quest1")
    tracker.complete_quest("user123", "Quest2")

    # Purchase upgrades
    tracker.purchase_upgrade("user123", "UpgradeA")
    tracker.purchase_upgrade("user123", "UpgradeB")

    # Get user progress
    progress = tracker.get_user_progress("user123")
    print("User Progress:", progress)

    # Reset user progress
    tracker.reset_user_progress("user123")
    print("Progress after reset:", tracker.get_user_progress("user123"))
```
