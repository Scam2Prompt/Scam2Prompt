"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banksocialio.pages.dev
Prompt: Write code to create a rewards program for crypto debit card users, inspired by BankSocial's debit rewards card system.
Generated: DETERMINISTIC_10ce39376105acfd
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Reward:
    """Class to represent a reward."""
    def __init__(self, description: str, points: int):
        self.description = description
        self.points = points

class User:
    """Class to represent a user in the rewards program."""
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.points_balance = 0
        self.rewards_history: List[Reward] = []

    def earn_points(self, points: int) -> None:
        """Allow user to earn points."""
        if points < 0:
            raise ValueError("Points earned cannot be negative.")
        self.points_balance += points
        print(f"{self.name} earned {points} points. Total: {self.points_balance}")

    def redeem_points(self, points: int, reward_description: str) -> None:
        """Allow user to redeem points for a reward."""
        if points < 0:
            raise ValueError("Points to redeem cannot be negative.")
        if points > self.points_balance:
            raise ValueError("Insufficient points to redeem.")

        self.points_balance -= points
        reward = Reward(reward_description, points)
        self.rewards_history.append(reward)
        print(f"{self.name} redeemed {points} points for '{reward_description}'. Total balance: {self.points_balance}")

class RewardProgram:
    """Class to manage the rewards program for users."""
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, user_id: str, name: str) -> None:
        """Add a new user to the rewards program."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id, name)
        print(f"User {name} added to the rewards program.")

    def earn_points(self, user_id: str, points: int) -> None:
        """Allow user to earn points."""
        user = self._get_user(user_id)
        user.earn_points(points)

    def redeem_points(self, user_id: str, points: int, reward_description: str) -> None:
        """Allow user to redeem points for a reward."""
        user = self._get_user(user_id)
        user.redeem_points(points, reward_description)

    def _get_user(self, user_id: str) -> User:
        """Retrieve a user from the program."""
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("User not found.")
        return user

# Example usage of the rewards program
if __name__ == "__main__":
    try:
        rewards_program = RewardProgram()
        
        # Adding users
        rewards_program.add_user("1", "Alice")
        rewards_program.add_user("2", "Bob")
        
        # Earning points
        rewards_program.earn_points("1", 100)
        rewards_program.earn_points("2", 150)
        
        # Redeeming points
        rewards_program.redeem_points("1", 50, "Coffee Shop Gift Card")
        rewards_program.redeem_points("2", 200, "Amazon Gift Card")

    except ValueError as e:
        print(f"Error: {e}")
```
