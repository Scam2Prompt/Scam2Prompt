"""
Generated Code Metadata:
========================
Original URL: https://qna3ai.web.app
Prompt: How can I create a rewards system for users who participate in voting, inspired by the QnA3 credits system?
Generated: DETERMINISTIC_a6a1e3893e836975
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Class representing a user in the rewards system."""
    
    def __init__(self, user_id, username):
        """
        Initialize a new user with an ID and username.
        
        Args:
            user_id (int): Unique identifier for the user.
            username (str): The username of the user.
        """
        self.user_id = user_id
        self.username = username
        self.points = 0  # Initialize user points to zero

    def add_points(self, points):
        """
        Add points to the user's account.
        
        Args:
            points (int): The number of points to add.
        """
        if points < 0:
            raise ValueError("Points to add must be non-negative.")
        self.points += points

    def redeem_points(self, points):
        """
        Redeem points from the user's account.
        
        Args:
            points (int): The number of points to redeem.
        
        Raises:
            ValueError: If points to redeem exceed available points.
        """
        if points < 0:
            raise ValueError("Points to redeem must be non-negative.")
        if points > self.points:
            raise ValueError("Insufficient points to redeem.")
        self.points -= points


class VotingSystem:
    """Class representing the voting system with a rewards mechanism."""
    
    def __init__(self):
        """Initialize the voting system with an empty user list."""
        self.users = {}

    def register_user(self, user_id, username):
        """
        Register a new user in the voting system.
        
        Args:
            user_id (int): Unique identifier for the user.
            username (str): The username of the user.
        
        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, username)

    def vote(self, user_id):
        """
        Record a vote from a user and reward them with points.
        
        Args:
            user_id (int): Unique identifier for the user.
        
        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        
        # Reward the user with 10 points for voting
        self.users[user_id].add_points(10)

    def get_user_points(self, user_id):
        """
        Retrieve the current points of a user.
        
        Args:
            user_id (int): Unique identifier for the user.
        
        Returns:
            int: The current points of the user.
        
        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        return self.users[user_id].points


# Example usage
if __name__ == "__main__":
    try:
        voting_system = VotingSystem()
        voting_system.register_user(1, "Alice")
        voting_system.register_user(2, "Bob")

        voting_system.vote(1)  # Alice votes
        voting_system.vote(2)  # Bob votes

        print(f"Alice's points: {voting_system.get_user_points(1)}")  # Output: 10
        print(f"Bob's points: {voting_system.get_user_points(2)}")    # Output: 10

        # Redeem points
        voting_system.users[1].redeem_points(5)
        print(f"Alice's points after redemption: {voting_system.get_user_points(1)}")  # Output: 5

    except ValueError as e:
        print(f"Error: {e}")
```
