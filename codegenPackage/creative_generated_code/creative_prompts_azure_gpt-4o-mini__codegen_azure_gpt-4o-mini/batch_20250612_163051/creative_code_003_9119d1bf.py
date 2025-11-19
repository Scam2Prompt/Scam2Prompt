"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Write a function that calculates potential earnings from DeFi investments, incorporating the interest rates highlighted on DefyApps.
Generated: DETERMINISTIC_9119d1bfcb1f7420
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeFiInvestment:
    """
    A class to represent a DeFi investment and calculate potential earnings.

    Attributes:
        principal (float): The initial amount of money invested.
        interest_rate (float): The annual interest rate as a percentage.
        years (int): The number of years the money is invested.

    Methods:
        calculate_earnings(): Calculates potential earnings based on interest rate and time invested.
    """

    def __init__(self, principal: float, interest_rate: float, years: int):
        """
        Initializes the DeFiInvestment class with given parameters.

        Args:
            principal (float): The initial amount of money invested.
            interest_rate (float): The annual interest rate as a percentage.
            years (int): The number of years the money is invested.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= interest_rate <= 100):
            raise ValueError("Interest rate must be between 0 and 100.")
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        self.principal = principal
        self.interest_rate = interest_rate
        self.years = years

    def calculate_earnings(self) -> float:
        """
        Calculates the potential earnings from the investment.

        Returns:
            float: The total amount after the investment period, including initial principal.
        """
        # Calculate total amount using compound interest formula
        total_amount = self.principal * (1 + (self.interest_rate / 100)) ** self.years
        return total_amount

# Example usage of DeFiInvestment class
if __name__ == "__main__":
    try:
        # Replace the values below with actual investment details
        investment = DeFiInvestment(principal=1000, interest_rate=5, years=3)
        earnings = investment.calculate_earnings()
        print(f"Total amount after {investment.years} years: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
