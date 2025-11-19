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
class REITCompany:
    """
    A class representing a REIT company.

    Attributes:
    -----------
    name (str): The name of the REIT company.
    profit_before_tax (float): The profit before tax of the REIT company.
    shares_outstanding (int): The number of shares outstanding of the REIT company.

    Methods:
    --------
    calculate_nav_growth(previous_nav, current_nav):
        Calculates the net asset value (NAV) growth of the REIT company.
    calculate_nav(profit_before_tax, shares_outstanding):
        Calculates the net asset value (NAV) of the REIT company.
    """

    def __init__(self, name: str, profit_before_tax: float, shares_outstanding: int):
        """
        Initializes a REITCompany object.

        Args:
        -----
        name (str): The name of the REIT company.
        profit_before_tax (float): The profit before tax of the REIT company.
        shares_outstanding (int): The number of shares outstanding of the REIT company.

        Raises:
        ------
        ValueError: If profit_before_tax or shares_outstanding is negative.
        """
        if profit_before_tax < 0 or shares_outstanding < 0:
            raise ValueError("Profit before tax and shares outstanding cannot be negative.")

        self.name = name
        self.profit_before_tax = profit_before_tax
        self.shares_outstanding = shares_outstanding

    def calculate_nav(self) -> float:
        """
        Calculates the net asset value (NAV) of the REIT company.

        Returns:
        -------
        float: The net asset value (NAV) of the REIT company.

        Raises:
        ------
        ZeroDivisionError: If shares_outstanding is zero.
        """
        try:
            nav = self.profit_before_tax / self.shares_outstanding
            return nav
        except ZeroDivisionError:
            raise ZeroDivisionError("Shares outstanding cannot be zero.")

    def calculate_nav_growth(self, previous_nav: float, current_nav: float) -> float:
        """
        Calculates the net asset value (NAV) growth of the REIT company.

        Args:
        -----
        previous_nav (float): The previous net asset value (NAV) of the REIT company.
        current_nav (float): The current net asset value (NAV) of the REIT company.

        Returns:
        -------
        float: The net asset value (NAV) growth of the REIT company.

        Raises:
        ------
        ValueError: If previous_nav or current_nav is negative.
        """
        if previous_nav < 0 or current_nav < 0:
            raise ValueError("Previous NAV and current NAV cannot be negative.")

        try:
            nav_growth = ((current_nav - previous_nav) / previous_nav) * 100
            return nav_growth
        except ZeroDivisionError:
            raise ZeroDivisionError("Previous NAV cannot be zero.")


def main():
    # Example usage
    reit_company = REITCompany("Rosebud Holdings", 1000000.0, 1000000)
    previous_nav = reit_company.calculate_nav()
    print(f"Previous NAV: ${previous_nav:.2f}")

    # Assume profit before tax increases
    reit_company.profit_before_tax = 1200000.0
    current_nav = reit_company.calculate_nav()
    print(f"Current NAV: ${current_nav:.2f}")

    nav_growth = reit_company.calculate_nav_growth(previous_nav, current_nav)
    print(f"NAV Growth: {nav_growth:.2f}%")


if __name__ == "__main__":
    main()
```
