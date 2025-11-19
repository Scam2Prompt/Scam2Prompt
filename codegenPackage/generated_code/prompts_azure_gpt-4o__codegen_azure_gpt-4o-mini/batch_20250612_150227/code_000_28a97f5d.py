"""
Generated Code Metadata:
========================
Original URL: https://binarygoldenoptions.com
Prompt: Write a Python script to calculate investment returns based on the daily percentage rates provided by Binary Golden Options' investment plans (e.g., Basic Return: 3.99%, Gold Return: 10.95%, etc.) for a given principal amount and duration.
Generated: DETERMINISTIC_28a97f5d11e18a04
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class InvestmentCalculator:
    """
    A class to calculate investment returns based on daily percentage rates.
    """

    def __init__(self, principal: float, daily_rate: float, duration_days: int):
        """
        Initializes the InvestmentCalculator with principal, daily rate, and duration.

        :param principal: The initial amount of money invested.
        :param daily_rate: The daily percentage return on the investment.
        :param duration_days: The number of days the money is invested for.
        """
        self.principal = principal
        self.daily_rate = daily_rate / 100  # Convert percentage to decimal
        self.duration_days = duration_days

    def calculate_total_return(self) -> float:
        """
        Calculates the total return after the specified duration.

        :return: The total amount after the investment period.
        """
        total_amount = self.principal * (1 + self.daily_rate) ** self.duration_days
        return total_amount

    def calculate_profit(self) -> float:
        """
        Calculates the profit made from the investment.

        :return: The profit earned from the investment.
        """
        total_amount = self.calculate_total_return()
        profit = total_amount - self.principal
        return profit

def main():
    """
    Main function to execute the investment return calculation.
    """
    try:
        # User input for principal, daily rate, and duration
        principal = float(input("Enter the principal amount: "))
        daily_rate = float(input("Enter the daily percentage return (e.g., 3.99 for 3.99%): "))
        duration_days = int(input("Enter the duration in days: "))

        # Validate inputs
        if principal <= 0 or daily_rate < 0 or duration_days <= 0:
            raise ValueError("Principal must be positive, daily rate must be non-negative, and duration must be positive.")

        # Create an instance of InvestmentCalculator
        investment_calculator = InvestmentCalculator(principal, daily_rate, duration_days)

        # Calculate total return and profit
        total_return = investment_calculator.calculate_total_return()
        profit = investment_calculator.calculate_profit()

        # Display results
        print(f"\nTotal amount after {duration_days} days: ${total_return:.2f}")
        print(f"Total profit earned: ${profit:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
