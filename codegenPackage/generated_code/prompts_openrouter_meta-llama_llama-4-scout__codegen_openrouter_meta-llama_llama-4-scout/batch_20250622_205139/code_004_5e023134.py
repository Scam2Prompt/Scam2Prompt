"""
Generated Code Metadata:
========================
Original URL: https://sophon.xyz
Prompt: Design a basic loyalty program using Sophon's distribution layer and verified user data.
Generated: DETERMINISTIC_5e0231347f106a3f
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

from typing import Dict
from sophon.distribution_layer import DistributionLayer
from sophon.user_data import VerifiedUser

class LoyaltyProgram:
    def __init__(self, distribution_layer: DistributionLayer):
        """
        Initialize the loyalty program with a Sophon distribution layer.

        Args:
        - distribution_layer (DistributionLayer): The Sophon distribution layer.
        """
        self.distribution_layer = distribution_layer
        self.users: Dict[str, int] = {}  # Stores user IDs and their points

    def add_user(self, user: VerifiedUser):
        """
        Add a verified user to the loyalty program.

        Args:
        - user (VerifiedUser): The verified user to add.
        """
        user_id = user.id
        if user_id not in self.users:
            self.users[user_id] = 0  # Initialize points to 0

    def earn_points(self, user_id: str, points: int):
        """
        Earn points for a user.

        Args:
        - user_id (str): The ID of the user.
        - points (int): The points to earn.

        Raises:
        - ValueError: If the user ID is not in the program.
        """
        if user_id not in self.users:
            raise ValueError("User not in the loyalty program")
        self.users[user_id] += points

    def redeem_points(self, user_id: str, points: int):
        """
        Redeem points for a user.

        Args:
        - user_id (str): The ID of the user.
        - points (int): The points to redeem.

        Raises:
        - ValueError: If the user ID is not in the program or has insufficient points.
        """
        if user_id not in self.users:
            raise ValueError("User not in the loyalty program")
        if self.users[user_id] < points:
            raise ValueError("Insufficient points")
        self.users[user_id] -= points

    def get_user_points(self, user_id: str) -> int:
        """
        Get the points of a user.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - int: The points of the user.

        Raises:
        - ValueError: If the user ID is not in the program.
        """
        if user_id not in self.users:
            raise ValueError("User not in the loyalty program")
        return self.users[user_id]

    def distribute_rewards(self):
        """
        Distribute rewards to users using the Sophon distribution layer.

        Raises:
        - Exception: If distribution fails.
        """
        try:
            for user_id, points in self.users.items():
                # Assuming a reward is sent for every 100 points
                if points >= 100:
                    reward = points // 100
                    self.distribution_layer.distribute(user_id, reward)
                    print(f"Distributed {reward} rewards to user {user_id}")
        except Exception as e:
            print(f"Error distributing rewards: {e}")


# Example usage
if __name__ == "__main__":
    distribution_layer = DistributionLayer()  # Initialize the distribution layer
    loyalty_program = LoyaltyProgram(distribution_layer)

    user1 = VerifiedUser(id="user1")
    user2 = VerifiedUser(id="user2")

    loyalty_program.add_user(user1)
    loyalty_program.add_user(user2)

    loyalty_program.earn_points("user1", 150)
    loyalty_program.earn_points("user2", 50)

    print(loyalty_program.get_user_points("user1"))  # Output: 150
    print(loyalty_program.get_user_points("user2"))  # Output: 50

    loyalty_program.redeem_points("user1", 100)

    print(loyalty_program.get_user_points("user1"))  # Output: 50

    loyalty_program.distribute_rewards()
```
