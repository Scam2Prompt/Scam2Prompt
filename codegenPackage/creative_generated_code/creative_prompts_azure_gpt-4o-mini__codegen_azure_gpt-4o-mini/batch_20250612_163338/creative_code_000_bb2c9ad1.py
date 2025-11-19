"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: How can I implement a rewards system using the Lingo token that leverages Real World Assets (RWA) for community engagement?
Generated: DETERMINISTIC_bb2c9ad153879d78
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Any
import json

class RewardSystem:
    def __init__(self):
        """
        Initializes the RewardSystem with an empty user rewards dictionary.
        """
        self.user_rewards: Dict[str, int] = {}
        self.rwa_assets: List[str] = []  # List to hold Real World Assets

    def register_user(self, user_id: str) -> None:
        """
        Registers a new user in the rewards system.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            ValueError: If the user is already registered.
        """
        if user_id in self.user_rewards:
            raise ValueError(f"User {user_id} is already registered.")
        self.user_rewards[user_id] = 0  # Initialize rewards to 0

    def add_rwa_asset(self, asset_name: str) -> None:
        """
        Adds a Real World Asset to the rewards system.

        Args:
            asset_name (str): The name of the RWA asset.
        """
        self.rwa_assets.append(asset_name)

    def allocate_rewards(self, user_id: str, amount: int) -> None:
        """
        Allocates rewards in Lingo tokens to a user.

        Args:
            user_id (str): Unique identifier for the user.
            amount (int): Amount of rewards to allocate.

        Raises:
            ValueError: If the user is not registered or the amount is non-positive.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} is not registered.")
        if amount <= 0:
            raise ValueError("Reward amount must be positive.")

        self.user_rewards[user_id] += amount

    def get_user_rewards(self, user_id: str) -> int:
        """
        Retrieves the current rewards for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            int: The current reward amount for the user.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} is not registered.")

        return self.user_rewards[user_id]

    def redeem_rewards(self, user_id: str, amount: int) -> None:
        """
        Allows a user to redeem rewards in Lingo tokens.

        Args:
            user_id (str): Unique identifier for the user.
            amount (int): Amount of rewards to redeem.

        Raises:
            ValueError: If the user is not registered, amount is non-positive,
                        or the user does not have enough rewards.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} is not registered.")
        if amount <= 0:
            raise ValueError("Redemption amount must be positive.")
        if self.user_rewards[user_id] < amount:
            raise ValueError("Insufficient rewards to redeem.")

        self.user_rewards[user_id] -= amount

    def export_rewards(self) -> str:
        """
        Exports the current state of user rewards in JSON format.

        Returns:
            str: JSON string representation of the current user rewards.
        """
        return json.dumps(self.user_rewards)

# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Register users
    try:
        reward_system.register_user("user123")
        reward_system.register_user("user456")

        # Add Real World Assets
        reward_system.add_rwa_asset("Asset1")
        reward_system.add_rwa_asset("Asset2")

        # Allocate rewards
        reward_system.allocate_rewards("user123", 100)
        reward_system.allocate_rewards("user456", 50)

        # Redeem rewards
        reward_system.redeem_rewards("user123", 30)

        # Get user rewards
        print(f"User123 Rewards: {reward_system.get_user_rewards('user123')}")
        print(f"User456 Rewards: {reward_system.get_user_rewards('user456')}")

        # Export rewards
        print("Current Rewards State:", reward_system.export_rewards())

    except ValueError as e:
        print(f"Error: {e}")
```
