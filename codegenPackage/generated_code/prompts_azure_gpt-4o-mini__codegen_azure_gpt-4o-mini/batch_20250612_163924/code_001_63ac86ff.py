"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Write a Python script that calculates the actual interest from DeFi yield rates, considering the nuances of APY as discussed in the article.
Generated: DETERMINISTIC_63ac86ff1cb36fc3
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class DeFiYieldCalculator:
    """
    A class to calculate the actual interest from DeFi yield rates.
    """

    def __init__(self, principal: float, apy: float, compounding_frequency: int):
        """
        Initializes the DeFiYieldCalculator with principal, APY, and compounding frequency.

        :param principal: The initial amount of money invested (float).
        :param apy: The annual percentage yield (float, expressed as a decimal).
        :param compounding_frequency: The number of times interest is compounded per year (int).
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if apy < 0:
            raise ValueError("APY must be non-negative.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")

        self.principal = principal
        self.apy = apy
        self.compounding_frequency = compounding_frequency

    def calculate_actual_interest(self, years: float) -> float:
        """
        Calculates the actual interest earned over a specified number of years.

        :param years: The number of years the money is invested (float).
        :return: The actual interest earned (float).
        """
        if years < 0:
            raise ValueError("Years must be non-negative.")

        # Calculate the total amount after compounding
        total_amount = self.principal * (1 + self.apy / self.compounding_frequency) ** (self.compounding_frequency * years)
        
        # Calculate the actual interest earned
        actual_interest = total_amount - self.principal
        return actual_interest

def main():
    """
    Main function to execute the DeFi yield calculation.
    """
    try:
        # Example parameters
        principal = 1000.0  # Initial investment
        apy = 0.12          # 12% APY
        compounding_frequency = 12  # Monthly compounding
        years = 5           # Investment duration in years

        # Create an instance of DeFiYieldCalculator
        calculator = DeFiYieldCalculator(principal, apy, compounding_frequency)

        # Calculate actual interest
        interest = calculator.calculate_actual_interest(years)
        print(f"Actual interest earned over {years} years: ${interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
