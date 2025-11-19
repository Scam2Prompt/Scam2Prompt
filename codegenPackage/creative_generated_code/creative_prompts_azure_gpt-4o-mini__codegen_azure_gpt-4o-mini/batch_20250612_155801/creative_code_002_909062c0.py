"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Generate a sample code for a loyalty program that rewards users with points for playing games, inspired by the venez888 rewards system.
Generated: DETERMINISTIC_909062c0b3270c1d
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    """
    A class to represent a loyalty program that rewards users with points for playing games.
    Inspired by the venez888 rewards system.
    """

    def __init__(self):
        """
        Initializes the loyalty program with an empty users dictionary.
        """
        self.users = {}

    def add_user(self, user_id):
        """
        Adds a new user to the loyalty program.

        :param user_id: Unique identifier for the user
        :raises ValueError: If user_id already exists
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        self.users[user_id] = 0  # Initialize with 0 points

    def remove_user(self, user_id):
        """
        Removes a user from the loyalty program.

        :param user_id: Unique identifier for the user
        :raises ValueError: If user_id does not exist
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        del self.users[user_id]

    def reward_points(self, user_id, points):
        """
        Rewards points to a user for playing games.

        :param user_id: Unique identifier for the user
        :param points: Number of points to reward
        :raises ValueError: If user_id does not exist or points is negative
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        if points < 0:
            raise ValueError("Points cannot be negative.")

        self.users[user_id] += points

    def get_user_points(self, user_id):
        """
        Retrieves the total points for a user.

        :param user_id: Unique identifier for the user
        :return: Total points of the user
        :raises ValueError: If user_id does not exist
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        return self.users[user_id]

    def display_users(self):
        """
        Displays all users and their points in the loyalty program.
        """
        for user_id, points in self.users.items():
            print(f"User ID: {user_id}, Points: {points}")


if __name__ == "__main__":
    # Sample usage of the LoyaltyProgram class
    loyalty_program = LoyaltyProgram()

    try:
        loyalty_program.add_user("user1")
        loyalty_program.reward_points("user1", 10)
        print(f"User1 Points: {loyalty_program.get_user_points('user1')}")
        
        loyalty_program.add_user("user2")
        loyalty_program.reward_points("user2", 20)
        
        # Display all users
        loyalty_program.display_users()
        
        # Attempt to remove a user
        loyalty_program.remove_user("user1")
        loyalty_program.display_users()

    except ValueError as e:
        print(f"Error: {e}")
```
