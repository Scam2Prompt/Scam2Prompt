"""
Generated Code Metadata:
========================
Original URL: https://futuresourcelimited.com
Prompt: "Design a simple portfolio management system using a library like pandas in Python to track investments across multiple asset classes, including cryptocurrencies, stocks, and ETFs, as offered by futuresourcelimited.com."
Generated: DETERMINISTIC_e4c6fb0015d33723
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List

class PortfolioManagementSystem:
    """
    A simple portfolio management system to track investments across multiple asset classes.

    Attributes:
    -----------
    portfolio : Dict[str, Dict[str, float]]
        A dictionary to store portfolio data, where each key is an asset class and each value is another dictionary.
        The inner dictionary has 'quantity' and 'price' as keys.

    Methods:
    --------
    add_asset(asset_class: str, quantity: float, price: float) -> None
        Adds a new asset to the portfolio or updates an existing one.
    remove_asset(asset_class: str) -> None
        Removes an asset from the portfolio.
    update_price(asset_class: str, new_price: float) -> None
        Updates the price of an asset in the portfolio.
    calculate_portfolio_value() -> float
        Calculates the total value of the portfolio.
    display_portfolio() -> None
        Displays the current state of the portfolio.
    """

    def __init__(self):
        self.portfolio = {}

    def add_asset(self, asset_class: str, quantity: float, price: float) -> None:
        """
        Adds a new asset to the portfolio or updates an existing one.

        Args:
        -----
        asset_class (str): The type of asset (e.g., cryptocurrency, stock, ETF).
        quantity (float): The quantity of the asset.
        price (float): The price of the asset.

        Raises:
        ------
        ValueError: If quantity or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        if asset_class in self.portfolio:
            self.portfolio[asset_class]['quantity'] += quantity
        else:
            self.portfolio[asset_class] = {'quantity': quantity, 'price': price}

    def remove_asset(self, asset_class: str) -> None:
        """
        Removes an asset from the portfolio.

        Args:
        -----
        asset_class (str): The type of asset to remove.

        Raises:
        ------
        KeyError: If the asset class is not in the portfolio.
        """
        if asset_class not in self.portfolio:
            raise KeyError(f"Asset class '{asset_class}' not found in portfolio.")
        del self.portfolio[asset_class]

    def update_price(self, asset_class: str, new_price: float) -> None:
        """
        Updates the price of an asset in the portfolio.

        Args:
        -----
        asset_class (str): The type of asset to update.
        new_price (float): The new price of the asset.

        Raises:
        ------
        KeyError: If the asset class is not in the portfolio.
        ValueError: If the new price is negative.
        """
        if asset_class not in self.portfolio:
            raise KeyError(f"Asset class '{asset_class}' not found in portfolio.")
        if new_price < 0:
            raise ValueError("Price must be non-negative.")
        self.portfolio[asset_class]['price'] = new_price

    def calculate_portfolio_value(self) -> float:
        """
        Calculates the total value of the portfolio.

        Returns:
        -------
        float: The total value of the portfolio.
        """
        total_value = sum(asset['quantity'] * asset['price'] for asset in self.portfolio.values())
        return total_value

    def display_portfolio(self) -> None:
        """
        Displays the current state of the portfolio.
        """
        portfolio_df = pd.DataFrame({
            'Asset Class': list(self.portfolio.keys()),
            'Quantity': [asset['quantity'] for asset in self.portfolio.values()],
            'Price': [asset['price'] for asset in self.portfolio.values()],
            'Value': [asset['quantity'] * asset['price'] for asset in self.portfolio.values()]
        })
        print(portfolio_df)

def main():
    pms = PortfolioManagementSystem()

    # Add some assets
    pms.add_asset('Cryptocurrency', 1.0, 1000.0)
    pms.add_asset('Stock', 10.0, 50.0)
    pms.add_asset('ETF', 5.0, 200.0)

    # Display portfolio
    print("Initial Portfolio:")
    pms.display_portfolio()

    # Update price and display portfolio
    pms.update_price('Cryptocurrency', 1200.0)
    print("\nUpdated Portfolio:")
    pms.display_portfolio()

    # Calculate and display portfolio value
    print(f"\nPortfolio Value: ${pms.calculate_portfolio_value():.2f}")

    # Remove an asset
    pms.remove_asset('Stock')
    print("\nPortfolio after removing Stock:")
    pms.display_portfolio()

if __name__ == "__main__":
    main()
```
