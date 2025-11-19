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
    A class to calculate the net asset value (NAV) per share for a REIT portfolio.

    Attributes:
    profit_before_tax (float): The profit before tax in millions of dollars.
    property_portfolio_value (float): The total value of the property portfolio in millions of dollars.
    shares_outstanding (int): The total number of shares outstanding.

    Methods:
    calculate_nav_per_share(): Calculates the NAV per share.
    """

    def __init__(self, profit_before_tax, property_portfolio_value, nav_per_share=None, shares_outstanding=1000000):
        """
        Initializes a REITPortfolio object.

        Args:
        profit_before_tax (float): The profit before tax in millions of dollars.
        property_portfolio_value (float): The total value of the property portfolio in millions of dollars.
        nav_per_share (float, optional): The NAV per share. Defaults to None.
        shares_outstanding (int, optional): The total number of shares outstanding. Defaults to 1000000.
        """
        self.profit_before_tax = profit_before_tax
        self.property_portfolio_value = property_portfolio_value
        self.nav_per_share = nav_per_share
        self.shares_outstanding = shares_outstanding

    def calculate_nav(self):
        """
        Calculates the net asset value (NAV).

        Returns:
        float: The NAV in millions of dollars.
        """
        # Calculate NAV as property portfolio value + profit before tax
        nav = self.property_portfolio_value + self.profit_before_tax
        return nav

    def calculate_nav_per_share(self):
        """
        Calculates the NAV per share.

        Returns:
        float: The NAV per share in dollars.

        Raises:
        ZeroDivisionError: If shares outstanding is zero.
        """
        try:
            nav = self.calculate_nav()
            nav_per_share = nav / (self.shares_outstanding / 1000000)  # Convert shares to millions
            return nav_per_share
        except ZeroDivisionError:
            print("Error: Shares outstanding cannot be zero.")
            return None


def main():
    # Example usage
    reit_portfolio = REITPortfolio(
        profit_before_tax=0.4, 
        property_portfolio_value=0.3, 
        shares_outstanding=1000000
    )

    nav_per_share = reit_portfolio.calculate_nav_per_share()
    print(f"NAV per share: ${nav_per_share:.4f}")


if __name__ == "__main__":
    main()
```
