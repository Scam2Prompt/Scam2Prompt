"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-money.pages.dev
Prompt: Generate code to calculate the yield earned from staking $MONEY on DeFi.money, given a specific staking duration and rate.
Generated: DETERMINISTIC_07d819e7d54f21aa
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeFiStakingCalculator:
    """
    A class to calculate the yield earned from staking on DeFi.money.

    Attributes:
        principal (float): The amount of money staked.
        annual_rate (float): The annual yield rate (as a decimal).
        duration_days (int): The duration of staking in days.
    """
    
    def __init__(self, principal: float, annual_rate: float, duration_days: int):
        """
        Initializes the DeFiStakingCalculator with principal, annual rate, and duration.

        Parameters:
            principal (float): The amount of money to stake.
            annual_rate (float): The annual yield rate (as a decimal).
            duration_days (int): The duration in days for which the money is staked.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if not (0 <= annual_rate <= 1):
            raise ValueError("Annual rate must be between 0 and 1.")
        if duration_days <= 0:
            raise ValueError("Duration in days must be greater than zero.")
        
        self.principal = principal
        self.annual_rate = annual_rate
        self.duration_days = duration_days

    def calculate_yield(self) -> float:
        """
        Calculate the yield earned from staking.

        Returns:
            float: The calculated yield earned from staking.
        """
        # Calculate the yield using simple interest formula
        yield_earned = self.principal * self.annual_rate * (self.duration_days / 365)
        return yield_earned

    def get_total_value(self) -> float:
        """
        Get the total value of the investment after staking.

        Returns:
            float: The total value, including principal and yield.
        """
        return self.principal + self.calculate_yield()


if __name__ == "__main__":
    try:
        # Example usage
        principal_amount = 1000  # Principal amount in $
        annual_yield_rate = 0.05  # Annual yield rate (5%)
        staking_duration = 30  # Duration in days

        staking_calculator = DeFiStakingCalculator(principal_amount, annual_yield_rate, staking_duration)
        yield_earned = staking_calculator.calculate_yield()
        total_value = staking_calculator.get_total_value()

        print(f"Yield earned: ${yield_earned:.2f}")
        print(f"Total value after staking: ${total_value:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
