"""
Generated Code Metadata:
========================
Original URL: https://coindexe.fx-inc.us
Prompt: Write Python code to calculate investment returns for the "Starter Plan" on Coindexe FX, using the weekly 15% profit rate and an initial investment of $500. Include functionality to calculate returns for multiple weeks.
Generated: DETERMINISTIC_d483eeb706bf9378
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentCalculator:
    """
    A class to calculate investment returns based on a fixed weekly profit rate.
    """

    def __init__(self, initial_investment: float, weekly_rate: float):
        """
        Initializes the InvestmentCalculator with an initial investment and weekly profit rate.

        :param initial_investment: The amount of money to invest initially.
        :param weekly_rate: The weekly profit rate as a decimal (e.g., 0.15 for 15%).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 < weekly_rate < 1):
            raise ValueError("Weekly rate must be between 0 and 1.")

        self.initial_investment = initial_investment
        self.weekly_rate = weekly_rate

    def calculate_returns(self, weeks: int) -> float:
        """
        Calculates the total returns after a specified number of weeks.

        :param weeks: The number of weeks to calculate returns for.
        :return: The total amount after the specified number of weeks.
        """
        if weeks < 0:
            raise ValueError("Number of weeks cannot be negative.")

        total_amount = self.initial_investment * ((1 + self.weekly_rate) ** weeks)
        return total_amount

def main():
    """
    Main function to execute the investment return calculation.
    """
    try:
        initial_investment = 500.0  # Initial investment amount
        weekly_profit_rate = 0.15    # Weekly profit rate (15%)
        weeks = int(input("Enter the number of weeks to calculate returns for: "))

        # Create an instance of InvestmentCalculator
        investment_calculator = InvestmentCalculator(initial_investment, weekly_profit_rate)

        # Calculate the returns
        total_returns = investment_calculator.calculate_returns(weeks)

        # Display the results
        print(f"Total amount after {weeks} weeks: ${total_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
