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

class Asset:
    """Represents a financial asset in the portfolio with its name and current price."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def update_price(self, price_change: float):
        """Update the asset price based on the price change percentage."""
        self.price += self.price * price_change
        self.price = max(self.price, 0)  # Ensure price does not go negative


class Portfolio:
    """Represents a diversified investment portfolio."""
    def __init__(self):
        self.assets = {}
    
    def add_asset(self, asset: Asset, quantity: int):
        """Adds an asset to the portfolio with a specified quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.assets[asset.name] = {'asset': asset, 'quantity': quantity}

    def remove_asset(self, asset_name: str):
        """Removes an asset from the portfolio."""
        if asset_name in self.assets:
            del self.assets[asset_name]
        else:
            raise ValueError("Asset not found in portfolio")

    def adjust_assets(self):
        """Adjust assets based on random market price movements."""
        for name, data in self.assets.items():
            price_change = random.uniform(-0.1, 0.1)  # Simulate price change between -10% and +10%
            data['asset'].update_price(price_change)

    def get_portfolio_value(self) -> float:
        """Calculates the total value of the portfolio."""
        total_value = 0.0
        for data in self.assets.values():
            total_value += data['asset'].price * data['quantity']
        return total_value

    def __str__(self):
        """Returns a string representation of the portfolio."""
        portfolio_str = "Portfolio:\n"
        for name, data in self.assets.items():
            portfolio_str += f"{data['quantity']} x {name} at ${data['asset'].price:.2f}\n"
        portfolio_str += f"Total Portfolio Value: ${self.get_portfolio_value():.2f}"
        return portfolio_str


def main():
    """Main function to simulate portfolio creation and adjustment."""
    try:
        portfolio = Portfolio()
        
        # Adding assets to the portfolio
        portfolio.add_asset(Asset("Stock A", 100.0), 10)
        portfolio.add_asset(Asset("Bond B", 200.0), 5)
        portfolio.add_asset(Asset("Crypto C", 50.0), 20)

        print(portfolio)

        # Simulate market changes
        for _ in range(5):  # Simulate 5 market adjustments
            print("\nAdjusting asset prices...")
            portfolio.adjust_assets()
            print(portfolio)
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
