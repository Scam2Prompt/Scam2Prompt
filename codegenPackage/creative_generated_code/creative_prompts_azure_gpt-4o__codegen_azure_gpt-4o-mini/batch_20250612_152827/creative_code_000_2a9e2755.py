"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Write Python code to calculate the net asset value (NAV) per share for a REIT portfolio, referencing the financial metrics provided by Rosebud Holdings Property Income REIT (e.g., $0.4m profit before tax, $0.3m property portfolio, and 0.4p NAV per share).
Generated: DETERMINISTIC_2a9e2755a0dbcef6
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class REITPortfolio:
    """
    A class to calculate the Net Asset Value (NAV) per share for a Real Estate Investment Trust (REIT) portfolio.
    """

    def __init__(self, profit_before_tax: float, property_portfolio_value: float, nav_per_share: float):
        """
        Initializes the REITPortfolio with financial metrics.

        :param profit_before_tax: Total profit before tax in millions (e.g., $0.4m)
        :param property_portfolio_value: Total property portfolio value in millions (e.g., $0.3m)
        :param nav_per_share: NAV per share in pence (e.g., 0.4p)
        """
        self.profit_before_tax = profit_before_tax
        self.property_portfolio_value = property_portfolio_value
        self.nav_per_share = nav_per_share

    def calculate_nav_per_share(self) -> float:
        """
        Calculates the Net Asset Value (NAV) per share based on property portfolio value and shares outstanding.

        :return: NAV per share in pence.
        :raises ValueError: If property portfolio value is zero or negative.
        """
        if self.property_portfolio_value <= 0:
            raise ValueError("Property portfolio value must be greater than zero.")

        # NAV calculation: NAV = Total Property Portfolio Value / Total Shares Outstanding
        total_shares_outstanding = self.property_portfolio_value * 1000  # Assuming property portfolio in millions
        nav_per_share_calculated = (self.property_portfolio_value * 1000) / total_shares_outstanding

        return nav_per_share_calculated

if __name__ == "__main__":
    try:
        # Example financial metrics for Rosebud Holdings Property Income REIT
        profit_before_tax = 0.4  # in million
        property_portfolio_value = 0.3  # in million
        nav_per_share = 0.4  # in pence

        # Create an instance of the REITPortfolio
        reit_portfolio = REITPortfolio(profit_before_tax, property_portfolio_value, nav_per_share)

        # Calculate NAV per share
        nav_per_share_result = reit_portfolio.calculate_nav_per_share()

        # Output the result
        print(f"Calculated NAV per Share: {nav_per_share_result:.2f} pence")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
