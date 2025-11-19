"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Create a function to implement a loyalty rewards program for users, inspired by the features mentioned on the BaxBet platform.
Generated: DETERMINISTIC_76c32c2b4076400b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoyaltyProgram:
    def __init__(self):
        """
        Initializes the LoyaltyProgram with an empty user database.
        Each user will have a unique ID, a name, and a reward points balance.
        """
        self.users = {}

    def add_user(self, user_id: str, name: str) -> None:
        """
        Adds a new user to the loyalty program.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :raises ValueError: If the user_id already exists
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        self.users[user_id] = {'name': name, 'points': 0}

    def add_points(self, user_id: str, points: int) -> None:
        """
        Adds points to a user's account.

        :param user_id: Unique identifier for the user
        :param points: Number of points to add
        :raises ValueError: If the user_id does not exist or points are negative
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        if points < 0:
            raise ValueError("Points to add must be non-negative.")
        
        self.users[user_id]['points'] += points

    def redeem_points(self, user_id: str, points: int) -> None:
        """
        Redeems points from a user's account.

        :param user_id: Unique identifier for the user
        :param points: Number of points to redeem
        :raises ValueError: If the user_id does not exist, points are negative, or insufficient points
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        if points < 0:
            raise ValueError("Points to redeem must be non-negative.")
        if self.users[user_id]['points'] < points:
            raise ValueError("Insufficient points to redeem.")

        self.users[user_id]['points'] -= points

    def get_user_points(self, user_id: str) -> int:
        """
        Retrieves the current points balance for a user.

        :param user_id: Unique identifier for the user
        :return: Current points balance
        :raises ValueError: If the user_id does not exist
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        return self.users[user_id]['points']

    def __str__(self) -> str:
        """
        Returns a string representation of the loyalty program's user database.
        """
        return str(self.users)


# Example usage:
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Adding users
    loyalty_program.add_user("user1", "Alice")
    loyalty_program.add_user("user2", "Bob")

    # Adding points
    loyalty_program.add_points("user1", 100)
    loyalty_program.add_points("user2", 50)

    # Redeeming points
    loyalty_program.redeem_points("user1", 30)

    # Getting user points
    print(f"Alice's points: {loyalty_program.get_user_points('user1')}")
    print(f"Bob's points: {loyalty_program.get_user_points('user2')}")

    # Print the current state of the loyalty program
    print(loyalty_program)
```
