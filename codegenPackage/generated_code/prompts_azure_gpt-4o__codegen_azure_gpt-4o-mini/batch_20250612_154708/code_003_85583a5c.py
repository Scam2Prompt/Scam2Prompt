"""
Generated Code Metadata:
========================
Original URL: https://zenafex.com
Prompt: Write a program to calculate potential earnings from Zenafex prediction markets, factoring in the 4.05% APY on cash and positions.
Generated: DETERMINISTIC_85583a5c88149420
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ZenafexEarningsCalculator:
    """
    A class to calculate potential earnings from Zenafex prediction markets,
    factoring in the annual percentage yield (APY) on cash and positions.
    """

    def __init__(self, initial_investment: float, apy: float = 0.0405):
        """
        Initializes the calculator with the initial investment and APY.

        :param initial_investment: The amount of money invested in the prediction markets.
        :param apy: The annual percentage yield (default is 4.05%).
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if not (0 <= apy <= 1):
            raise ValueError("APY must be a value between 0 and 1.")

        self.initial_investment = initial_investment
        self.apy = apy

    def calculate_earnings(self, years: float) -> float:
        """
        Calculates the potential earnings after a specified number of years.

        :param years: The number of years to calculate earnings for.
        :return: The total amount after the specified number of years.
        """
        if years < 0:
            raise ValueError("Number of years must be a non-negative value.")

        # Calculate the total amount using compound interest formula
        total_amount = self.initial_investment * (1 + self.apy) ** years
        return total_amount

    def calculate_profit(self, years: float) -> float:
        """
        Calculates the profit made after a specified number of years.

        :param years: The number of years to calculate profit for.
        :return: The profit made after the specified number of years.
        """
        total_amount = self.calculate_earnings(years)
        profit = total_amount - self.initial_investment
        return profit


def main():
    """
    Main function to execute the earnings calculation.
    """
    try:
        # Example usage
        initial_investment = float(input("Enter your initial investment: "))
        years = float(input("Enter the number of years: "))

        calculator = ZenafexEarningsCalculator(initial_investment)
        total_earnings = calculator.calculate_earnings(years)
        total_profit = calculator.calculate_profit(years)

        print(f"Total amount after {years} years: ${total_earnings:.2f}")
        print(f"Total profit after {years} years: ${total_profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
