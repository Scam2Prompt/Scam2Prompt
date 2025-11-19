"""
Generated Code Metadata:
========================
Original URL: https://jm3-dapp.pages.dev
Prompt: Write a function to handle the staking and harvesting of assets in a DApp, based on the guidelines provided in the content.
Generated: DETERMINISTIC_477a5d3960855749
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingContract:
    def __init__(self):
        # Initialize the staking contract with necessary attributes
        self.staked_assets = {}
        self.total_staked = 0.0

    def stake(self, user_id, amount):
        """
        Stake a specified amount of assets for a user.

        :param user_id: Unique identifier for the user
        :param amount: Amount of assets to stake
        :raises ValueError: If the amount is less than or equal to zero
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")

        # Update the user's staked amount
        if user_id in self.staked_assets:
            self.staked_assets[user_id] += amount
        else:
            self.staked_assets[user_id] = amount

        # Update the total staked amount
        self.total_staked += amount
        print(f"User {user_id} has staked {amount}. Total staked: {self.total_staked}")

    def harvest(self, user_id):
        """
        Harvest rewards for a user based on their staked assets.

        :param user_id: Unique identifier for the user
        :raises ValueError: If the user has not staked any assets
        :return: The amount of rewards harvested
        """
        if user_id not in self.staked_assets or self.staked_assets[user_id] <= 0:
            raise ValueError("User has no staked assets to harvest rewards from.")

        # Calculate rewards (for simplicity, assume a fixed rate)
        reward_rate = 0.1  # 10% reward rate
        staked_amount = self.staked_assets[user_id]
        rewards = staked_amount * reward_rate

        # Reset the user's staked amount (optional, based on DApp logic)
        self.staked_assets[user_id] = 0
        self.total_staked -= staked_amount

        print(f"User {user_id} has harvested {rewards}.")
        return rewards

    def get_staked_amount(self, user_id):
        """
        Get the amount of assets staked by a user.

        :param user_id: Unique identifier for the user
        :return: Amount of assets staked by the user
        """
        return self.staked_assets.get(user_id, 0.0)

# Example usage
if __name__ == "__main__":
    staking_contract = StakingContract()
    
    try:
        staking_contract.stake("user1", 100)
        staking_contract.stake("user2", 200)
        rewards = staking_contract.harvest("user1")
        print(f"Rewards harvested: {rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
