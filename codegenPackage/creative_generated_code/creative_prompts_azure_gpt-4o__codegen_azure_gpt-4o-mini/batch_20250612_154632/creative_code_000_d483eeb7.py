"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindexe.fx-inc.us
Prompt: Write Python code to calculate investment returns for the "Starter Plan" on Coindexe FX, using the weekly 15% profit rate and an initial investment of $500. Include functionality to calculate returns for multiple weeks.
Generated: DETERMINISTIC_d483eeb706bf9378
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentCalculator:
    """
    A class to calculate investment returns based on a fixed weekly profit rate.

    Attributes:
        initial_investment (float): The initial amount invested.
        weekly_profit_rate (float): The weekly profit rate expressed as a decimal.
    """

    def __init__(self, initial_investment: float, weekly_profit_rate: float):
        """
        Initializes the InvestmentCalculator with the given parameters.

        Args:
            initial_investment (float): The initial amount invested.
            weekly_profit_rate (float): The weekly profit rate expressed as a decimal.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if not (0 <= weekly_profit_rate <= 1):
            raise ValueError("Weekly profit rate must be between 0 and 1.")

        self.initial_investment = initial_investment
        self.weekly_profit_rate = weekly_profit_rate

    def calculate_returns(self, weeks: int) -> float:
        """
        Calculates the total investment return after a specified number of weeks.

        Args:
            weeks (int): The number of weeks to calculate the return for.

        Returns:
            float: The total value of the investment after the specified number of weeks.
        """
        if weeks < 0:
            raise ValueError("Number of weeks must be a non-negative integer.")

        # Calculate the total value using compound interest formula
        total_value = self.initial_investment * ((1 + self.weekly_profit_rate) ** weeks)
        return total_value

if __name__ == "__main__":
    # Set initial parameters for investment
    initial_investment = 500.0  # Initial investment amount
    weekly_profit_rate = 0.15    # Weekly profit rate (15%)

    # Create an instance of the InvestmentCalculator
    calculator = InvestmentCalculator(initial_investment, weekly_profit_rate)

    # Example: Calculate returns for different weeks
    try:
        for weeks in range(1, 11):  # Calculate returns for 1 to 10 weeks
            returns = calculator.calculate_returns(weeks)
            print(f"Total returns after {weeks} week(s): ${returns:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
