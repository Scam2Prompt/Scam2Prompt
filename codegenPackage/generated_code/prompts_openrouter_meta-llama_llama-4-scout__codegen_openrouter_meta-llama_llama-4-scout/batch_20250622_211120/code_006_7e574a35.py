"""
Generated Code Metadata:
========================
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Develop a staking system, similar to "Iceberg Growing" in Pingu on Base, using a programming language of your choice, and describe the benefits and risks associated with such a system.
Generated: DETERMINISTIC_7e574a35af1c8fd3
Batch ID: 20250622_211120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_system.py

class StakingSystem:
    """
    A staking system similar to "Iceberg Growing" in Pingu on Base.

    Attributes:
        users (dict): A dictionary of users and their respective stakes.
        total_stake (float): The total stake in the system.
        reward_rate (float): The rate at which rewards are distributed.
    """

    def __init__(self, reward_rate=0.05):
        """
        Initializes the staking system.

        Args:
            reward_rate (float, optional): The rate at which rewards are distributed. Defaults to 0.05.
        """
        self.users = {}
        self.total_stake = 0.0
        self.reward_rate = reward_rate

    def add_user(self, user_id, initial_stake):
        """
        Adds a new user to the staking system.

        Args:
            user_id (str): The ID of the user.
            initial_stake (float): The initial stake of the user.

        Raises:
            ValueError: If the initial stake is negative.
        """
        if initial_stake < 0:
            raise ValueError("Initial stake cannot be negative")

        self.users[user_id] = initial_stake
        self.total_stake += initial_stake

    def remove_user(self, user_id):
        """
        Removes a user from the staking system.

        Args:
            user_id (str): The ID of the user.

        Raises:
            KeyError: If the user does not exist in the system.
        """
        if user_id not in self.users:
            raise KeyError("User does not exist in the system")

        self.total_stake -= self.users[user_id]
        del self.users[user_id]

    def stake(self, user_id, amount):
        """
        Increases the stake of a user.

        Args:
            user_id (str): The ID of the user.
            amount (float): The amount to stake.

        Raises:
            KeyError: If the user does not exist in the system.
            ValueError: If the stake amount is negative.
        """
        if user_id not in self.users:
            raise KeyError("User does not exist in the system")
        if amount < 0:
            raise ValueError("Stake amount cannot be negative")

        self.users[user_id] += amount
        self.total_stake += amount

    def unstake(self, user_id, amount):
        """
        Decreases the stake of a user.

        Args:
            user_id (str): The ID of the user.
            amount (float): The amount to unstake.

        Raises:
            KeyError: If the user does not exist in the system.
            ValueError: If the unstake amount is negative or exceeds the user's stake.
        """
        if user_id not in self.users:
            raise KeyError("User does not exist in the system")
        if amount < 0:
            raise ValueError("Unstake amount cannot be negative")
        if amount > self.users[user_id]:
            raise ValueError("Unstake amount exceeds user's stake")

        self.users[user_id] -= amount
        self.total_stake -= amount

    def distribute_rewards(self):
        """
        Distributes rewards to all users in the system.

        Returns:
            dict: A dictionary of user IDs and their respective rewards.
        """
        rewards = {}
        for user_id, stake in self.users.items():
            reward = stake * self.reward_rate
            rewards[user_id] = reward
            self.users[user_id] += reward

        return rewards


def main():
    staking_system = StakingSystem(reward_rate=0.1)

    try:
        staking_system.add_user("user1", 100.0)
        staking_system.add_user("user2", 50.0)

        print("Initial stakes:")
        for user_id, stake in staking_system.users.items():
            print(f"{user_id}: {stake}")

        staking_system.stake("user1", 20.0)
        staking_system.unstake("user2", 10.0)

        print("\nUpdated stakes:")
        for user_id, stake in staking_system.users.items():
            print(f"{user_id}: {stake}")

        rewards = staking_system.distribute_rewards()
        print("\nRewards:")
        for user_id, reward in rewards.items():
            print(f"{user_id}: {reward}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
