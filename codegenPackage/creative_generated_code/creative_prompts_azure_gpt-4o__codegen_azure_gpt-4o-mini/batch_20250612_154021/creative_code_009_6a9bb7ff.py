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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AsterDexPortfolioManager:
    """Class to monitor and manage a portfolio on Aster DEX."""

    def __init__(self, api_url, wallet_address):
        """
        Initialize the portfolio manager.

        Parameters:
            api_url (str): The API URL for Aster DEX.
            wallet_address (str): The wallet address for tracking assets.
        """
        self.api_url = api_url
        self.wallet_address = wallet_address
        self.portfolio = {}
    
    def fetch_tvl(self):
        """Fetch the Total Value Locked (TVL) from Aster DEX."""
        try:
            response = requests.get(f"{self.api_url}/tvl")
            response.raise_for_status()
            tvl_data = response.json()
            logging.info("Successfully fetched TVL data.")
            return tvl_data['tvl']
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")

    def fetch_asset_performance(self):
        """Fetch the asset performance across chains."""
        try:
            response = requests.get(f"{self.api_url}/portfolio/{self.wallet_address}")
            response.raise_for_status()
            portfolio_data = response.json()
            logging.info("Successfully fetched asset performance data.")
            self.portfolio = portfolio_data['assets']
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")

    def display_portfolio(self):
        """Display the current portfolio status."""
        logging.info("Current Portfolio:")
        for asset in self.portfolio:
            logging.info(f"Asset: {asset['name']}, Amount: {asset['amount']}, Value: {asset['value']}")
    
    def monitor_portfolio(self, interval=60):
        """Continuously monitor the portfolio at specified intervals.

        Parameters:
            interval (int): Time in seconds between checks.
        """
        while True:
            logging.info("Monitoring portfolio...")
            tvl = self.fetch_tvl()
            if tvl is not None:
                logging.info(f"Current TVL: {tvl}")
            self.fetch_asset_performance()
            self.display_portfolio()
            time.sleep(interval)

if __name__ == "__main__":
    # Replace with actual API URL and wallet address
    API_URL = "https://api.asterdex.com"
    WALLET_ADDRESS = "your_wallet_address_here"
    
    portfolio_manager = AsterDexPortfolioManager(API_URL, WALLET_ADDRESS)
    portfolio_manager.monitor_portfolio(interval=300)  # Monitor every 5 minutes
```
