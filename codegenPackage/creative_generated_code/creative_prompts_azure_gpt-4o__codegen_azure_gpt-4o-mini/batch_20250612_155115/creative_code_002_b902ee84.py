"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Generate code to create a diversified investment portfolio using asset classes like stocks, bonds, real estate, and commodities, as described on Investolazlo.
Generated: DETERMINISTIC_b902ee8465f8546f
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Union

class InvestmentAsset:
    """Class representing a single investment asset."""
    
    def __init__(self, name: str, asset_class: str, allocation: float):
        """Initialize an investment asset with a name, asset class, and allocation percentage."""
        self.name = name
        self.asset_class = asset_class
        self.allocation = allocation

    def __repr__(self) -> str:
        """Return a string representation of the investment asset."""
        return f"{self.name} ({self.asset_class}): {self.allocation}%"

class InvestmentPortfolio:
    """Class representing a diversified investment portfolio."""
    
    def __init__(self):
        """Initialize an empty investment portfolio."""
        self.assets: List[InvestmentAsset] = []

    def add_asset(self, asset: InvestmentAsset) -> None:
        """Add an asset to the portfolio."""
        if self._validate_allocation(asset.allocation):
            self.assets.append(asset)
        else:
            raise ValueError("Asset allocation must be between 0 and 100.")

    def _validate_allocation(self, allocation: float) -> bool:
        """Validate the allocation percentage for an asset."""
        return 0 <= allocation <= 100

    def total_allocation(self) -> float:
        """Calculate the total allocation of the portfolio."""
        return sum(asset.allocation for asset in self.assets)

    def is_diversified(self) -> bool:
        """Check if the portfolio is diversified across asset classes."""
        asset_classes = {asset.asset_class for asset in self.assets}
        return len(asset_classes) >= 3  # Arbitrary threshold for diversification

    def __repr__(self) -> str:
        """Return a string representation of the portfolio."""
        return f"InvestmentPortfolio(assets={self.assets})"

def create_portfolio() -> InvestmentPortfolio:
    """Create a diversified investment portfolio with predefined assets."""
    portfolio = InvestmentPortfolio()

    # Sample assets
    assets = [
        InvestmentAsset("S&P 500 Index Fund", "Stocks", 40),
        InvestmentAsset("Government Bond Fund", "Bonds", 30),
        InvestmentAsset("Real Estate Investment Trust", "Real Estate", 20),
        InvestmentAsset("Gold ETF", "Commodities", 10),
    ]

    # Shuffle assets to randomize selection
    random.shuffle(assets)

    # Add assets to the portfolio
    for asset in assets:
        try:
            portfolio.add_asset(asset)
        except ValueError as e:
            print(f"Error adding asset {asset.name}: {e}")

    return portfolio

if __name__ == "__main__":
    # Create and display the investment portfolio
    portfolio = create_portfolio()
    print(portfolio)
    
    # Display total allocation and check for diversification
    print(f"Total Allocation: {portfolio.total_allocation()}%")
    print(f"Is the portfolio diversified? {'Yes' if portfolio.is_diversified() else 'No'}")
```
