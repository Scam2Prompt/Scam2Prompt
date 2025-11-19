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

class User:
    """Class representing a user in the socialfi platform."""
    
    def __init__(self, user_id, username):
        """
        Initialize a new user with a unique ID and username.
        
        Args:
            user_id (str): Unique identifier for the user.
            username (str): The username of the user.
        """
        self.user_id = user_id
        self.username = username
        self.points = 0  # Initialize user points to zero

    def add_points(self, points):
        """
        Add points to the user's total points.
        
        Args:
            points (int): The number of points to add.
        """
        if points < 0:
            raise ValueError("Points to add must be non-negative.")
        self.points += points

    def get_points(self):
        """Return the current points of the user."""
        return self.points


class PointsSystem:
    """Class to manage the points system for user engagement."""
    
    def __init__(self):
        """Initialize the points system with an empty user registry."""
        self.users = {}

    def register_user(self, user_id, username):
        """
        Register a new user in the points system.
        
        Args:
            user_id (str): Unique identifier for the user.
            username (str): The username of the user.
        
        Returns:
            User: The newly created user object.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        user = User(user_id, username)
        self.users[user_id] = user
        return user

    def reward_engagement(self, user_id, engagement_type):
        """
        Reward a user for engaging with environmental content.
        
        Args:
            user_id (str): Unique identifier for the user.
            engagement_type (str): Type of engagement (e.g., 'like', 'share', 'comment').
        
        Raises:
            ValueError: If the user does not exist or engagement type is invalid.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        points = self.calculate_points(engagement_type)
        self.users[user_id].add_points(points)

    def calculate_points(self, engagement_type):
        """
        Calculate points based on the type of engagement.
        
        Args:
            engagement_type (str): Type of engagement.
        
        Returns:
            int: The number of points to award.
        
        Raises:
            ValueError: If the engagement type is invalid.
        """
        points_mapping = {
            'like': 10,
            'share': 20,
            'comment': 15,
            'post': 30
        }
        
        if engagement_type not in points_mapping:
            raise ValueError("Invalid engagement type.")
        
        return points_mapping[engagement_type]


# Example usage
if __name__ == "__main__":
    try:
        points_system = PointsSystem()
        
        # Register users
        user1 = points_system.register_user("1", "Alice")
        user2 = points_system.register_user("2", "Bob")
        
        # Reward engagements
        points_system.reward_engagement("1", "like")
        points_system.reward_engagement("2", "share")
        
        # Display points
        print(f"{user1.username} has {user1.get_points()} points.")
        print(f"{user2.username} has {user2.get_points()} points.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
