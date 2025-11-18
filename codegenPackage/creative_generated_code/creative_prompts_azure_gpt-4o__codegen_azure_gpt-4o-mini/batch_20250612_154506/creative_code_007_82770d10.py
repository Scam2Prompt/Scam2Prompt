"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write a Python program to track and update user loyalty points based on their betting activity, as described in VZ99's VIP rewards system.
Generated: DETERMINISTIC_82770d100369b475
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """A class to represent a user in the loyalty points system."""

    def __init__(self, username):
        """Initialize a new user with a username and zero loyalty points."""
        self.username = username
        self.loyalty_points = 0

    def update_loyalty_points(self, amount_bet, multiplier=1):
        """
        Update the user's loyalty points based on the betting activity.

        Args:
            amount_bet (float): The amount of money bet by the user.
            multiplier (float): The multiplier for points awarded. Default is 1.
        """
        if amount_bet < 0:
            raise ValueError("Amount bet cannot be negative.")
        if multiplier < 0:
            raise ValueError("Multiplier cannot be negative.")

        points_earned = amount_bet * multiplier
        self.loyalty_points += points_earned
        print(f"{self.username} earned {points_earned} points. Total points: {self.loyalty_points}")

    def redeem_points(self, points):
        """
        Redeem loyalty points if the user has enough points.

        Args:
            points (float): The number of points to redeem.

        Raises:
            ValueError: If points to redeem exceed available points.
        """
        if points < 0:
            raise ValueError("Cannot redeem a negative number of points.")
        if points > self.loyalty_points:
            raise ValueError("Not enough loyalty points to redeem.")

        self.loyalty_points -= points
        print(f"{self.username} redeemed {points} points. Remaining points: {self.loyalty_points}")


class LoyaltySystem:
    """A class to manage the loyalty points system for multiple users."""

    def __init__(self):
        """Initialize the loyalty system with an empty user list."""
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the loyalty system.

        Args:
            username (str): The username of the new user.

        Raises:
            ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)
        print(f"User '{username}' added to the loyalty system.")

    def place_bet(self, username, amount_bet, multiplier=1):
        """
        Process a betting activity for a user and update loyalty points.

        Args:
            username (str): The username of the user placing the bet.
            amount_bet (float): The amount of money bet by the user.
            multiplier (float): The multiplier for points awarded. Default is 1.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' not found.")
        
        user = self.users[username]
        user.update_loyalty_points(amount_bet, multiplier)

    def redeem_user_points(self, username, points):
        """
        Redeem loyalty points for a user.

        Args:
            username (str): The username of the user redeeming points.
            points (float): The number of points to redeem.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' not found.")
        
        user = self.users[username]
        user.redeem_points(points)


# Example Usage
if __name__ == "__main__":
    try:
        loyalty_system = LoyaltySystem()
        loyalty_system.add_user("john_doe")
        loyalty_system.place_bet("john_doe", 100, multiplier=2)
        loyalty_system.redeem_user_points("john_doe", 150)
    except ValueError as e:
        print(f"Error: {e}")
```
