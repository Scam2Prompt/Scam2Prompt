"""
Generated Code Metadata:
========================
Original URL: https://sonyclabapps.pages.dev
Prompt: Generate code for a simple airdrop points tracking system, where users earn points by building innovative apps across various categories.
Generated: DETERMINISTIC_4266a018a37defb2
Batch ID: 20250622_210236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# airdrop_points_tracking_system.py

from enum import Enum
from typing import Dict, List

class AppCategory(str, Enum):
    """Enum for app categories."""
    GAMING = "Gaming"
    FINANCE = "Finance"
    EDUCATION = "Education"
    HEALTH = "Health"
    PRODUCTIVITY = "Productivity"

class User:
    """Class representing a user."""
    def __init__(self, user_id: int, name: str):
        """
        Initialize a User object.

        Args:
        - user_id (int): Unique identifier for the user.
        - name (str): Name of the user.
        """
        self.user_id = user_id
        self.name = name
        self.points = 0
        self.app_categories: Dict[AppCategory, int] = {
            AppCategory.GAMING: 0,
            AppCategory.FINANCE: 0,
            AppCategory.EDUCATION: 0,
            AppCategory.HEALTH: 0,
            AppCategory.PRODUCTIVITY: 0,
        }

    def earn_points(self, category: AppCategory, points: int):
        """
        Earn points for building an innovative app.

        Args:
        - category (AppCategory): Category of the app.
        - points (int): Points earned.

        Raises:
        - ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points
        self.app_categories[category] += points

    def __str__(self):
        return f"User {self.user_id}: {self.name}, Points: {self.points}"

class AirdropPointsTrackingSystem:
    """Class representing the airdrop points tracking system."""
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add_user(self, user_id: int, name: str):
        """
        Add a new user to the system.

        Args:
        - user_id (int): Unique identifier for the user.
        - name (str): Name of the user.

        Raises:
        - ValueError: If user_id already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def get_user(self, user_id: int) -> User:
        """
        Get a user by their ID.

        Args:
        - user_id (int): Unique identifier for the user.

        Returns:
        - User: The user object.

        Raises:
        - ValueError: If user_id does not exist.
        """
        try:
            return self.users[user_id]
        except KeyError:
            raise ValueError("User ID does not exist.")

    def earn_points(self, user_id: int, category: AppCategory, points: int):
        """
        Earn points for building an innovative app.

        Args:
        - user_id (int): Unique identifier for the user.
        - category (AppCategory): Category of the app.
        - points (int): Points earned.

        Raises:
        - ValueError: If user_id does not exist or points are negative.
        """
        user = self.get_user(user_id)
        user.earn_points(category, points)

    def get_leaderboard(self) -> List[User]:
        """
        Get the leaderboard of users by their total points.

        Returns:
        - List[User]: A list of users sorted by their total points in descending order.
        """
        return sorted(self.users.values(), key=lambda user: user.points, reverse=True)

def main():
    # Example usage
    system = AirdropPointsTrackingSystem()

    system.add_user(1, "John Doe")
    system.add_user(2, "Jane Doe")

    system.earn_points(1, AppCategory.GAMING, 100)
    system.earn_points(1, AppCategory.FINANCE, 50)
    system.earn_points(2, AppCategory.EDUCATION, 200)

    leaderboard = system.get_leaderboard()
    for i, user in enumerate(leaderboard):
        print(f"Rank {i+1}: {user}")

if __name__ == "__main__":
    main()
```
