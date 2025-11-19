"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Generate code to calculate the total rewards earned from staking AITECH tokens over different lock periods, as mentioned in the Solidus AI Tech staking tiers.
Generated: DETERMINISTIC_a035ef85412f78d0
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingTier:
    """Class to represent a staking tier for AITECH tokens."""

    def __init__(self, tier_name: str, lock_period_days: int, reward_rate: float):
        """
        Initialize a new StakingTier.

        Args:
            tier_name (str): The name of the staking tier.
            lock_period_days (int): The number of days tokens are locked.
            reward_rate (float): The reward rate as a percentage (e.g., 0.05 for 5%).
        """
        self.tier_name = tier_name
        self.lock_period_days = lock_period_days
        self.reward_rate = reward_rate

    def calculate_rewards(self, staked_amount: float) -> float:
        """
        Calculate the total rewards earned for the given staked amount.

        Args:
            staked_amount (float): The amount of AITECH tokens staked.

        Returns:
            float: The total rewards earned.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        
        # Calculate rewards based on the staked amount and reward rate
        rewards = staked_amount * self.reward_rate * (self.lock_period_days / 365)
        return rewards


class StakingCalculator:
    """Class to manage multiple staking tiers and calculate total rewards."""

    def __init__(self, tiers: list):
        """
        Initialize the StakingCalculator with a list of staking tiers.

        Args:
            tiers (list): A list of StakingTier instances.
        """
        if not all(isinstance(tier, StakingTier) for tier in tiers):
            raise TypeError("All items in tiers must be instances of StakingTier.")
        
        self.tiers = tiers

    def calculate_total_rewards(self, staked_amounts: dict) -> float:
        """
        Calculate the total rewards earned across all staking tiers for given staked amounts.

        Args:
            staked_amounts (dict): A dictionary mapping tier names to staked amounts.

        Returns:
            float: Total rewards earned across all tiers.
        """
        total_rewards = 0.0

        for tier in self.tiers:
            staked_amount = staked_amounts.get(tier.tier_name, 0.0)

            try:
                tier_rewards = tier.calculate_rewards(staked_amount)
                total_rewards += tier_rewards
            except ValueError as e:
                print(f"Error calculating rewards for tier '{tier.tier_name}': {e}")

        return total_rewards


# Example usage
if __name__ == "__main__":
    # Define staking tiers (example values)
    tiers = [
        StakingTier("Basic", lock_period_days=30, reward_rate=0.05),
        StakingTier("Silver", lock_period_days=90, reward_rate=0.075),
        StakingTier("Gold", lock_period_days=180, reward_rate=0.1),
    ]

    # Create a staking calculator with the defined tiers
    staking_calculator = StakingCalculator(tiers)

    # Define staked amounts for each tier
    staked_amounts = {
        "Basic": 1000.0,
        "Silver": 2000.0,
        "Gold": 1500.0,
    }

    # Calculate total rewards
    total_rewards = staking_calculator.calculate_total_rewards(staked_amounts)

    print(f"Total rewards earned from staking: {total_rewards:.2f} AITECH tokens")
```
