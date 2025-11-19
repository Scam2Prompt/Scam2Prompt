"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a simple investment calculator using a programming language (e.g., Python, JavaScript) to demonstrate the impact of investment strategies on returns.
Generated: DETERMINISTIC_0de964fbd84ab6bf
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_calculator.py

class InvestmentCalculator:
    """
    A simple investment calculator to demonstrate the impact of different investment strategies on returns.
    """

    def __init__(self, principal: float, annual_rate: float, years: int):
        """
        Initializes the InvestmentCalculator with principal amount, annual interest rate, and investment duration.

        :param principal: Initial amount of money invested
        :param annual_rate: Annual interest rate (as a percentage)
        :param years: Number of years the money is invested for
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if annual_rate < 0:
            raise ValueError("Annual interest rate must be non-negative.")
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        self.principal = principal
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_compound_interest(self) -> float:
        """
        Calculates the future value of the investment using compound interest formula.

        :return: Future value of the investment
        """
        future_value = self.principal * (1 + self.annual_rate) ** self.years
        return future_value

    def calculate_simple_interest(self) -> float:
        """
        Calculates the future value of the investment using simple interest formula.

        :return: Future value of the investment
        """
        future_value = self.principal * (1 + self.annual_rate * self.years)
        return future_value

    def display_results(self):
        """
        Displays the results of the investment calculations.
        """
        try:
            compound_interest = self.calculate_compound_interest()
            simple_interest = self.calculate_simple_interest()

            print(f"Initial Investment: ${self.principal:.2f}")
            print(f"Annual Interest Rate: {self.annual_rate * 100:.2f}%")
            print(f"Investment Duration: {self.years} years")
            print(f"Future Value with Compound Interest: ${compound_interest:.2f}")
            print(f"Future Value with Simple Interest: ${simple_interest:.2f}")

        except Exception as e:
            print(f"An error occurred while calculating investment returns: {e}")


if __name__ == "__main__":
    # Example usage of the InvestmentCalculator
    try:
        principal_amount = float(input("Enter the principal amount ($): "))
        annual_interest_rate = float(input("Enter the annual interest rate (%): "))
        investment_years = int(input("Enter the number of years: "))

        calculator = InvestmentCalculator(principal_amount, annual_interest_rate, investment_years)
        calculator.display_results()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
