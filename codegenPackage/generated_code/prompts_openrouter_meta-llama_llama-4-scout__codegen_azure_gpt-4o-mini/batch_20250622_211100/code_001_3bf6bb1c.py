"""
Generated Code Metadata:
========================
Original URL: https://compoundclaims.net
Prompt: Generate a Python script to calculate compound claims in finance.
Generated: DETERMINISTIC_3bf6bb1c303c5bf5
Batch ID: 20250622_211100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompoundInterestCalculator:
    """
    A class to calculate compound interest and total amount after a specified number of periods.
    """

    def __init__(self, principal: float, rate: float, times_compounded: int, years: int):
        """
        Initializes the calculator with principal, interest rate, number of times interest is compounded per year, and number of years.

        :param principal: Initial amount of money (the principal)
        :param rate: Annual interest rate (as a decimal)
        :param times_compounded: Number of times interest is compounded per year
        :param years: Number of years the money is invested or borrowed
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        if times_compounded <= 0:
            raise ValueError("Times compounded must be a positive integer.")
        if years < 0:
            raise ValueError("Years must be non-negative.")

        self.principal = principal
        self.rate = rate
        self.times_compounded = times_compounded
        self.years = years

    def calculate_compound_interest(self) -> float:
        """
        Calculates the compound interest.

        :return: The compound interest earned
        """
        amount = self.principal * (1 + self.rate / self.times_compounded) ** (self.times_compounded * self.years)
        compound_interest = amount - self.principal
        return compound_interest

    def calculate_total_amount(self) -> float:
        """
        Calculates the total amount after interest.

        :return: The total amount after interest
        """
        total_amount = self.principal * (1 + self.rate / self.times_compounded) ** (self.times_compounded * self.years)
        return total_amount


def main():
    """
    Main function to execute the compound interest calculation.
    """
    try:
        # Example values for the calculation
        principal = 1000.0  # Initial investment
        rate = 0.05         # Annual interest rate (5%)
        times_compounded = 4 # Quarterly compounding
        years = 10          # Investment duration in years

        # Create an instance of the calculator
        calculator = CompoundInterestCalculator(principal, rate, times_compounded, years)

        # Calculate compound interest and total amount
        compound_interest = calculator.calculate_compound_interest()
        total_amount = calculator.calculate_total_amount()

        # Output the results
        print(f"Compound Interest: ${compound_interest:.2f}")
        print(f"Total Amount after {years} years: ${total_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
