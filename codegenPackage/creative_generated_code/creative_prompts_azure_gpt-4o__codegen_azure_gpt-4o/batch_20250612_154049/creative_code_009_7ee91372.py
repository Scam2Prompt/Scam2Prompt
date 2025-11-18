"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guapzenith.com
Prompt: Build a Python script to simulate diversified portfolio creation and automatic adjustments based on market price movements, inspired by guapzenith.com’s risk mitigation strategies.
Generated: DETERMINISTIC_7ee913727e673124
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class Portfolio:
    """
    Represents a diversified portfolio. Handles asset allocation,
    portfolio adjustments based on market price movements.
    """
    def __init__(self, assets, initial_allocations):
        """
        Initializes the portfolio.

        :param assets: List of asset names.
        :param initial_allocations: Dictionary with asset names as keys and allocation percentage as values.
        """
        if not set(assets).issubset(initial_allocations.keys()):
            raise ValueError("All assets must have an initial allocation.")
        if sum(initial_allocations.values()) != 100:
            raise ValueError("Initial allocations must sum to 100%.")
        
        self.assets = assets
        self.allocations = initial_allocations
        self.market_prices = {asset: random.uniform(50, 150) for asset in assets}  # Simulated initial market prices

    def adjust_allocations(self):
        """
        Adjust portfolio allocations based on simulated market price movements.
        
        :return: Updated allocations dictionary.
        """
        # Simulate market price movements
        self.market_prices = {
            asset: price * random.uniform(0.95, 1.05)  # Random daily price change of ±5%
            for asset, price in self.market_prices.items()
        }
        
        # Adjust allocations based on market prices
        total_value = sum(self.market_prices.values())
        self.allocations = {
            asset: (price / total_value) * 100
            for asset, price in self.market_prices.items()
        }
        return self.allocations

    def display_portfolio(self):
        """
        Prints the current portfolio allocations and market prices.
        """
        print("\nPortfolio Snapshot:")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'Asset':<10}{'Price':<10}{'Allocation (%)':<15}")
        print("-" * 35)
        for asset in self.assets:
            print(f"{asset:<10}{self.market_prices[asset]:<10.2f}{self.allocations[asset]:<15.2f}")

def simulate_portfolio():
    """
    Simulates portfolio creation and adjustment.
    """
    # Define portfolio assets and initial allocations
    assets = ["StockA", "StockB", "StockC", "BondA", "BondB"]
    initial_allocations = {
        "StockA": 20,
        "StockB": 25,
        "StockC": 15,
        "BondA": 25,
        "BondB": 15
    }
    
    # Create portfolio
    portfolio = Portfolio(assets, initial_allocations)
    
    # Simulate daily adjustments over a period of 5 days
    for day in range(1, 6):
        print(f"\nDay {day}")
        portfolio.adjust_allocations()
        portfolio.display_portfolio()

if __name__ == "__main__":
    try:
        simulate_portfolio()
    except Exception as e:
        print(f"An error occurred: {e}")
```
