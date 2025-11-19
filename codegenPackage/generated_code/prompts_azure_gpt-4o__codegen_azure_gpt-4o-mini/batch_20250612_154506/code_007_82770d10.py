"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Write a Python program to track and update user loyalty points based on their betting activity, as described in VZ99's VIP rewards system.
Generated: DETERMINISTIC_82770d100369b475
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Class to represent a user in the loyalty points system."""
    
    def __init__(self, user_id, name):
        """
        Initialize a new user with a unique ID and name.
        
        Args:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.
        """
        self.user_id = user_id
        self.name = name
        self.loyalty_points = 0

    def update_points(self, bet_amount):
        """
        Update the user's loyalty points based on their betting activity.
        
        Args:
            bet_amount (float): The amount the user has bet.
        
        Raises:
            ValueError: If bet_amount is negative.
        """
        if bet_amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        
        # Points are awarded at a rate of 1 point per $10 bet
        points_earned = int(bet_amount // 10)
        self.loyalty_points += points_earned
        return points_earned


class LoyaltySystem:
    """Class to manage the loyalty points system for multiple users."""
    
    def __init__(self):
        """Initialize the loyalty system with an empty user database."""
        self.users = {}

    def add_user(self, user_id, name):
        """
        Add a new user to the loyalty system.
        
        Args:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.
        
        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        
        self.users[user_id] = User(user_id, name)

    def place_bet(self, user_id, bet_amount):
        """
        Process a bet for a user and update their loyalty points.
        
        Args:
            user_id (str): Unique identifier for the user.
            bet_amount (float): The amount the user has bet.
        
        Raises:
            ValueError: If the user does not exist or if bet_amount is negative.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        points_earned = self.users[user_id].update_points(bet_amount)
        return points_earned

    def get_user_points(self, user_id):
        """
        Retrieve the current loyalty points for a user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            int: The current loyalty points of the user.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        return self.users[user_id].loyalty_points


# Example usage
if __name__ == "__main__":
    loyalty_system = LoyaltySystem()
    
    # Adding users
    try:
        loyalty_system.add_user("user123", "Alice")
        loyalty_system.add_user("user456", "Bob")
        
        # Placing bets
        points = loyalty_system.place_bet("user123", 150)
        print(f"Alice earned {points} points. Total points: {loyalty_system.get_user_points('user123')}")
        
        points = loyalty_system.place_bet("user456", 75)
        print(f"Bob earned {points} points. Total points: {loyalty_system.get_user_points('user456')}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
