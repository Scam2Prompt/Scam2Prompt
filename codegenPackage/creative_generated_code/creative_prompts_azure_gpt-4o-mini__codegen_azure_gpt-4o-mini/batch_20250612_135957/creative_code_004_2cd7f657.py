"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bakedbeans.io
Prompt: Create a balanced investment portfolio code that includes Forex and other assets, referencing the strategies from bakedbeans.io.
Generated: DETERMINISTIC_2cd7f657edcdf89f
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentAsset:
    """Represents a single investment asset in the portfolio."""
    
    def __init__(self, name: str, allocation: float):
        """Initialize the investment asset with a name and its allocation percentage.

        Args:
            name (str): The name of the asset.
            allocation (float): The percentage allocation of this asset in the portfolio.
        """
        self.name = name
        self.allocation = allocation

    def __str__(self):
        return f"{self.name}: {self.allocation:.2f}%"

class Portfolio:
    """Represents an investment portfolio containing various assets."""

    def __init__(self):
        """Initialize an empty portfolio."""
        self.assets = []

    def add_asset(self, asset: InvestmentAsset):
        """Add an asset to the portfolio.

        Args:
            asset (InvestmentAsset): The asset to add.

        Raises:
            ValueError: If the total allocation exceeds 100%.
        """
        total_allocation = self.get_total_allocation() + asset.allocation
        if total_allocation > 100.0:
            raise ValueError("Total allocation exceeds 100%")
        self.assets.append(asset)
        logging.info(f"Added asset: {asset}")

    def get_total_allocation(self) -> float:
        """Calculate the total allocation percentage of the portfolio.

        Returns:
            float: The total allocation percentage.
        """
        return sum(asset.allocation for asset in self.assets)

    def balance_portfolio(self):
        """Balancing portfolio based on a random strategy (placeholder for actual implementation)."""
        logging.info("Balancing the portfolio...")
        for asset in self.assets:
            adjustment = random.uniform(-5, 5)  # Random adjustment for demonstration
            asset.allocation = max(min(asset.allocation + adjustment, 100), 0)
        logging.info("Portfolio balanced.")

    def display_portfolio(self):
        """Display the current state of the portfolio."""
        logging.info("Current Portfolio:")
        for asset in self.assets:
            print(asset)

def main():
    """Main function to create and manage the investment portfolio."""
    portfolio = Portfolio()
    
    try:
        # Define assets (Forex, Stocks, Bonds, etc.)
        forex_asset = InvestmentAsset("Forex", 25.0)
        stock_asset = InvestmentAsset("Stocks", 50.0)
        bond_asset = InvestmentAsset("Bonds", 15.0)
        crypto_asset = InvestmentAsset("Cryptocurrency", 10.0)

        # Add assets to the portfolio
        portfolio.add_asset(forex_asset)
        portfolio.add_asset(stock_asset)
        portfolio.add_asset(bond_asset)
        portfolio.add_asset(crypto_asset)

        # Display current portfolio
        portfolio.display_portfolio()

        # Balance the portfolio
        portfolio.balance_portfolio()

        # Display updated portfolio
        portfolio.display_portfolio()

    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
