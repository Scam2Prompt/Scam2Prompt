"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.nl
Prompt: In what ways does Immediate Peak help users understand the principles of asset allocation and diversification in investing?
Generated: DETERMINISTIC_7ba610d6c5e8a2ba
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPortfolio:
    """
    A class to represent an investment portfolio with methods to help
    users understand asset allocation and diversification in investing.
    """

    def __init__(self):
        """
        Initializes an empty portfolio.
        """
        self.assets = {}
    
    def add_asset(self, asset_name, value):
        """
        Adds an asset to the portfolio.

        :param asset_name: The name of the asset
        :param value: The value of the asset
        :raises ValueError: If the value is negative
        """
        if value < 0:
            raise ValueError("Asset value cannot be negative.")
        self.assets[asset_name] = value

    def total_value(self):
        """
        Calculates the total value of the portfolio.

        :return: Total value of all assets in the portfolio
        """
        return sum(self.assets.values())

    def asset_allocation(self):
        """
        Calculates the allocation of each asset as a percentage of the total portfolio.

        :return: A dictionary with asset names as keys and their allocation percentages as values
        """
        total = self.total_value()
        if total == 0:
            return {}

        allocation = {asset: (value / total) * 100 for asset, value in self.assets.items()}
        return allocation

    def diversification_score(self):
        """
        Evaluates the diversification of the portfolio.

        :return: A score based on the number of unique assets
        """
        num_assets = len(self.assets)
        if num_assets == 0:
            return 0
        # A simple score based on the number of unique assets
        return min(num_assets, 10)  # Capping to a maximum score of 10 for simplicity

    def report(self):
        """
        Generates a report of the portfolio showing total value,
        asset allocation, and diversification score.
        
        :return: A formatted report string
        """
        report_lines = []
        report_lines.append(f"Total Portfolio Value: ${self.total_value():,.2f}")
        report_lines.append("Asset Allocation:")
        
        allocation = self.asset_allocation()
        for asset, percentage in allocation.items():
            report_lines.append(f" - {asset}: {percentage:.2f}%")
        
        diversity_score = self.diversification_score()
        report_lines.append(f"Diversification Score: {diversity_score}/10")
        
        return "\n".join(report_lines)


# Example Usage
if __name__ == "__main__":
    try:
        portfolio = InvestmentPortfolio()
        portfolio.add_asset("Stocks", 5000)
        portfolio.add_asset("Bonds", 3000)
        portfolio.add_asset("Real Estate", 2000)

        print(portfolio.report())
    except ValueError as e:
        print(f"Error: {e}")
```
