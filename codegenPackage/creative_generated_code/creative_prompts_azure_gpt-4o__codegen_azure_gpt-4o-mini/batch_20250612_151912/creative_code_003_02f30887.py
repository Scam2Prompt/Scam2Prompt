"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptobalancer.co.uk
Prompt: Generate code to implement a feature that logs updates and fixes in a cryptocurrency portfolio management tool like CryptoBalancer.
Generated: DETERMINISTIC_02f308879374968d
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='portfolio_updates.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PortfolioManager:
    """
    A class to manage a cryptocurrency portfolio and log updates and fixes.
    """

    def __init__(self):
        """Initialize the portfolio manager with an empty portfolio."""
        self.portfolio = {}

    def add_asset(self, asset: str, amount: float):
        """
        Add a new asset to the portfolio.
        
        Parameters:
        asset (str): The name of the cryptocurrency asset.
        amount (float): The amount of the asset being added.
        """
        if amount < 0:
            logging.error(f"Attempted to add a negative amount of {asset}: {amount}")
            raise ValueError("Amount must be a positive number.")
        
        if asset in self.portfolio:
            self.portfolio[asset] += amount
            logging.info(f"Updated {asset}: Added {amount}. Total now: {self.portfolio[asset]}")
        else:
            self.portfolio[asset] = amount
            logging.info(f"Added new asset {asset}: {amount}")

    def remove_asset(self, asset: str, amount: float):
        """
        Remove an asset from the portfolio.
        
        Parameters:
        asset (str): The name of the cryptocurrency asset.
        amount (float): The amount of the asset being removed.
        """
        if asset not in self.portfolio:
            logging.error(f"Attempted to remove non-existent asset: {asset}")
            raise KeyError(f"Asset {asset} not found in portfolio.")

        if amount < 0:
            logging.error(f"Attempted to remove a negative amount of {asset}: {amount}")
            raise ValueError("Amount must be a positive number.")
        
        if amount > self.portfolio[asset]:
            logging.error(f"Attempted to remove more than available for {asset}: {amount}")
            raise ValueError("Cannot remove more than available in the portfolio.")
        
        self.portfolio[asset] -= amount
        logging.info(f"Removed {amount} of {asset}. Total remaining: {self.portfolio[asset]}")
        
        if self.portfolio[asset] == 0:
            del self.portfolio[asset]
            logging.info(f"Removed {asset} completely from portfolio.")

    def get_portfolio(self):
        """
        Retrieve the current portfolio.
        
        Returns:
        dict: A dictionary representing the portfolio with asset amounts.
        """
        return self.portfolio

# Example usage
if __name__ == "__main__":
    manager = PortfolioManager()
    try:
        manager.add_asset("Bitcoin", 1.5)
        manager.add_asset("Ethereum", 3)
        manager.remove_asset("Bitcoin", 0.5)
        print(manager.get_portfolio())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
