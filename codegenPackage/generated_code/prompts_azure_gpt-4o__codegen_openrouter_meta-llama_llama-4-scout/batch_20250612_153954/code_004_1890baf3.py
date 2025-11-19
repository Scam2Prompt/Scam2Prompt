"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: Write a program to simulate the revenue allocation process described in the World Mobile Token ecosystem, including purchasing WMTx from open markets and distributing rewards to stakers.
Generated: DETERMINISTIC_1890baf38710e0aa
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# world_mobile_token.py

class WorldMobileToken:
    def __init__(self, total_supply):
        """
        Initializes the World Mobile Token ecosystem.

        Args:
        total_supply (float): The total supply of WMTx tokens.
        """
        self.total_supply = total_supply
        self.stakers = {}
        self.wmtx_price = 0.0

    def set_wmtx_price(self, price):
        """
        Sets the current price of WMTx tokens.

        Args:
        price (float): The current price of WMTx tokens.
        """
        self.wmtx_price = price

    def add_staker(self, staker_id, stake_amount):
        """
        Adds a new staker to the ecosystem.

        Args:
        staker_id (str): The unique ID of the staker.
        stake_amount (float): The initial stake amount of the staker.

        Raises:
        ValueError: If the stake amount is negative.
        """
        if stake_amount < 0:
            raise ValueError("Stake amount cannot be negative")

        self.stakers[staker_id] = stake_amount

    def remove_staker(self, staker_id):
        """
        Removes a staker from the ecosystem.

        Args:
        staker_id (str): The unique ID of the staker.

        Raises:
        KeyError: If the staker ID does not exist.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID does not exist")

        del self.stakers[staker_id]

    def purchase_wmtx(self, amount):
        """
        Simulates purchasing WMTx tokens from open markets.

        Args:
        amount (float): The amount of WMTx tokens to purchase.

        Raises:
        ValueError: If the purchase amount is negative.
        """
        if amount < 0:
            raise ValueError("Purchase amount cannot be negative")

        # Simulate purchasing WMTx tokens
        print(f"Purchased {amount} WMTx tokens at ${self.wmtx_price:.2f} each.")

    def distribute_rewards(self, reward_amount):
        """
        Distributes rewards to stakers.

        Args:
        reward_amount (float): The total reward amount to distribute.

        Raises:
        ValueError: If the reward amount is negative.
        """
        if reward_amount < 0:
            raise ValueError("Reward amount cannot be negative")

        # Calculate the total stake amount
        total_stake = sum(self.stakers.values())

        # Distribute rewards to stakers
        for staker_id, stake_amount in self.stakers.items():
            reward = (stake_amount / total_stake) * reward_amount
            print(f"Distributed ${reward:.2f} reward to staker {staker_id}.")

    def update_stake(self, staker_id, new_stake_amount):
        """
        Updates the stake amount of a staker.

        Args:
        staker_id (str): The unique ID of the staker.
        new_stake_amount (float): The new stake amount.

        Raises:
        KeyError: If the staker ID does not exist.
        ValueError: If the new stake amount is negative.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID does not exist")

        if new_stake_amount < 0:
            raise ValueError("New stake amount cannot be negative")

        self.stakers[staker_id] = new_stake_amount


def main():
    # Create a new World Mobile Token ecosystem
    wmt = WorldMobileToken(1000000.0)

    # Set the initial WMTx price
    wmt.set_wmtx_price(10.0)

    # Add stakers
    wmt.add_staker("staker1", 1000.0)
    wmt.add_staker("staker2", 2000.0)

    # Purchase WMTx tokens
    wmt.purchase_wmtx(100.0)

    # Distribute rewards
    wmt.distribute_rewards(1000.0)

    # Update stake amount
    wmt.update_stake("staker1", 1500.0)

    # Remove a staker
    wmt.remove_staker("staker2")

    # Distribute rewards again
    wmt.distribute_rewards(500.0)


if __name__ == "__main__":
    main()
```
