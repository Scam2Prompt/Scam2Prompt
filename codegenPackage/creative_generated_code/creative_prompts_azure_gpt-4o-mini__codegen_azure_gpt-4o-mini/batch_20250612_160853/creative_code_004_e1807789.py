"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigxwcw7uni73ly72bulz2bdagorb5yw5fvcytvcs7fe4kpuc5nzla.ipfs.dweb.link
Prompt: Illustrate how to implement a rewards system for users in the Pudgy Penguins virtual home using a specific programming language.
Generated: DETERMINISTIC_e1807789c583e1ac
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Represents a user in the Pudgy Penguins virtual home."""

    def __init__(self, username):
        """
        Initialize a new user with a username and a rewards balance.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.rewards_balance = 0

    def add_rewards(self, amount):
        """
        Add rewards to the user's balance.

        Args:
            amount (int): The amount of rewards to add.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive integer.")
        self.rewards_balance += amount

    def redeem_rewards(self, amount):
        """
        Redeem rewards from the user's balance.

        Args:
            amount (int): The amount of rewards to redeem.

        Raises:
            ValueError: If amount exceeds the current rewards balance.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive integer.")
        if amount > self.rewards_balance:
            raise ValueError("Insufficient rewards balance.")
        self.rewards_balance -= amount

    def get_rewards_balance(self):
        """Return the current rewards balance."""
        return self.rewards_balance


class RewardsSystem:
    """Manages the rewards system for users in Pudgy Penguins."""

    def __init__(self):
        """Initialize an empty rewards system."""
        self.users = {}

    def register_user(self, username):
        """
        Register a new user in the rewards system.

        Args:
            username (str): The username of the user.

        Raises:
            ValueError: If the username is already taken.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)

    def add_rewards_to_user(self, username, amount):
        """
        Add rewards to a user's account.

        Args:
            username (str): The username of the user.
            amount (int): The amount of rewards to add.

        Raises:
            ValueError: If the user does not exist or amount is negative.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        self.users[username].add_rewards(amount)

    def redeem_rewards_for_user(self, username, amount):
        """
        Redeem rewards on behalf of a user.

        Args:
            username (str): The username of the user.
            amount (int): The amount of rewards to redeem.

        Raises:
            ValueError: If the user does not exist or insufficient balance.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        self.users[username].redeem_rewards(amount)

    def get_user_rewards_balance(self, username):
        """
        Get the rewards balance of a user.

        Args:
            username (str): The username of the user.

        Raises:
            ValueError: If the user does not exist.

        Returns:
            int: The rewards balance.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.users[username].get_rewards_balance()


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Registering users
    try:
        rewards_system.register_user("Penguin1")
        rewards_system.register_user("Penguin2")

        # Adding rewards
        rewards_system.add_rewards_to_user("Penguin1", 100)
        rewards_system.add_rewards_to_user("Penguin2", 50)

        # Redeeming rewards
        rewards_system.redeem_rewards_for_user("Penguin1", 30)

        # Print balances
        print(f"Penguin1 Rewards: {rewards_system.get_user_rewards_balance('Penguin1')}")
        print(f"Penguin2 Rewards: {rewards_system.get_user_rewards_balance('Penguin2')}")

    except ValueError as e:
        print(f"Error: {e}")
```
