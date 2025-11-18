"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aserdex.com
Prompt: Develop a script to monitor and manage a portfolio on Aster DEX, including tracking TVL (Total Value Locked) and asset performance across chains.
Generated: DETERMINISTIC_6a9bb7ff83537672
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.asterdex.com": {
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
import requests
import json
import time
from datetime import datetime

class AsterDexPortfolioManager:
    """
    AsterDexPortfolioManager is a class to monitor and manage a portfolio on Aster DEX.
    It tracks TVL (Total Value Locked) and asset performance across chains.
    """

    def __init__(self, api_base_url, chains, portfolio_assets):
        """
        Initialize the portfolio manager with API base URL, chains, and portfolio assets.

        :param api_base_url: Base URL for Aster DEX API
        :param chains: A list of blockchain names to track
        :param portfolio_assets: A dictionary with assets and their allocation
        """
        self.api_base_url = api_base_url
        self.chains = chains
        self.portfolio_assets = portfolio_assets

    def fetch_tvl(self, chain):
        """
        Fetch the Total Value Locked (TVL) for a specific chain.

        :param chain: Blockchain name
        :return: TVL value for the chain or None if an error occurs
        """
        try:
            url = f"{self.api_base_url}/tvl/{chain}"
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            data = response.json()
            return data.get('tvl', None)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to fetch TVL for chain '{chain}': {e}")
            return None

    def fetch_asset_performance(self, asset):
        """
        Fetch the performance (current price, change) of a specific asset.

        :param asset: Asset symbol (e.g., BTC, ETH)
        :return: A dictionary with performance data or None if an error occurs
        """
        try:
            url = f"{self.api_base_url}/assets/{asset}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to fetch performance data for asset '{asset}': {e}")
            return None

    def monitor_tvl(self):
        """
        Monitor the TVL across the specified chains.

        :return: A dictionary with chain names and their TVL values
        """
        tvl_data = {}
        for chain in self.chains:
            tvl = self.fetch_tvl(chain)
            if tvl is not None:
                tvl_data[chain] = tvl
        return tvl_data

    def monitor_asset_performance(self):
        """
        Monitor the performance of assets in the portfolio.

        :return: A dictionary with asset symbols and their performance data
        """
        performance_data = {}
        for asset in self.portfolio_assets:
            data = self.fetch_asset_performance(asset)
            if data is not None:
                performance_data[asset] = data
        return performance_data

    def display_portfolio_summary(self, tvl_data, performance_data):
        """
        Display the portfolio summary including TVL and asset performance.

        :param tvl_data: TVL data across chains
        :param performance_data: Performance data for portfolio assets
        """
        print("\nPortfolio Summary")
        print("====================================")
        
        print("\nTotal Value Locked (TVL) by Chain:")
        for chain, tvl in tvl_data.items():
            print(f"- {chain}: ${tvl:,.2f}")
        
        print("\nAsset Performance:")
        for asset, data in performance_data.items():
            price = data.get('price', 'N/A')
            change_24h = data.get('change_24h', 'N/A')
            print(f"- {asset}: Price = ${price:,.2f}, 24h Change = {change_24h}%")

    def run_monitoring(self, interval=60):
        """
        Run the portfolio monitoring loop.

        :param interval: Interval (in seconds) between monitoring updates
        """
        while True:
            print(f"\nMonitoring Update: {datetime.now()}")
            tvl_data = self.monitor_tvl()
            performance_data = self.monitor_asset_performance()
            self.display_portfolio_summary(tvl_data, performance_data)
            print(f"\nNext update in {interval} seconds...\n")
            time.sleep(interval)


if __name__ == "__main__":
    # Configuration
    API_BASE_URL = "https://api.asterdex.com"
    CHAINS = ["ethereum", "polygon", "binance-smart-chain"]
    PORTFOLIO_ASSETS = {"BTC": 0.5, "ETH": 1.0, "ADA": 10.0}

    # Initialize the portfolio manager
    manager = AsterDexPortfolioManager(API_BASE_URL, CHAINS, PORTFOLIO_ASSETS)

    # Start monitoring (update every 60 seconds)
    manager.run_monitoring(interval=60)
```
