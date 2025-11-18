"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binarygoldenoptions.com
Prompt: Write a Python script to calculate investment returns based on the daily percentage rates provided by Binary Golden Options' investment plans (e.g., Basic Return: 3.99%, Gold Return: 10.95%, etc.) for a given principal amount and duration.
Generated: DETERMINISTIC_28a97f5d11e18a04
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentCalculator:
    """
    A class to calculate investment returns based on daily percentage rates.
    """

    def __init__(self, principal: float, daily_rate: float, days: int):
        """
        Initialize the InvestmentCalculator with principal, daily rate, and duration.

        :param principal: The initial amount of money invested.
        :param daily_rate: The daily return rate as a percentage (e.g., 3.99 for 3.99%).
        :param days: The number of days the money is invested for.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if daily_rate <= 0:
            raise ValueError("Daily rate must be greater than zero.")
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")

        self.principal = principal
        self.daily_rate = daily_rate / 100  # Convert percentage to decimal
        self.days = days

    def calculate_return(self) -> float:
        """
        Calculate the total return after the investment duration.

        :return: The total amount after the investment period.
        """
        total_amount = self.principal * (1 + self.daily_rate) ** self.days
        return total_amount

    def calculate_profit(self) -> float:
        """
        Calculate the profit made from the investment.

        :return: The profit amount after the investment period.
        """
        total_amount = self.calculate_return()
        profit = total_amount - self.principal
        return profit


def main():
    """
    Main function to execute the investment calculation.
    """
    try:
        # Example input values
        principal = float(input("Enter the principal amount: "))
        daily_rate = float(input("Enter the daily percentage rate (e.g., for 3.99% enter 3.99): "))
        days = int(input("Enter the number of days: "))

        # Create an instance of InvestmentCalculator
        calculator = InvestmentCalculator(principal, daily_rate, days)

        # Calculate return and profit
        total_return = calculator.calculate_return()
        profit = calculator.calculate_profit()

        # Display the results
        print(f"Total amount after {days} days: ${total_return:.2f}")
        print(f"Total profit: ${profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
