"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://20eth.vip
Prompt: Explain the flexible lock period and how it affects the annual yield of 5.2% APR for staking on the 20eth.vip platform.
Generated: DETERMINISTIC_9a70a3116af29939
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script explains the concept of a flexible lock period and how it impacts the annual yield (APR) of 5.2% 
on staking for the 20eth.vip platform. The flexible lock period allows users to withdraw staked funds 
at any time without penalties, but the yield calculation is proportional to the staking duration.
"""

class StakingCalculator:
    """
    A class to calculate staking rewards based on flexible lock period and APR.
    """

    def __init__(self, apr: float):
        """
        Initialize the staking calculator with a specific APR.
        :param apr: Annual Percentage Rate as a percentage (e.g., 5.2 for 5.2%)
        """
        self.apr = apr / 100  # Convert APR from percentage to decimal

    def calculate_yield(self, stake_amount: float, staking_days: int) -> float:
        """
        Calculate the staking yield based on the amount, APR, and staking duration.
        :param stake_amount: The amount staked in ETH.
        :param staking_days: The duration of staking in days.
        :return: The yield earned (in ETH).
        """
        try:
            # Ensure staking amount and days are valid
            if stake_amount <= 0:
                raise ValueError("Staking amount must be greater than 0.")
            if staking_days < 0:
                raise ValueError("Staking days cannot be negative.")

            # Calculate annual yield (APR) over the staking period
            yearly_yield = stake_amount * self.apr
            daily_yield = yearly_yield / 365  # Divide the annual yield by the number of days in a year
            total_yield = daily_yield * staking_days  # Multiply daily yield by the staking duration

            return total_yield
        except Exception as e:
            print(f"Error calculating yield: {e}")
            return 0.0

def main():
    """
    Main function to demonstrate staking calculation with flexible lock period.
    """
    # APR for the platform (e.g., 5.2%)
    apr = 5.2

    # Initialize staking calculator
    calculator = StakingCalculator(apr)

    # Example input: Stake amount and staking duration
    stake_amount = 10.0  # 10 ETH
    staking_days = 180  # 180 days

    # Calculate yield
    yield_earned = calculator.calculate_yield(stake_amount, staking_days)

    # Output the results
    print(f"Staking Amount: {stake_amount} ETH")
    print(f"Staking Duration: {staking_days} days")
    print(f"Annual Yield (APR): {apr}%")
    print(f"Yield Earned: {yield_earned:.6f} ETH")  # Display result with precision

if __name__ == "__main__":
    main()
```
