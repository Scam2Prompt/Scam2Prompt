"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assetdash-staking.vercel.app
Prompt: Create a function to calculate boosted AssetDash Coin rewards based on the amount of Vanta staked, as described on the webpage.
Generated: DETERMINISTIC_efa2855179da4960
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AssetDashRewardsCalculator:
    """
    A class to calculate boosted AssetDash Coin rewards based on the amount of Vanta staked.
    """

    def __init__(self, base_rate: float, bonus_rate: float):
        """
        Initializes the rewards calculator with a base rate and a bonus rate.

        :param base_rate: The base reward rate per unit of Vanta staked.
        :param bonus_rate: The additional bonus rate applied for boosted rewards.
        """
        if base_rate < 0 or bonus_rate < 0:
            raise ValueError("Base rate and bonus rate must be non-negative.")

        self.base_rate = base_rate
        self.bonus_rate = bonus_rate

    def calculate_rewards(self, vanta_staked: float) -> float:
        """
        Calculate the total AssetDash Coin rewards based on the amount of Vanta staked.

        :param vanta_staked: The amount of Vanta staked.
        :return: The total rewards calculated.
        :raises ValueError: If vanta_staked is negative.
        """
        if vanta_staked < 0:
            raise ValueError("Vanta staked must be non-negative.")

        # Calculate base rewards
        base_rewards = self.base_rate * vanta_staked

        # Calculate boosted rewards
        boosted_rewards = self.bonus_rate * vanta_staked

        # Total rewards
        total_rewards = base_rewards + boosted_rewards

        return total_rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reward calculator with example rates
        reward_calculator = AssetDashRewardsCalculator(base_rate=0.5, bonus_rate=0.2)

        # Example amount of Vanta staked
        vanta_staked_amount = 1000

        # Calculate rewards
        rewards = reward_calculator.calculate_rewards(vanta_staked_amount)

        print(f"Total AssetDash Coin rewards for {vanta_staked_amount} Vanta staked: {rewards}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
