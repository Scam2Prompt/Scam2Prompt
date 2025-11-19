"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Write a Python script that calculates the actual interest from DeFi yield rates, considering the nuances of APY as discussed in the article.
Generated: DETERMINISTIC_63ac86ff1cb36fc3
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class DeFiYieldCalculator:
    """
    A class to calculate the actual interest from DeFi yield rates based on APY.
    """

    def __init__(self, principal: float, apy: float, periods: int = 365):
        """
        Initializes the DeFiYieldCalculator with principal amount, APY, and compounding periods.

        :param principal: Initial amount of money (float).
        :param apy: Annual Percentage Yield as a decimal (i.e., 0.05 for 5%).
        :param periods: Number of times interest is compounded per year (default is 365).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if not (0 <= apy <= 1):
            raise ValueError("APY must be a decimal between 0 and 1.")
        if periods <= 0:
            raise ValueError("Compounding periods must be a positive integer.")

        self.principal = principal
        self.apy = apy
        self.periods = periods

    def calculate_compound_interest(self, years: float) -> float:
        """
        Calculates the total amount after applying compound interest over a given number of years.

        :param years: The number of years to calculate interest for (float).
        :return: Total amount after interest (float).
        """
        if years < 0:
            raise ValueError("Years must be a non-negative number.")

        # Using the compound interest formula A = P(1 + r/n)^(nt)
        total_amount = self.principal * math.pow((1 + self.apy / self.periods), self.periods * years)
        return total_amount

    def calculate_actual_interest(self, years: float) -> float:
        """
        Calculates the actual interest earned after a certain number of years.

        :param years: The number of years to calculate interest for (float).
        :return: Actual interest earned (float).
        """
        total_amount = self.calculate_compound_interest(years)
        actual_interest = total_amount - self.principal
        return actual_interest

def main():
    """
    Main function to execute the interest calculation.
    """
    try:
        # Example parameters for calculation
        principal_amount = 1000.0  # Principal amount in currency
        annual_percentage_yield = 0.05  # APY as a decimal (5%)
        investment_duration = 5  # Duration in years

        # Create an instance of the DeFiYieldCalculator
        calculator = DeFiYieldCalculator(principal_amount, annual_percentage_yield)

        # Calculate actual interest earned
        interest_earned = calculator.calculate_actual_interest(investment_duration)

        # Display results
        print(f"Principal Amount: ${principal_amount:.2f}")
        print(f"APY: {annual_percentage_yield * 100:.2f}%")
        print(f"Investment Duration: {investment_duration} years")
        print(f"Actual Interest Earned: ${interest_earned:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
