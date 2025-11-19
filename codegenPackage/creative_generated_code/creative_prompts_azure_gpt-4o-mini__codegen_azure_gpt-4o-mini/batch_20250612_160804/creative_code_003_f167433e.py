"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yehudit-taxes.co.il
Prompt: How do I prepare a wealth declaration accurately, and what specific details should I pay attention to according to Yehudit Benedict's guidelines?
Generated: DETERMINISTIC_f167433ed0a34d59
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WealthDeclaration:
    """
    A class to represent a wealth declaration.

    Attributes
    ----------
    assets : dict
        A dictionary to hold asset types and their respective values.
    liabilities : dict
        A dictionary to hold liability types and their respective values.
    net_worth : float
        The calculated net worth from assets and liabilities.
    """

    def __init__(self):
        """
        Initializes the WealthDeclaration with empty assets and liabilities.
        """
        self.assets = {}
        self.liabilities = {}
        self.net_worth = 0.0

    def add_asset(self, asset_name: str, value: float) -> None:
        """
        Adds an asset to the wealth declaration.

        Parameters
        ----------
        asset_name : str
            The name of the asset.
        value : float
            The value of the asset.

        Raises
        ------
        ValueError
            If the value is negative.
        """
        if value < 0:
            raise ValueError("Asset value cannot be negative.")
        self.assets[asset_name] = value

    def add_liability(self, liability_name: str, value: float) -> None:
        """
        Adds a liability to the wealth declaration.

        Parameters
        ----------
        liability_name : str
            The name of the liability.
        value : float
            The value of the liability.

        Raises
        ------
        ValueError
            If the value is negative.
        """
        if value < 0:
            raise ValueError("Liability value cannot be negative.")
        self.liabilities[liability_name] = value

    def calculate_net_worth(self) -> float:
        """
        Calculates the net worth by subtracting total liabilities from total assets.

        Returns
        -------
        float
            The calculated net worth.
        """
        total_assets = sum(self.assets.values())
        total_liabilities = sum(self.liabilities.values())
        self.net_worth = total_assets - total_liabilities
        return self.net_worth

    def generate_declaration(self) -> str:
        """
        Generates a formatted wealth declaration report.

        Returns
        -------
        str
            A string representation of the wealth declaration.
        """
        report = "Wealth Declaration\n"
        report += "=" * 30 + "\n"
        report += "Assets:\n"
        for asset, value in self.assets.items():
            report += f" - {asset}: ${value:,.2f}\n"
        report += "\nLiabilities:\n"
        for liability, value in self.liabilities.items():
            report += f" - {liability}: ${value:,.2f}\n"
        report += "\nNet Worth: ${:,.2f}\n".format(self.calculate_net_worth())
        return report

# Example usage
if __name__ == "__main__":
    try:
        declaration = WealthDeclaration()
        declaration.add_asset("House", 300000)
        declaration.add_asset("Car", 15000)
        declaration.add_liability("Mortgage", 250000)
        declaration.add_liability("Car Loan", 5000)

        print(declaration.generate_declaration())
    except ValueError as e:
        print(f"Error: {e}")
```
