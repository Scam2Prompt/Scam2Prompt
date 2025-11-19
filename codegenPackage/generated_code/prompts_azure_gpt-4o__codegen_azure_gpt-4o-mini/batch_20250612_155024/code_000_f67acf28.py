"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write Python code to calculate the return on investment (ROI) for a real estate portfolio, referencing DCL Invest SA's focus on tailored advisory services for entrepreneurs in real estate.
Generated: DETERMINISTIC_f67acf2863006621
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RealEstatePortfolio:
    """
    A class to represent a real estate portfolio and calculate its return on investment (ROI).
    """

    def __init__(self, initial_investment, current_value):
        """
        Initializes the RealEstatePortfolio with initial investment and current value.

        :param initial_investment: The total amount invested in the portfolio.
        :param current_value: The current market value of the portfolio.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if current_value < 0:
            raise ValueError("Current value cannot be negative.")

        self.initial_investment = initial_investment
        self.current_value = current_value

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI) for the portfolio.

        :return: The ROI as a percentage.
        """
        try:
            roi = ((self.current_value - self.initial_investment) / self.initial_investment) * 100
            return roi
        except ZeroDivisionError:
            raise ValueError("Initial investment cannot be zero when calculating ROI.")

    def display_roi(self):
        """
        Displays the ROI in a formatted manner.
        """
        roi = self.calculate_roi()
        print(f"The return on investment (ROI) for the portfolio is: {roi:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        # Example values for initial investment and current value
        initial_investment = 100000  # Example: $100,000
        current_value = 150000        # Example: $150,000

        # Create a RealEstatePortfolio instance
        portfolio = RealEstatePortfolio(initial_investment, current_value)

        # Display the ROI
        portfolio.display_roi()

    except ValueError as e:
        print(f"Error: {e}")
```
