"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Describe how to create a points system for a socialfi platform that rewards users for engaging with environmental content, inspired by Everyworld's model.
Generated: DETERMINISTIC_9e3ab1774bd226b5
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# points_system.py

from datetime import datetime, timedelta
from typing import Dict

class User:
    def __init__(self, user_id: int):
        """
        Initialize a User object.

        Args:
        user_id (int): Unique identifier for the user.
        """
        self.user_id = user_id
        self.points = 0
        self.engagement_history = []

class EnvironmentalContent:
    def __init__(self, content_id: int, content_type: str):
        """
        Initialize an EnvironmentalContent object.

        Args:
        content_id (int): Unique identifier for the content.
        content_type (str): Type of environmental content (e.g., article, video, image).
        """
        self.content_id = content_id
        self.content_type = content_type

class PointsSystem:
    def __init__(self):
        """
        Initialize a PointsSystem object.
        """
        self.users: Dict[int, User] = {}
        self.content: Dict[int, EnvironmentalContent] = {}
        self.point_values = {
            'like': 10,
            'comment': 50,
            'share': 100,
            'view': 5
        }

    def add_user(self, user_id: int):
        """
        Add a new user to the points system.

        Args:
        user_id (int): Unique identifier for the user.
        """
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def add_content(self, content_id: int, content_type: str):
        """
        Add new environmental content to the points system.

        Args:
        content_id (int): Unique identifier for the content.
        content_type (str): Type of environmental content.
        """
        if content_id not in self.content:
            self.content[content_id] = EnvironmentalContent(content_id, content_type)

    def engage_with_content(self, user_id: int, content_id: int, engagement_type: str):
        """
        Record user engagement with environmental content.

        Args:
        user_id (int): Unique identifier for the user.
        content_id (int): Unique identifier for the content.
        engagement_type (str): Type of engagement (e.g., like, comment, share, view).

        Raises:
        ValueError: If the engagement type is not valid.
        """
        if user_id not in self.users:
            raise ValueError("User not found")
        if content_id not in self.content:
            raise ValueError("Content not found")
        if engagement_type not in self.point_values:
            raise ValueError("Invalid engagement type")

        user = self.users[user_id]
        content = self.content[content_id]

        # Update user points
        user.points += self.point_values[engagement_type]

        # Record engagement history
        user.engagement_history.append({
            'content_id': content_id,
            'engagement_type': engagement_type,
            'timestamp': datetime.now()
        })

    def get_user_points(self, user_id: int) -> int:
        """
        Get the current points balance for a user.

        Args:
        user_id (int): Unique identifier for the user.

        Returns:
        int: The user's current points balance.

        Raises:
        ValueError: If the user is not found.
        """
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].points

    def get_leaderboard(self, top_n: int = 10) -> list:
        """
        Get the top N users with the most points.

        Args:
        top_n (int): The number of top users to return (default: 10).

        Returns:
        list: A list of tuples containing user IDs and their points balances.
        """
        sorted_users = sorted(self.users.items(), key=lambda x: x[1].points, reverse=True)
        return [(user[0], user[1].points) for user in sorted_users[:top_n]]

def main():
    points_system = PointsSystem()

    # Add users
    points_system.add_user(1)
    points_system.add_user(2)

    # Add content
    points_system.add_content(1, 'article')
    points_system.add_content(2, 'video')

    # Simulate user engagement
    points_system.engage_with_content(1, 1, 'like')
    points_system.engage_with_content(1, 2, 'view')
    points_system.engage_with_content(2, 1, 'comment')

    # Get user points
    print(points_system.get_user_points(1))  # Output: 15
    print(points_system.get_user_points(2))  # Output: 50

    # Get leaderboard
    print(points_system.get_leaderboard())  # Output: [(2, 50), (1, 15)]

if __name__ == "__main__":
    main()
```
