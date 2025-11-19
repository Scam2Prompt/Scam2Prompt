"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Write a code snippet to calculate the rewards for holding $BANANA based on the current APY and epoch duration.
Generated: DETERMINISTIC_51f8b4887de284cf
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BananaRewardsCalculator:
    """
    A class to calculate rewards for holding BANANA based on the current APY and epoch duration.
    """

    def __init__(self, current_balance: float, annual_percentage_yield: float, epoch_duration_days: int):
        """
        Initializes the rewards calculator with the user's BANANA balance, current APY, and epoch duration.

        :param current_balance: The amount of BANANA held by the user.
        :param annual_percentage_yield: The annual percentage yield as a decimal (e.g., 0.15 for 15%).
        :param epoch_duration_days: The duration of an epoch in days.
        """
        self.current_balance = current_balance
        self.annual_percentage_yield = annual_percentage_yield
        self.epoch_duration_days = epoch_duration_days

    def calculate_rewards(self) -> float:
        """
        Calculates the rewards for holding BANANA over the specified epoch duration.

        :return: The calculated rewards for the epoch.
        :raises ValueError: If current_balance or annual_percentage_yield is negative,
                            or if epoch_duration_days is non-positive.
        """
        # Validate inputs
        if self.current_balance < 0:
            raise ValueError("Current balance cannot be negative.")
        if self.annual_percentage_yield < 0:
            raise ValueError("Annual percentage yield cannot be negative.")
        if self.epoch_duration_days <= 0:
            raise ValueError("Epoch duration must be a positive integer.")

        # Calculate daily yield
        daily_yield = self.annual_percentage_yield / 365
        # Calculate rewards for the duration of the epoch
        rewards = self.current_balance * daily_yield * self.epoch_duration_days
        return rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with user inputs
        calculator = BananaRewardsCalculator(current_balance=1000.0, annual_percentage_yield=0.15, epoch_duration_days=30)
        # Calculate and print the rewards for the given epoch
        rewards = calculator.calculate_rewards()
        print(f"Rewards for holding $BANANA for {calculator.epoch_duration_days} days: ${rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
