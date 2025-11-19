"""
Generated Code Metadata:
========================
Original URL: https://beefy.pages.dev
Prompt: Write a code snippet to calculate compound interest on a crypto holding using Beefy's interest rates and compounding frequency.
Generated: DETERMINISTIC_e70ffe37643da7b6
Batch ID: 20250622_205156
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
    A class to calculate compound interest for crypto holdings based on Beefy's interest rates and compounding frequency.
    """

    def __init__(self, principal: float, annual_rate: float, compounding_frequency: int):
        """
        Initializes the CompoundInterestCalculator with the principal amount, annual interest rate, and compounding frequency.

        :param principal: The initial amount of money (the principal).
        :param annual_rate: The annual interest rate (as a decimal, e.g., 0.05 for 5%).
        :param compounding_frequency: The number of times that interest is compounded per year.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if annual_rate < 0:
            raise ValueError("Annual interest rate must be non-negative.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")

        self.principal = principal
        self.annual_rate = annual_rate
        self.compounding_frequency = compounding_frequency

    def calculate_compound_interest(self, years: float) -> float:
        """
        Calculates the compound interest over a specified number of years.

        :param years: The number of years the money is invested or borrowed for.
        :return: The total amount after interest.
        """
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        # Compound interest formula: A = P (1 + r/n)^(nt)
        amount = self.principal * (1 + self.annual_rate / self.compounding_frequency) ** (self.compounding_frequency * years)
        return amount

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a principal of 1000, an annual rate of 5%, and compounding monthly
        calculator = CompoundInterestCalculator(principal=1000, annual_rate=0.05, compounding_frequency=12)
        
        # Calculate the total amount after 10 years
        total_amount = calculator.calculate_compound_interest(years=10)
        print(f"Total amount after 10 years: ${total_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
