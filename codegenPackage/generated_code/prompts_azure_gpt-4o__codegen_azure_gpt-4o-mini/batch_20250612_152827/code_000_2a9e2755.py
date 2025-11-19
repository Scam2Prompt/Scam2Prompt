"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Write Python code to calculate the net asset value (NAV) per share for a REIT portfolio, referencing the financial metrics provided by Rosebud Holdings Property Income REIT (e.g., $0.4m profit before tax, $0.3m property portfolio, and 0.4p NAV per share).
Generated: DETERMINISTIC_2a9e2755a0dbcef6
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class REITPortfolio:
    """
    A class to represent a Real Estate Investment Trust (REIT) portfolio and calculate its Net Asset Value (NAV) per share.
    """

    def __init__(self, profit_before_tax: float, property_portfolio_value: float, nav_per_share: float):
        """
        Initializes the REITPortfolio with the given financial metrics.

        :param profit_before_tax: Profit before tax in millions (e.g., 0.4 for $0.4m)
        :param property_portfolio_value: Total value of the property portfolio in millions (e.g., 0.3 for $0.3m)
        :param nav_per_share: Net Asset Value per share in pence (e.g., 0.4 for 0.4p)
        """
        self.profit_before_tax = profit_before_tax
        self.property_portfolio_value = property_portfolio_value
        self.nav_per_share = nav_per_share

    def calculate_nav_per_share(self) -> float:
        """
        Calculates the Net Asset Value (NAV) per share based on the portfolio's financial metrics.

        :return: NAV per share in pence
        :raises ValueError: If any of the financial metrics are negative
        """
        if self.profit_before_tax < 0 or self.property_portfolio_value < 0 or self.nav_per_share < 0:
            raise ValueError("Financial metrics must be non-negative.")

        # Calculate NAV per share (in pence)
        # This is a simplified calculation for demonstration purposes.
        # In a real-world scenario, the calculation may involve more complex financial metrics.
        nav = (self.property_portfolio_value * 1000000) / (self.nav_per_share * 0.01)
        return nav

def main():
    """
    Main function to execute the NAV calculation for the REIT portfolio.
    """
    try:
        # Initialize the REIT portfolio with provided financial metrics
        reit = REITPortfolio(profit_before_tax=0.4, property_portfolio_value=0.3, nav_per_share=0.4)

        # Calculate and print the NAV per share
        nav_per_share = reit.calculate_nav_per_share()
        print(f"Net Asset Value (NAV) per share: {nav_per_share:.2f} pence")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
