"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Generate a Python code snippet to calculate the net asset value (NAV) growth of a REIT company like Rosebud Holdings, given its profit before tax and number of shares outstanding.
Generated: DETERMINISTIC_6ff9c33fcab57094
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class REIT:
    def __init__(self, profit_before_tax: float, shares_outstanding: int):
        """
        Initializes the REIT instance with profit before tax and shares outstanding.

        :param profit_before_tax: Total profit before tax of the REIT.
        :param shares_outstanding: Total number of shares outstanding for the REIT.
        """
        if profit_before_tax < 0:
            raise ValueError("Profit before tax must be a non-negative value.")
        if shares_outstanding <= 0:
            raise ValueError("Number of shares outstanding must be a positive integer.")

        self.profit_before_tax = profit_before_tax
        self.shares_outstanding = shares_outstanding

    def calculate_nav_growth(self) -> float:
        """
        Calculates the net asset value (NAV) growth per share.

        :return: NAV growth per share.
        """
        # Calculate NAV growth per share
        nav_growth = self.profit_before_tax / self.shares_outstanding
        return nav_growth

def main():
    try:
        # Example values for profit before tax and shares outstanding
        profit_before_tax = 1000000.0  # Example profit before tax
        shares_outstanding = 100000      # Example number of shares outstanding

        # Create a REIT instance
        reit = REIT(profit_before_tax, shares_outstanding)

        # Calculate and print the NAV growth
        nav_growth = reit.calculate_nav_growth()
        print(f"Net Asset Value (NAV) growth per share: ${nav_growth:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
