"""
Generated Code Metadata:
========================
Original URL: https://pogarex.com
Prompt: "Generate a code snippet to calculate the potential earnings of a user on Pogarex with a 4.05% APY on their cash and positions."
Generated: DETERMINISTIC_f800e658769d26ce
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PogarexEarningsCalculator:
    """
    A class to calculate potential earnings on Pogarex based on a given APY (Annual Percentage Yield).
    """

    def __init__(self, apy: float):
        """
        Initializes the calculator with the specified APY.

        :param apy: Annual Percentage Yield as a decimal (e.g., 4.05% should be passed as 0.0405)
        """
        if apy < 0:
            raise ValueError("APY must be a non-negative value.")
        self.apy = apy

    def calculate_earnings(self, principal: float, years: float) -> float:
        """
        Calculates the potential earnings based on the principal amount and the number of years.

        :param principal: The initial amount of cash or positions (must be non-negative).
        :param years: The number of years the money is invested (must be non-negative).
        :return: The total earnings after the specified number of years.
        """
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if years < 0:
            raise ValueError("Number of years must be a non-negative value.")

        # Calculate the total amount after the specified number of years using compound interest formula
        total_amount = principal * (1 + self.apy) ** years
        earnings = total_amount - principal
        return earnings

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a 4.05% APY
        calculator = PogarexEarningsCalculator(apy=0.0405)

        # Define principal and investment duration
        principal_amount = 1000.0  # Example principal amount in currency
        investment_years = 5.0      # Example investment duration in years

        # Calculate potential earnings
        potential_earnings = calculator.calculate_earnings(principal=principal_amount, years=investment_years)

        # Output the result
        print(f"Potential earnings after {investment_years} years: ${potential_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
