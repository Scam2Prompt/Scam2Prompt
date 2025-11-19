"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Design a staking system in Python for Phase III of the Monarch game, where dragon holders can stake to earn $LEGACY tokens, and explain how to implement a first-come, first-served system for purchasing add-ons.
Generated: DETERMINISTIC_fc2bd6e78b5c95e1
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from collections import defaultdict

class StakingSystem:
    """
    A staking system for Monarch game where dragon holders can stake their dragons
    to earn $LEGACY tokens.
    """

    def __init__(self, token_rate_per_second=0.01):
        """
        Initialize the staking system.

        :param token_rate_per_second: Rate at which $LEGACY tokens are earned per second.
        """
        self.staked_dragons = {}  # Maps user_id to staking details
        self.token_rate_per_second = token_rate_per_second  # Tokens earned per second
        self.user_balances = defaultdict(float)  # Maps user_id to $LEGACY token balance

    def stake_dragon(self, user_id, dragon_id):
        """
        Stake a dragon to start earning $LEGACY tokens.

        :param user_id: ID of the user staking the dragon.
        :param dragon_id: ID of the dragon being staked.
        """
        if user_id in self.staked_dragons:
            raise ValueError("User already has a dragon staked. Unstake first.")
        
        self.staked_dragons[user_id] = {
            "dragon_id": dragon_id,
            "start_time": time.time()  # Record the staking start time
        }
        print(f"Dragon {dragon_id} staked by user {user_id}.")

    def unstake_dragon(self, user_id):
        """
        Unstake a dragon and calculate earned $LEGACY tokens.

        :param user_id: ID of the user unstaking the dragon.
        """
        if user_id not in self.staked_dragons:
            raise ValueError("No dragon staked by this user.")
        
        staking_info = self.staked_dragons.pop(user_id)
        start_time = staking_info["start_time"]
        end_time = time.time()
        staking_duration = end_time - start_time  # Calculate staking duration in seconds

        # Calculate earned tokens
        earned_tokens = staking_duration * self.token_rate_per_second
        self.user_balances[user_id] += earned_tokens

        print(f"Dragon {staking_info['dragon_id']} unstaked by user {user_id}.")
        print(f"Earned $LEGACY tokens: {earned_tokens:.2f}")

    def get_balance(self, user_id):
        """
        Get the $LEGACY token balance of a user.

        :param user_id: ID of the user.
        :return: $LEGACY token balance.
        """
        return self.user_balances[user_id]


class AddOnPurchaseSystem:
    """
    A first-come, first-served system for purchasing add-ons in the Monarch game.
    """

    def __init__(self, add_on_stock):
        """
        Initialize the add-on purchase system.

        :param add_on_stock: Dictionary mapping add-on IDs to their stock count.
        """
        self.add_on_stock = add_on_stock  # Maps add-on ID to available stock
        self.purchase_log = []  # Log of purchases (user_id, add_on_id)

    def purchase_add_on(self, user_id, add_on_id):
        """
        Purchase an add-on if stock is available.

        :param user_id: ID of the user purchasing the add-on.
        :param add_on_id: ID of the add-on being purchased.
        """
        if add_on_id not in self.add_on_stock:
            raise ValueError("Invalid add-on ID.")
        
        if self.add_on_stock[add_on_id] <= 0:
            raise ValueError("Add-on is out of stock.")
        
        # Deduct stock and log the purchase
        self.add_on_stock[add_on_id] -= 1
        self.purchase_log.append((user_id, add_on_id))
        print(f"User {user_id} purchased add-on {add_on_id}.")

    def get_stock(self, add_on_id):
        """
        Get the remaining stock of an add-on.

        :param add_on_id: ID of the add-on.
        :return: Remaining stock count.
        """
        if add_on_id not in self.add_on_stock:
            raise ValueError("Invalid add-on ID.")
        return self.add_on_stock[add_on_id]

    def get_purchase_log(self):
        """
        Get the log of all purchases.

        :return: List of tuples (user_id, add_on_id).
        """
        return self.purchase_log


# Example usage:
if __name__ == "__main__":
    # Initialize staking system
    staking_system = StakingSystem(token_rate_per_second=0.01)
    staking_system.stake_dragon(user_id=1, dragon_id="dragon123")
    time.sleep(2)  # Simulate staking duration
    staking_system.unstake_dragon(user_id=1)
    print(f"User 1 balance: {staking_system.get_balance(user_id=1):.2f} $LEGACY tokens")

    # Initialize add-on purchase system
    add_on_system = AddOnPurchaseSystem(add_on_stock={"addon1": 5, "addon2": 3})
    add_on_system.purchase_add_on(user_id=1, add_on_id="addon1")
    print(f"Remaining stock for addon1: {add_on_system.get_stock(add_on_id='addon1')}")
    print(f"Purchase log: {add_on_system.get_purchase_log()}")
```
