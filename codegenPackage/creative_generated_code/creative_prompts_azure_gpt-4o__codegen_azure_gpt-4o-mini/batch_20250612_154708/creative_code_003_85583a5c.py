"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenafex.com
Prompt: Write a program to calculate potential earnings from Zenafex prediction markets, factoring in the 4.05% APY on cash and positions.
Generated: DETERMINISTIC_85583a5c88149420
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ZenafexEarningsCalculator:
    """
    A class to calculate potential earnings from Zenafex prediction markets.
    It factors in the 4.05% Annual Percentage Yield (APY) on cash and positions.
    """

    def __init__(self, initial_investment: float, duration_years: float):
        """
        Initialize the calculator with the initial investment and duration.

        :param initial_investment: The amount of money invested in Zenafex markets.
        :param duration_years: The duration for which the investment is held, in years.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if duration_years < 0:
            raise ValueError("Duration in years cannot be negative.")
        
        self.initial_investment = initial_investment
        self.duration_years = duration_years
        self.apy = 0.0405  # 4.05% APY

    def calculate_earnings(self) -> float:
        """
        Calculate the potential earnings based on the initial investment and duration.

        :return: The total amount after the duration with interest.
        """
        # Compound interest formula: A = P * (1 + r/n)^(nt)
        n = 1  # Assuming interest is compounded annually
        total_amount = self.initial_investment * (1 + self.apy / n) ** (n * self.duration_years)
        return total_amount

    def total_earnings(self) -> float:
        """
        Calculate the total earnings, which is the difference between the total amount
        and the initial investment.

        :return: The earnings gained from the investment.
        """
        total_amount = self.calculate_earnings()
        return total_amount - self.initial_investment


def main():
    """
    Main function to execute the earnings calculator.
    It prompts the user for input and displays the potential earnings.
    """
    try:
        initial_investment = float(input("Enter the initial investment amount ($): "))
        duration_years = float(input("Enter the duration of investment (in years): "))

        calculator = ZenafexEarningsCalculator(initial_investment, duration_years)

        total_earnings = calculator.total_earnings()
        print(f"Total earnings after {duration_years} years: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
