"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starsarena.trade
Prompt: What are the best practices for creating a user engagement system in a SocialFi experience?
Generated: DETERMINISTIC_1e3f2759e9a4453d
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Engagement System for a SocialFi Experience

This Python code implements a user engagement system following best practices 
for scalability, maintainability, and performance.
"""

import datetime
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom exception for the engagement system
class EngagementSystemError(Exception):
    pass

class UserEngagementSystem:
    """
    A class to manage user engagement in a SocialFi experience.
    """

    def __init__(self):
        # Store user data and engagement metrics
        self.users = {}  # {user_id: {'name': str, 'points': int, 'last_engaged': datetime}}

    def add_user(self, user_id: str, name: str) -> None:
        """
        Add a new user to the system.
        Parameters:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.
        Raises:
            EngagementSystemError: If the user_id already exists.
        """
        if user_id in self.users:
            raise EngagementSystemError(f"User ID {user_id} already exists.")
        self.users[user_id] = {'name': name, 'points': 0, 'last_engaged': None}
        logging.info(f"User {name} added successfully.")

    def engage_user(self, user_id: str, points: int) -> None:
        """
        Engage a user and update their points.
        Parameters:
            user_id (str): Unique identifier for the user.
            points (int): Number of points to add for engagement.
        Raises:
            EngagementSystemError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise EngagementSystemError(f"User ID {user_id} does not exist.")
        self.users[user_id]['points'] += points
        self.users[user_id]['last_engaged'] = datetime.datetime.now()
        logging.info(f"User {self.users[user_id]['name']} engaged with {points} points.")

    def get_user_stats(self, user_id: str) -> Dict:
        """
        Retrieve user engagement statistics.
        Parameters:
            user_id (str): Unique identifier for the user.
        Returns:
            dict: User statistics including name, points, and last engagement time.
        Raises:
            EngagementSystemError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise EngagementSystemError(f"User ID {user_id} does not exist.")
        return self.users[user_id]

    def leaderboard(self, top_n: int = 10) -> List[Dict]:
        """
        Generate a leaderboard sorted by points.
        Parameters:
            top_n (int): Number of top users to return (default is 10).
        Returns:
            list: List of top users sorted by points.
        """
        sorted_users = sorted(
            self.users.items(),
            key=lambda x: x[1]['points'],
            reverse=True
        )
        return [
            {'user_id': user_id, 'name': data['name'], 'points': data['points']}
            for user_id, data in sorted_users[:top_n]
        ]

if __name__ == "__main__":
    # Example usage of the UserEngagementSystem
    engagement_system = UserEngagementSystem()

    try:
        # Add users
        engagement_system.add_user('user1', 'Alice')
        engagement_system.add_user('user2', 'Bob')

        # Engage users
        engagement_system.engage_user('user1', 50)
        engagement_system.engage_user('user2', 30)

        # Display user stats
        print("User stats for Alice:", engagement_system.get_user_stats('user1'))

        # Display leaderboard
        print("Leaderboard:", engagement_system.leaderboard())
    except EngagementSystemError as e:
        logging.error(f"Error in engagement system: {e}")
```
