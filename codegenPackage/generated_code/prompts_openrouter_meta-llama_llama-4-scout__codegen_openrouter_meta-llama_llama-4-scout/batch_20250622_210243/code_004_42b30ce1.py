"""
Generated Code Metadata:
========================
Original URL: https://mocaverse-b29.pages.dev
Prompt: "Create a library to track and manage Moca XP Rankings and Experiences on the Mocaverse platform."
Generated: DETERMINISTIC_42b30ce1f7686ca6
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# moca_xp_rankings.py

"""
Library to track and manage Moca XP Rankings and Experiences on the Mocaverse platform.
"""

import logging
from typing import Dict, List

class MocaXPRankings:
    def __init__(self):
        """
        Initialize the MocaXPRankings library.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Initialize an empty dictionary to store user XP rankings
        self.user_rankings: Dict[str, int] = {}

        # Initialize an empty dictionary to store user experiences
        self.user_experiences: Dict[str, List[str]] = {}

    def add_user(self, user_id: str):
        """
        Add a new user to the rankings.

        Args:
            user_id (str): The ID of the user to add.

        Raises:
            ValueError: If the user ID is empty or None.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty or None")

        if user_id not in self.user_rankings:
            self.user_rankings[user_id] = 0
            self.user_experiences[user_id] = []

    def update_user_xp(self, user_id: str, xp: int):
        """
        Update a user's XP ranking.

        Args:
            user_id (str): The ID of the user to update.
            xp (int): The new XP value.

        Raises:
            ValueError: If the user ID is empty or None.
            ValueError: If the XP value is negative.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty or None")
        if xp < 0:
            raise ValueError("XP value cannot be negative")

        if user_id in self.user_rankings:
            self.user_rankings[user_id] = xp
        else:
            self.add_user(user_id)
            self.user_rankings[user_id] = xp

    def add_user_experience(self, user_id: str, experience: str):
        """
        Add a new experience to a user's profile.

        Args:
            user_id (str): The ID of the user to update.
            experience (str): The new experience to add.

        Raises:
            ValueError: If the user ID is empty or None.
            ValueError: If the experience is empty or None.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty or None")
        if not experience:
            raise ValueError("Experience cannot be empty or None")

        if user_id in self.user_experiences:
            self.user_experiences[user_id].append(experience)
        else:
            self.add_user(user_id)
            self.user_experiences[user_id] = [experience]

    def get_user_ranking(self, user_id: str) -> int:
        """
        Get a user's XP ranking.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            int: The user's XP ranking.

        Raises:
            ValueError: If the user ID is empty or None.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty or None")

        return self.user_rankings.get(user_id, 0)

    def get_user_experiences(self, user_id: str) -> List[str]:
        """
        Get a user's experiences.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            List[str]: The user's experiences.

        Raises:
            ValueError: If the user ID is empty or None.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty or None")

        return self.user_experiences.get(user_id, [])

    def __str__(self):
        """
        Return a string representation of the MocaXPRankings library.

        Returns:
            str: A string representation of the library.
        """
        return f"MocaXPRankings(user_rankings={self.user_rankings}, user_experiences={self.user_experiences})"


def main():
    # Create a new instance of the MocaXPRankings library
    moca_xp_rankings = MocaXPRankings()

    # Add some users
    moca_xp_rankings.add_user("user1")
    moca_xp_rankings.add_user("user2")

    # Update user XP rankings
    moca_xp_rankings.update_user_xp("user1", 100)
    moca_xp_rankings.update_user_xp("user2", 200)

    # Add user experiences
    moca_xp_rankings.add_user_experience("user1", "experience1")
    moca_xp_rankings.add_user_experience("user2", "experience2")

    # Get user rankings and experiences
    print(moca_xp_rankings.get_user_ranking("user1"))  # Output: 100
    print(moca_xp_rankings.get_user_experiences("user2"))  # Output: ['experience2']

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
```
