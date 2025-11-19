"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ai-liveclaim.pages.dev
Prompt: Design a staking rewards calculator for WienerAI, taking into account the 71% staking ratio and 114% annual rewards.
Generated: DETERMINISTIC_e1dfedcbabe30e8a
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WienerAIStakingRewardsCalculator:
    """
    Calculates staking rewards for WienerAI.

    Attributes:
        staking_ratio (float): The staking ratio as a decimal.
        annual_rewards (float): The annual rewards as a decimal.
    """

    def __init__(self, staking_ratio=0.71, annual_rewards=1.14):
        """
        Initializes the calculator with the staking ratio and annual rewards.

        Args:
            staking_ratio (float, optional): The staking ratio. Defaults to 0.71.
            annual_rewards (float, optional): The annual rewards. Defaults to 1.14.
        """
        self.staking_ratio = staking_ratio
        self.annual_rewards = annual_rewards

    def calculate_rewards(self, total_supply, staked_amount):
        """
        Calculates the staking rewards.

        Args:
            total_supply (float): The total supply of WienerAI.
            staked_amount (float): The amount of WienerAI staked.

        Returns:
            float: The staking rewards.

        Raises:
            ValueError: If the total supply or staked amount is negative.
        """
        if total_supply < 0 or staked_amount < 0:
            raise ValueError("Total supply and staked amount must be non-negative.")

        # Calculate the staked ratio
        staked_ratio = staked_amount / total_supply

        # Check if the staked ratio exceeds the staking ratio
        if staked_ratio > self.staking_ratio:
            raise ValueError("Staked ratio cannot exceed the staking ratio.")

        # Calculate the annual rewards
        annual_rewards_amount = staked_amount * (self.annual_rewards - 1)

        return annual_rewards_amount

    def calculate_apr(self, total_supply, staked_amount):
        """
        Calculates the annual percentage rate (APR) for the staked amount.

        Args:
            total_supply (float): The total supply of WienerAI.
            staked_amount (float): The amount of WienerAI staked.

        Returns:
            float: The APR.

        Raises:
            ValueError: If the total supply or staked amount is negative.
        """
        if total_supply <= 0 or staked_amount <= 0:
            raise ValueError("Total supply and staked amount must be positive.")

        # Calculate the staked ratio
        staked_ratio = staked_amount / total_supply

        # Check if the staked ratio exceeds the staking ratio
        if staked_ratio > self.staking_ratio:
            raise ValueError("Staked ratio cannot exceed the staking ratio.")

        # Calculate the APR
        apr = ((staked_amount * (self.annual_rewards - 1)) / staked_amount) * 100

        return apr


def main():
    calculator = WienerAIStakingRewardsCalculator()

    total_supply = 1000000  # Total supply of WienerAI
    staked_amount = 710000  # Staked amount of WienerAI

    try:
        rewards = calculator.calculate_rewards(total_supply, staked_amount)
        apr = calculator.calculate_apr(total_supply, staked_amount)

        print(f"Rewards: {rewards}")
        print(f"APR: {apr}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
