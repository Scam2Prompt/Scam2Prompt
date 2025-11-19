"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nigger-2aa.pages.dev
Prompt: Generate a sample code for earning Karma Points through user activities on the Magic Square platform.
Generated: DETERMINISTIC_831f38bcbca183c5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Represents a user on the Magic Square platform."""
    
    def __init__(self, username):
        """Initializes a new user with a username and zero Karma Points."""
        self.username = username
        self.karma_points = 0

    def earn_karma(self, points):
        """Increases the user's Karma Points.

        Args:
            points (int): The number of Karma Points to earn. Must be positive.

        Raises:
            ValueError: If points is not a positive integer.
        """
        if not isinstance(points, int) or points <= 0:
            raise ValueError("Points must be a positive integer.")
        
        self.karma_points += points
        print(f"{self.username} earned {points} Karma Points. Total: {self.karma_points}")

    def redeem_karma(self, points):
        """Reduces the user's Karma Points.

        Args:
            points (int): The number of Karma Points to redeem. Must not exceed current points.

        Raises:
            ValueError: If points is not a positive integer or exceeds current Karma Points.
        """
        if not isinstance(points, int) or points <= 0:
            raise ValueError("Points must be a positive integer.")
        if points > self.karma_points:
            raise ValueError("Cannot redeem more Karma Points than currently held.")
        
        self.karma_points -= points
        print(f"{self.username} redeemed {points} Karma Points. Total: {self.karma_points}")

    def get_karma_points(self):
        """Returns the current Karma Points of the user."""
        return self.karma_points


class Activity:
    """Represents an activity that a user can perform to earn Karma Points."""
    
    def __init__(self, name, points):
        """Initializes a new activity.

        Args:
            name (str): The name of the activity.
            points (int): The number of Karma Points awarded for the activity. Must be positive.

        Raises:
            ValueError: If points is not a positive integer.
        """
        if not isinstance(points, int) or points <= 0:
            raise ValueError("Points must be a positive integer.")
        
        self.name = name
        self.points = points

    def perform(self, user):
        """Performs the activity for a user, awarding Karma Points.

        Args:
            user (User): The user performing the activity. Must be a User instance.

        Raises:
            TypeError: If the user is not an instance of User.
        """
        if not isinstance(user, User):
            raise TypeError("User must be an instance of the User class.")
        
        user.earn_karma(self.points)


# Example usage:
if __name__ == "__main__":
    # Create a new user
    user1 = User("Alice")
    
    # Create activities
    activity1 = Activity("Daily Login", 10)
    activity2 = Activity("Complete a Task", 20)

    # Perform activities
    activity1.perform(user1)
    activity2.perform(user1)

    # Redeem Karma Points
    try:
        user1.redeem_karma(15)  # Redeem 15 points
    except ValueError as e:
        print(f"Error: {e}")
    
    # Get current Karma Points
    print(f"{user1.username} has {user1.get_karma_points()} Karma Points.")
```
