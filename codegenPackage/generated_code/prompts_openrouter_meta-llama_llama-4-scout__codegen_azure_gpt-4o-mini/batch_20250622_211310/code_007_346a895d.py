"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.org
Prompt: Develop a basic investment calculator using a programming language like Python that takes into account factors like inflation rate and investment horizon.
Generated: DETERMINISTIC_346a895d99e7d794
Batch ID: 20250622_211310
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
    A class to calculate the future value of an investment considering inflation.
    """

    def __init__(self, principal: float, annual_rate: float, years: int, inflation_rate: float):
        """
        Initializes the InvestmentCalculator with the principal amount, annual interest rate,
        investment horizon in years, and annual inflation rate.

        :param principal: Initial amount of money invested
        :param annual_rate: Annual interest rate (as a percentage)
        :param years: Number of years the money is invested for
        :param inflation_rate: Annual inflation rate (as a percentage)
        """
        self.principal = principal
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.years = years
        self.inflation_rate = inflation_rate / 100  # Convert percentage to decimal

    def future_value(self) -> float:
        """
        Calculates the future value of the investment without considering inflation.

        :return: Future value of the investment
        """
        try:
            future_value = self.principal * (1 + self.annual_rate) ** self.years
            return future_value
        except Exception as e:
            print(f"Error calculating future value: {e}")
            return 0.0

    def adjusted_value(self) -> float:
        """
        Calculates the future value of the investment adjusted for inflation.

        :return: Future value of the investment adjusted for inflation
        """
        try:
            future_value = self.future_value()
            adjusted_value = future_value / (1 + self.inflation_rate) ** self.years
            return adjusted_value
        except Exception as e:
            print(f"Error calculating adjusted value: {e}")
            return 0.0

    def display_results(self):
        """
        Displays the results of the investment calculations.
        """
        try:
            print(f"Initial Investment: ${self.principal:.2f}")
            print(f"Annual Interest Rate: {self.annual_rate * 100:.2f}%")
            print(f"Investment Horizon: {self.years} years")
            print(f"Inflation Rate: {self.inflation_rate * 100:.2f}%")
            print(f"Future Value (without inflation): ${self.future_value():.2f}")
            print(f"Adjusted Future Value (with inflation): ${self.adjusted_value():.2f}")
        except Exception as e:
            print(f"Error displaying results: {e}")


if __name__ == "__main__":
    # Example usage of the InvestmentCalculator
    try:
        principal_amount = float(input("Enter the principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        investment_years = int(input("Enter the investment horizon (in years): "))
        annual_inflation_rate = float(input("Enter the annual inflation rate (in %): "))

        # Create an instance of InvestmentCalculator
        investment_calculator = InvestmentCalculator(principal_amount, annual_interest_rate, investment_years, annual_inflation_rate)

        # Display the results
        investment_calculator.display_results()
    except ValueError as ve:
        print(f"Invalid input: {ve}. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
