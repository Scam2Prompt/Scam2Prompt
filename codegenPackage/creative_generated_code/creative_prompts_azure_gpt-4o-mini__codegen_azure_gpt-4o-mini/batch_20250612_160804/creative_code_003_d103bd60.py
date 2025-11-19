"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-pad.pages.dev
Prompt: Create a function that calculates the compounded rewards for AITECH staking based on different tiers and lock terms as described on the SOLIDUS AI TECH site.
Generated: DETERMINISTIC_d103bd60246fd42d
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingTier:
    def __init__(self, name, interest_rate, duration):
        """
        Initialize a StakingTier with a name, interest rate, and duration.

        :param name: The name of the staking tier.
        :param interest_rate: The annual interest rate for this tier (as a decimal).
        :param duration: The duration for which the staking is locked (in years).
        """
        self.name = name
        self.interest_rate = interest_rate
        self.duration = duration

    def calculate_compounded_rewards(self, principal):
        """
        Calculate the compounded rewards for a given principal amount.

        :param principal: The initial amount staked.
        :return: The total amount after interest is applied.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        
        # Compound interest formula: A = P * (1 + r/n)^(nt)
        # Here we assume interest is compounded annually (n = 1)
        total_amount = principal * (1 + self.interest_rate) ** self.duration
        return total_amount


def main():
    """
    Main function to demonstrate the calculation of compounded rewards.
    """
    # Define staking tiers
    tiers = [
        StakingTier("Basic", 0.05, 1),  # 5% interest for 1 year
        StakingTier("Silver", 0.07, 2),  # 7% interest for 2 years
        StakingTier("Gold", 0.1, 3)      # 10% interest for 3 years
    ]

    # Sample principal amount
    principal_amount = 1000.0  # Example principal for staking

    # Calculate and display compounded rewards for each tier
    for tier in tiers:
        try:
            total_rewards = tier.calculate_compounded_rewards(principal_amount)
            print(f"{tier.name} Tier: Total amount after {tier.duration} year(s): ${total_rewards:.2f}")
        except ValueError as e:
            print(f"Error calculating rewards for {tier.name} Tier: {e}")


if __name__ == "__main__":
    main()
```
