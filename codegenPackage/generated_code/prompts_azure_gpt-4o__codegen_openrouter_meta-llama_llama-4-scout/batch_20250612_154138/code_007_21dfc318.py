"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Generate Python code to simulate a jackpot system where users can win large rewards, inspired by the "รางวัลแจ็คพอต" feature on venez888.vip.
Generated: DETERMINISTIC_21dfc318a2846f1f
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class JackpotSystem:
    """
    Simulates a jackpot system where users can win large rewards.
    """

    def __init__(self, min_reward=0, max_reward=1000, jackpot_amount=10000):
        """
        Initializes the jackpot system.

        Args:
            min_reward (int): The minimum reward a user can win. Defaults to 0.
            max_reward (int): The maximum reward a user can win. Defaults to 1000.
            jackpot_amount (int): The jackpot amount. Defaults to 10000.
        """
        self.min_reward = min_reward
        self.max_reward = max_reward
        self.jackpot_amount = jackpot_amount
        self.users = {}

    def add_user(self, user_id):
        """
        Adds a user to the system.

        Args:
            user_id (str): The ID of the user.
        """
        if user_id not in self.users:
            self.users[user_id] = {"balance": 0, "winnings": 0}

    def play(self, user_id):
        """
        Simulates a play of the jackpot system.

        Args:
            user_id (str): The ID of the user.

        Returns:
            int: The reward won by the user.
        """
        if user_id not in self.users:
            raise ValueError("User not found")

        # Generate a random number between 0 and 1
        roll = random.random()

        # 1% chance of winning the jackpot
        if roll < 0.01:
            reward = self.jackpot_amount
        # 10% chance of winning a large reward
        elif roll < 0.11:
            reward = random.randint(self.max_reward // 2, self.max_reward)
        # 20% chance of winning a small reward
        elif roll < 0.31:
            reward = random.randint(self.min_reward, self.max_reward // 2)
        else:
            reward = 0

        if reward > 0:
            self.users[user_id]["winnings"] += reward
            self.users[user_id]["balance"] += reward

        return reward

    def get_user_balance(self, user_id):
        """
        Gets the balance of a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            int: The balance of the user.
        """
        if user_id not in self.users:
            raise ValueError("User not found")

        return self.users[user_id]["balance"]

    def get_user_winnings(self, user_id):
        """
        Gets the total winnings of a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            int: The total winnings of the user.
        """
        if user_id not in self.users:
            raise ValueError("User not found")

        return self.users[user_id]["winnings"]


def main():
    jackpot = JackpotSystem()

    # Add users
    jackpot.add_user("user1")
    jackpot.add_user("user2")

    # Play the jackpot
    print("User 1 winnings:", jackpot.play("user1"))
    print("User 2 winnings:", jackpot.play("user2"))

    # Get user balances and winnings
    print("User 1 balance:", jackpot.get_user_balance("user1"))
    print("User 1 winnings:", jackpot.get_user_winnings("user1"))
    print("User 2 balance:", jackpot.get_user_balance("user2"))
    print("User 2 winnings:", jackpot.get_user_winnings("user2"))


if __name__ == "__main__":
    main()
```
