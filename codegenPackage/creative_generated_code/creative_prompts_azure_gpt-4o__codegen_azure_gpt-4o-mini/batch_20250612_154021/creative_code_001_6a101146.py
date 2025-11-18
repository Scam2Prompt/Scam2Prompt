"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdexx.com
Prompt: Generate Python code to calculate staking rewards on Aster using assets like BNB, USDT, BTC, and CAKE with up to 30%+ APY.
Generated: DETERMINISTIC_6a1011463592a974
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class StakingRewardCalculator:
    """A class to calculate staking rewards for various assets."""

    def __init__(self, principal, apy, years):
        """
        Initialize the calculator with principal amount, annual percentage yield (APY), and duration in years.

        :param principal: The initial amount of assets staked.
        :param apy: The annual percentage yield (in percentage).
        :param years: The number of years the assets are staked.
        """
        self.principal = decimal.Decimal(principal)
        self.apy = decimal.Decimal(apy) / 100  # Convert APY from percentage to decimal
        self.years = decimal.Decimal(years)

    def calculate_rewards(self):
        """
        Calculate the total rewards after the specified number of years.

        :return: Total amount including principal and rewards.
        """
        try:
            # Ensure the inputs are valid
            if self.principal < 0 or self.apy < 0 or self.years < 0:
                raise ValueError("Principal, APY, and years must be non-negative.")

            # Calculate total amount after staking
            total_amount = self.principal * (1 + self.apy) ** self.years
            return total_amount
        except Exception as e:
            print(f"Error calculating rewards: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    # Staking 1000 BNB with an APY of 30% for 5 years
    principal_amount = 1000  # Example principal amount
    apy_rate = 30  # Annual Percentage Yield
    staking_years = 5  # Duration in years

    # Create an instance of the calculator
    calculator = StakingRewardCalculator(principal_amount, apy_rate, staking_years)

    # Calculate and display the total rewards
    total_rewards = calculator.calculate_rewards()
    if total_rewards is not None:
        print(f"Total amount after {staking_years} years: {total_rewards:.2f}")
```
