"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rocketpool.club
Prompt: Explain how to develop an intelligent portfolio management system for crypto assets, referencing the strategies used by Rocket Pool.
Generated: DETERMINISTIC_7a69268d88bc480a
Batch ID: 20250612_161231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Intelligent Portfolio Management System for Crypto Assets

This script implements a portfolio management system for cryptocurrency assets that 
can dynamically rebalance based on market data and user-defined strategies. It references 
concepts like decentralized staking pools and portfolio optimization strategies similar 
to those used by Rocket Pool.

Note: This is a simplified example. In a production-ready environment, you would need 
to integrate secure APIs, authentication, and advanced market analysis tools.
"""

import json
import requests
from typing import List, Dict, Tuple

# Constants for external APIs and thresholds
COIN_GECKO_API = "https://api.coingecko.com/api/v3/simple/price"
SUPPORTED_ASSETS = ["bitcoin", "ethereum", "rocket-pool"]
REBALANCE_THRESHOLD_PERCENT = 5  # Threshold to trigger automatic rebalancing
MAX_RETRIES = 3

class PortfolioManager:
    """
    A class to manage and rebalance a crypto asset portfolio dynamically.
    """

    def __init__(self, initial_allocations: Dict[str, float]):
        """
        Initialize the portfolio manager with the user's asset allocations.

        Parameters:
        initial_allocations (Dict[str, float]): Mapping of assets to their allocation percentages.
        """
        self.asset_allocations = initial_allocations  # e.g., {"bitcoin": 50, "ethereum": 30, "rocket-pool": 20}
        self.asset_prices = {}  # Latest market prices for assets
    
    def fetch_asset_prices(self) -> Dict[str, float]:
        """
        Fetch the latest prices for supported assets using the CoinGecko API.

        Returns:
        Dict[str, float]: Mapping of assets to their current prices.
        """
        try:
            response = requests.get(
                COIN_GECKO_API,
                params={"ids": ",".join(SUPPORTED_ASSETS), "vs_currencies": "usd"}
            )
            response.raise_for_status()
            data = response.json()
            self.asset_prices = {asset: data[asset]["usd"] for asset in SUPPORTED_ASSETS}
            return self.asset_prices
        except requests.RequestException as e:
            print(f"Error fetching asset prices: {e}")
            return {}

    def calculate_portfolio_value(self, holdings: Dict[str, float]) -> float:
        """
        Calculate the total value of the portfolio based on current holdings and prices.

        Parameters:
        holdings (Dict[str, float]): Mapping of assets to their holdings in units.

        Returns:
        float: Total portfolio value in USD.
        """
        return sum(holdings[asset] * self.asset_prices.get(asset, 0) for asset in holdings)

    def rebalance_portfolio(self, holdings: Dict[str, float]) -> Dict[str, float]:
        """
        Perform portfolio rebalancing based on the target allocations.

        Parameters:
        holdings (Dict[str, float]): Current holdings of assets in units.

        Returns:
        Dict[str, float]: Updated holdings after rebalancing.
        """
        portfolio_value = self.calculate_portfolio_value(holdings)
        target_values = {asset: portfolio_value * (allocation / 100) for asset, allocation in self.asset_allocations.items()}
        updated_holdings = {asset: target_values[asset] / self.asset_prices[asset] for asset in holdings}
        return updated_holdings

    def check_rebalance_needed(self, holdings: Dict[str, float]) -> bool:
        """
        Check if portfolio rebalancing is needed based on deviation from target allocations.

        Parameters:
        holdings (Dict[str, float]): Current holdings of assets in units.

        Returns:
        bool: True if rebalancing is needed, False otherwise.
        """
        portfolio_value = self.calculate_portfolio_value(holdings)
        for asset, allocation in self.asset_allocations.items():
            current_value = holdings[asset] * self.asset_prices.get(asset, 0)
            target_value = portfolio_value * (allocation / 100)
            deviation_percent = abs((current_value - target_value) / target_value * 100)
            if deviation_percent > REBALANCE_THRESHOLD_PERCENT:
                return True
        return False

def main():
    """
    Main function to execute the portfolio management system.
    """
    # Initialize portfolio manager with example allocations
    initial_allocations = {"bitcoin": 50, "ethereum": 30, "rocket-pool": 20}
    portfolio_manager = PortfolioManager(initial_allocations)

    # Example current holdings (units of each asset)
    current_holdings = {"bitcoin": 0.5, "ethereum": 2, "rocket-pool": 4}

    # Fetch latest prices
    prices = portfolio_manager.fetch_asset_prices()
    if not prices:
        print("Failed to fetch asset prices. Please try again later.")
        return

    # Check if rebalancing is needed
    if portfolio_manager.check_rebalance_needed(current_holdings):
        print("Rebalancing portfolio...")
        updated_holdings = portfolio_manager.rebalance_portfolio(current_holdings)
        print(f"Updated Holdings: {json.dumps(updated_holdings, indent=2)}")
    else:
        print("Portfolio is already balanced.")

if __name__ == "__main__":
    main()
```
