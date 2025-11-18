"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Generate a script to calculate staking rewards for BlastUP tokens based on the tiered system (e.g., Bronze, Silver, Gold, etc.) and pool weights.
Generated: DETERMINISTIC_afc0a2654524fdf9
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardCalculator:
    """
    A class to calculate staking rewards for BlastUP tokens based on a tiered system.
    """

    # Define the tiers and their corresponding weights
    TIERS = {
        'Bronze': 1.0,
        'Silver': 1.5,
        'Gold': 2.0,
        'Platinum': 3.0,
    }

    def __init__(self, tier, staked_amount):
        """
        Initializes the StakingRewardCalculator with a specified tier and staked amount.

        :param tier: The staking tier (e.g., 'Bronze', 'Silver', 'Gold', 'Platinum').
        :param staked_amount: The amount of tokens staked.
        :raises ValueError: If the tier is invalid or the staked amount is non-positive.
        """
        if tier not in self.TIERS:
            raise ValueError(f"Invalid tier: {tier}. Valid tiers are: {', '.join(self.TIERS.keys())}.")
        
        if staked_amount <= 0:
            raise ValueError("Staked amount must be a positive number.")

        self.tier = tier
        self.staked_amount = staked_amount

    def calculate_rewards(self):
        """
        Calculates the staking rewards based on the tier and staked amount.

        :return: The calculated reward amount.
        """
        weight = self.TIERS[self.tier]
        rewards = self.staked_amount * weight
        return rewards

def main():
    """
    Main function to run the staking rewards calculation.
    """
    try:
        # Example usage
        tier = input("Enter your staking tier (Bronze, Silver, Gold, Platinum): ")
        staked_amount = float(input("Enter the amount of tokens staked: "))

        # Create a staking reward calculator instance
        calculator = StakingRewardCalculator(tier, staked_amount)

        # Calculate and display the rewards
        rewards = calculator.calculate_rewards()
        print(f"Your staking rewards for {staked_amount:.2f} tokens in the {tier} tier is: {rewards:.2f} tokens.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
