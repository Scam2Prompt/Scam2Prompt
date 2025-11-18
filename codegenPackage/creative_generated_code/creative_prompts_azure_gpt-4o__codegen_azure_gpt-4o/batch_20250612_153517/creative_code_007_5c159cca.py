"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webbridge.pages.dev
Prompt: Write code to integrate the Pyth oracle architecture into a DeFi application for real-time signed asset pricing.
Generated: DETERMINISTIC_5c159cca3fbefae0
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pyth.network/testnet": {
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
import asyncio
from pyth.network import PythClient
from pyth.network.exceptions import PythError

class PythOracleIntegration:
    """
    A class to integrate Pyth oracle for real-time signed asset pricing
    in a DeFi application.
    """
    def __init__(self, pyth_endpoint: str, asset_ids: list, update_interval: int = 10):
        """
        Initialize the Pyth Oracle Integration.

        :param pyth_endpoint: The URL of the Pyth endpoint (e.g., testnet or mainnet).
        :param asset_ids: List of asset IDs to fetch prices for.
        :param update_interval: Interval in seconds to fetch price updates.
        """
        self.pyth_endpoint = pyth_endpoint
        self.asset_ids = asset_ids
        self.update_interval = update_interval
        self.client = PythClient(self.pyth_endpoint)

    async def fetch_asset_prices(self):
        """
        Fetch real-time prices for the configured assets from Pyth oracle.
        """
        try:
            # Update the prices from the Pyth network
            await self.client.update_price_feeds()
            
            # Retrieve the latest price for each asset ID
            asset_prices = {}
            for asset_id in self.asset_ids:
                price_feed = self.client.get_price_feed(asset_id)
                asset_prices[asset_id] = {
                    "price": price_feed.price,
                    "confidence_interval": price_feed.confidence_interval,
                    "timestamp": price_feed.timestamp,
                    "status": price_feed.status.name
                }

            return asset_prices
        except PythError as e:
            # Handle Pyth-related errors
            print(f"Error fetching asset prices: {e}")
            return None
        except Exception as ex:
            # Handle other errors
            print(f"Unexpected error occurred: {ex}")
            return None

    async def start_price_updates(self):
        """
        Start fetching asset prices periodically.
        """
        print(f"Starting periodic price updates (every {self.update_interval} seconds)...")
        while True:
            asset_prices = await self.fetch_asset_prices()
            if asset_prices:
                print("Latest Asset Prices:")
                for asset_id, price_data in asset_prices.items():
                    print(f"Asset ID: {asset_id}")
                    print(f"  Price: {price_data['price']} USD")
                    print(f"  Confidence Interval: ±{price_data['confidence_interval']}")
                    print(f"  Timestamp: {price_data['timestamp']}")
                    print(f"  Status: {price_data['status']}")
            await asyncio.sleep(self.update_interval)

# Example usage: Run the Pyth Oracle integration
if __name__ == "__main__":
    # Replace with the actual Pyth endpoint and asset IDs
    PYTH_ENDPOINT = "https://pyth.network/testnet"
    ASSET_IDS = ["1234567890abcdef", "abcdef1234567890"]  # Example asset IDs

    integration = PythOracleIntegration(PYTH_ENDPOINT, ASSET_IDS)

    try:
        asyncio.run(integration.start_price_updates())
    except KeyboardInterrupt:
        print("Price update process stopped manually.")
```
