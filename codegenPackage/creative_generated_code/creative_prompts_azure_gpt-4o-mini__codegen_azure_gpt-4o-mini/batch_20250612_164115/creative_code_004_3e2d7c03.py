"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bi-verse.org
Prompt: Illustrate how to implement a wealth management strategy using a library that supports various asset classes, referencing bi-verse.org's approach to personalized financial planning.
Generated: DETERMINISTIC_3e2d7c0347aecd9f
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import logging

# Configure logging to capture errors and important information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Asset:
    """Class representing a financial asset."""
    
    def __init__(self, name, asset_class, expected_return, risk):
        """
        Initialize an Asset.

        :param name: Name of the asset.
        :param asset_class: Class of the asset (e.g., 'Equity', 'Bond', 'Real Estate').
        :param expected_return: Expected return of the asset as a percentage (e.g., 0.05 for 5%).
        :param risk: Risk level of the asset as a standard deviation (e.g., 0.1 for 10%).
        """
        self.name = name
        self.asset_class = asset_class
        self.expected_return = expected_return
        self.risk = risk

class Portfolio:
    """Class representing a collection of assets."""
    
    def __init__(self):
        """Initialize an empty portfolio."""
        self.assets = []

    def add_asset(self, asset):
        """
        Add an asset to the portfolio.

        :param asset: An Asset instance to add.
        """
        if not isinstance(asset, Asset):
            logging.error("Attempted to add a non-Asset object.")
            raise ValueError("Only Asset instances can be added.")
        self.assets.append(asset)
        logging.info(f"Asset '{asset.name}' added to portfolio.")

    def calculate_expected_return(self):
        """
        Calculate the expected return of the portfolio.

        :return: Expected return as a percentage.
        """
        try:
            total_return = sum(asset.expected_return for asset in self.assets)
            expected_return = total_return / len(self.assets) if self.assets else 0
            logging.info(f"Calculated expected return: {expected_return}")
            return expected_return
        except Exception as e:
            logging.error(f"Error calculating expected return: {e}")
            return 0

    def calculate_risk(self):
        """
        Calculate the risk (standard deviation) of the portfolio.

        :return: Combined risk as a standard deviation.
        """
        try:
            total_risk = np.std([asset.risk for asset in self.assets])
            logging.info(f"Calculated portfolio risk: {total_risk}")
            return total_risk
        except Exception as e:
            logging.error(f"Error calculating risk: {e}")
            return 0

def main():
    """Main function to demonstrate the portfolio management strategy."""
    portfolio = Portfolio()
    
    # Sample asset data
    assets_data = [
        Asset("Stock A", "Equity", 0.07, 0.15),
        Asset("Bond A", "Bond", 0.03, 0.05),
        Asset("Real Estate A", "Real Estate", 0.05, 0.10)
    ]

    # Adding assets to the portfolio
    for asset in assets_data:
        portfolio.add_asset(asset)

    # Calculating expected return and risk
    expected_return = portfolio.calculate_expected_return()
    risk = portfolio.calculate_risk()

    logging.info(f"Portfolio expected return: {expected_return * 100:.2f}%")
    logging.info(f"Portfolio risk: {risk:.2f}")

if __name__ == "__main__":
    main()
```
