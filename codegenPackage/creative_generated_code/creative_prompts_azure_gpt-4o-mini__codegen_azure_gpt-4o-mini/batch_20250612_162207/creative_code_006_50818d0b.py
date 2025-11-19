"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20in.pages.dev
Prompt: Create a function to calculate the rewards for DOGE20 stakers based on their share in the staking pool.
Generated: DETERMINISTIC_50818d0bf4eeb1e3
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPool:
    """
    A class to represent a staking pool for DOGE20 rewards.
    """

    def __init__(self):
        """
        Initializes a new StakingPool instance.
        """
        self.total_staked = 0.0  # Total amount staked in the pool
        self.stakers = {}         # A dictionary to hold staker balances

    def add_staker(self, address: str, amount: float) -> None:
        """
        Adds a new staker or updates the amount staked for an existing staker.

        :param address: The address of the staker.
        :param amount: The amount to stake.
        :raises ValueError: If the amount to stake is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be positive.")

        if address in self.stakers:
            self.stakers[address] += amount
        else:
            self.stakers[address] = amount
        
        self.total_staked += amount

    def calculate_rewards(self, total_rewards: float) -> dict:
        """
        Calculates rewards for each staker based on their share in the staking pool.

        :param total_rewards: The total amount of rewards to distribute.
        :return: A dictionary containing addresses and their corresponding rewards.
        :raises ValueError: If total rewards is non-positive or total staked is zero.
        """
        if total_rewards <= 0:
            raise ValueError("Total rewards must be positive.")
        if self.total_staked == 0:
            raise ValueError("Total staked amount cannot be zero.")

        rewards = {}
        for address, staked_amount in self.stakers.items():
            # Calculate the share of the staker
            share = staked_amount / self.total_staked
            # Calculate rewards based on the share
            rewards[address] = share * total_rewards

        return rewards

    def remove_staker(self, address: str) -> None:
        """
        Removes a staker from the staking pool.

        :param address: The address of the staker to remove.
        :raises KeyError: If the staker does not exist in the pool.
        """
        if address not in self.stakers:
            raise KeyError("Staker not found in the pool.")

        amount_staked = self.stakers[address]
        del self.stakers[address]
        self.total_staked -= amount_staked

# Example usage:
if __name__ == "__main__":
    pool = StakingPool()
    pool.add_staker("address1", 100.0)
    pool.add_staker("address2", 200.0)
    
    try:
        rewards = pool.calculate_rewards(300.0)
        print("Rewards distribution:", rewards)
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
