"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unionstandard-trust.com
Prompt: Write a Python script to manage client asset portfolios using the principles of long-term asset management as practiced by Union Standard Trust.
Generated: DETERMINISTIC_b5f7020bdf04852c
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Optional

# Configure logging to capture events throughout the script execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Asset:
    """Class representing a financial asset."""
    
    def __init__(self, name: str, value: float, risk_level: str):
        """Initialize an asset with a name, value, and risk level.
        
        Args:
            name (str): The name of the asset.
            value (float): The monetary value of the asset.
            risk_level (str): The risk level of the asset (e.g., 'low', 'medium', 'high').
        """
        self.name = name
        self.value = value
        self.risk_level = risk_level

    def __repr__(self):
        return f"Asset(name={self.name}, value={self.value}, risk_level={self.risk_level})"


class Portfolio:
    """Class representing a client's investment portfolio."""
    
    def __init__(self, client_name: str):
        """Initialize a portfolio for the given client name.
        
        Args:
            client_name (str): The name of the client.
        """
        self.client_name = client_name
        self.assets: List[Asset] = []
    
    def add_asset(self, asset: Asset) -> None:
        """Add an asset to the portfolio.
        
        Args:
            asset (Asset): The asset to add to the portfolio.
        """
        self.assets.append(asset)
        logging.info(f"Added asset: {asset} to {self.client_name}'s portfolio.")

    def remove_asset(self, asset_name: str) -> None:
        """Remove an asset from the portfolio by its name.
        
        Args:
            asset_name (str): The name of the asset to remove.
        """
        for asset in self.assets:
            if asset.name == asset_name:
                self.assets.remove(asset)
                logging.info(f"Removed asset: {asset} from {self.client_name}'s portfolio.")
                return
        logging.warning(f"Asset named {asset_name} not found in {self.client_name}'s portfolio.")

    def get_total_value(self) -> float:
        """Calculate the total value of the portfolio.
        
        Returns:
            float: The total monetary value of the assets in the portfolio.
        """
        total_value = sum(asset.value for asset in self.assets)
        logging.info(f"Total value for {self.client_name}'s portfolio: ${total_value:.2f}")
        return total_value

    def get_risk_profile(self) -> Dict[str, int]:
        """Generate a risk profile of the portfolio.
        
        Returns:
            Dict[str, int]: A dictionary with counts of each risk level.
        """
        risk_profile = {'low': 0, 'medium': 0, 'high': 0}
        for asset in self.assets:
            risk_profile[asset.risk_level] += 1
        logging.info(f"Risk profile for {self.client_name}: {risk_profile}")
        return risk_profile

    def __repr__(self):
        return f"Portfolio(client_name={self.client_name}, assets={self.assets})"


if __name__ == "__main__":
    try:
        # Example usage of the Portfolio and Asset classes
        portfolio = Portfolio("John Doe")

        # Adding assets to the portfolio
        portfolio.add_asset(Asset("Stock A", 15000, "medium"))
        portfolio.add_asset(Asset("Bond B", 5000, "low"))
        portfolio.add_asset(Asset("Stock C", 20000, "high"))

        # Display total value and risk profile
        total_value = portfolio.get_total_value()
        risk_profile = portfolio.get_risk_profile()

        # Removing an asset
        portfolio.remove_asset("Bond B")

        # Final portfolio state
        logging.info(f"Final portfolio state: {portfolio}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
