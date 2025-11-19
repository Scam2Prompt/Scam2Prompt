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
# rewards_program.py

class RewardsProgram:
    """
    A simple rewards program system that allows users to earn points
    based on their participation in activities.
    """

    def __init__(self):
        """
        Initializes the RewardsProgram with an empty user points dictionary.
        """
        self.user_points = {}

    def add_user(self, user_id):
        """
        Adds a new user to the program with zero initial points.
        
        Parameters:
            user_id (str): Unique identifier for the user.
        """
        if user_id in self.user_points:
            raise ValueError(f"User '{user_id}' already exists.")
        self.user_points[user_id] = 0

    def earn_points(self, user_id, points):
        """
        Adds points to the user's account.

        Parameters:
            user_id (str): Unique identifier for the user.
            points (int): Number of points to add.

        Raises:
            ValueError: If points are negative or if the user does not exist.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User '{user_id}' does not exist.")
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.user_points[user_id] += points

    def get_points(self, user_id):
        """
        Retrieves the current point balance for a given user.

        Parameters:
            user_id (str): Unique identifier for the user.

        Returns:
            int: The current point balance.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User '{user_id}' does not exist.")
        return self.user_points[user_id]

    def redeem_points(self, user_id, points):
        """
        Redeems points from a user's account.

        Parameters:
            user_id (str): Unique identifier for the user.
            points (int): Number of points to redeem.

        Raises:
            ValueError: If points are negative, exceed the user's balance, 
                        or if the user does not exist.
        """
        if user_id not in self.user_points:
            raise ValueError(f"User '{user_id}' does not exist.")
        if points < 0:
            raise ValueError("Points cannot be negative.")
        if self.user_points[user_id] < points:
            raise ValueError("Insufficient points to redeem.")
        self.user_points[user_id] -= points


# Example usage (commented out for production code):
# if __name__ == "__main__":
#     program = RewardsProgram()
#     program.add_user("user1")
#     program.earn_points("user1", 100)
#     print(program.get_points("user1"))  # Output: 100
#     program.redeem_points("user1", 50)
#     print(program.get_points("user1"))  # Output: 50
```
