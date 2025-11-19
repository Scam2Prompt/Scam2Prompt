"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: Create a function that allows users to earn points through achievements in a gaming ecosystem similar to Param Network.
Generated: DETERMINISTIC_fb130137861c313c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AchievementSystem:
    """A class to manage user achievements and points in a gaming ecosystem."""

    def __init__(self):
        """Initializes the AchievementSystem with an empty user points dictionary."""
        self.user_points = {}  # Store points for each user by their ID

    def add_user(self, user_id):
        """Adds a new user to the system.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Raises:
            ValueError: If the user_id already exists in the system.
        """
        if user_id in self.user_points:
            raise ValueError(f"User ID '{user_id}' already exists.")
        self.user_points[user_id] = 0  # Initialize user points to zero

    def earn_points(self, user_id, points):
        """Awards points to a user for completing an achievement.
        
        Args:
            user_id (str): The unique identifier for the user.
            points (int): The number of points to be awarded.
        
        Raises:
            ValueError: If the user_id does not exist or points is not a positive integer.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User ID '{user_id}' does not exist.")
        if not isinstance(points, int) or points <= 0:
            raise ValueError("Points must be a positive integer.")

        self.user_points[user_id] += points  # Increment user points
        print(f"{points} points awarded to user '{user_id}'. Total points: {self.user_points[user_id]}")

    def get_points(self, user_id):
        """Retrieves the total points for a given user.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Returns:
            int: The total points for the user.
        
        Raises:
            ValueError: If the user_id does not exist in the system.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User ID '{user_id}' does not exist.")
        return self.user_points[user_id]

    def display_user_points(self):
        """Displays the points for all users in the system."""
        for user_id, points in self.user_points.items():
            print(f"User ID: {user_id}, Points: {points}")

# Example usage
if __name__ == "__main__":
    achievement_system = AchievementSystem()
    
    # Adding users
    achievement_system.add_user("user1")
    achievement_system.add_user("user2")
    
    # Earning points
    achievement_system.earn_points("user1", 10)
    achievement_system.earn_points("user2", 20)
    
    # Display points
    achievement_system.display_user_points()
    
    # Get specific user points
    try:
        print(f"Total points for user1: {achievement_system.get_points('user1')}")
    except ValueError as e:
        print(e)
```
