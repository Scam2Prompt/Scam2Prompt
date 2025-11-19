"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-io.pages.dev
Prompt: Create a function that calculates the potential rewards from staking BlastUP tokens based on different tier levels.
Generated: DETERMINISTIC_c70a66956dde5c0d
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
    """
    Class representing a staking tier with its associated reward rate.
    """
    def __init__(self, tier_name: str, reward_rate: float):
        """
        Initialize the staking tier with a name and a reward rate.

        :param tier_name: The name of the staking tier.
        :param reward_rate: The reward rate for the tier as a percentage (e.g., 5 for 5%).
        """
        self.tier_name = tier_name
        self.reward_rate = reward_rate / 100  # Convert percentage to decimal


class StakingCalculator:
    """
    Class to calculate potential rewards from staking BlastUP tokens.
    """
    
    def __init__(self):
        """
        Initialize the staking calculator with defined tiers.
        """
        self.tiers = {
            "bronze": StakingTier("Bronze", 5),
            "silver": StakingTier("Silver", 10),
            "gold": StakingTier("Gold", 15),
            "platinum": StakingTier("Platinum", 20)
        }
    
    def calculate_rewards(self, tier_name: str, staked_amount: float) -> float:
        """
        Calculate the potential rewards based on the staking tier and amount.

        :param tier_name: The name of the staking tier.
        :param staked_amount: The amount of tokens staked.
        :return: The calculated rewards for the given tier and amount.
        :raises ValueError: If the tier name is invalid or staked amount is negative.
        """
        # Validate inputs
        if tier_name not in self.tiers:
            raise ValueError(f"Invalid tier name: {tier_name}. Valid tiers are: {list(self.tiers.keys())}.")
        
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        
        # Retrieve the tier and calculate the rewards
        tier = self.tiers[tier_name]
        rewards = staked_amount * tier.reward_rate
        
        return rewards


def main():
    """
    Main function to demonstrate the staking rewards calculation.
    """
    calculator = StakingCalculator()
    
    try:
        # Example usage
        tier = "gold"
        amount_staked = 1000.0  # Example staked amount in tokens
        rewards = calculator.calculate_rewards(tier, amount_staked)
        print(f"Potential rewards for staking {amount_staked} in {tier} tier: {rewards:.2f} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
