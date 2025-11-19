"""
Generated Code Metadata:
========================
Original URL: https://wasabi-012.pages.dev
Prompt: Create a function to calculate the total interest earned in the Wasabi WETH vault based on the deposited amount and the current APR.
Generated: DETERMINISTIC_62c677d005fcb052
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WasabiVault:
    def __init__(self, apr: float):
        """
        Initialize the WasabiVault with the given Annual Percentage Rate (APR).

        :param apr: The annual interest rate as a percentage (e.g., 5 for 5%).
        """
        if apr < 0:
            raise ValueError("APR must be a non-negative value.")
        self.apr = apr / 100  # Convert percentage to decimal

    def calculate_interest(self, principal: float, years: float) -> float:
        """
        Calculate the total interest earned based on the deposited amount and the current APR.

        :param principal: The initial amount of money deposited (in WETH).
        :param years: The number of years the money is deposited for.
        :return: The total interest earned.
        """
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if years < 0:
            raise ValueError("Years must be a non-negative value.")

        # Calculate total interest using the formula: Interest = Principal * APR * Time
        interest = principal * self.apr * years
        return interest

# Example usage:
if __name__ == "__main__":
    try:
        vault = WasabiVault(apr=5)  # Initialize vault with 5% APR
        principal_amount = 1000  # Amount in WETH
        investment_duration = 2  # Duration in years

        total_interest = vault.calculate_interest(principal=principal_amount, years=investment_duration)
        print(f"Total interest earned: {total_interest:.2f} WETH")
    except ValueError as e:
        print(f"Error: {e}")
```
