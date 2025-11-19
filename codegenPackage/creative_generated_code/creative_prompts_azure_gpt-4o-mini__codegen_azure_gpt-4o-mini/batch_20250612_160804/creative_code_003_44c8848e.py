"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pufferr.pages.dev
Prompt: Generate a function that allows users to earn points for participating in a rewards program, similar to the Puffer Points system mentioned on the site.
Generated: DETERMINISTIC_44c8848e2d98c35f
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardsProgram:
    def __init__(self):
        """
        Initializes the RewardsProgram with an empty user points dictionary.
        """
        self.user_points = {}

    def add_user(self, user_id):
        """
        Adds a new user to the rewards program.
        
        Parameters:
        user_id (str): Unique identifier for the user.
        
        Raises:
        ValueError: If the user already exists in the rewards program.
        """
        if user_id in self.user_points:
            raise ValueError(f"User '{user_id}' already exists.")
        self.user_points[user_id] = 0

    def earn_points(self, user_id, points):
        """
        Allows a user to earn points for participating in the rewards program.
        
        Parameters:
        user_id (str): Unique identifier for the user.
        points (int): Number of points to be added to the user's account.
        
        Raises:
        ValueError: If the user does not exist or points are negative.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User '{user_id}' does not exist.")
        if points < 0:
            raise ValueError("Points cannot be negative.")

        self.user_points[user_id] += points

    def get_points(self, user_id):
        """
        Retrieves the current points for a user.
        
        Parameters:
        user_id (str): Unique identifier for the user.
        
        Returns:
        int: The current points of the user.
        
        Raises:
        ValueError: If the user does not exist.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User '{user_id}' does not exist.")
        
        return self.user_points[user_id]

    def redeem_points(self, user_id, points):
        """
        Allows a user to redeem points from their account.
        
        Parameters:
        user_id (str): Unique identifier for the user.
        points (int): Number of points to be redeemed.
        
        Raises:
        ValueError: If the user does not exist, points are negative, or insufficient points.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User '{user_id}' does not exist.")
        if points < 0:
            raise ValueError("Points cannot be negative.")
        if self.user_points[user_id] < points:
            raise ValueError("Insufficient points for redemption.")

        self.user_points[user_id] -= points

# Example usage:
if __name__ == "__main__":
    rewards_program = RewardsProgram()
    try:
        rewards_program.add_user("user123")
        rewards_program.earn_points("user123", 150)
        print("User points:", rewards_program.get_points("user123"))  # Output: User points: 150
        rewards_program.redeem_points("user123", 50)
        print("User points after redemption:", rewards_program.get_points("user123"))  # Output: User points after redemption: 100
    except ValueError as e:
        print(e)
```
