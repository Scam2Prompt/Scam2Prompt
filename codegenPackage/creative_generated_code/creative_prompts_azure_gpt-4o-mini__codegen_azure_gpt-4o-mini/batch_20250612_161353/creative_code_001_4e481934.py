"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Write a Python script that calculates potential rewards for different staking tiers of AITECH based on the provided APY rates.
Generated: DETERMINISTIC_4e481934f2ac8893
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class StakingTier:
    """Class to represent a staking tier with its APY and principal amount."""

    def __init__(self, name, apy, principal):
        """
        Initialize a staking tier.

        :param name: Name of the staking tier.
        :param apy: Annual Percentage Yield for this tier (as a decimal).
        :param principal: The amount staked in this tier.
        """
        self.name = name
        self.apy = apy
        self.principal = principal

    def calculate_rewards(self, years):
        """
        Calculate potential rewards based on the staking tier APY.

        :param years: Number of years the amount is staked.
        :return: Calculated rewards.
        """
        # Compound interest formula: A = P(1 + r/n)^(nt)
        # Assuming compounding occurs annually (n=1)
        rewards = self.principal * ((1 + self.apy) ** years - 1)
        return rewards


def calculate_total_rewards(tiers, years):
    """
    Calculate total potential rewards for multiple staking tiers.

    :param tiers: List of StakingTier objects.
    :param years: Number of years the amounts are staked.
    :return: Total rewards from all tiers.
    """
    total_rewards = 0
    for tier in tiers:
        tier_rewards = tier.calculate_rewards(years)
        total_rewards += tier_rewards
        print(f"Rewards for {tier.name}: ${tier_rewards:.2f}")

    return total_rewards


def main():
    """
    Main function to run the staking rewards calculation.
    """
    # Define staking tiers with example APY rates and principal amounts
    staking_tiers = [
        StakingTier(name="Tier 1", apy=0.05, principal=1000),  # 5% APY
        StakingTier(name="Tier 2", apy=0.07, principal=2000),  # 7% APY
        StakingTier(name="Tier 3", apy=0.1, principal=5000)    # 10% APY
    ]

    # Get number of years from command line argument
    if len(sys.argv) != 2:
        print("Usage: python staking_rewards.py <number_of_years>")
        sys.exit(1)

    try:
        years = int(sys.argv[1])
        if years < 0:
            raise ValueError("Number of years must be a non-negative integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    # Calculate total rewards
    total_rewards = calculate_total_rewards(staking_tiers, years)
    print(f"Total rewards after {years} year(s): ${total_rewards:.2f}")


if __name__ == "__main__":
    main()
```
