"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: How can I design a gamification strategy using Mystery Boxes to incentivize user participation in a mobile application?
Generated: DETERMINISTIC_7b6ec320b9cd876f
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from typing import List, Dict

class MysteryBox:
    """
    Represents a Mystery Box that can contain rewards.
    """

    def __init__(self, rewards: List[str]):
        """
        Initializes the Mystery Box with a list of rewards.

        :param rewards: List of rewards contained in the Mystery Box.
        """
        if not rewards:
            raise ValueError("Rewards list cannot be empty.")
        self.rewards = rewards

    def open_box(self) -> str:
        """
        Opens the Mystery Box and returns a randomly selected reward.

        :return: A reward from the Mystery Box.
        """
        return random.choice(self.rewards)


class User:
    """
    Represents a user in the application who can earn Mystery Boxes.
    """

    def __init__(self, username: str):
        """
        Initializes the User with a username and a rewards history.

        :param username: The username of the user.
        """
        self.username = username
        self.rewards_history = []

    def earn_mystery_box(self, box: MysteryBox) -> None:
        """
        Allows the user to open a Mystery Box and earn a reward.

        :param box: The Mystery Box to be opened.
        """
        reward = box.open_box()
        self.rewards_history.append(reward)
        print(f"{self.username} opened a Mystery Box and earned: {reward}")

    def get_rewards_history(self) -> List[str]:
        """
        Returns the user's rewards history.

        :return: List of rewards earned by the user.
        """
        return self.rewards_history


class GamificationSystem:
    """
    Manages the gamification aspects of the application.
    """

    def __init__(self):
        self.users: Dict[str, User] = {}
        self.mystery_boxes: List[MysteryBox] = []

    def add_user(self, username: str) -> None:
        """
        Adds a new user to the system.

        :param username: The username of the user to add.
        """
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username)
        print(f"User {username} added successfully.")

    def create_mystery_box(self, rewards: List[str]) -> None:
        """
        Creates a Mystery Box with specified rewards and adds it to the system.

        :param rewards: List of rewards for the Mystery Box.
        """
        box = MysteryBox(rewards)
        self.mystery_boxes.append(box)
        print("Mystery Box created with rewards.")

    def let_user_open_box(self, username: str) -> None:
        """
        Allows a user to open a Mystery Box.

        :param username: The username of the user.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        if not self.mystery_boxes:
            raise ValueError("No Mystery Boxes available.")

        user = self.users[username]
        box = random.choice(self.mystery_boxes)
        user.earn_mystery_box(box)

    def get_user_rewards(self, username: str) -> List[str]:
        """
        Retrieves the rewards history for a specific user.

        :param username: The username of the user.
        :return: List of rewards earned by the user.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.users[username].get_rewards_history()


# Example Usage:
if __name__ == "__main__":
    try:
        gamification_system = GamificationSystem()

        # Adding users
        gamification_system.add_user("Alice")
        gamification_system.add_user("Bob")

        # Creating Mystery Boxes
        gamification_system.create_mystery_box(["10 Points", "20 Points", "50 Points"])
        gamification_system.create_mystery_box(["Bonus Item", "Free Access", "Special Badge"])

        # Users opening Mystery Boxes
        gamification_system.let_user_open_box("Alice")
        gamification_system.let_user_open_box("Bob")

        # Getting rewards history
        print(f"Alice's rewards: {gamification_system.get_user_rewards('Alice')}")
        print(f"Bob's rewards: {gamification_system.get_user_rewards('Bob')}")

    except ValueError as e:
        print(f"Error: {e}")
```
