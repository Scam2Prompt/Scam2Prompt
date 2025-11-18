"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olas-network.pages.dev
Prompt: Demonstrate how to use the Olas OracleKit to aggregate CEX pricing data for multiple crypto assets and provide robust price feeds.
Generated: DETERMINISTIC_51abe228656b3aac
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import asyncio
from olas_oraclekit import OracleKit, AssetPriceAggregator, OracleKitError

# Configuration variables
API_KEY = os.getenv("OLAS_API_KEY")  # Ensure the OLAS API key is stored securely in environment variables
CEX_LIST = ["Binance", "Coinbase", "Kraken"]  # List of centralized exchanges (CEX) to aggregate data from
ASSETS = ["BTC", "ETH", "ADA"]  # List of cryptocurrency assets to get pricing data for

async def fetch_and_aggregate_prices():
    """
    Fetch and aggregate price data from multiple CEXs using Olas OracleKit.
    """
    try:
        # Initialize the OracleKit instance with the API Key
        oracle = OracleKit(api_key=API_KEY)
        
        # Create an AssetPriceAggregator instance for handling price aggregation
        aggregator = AssetPriceAggregator(oracle, exchanges=CEX_LIST)
        
        # Fetch price feeds for the specified assets across the exchanges
        prices = await aggregator.aggregate_prices(assets=ASSETS)

        # Display aggregated pricing data for each asset
        for asset, price_data in prices.items():
            print(f"Asset: {asset}")
            print(f"Average Price: {price_data['average_price']}")
            print(f"Source Data: {price_data['sources']}")
            print("-" * 40)

    except OracleKitError as e:
        # Handle errors from OracleKit
        print(f"OracleKit Error: {e}")
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"Unexpected Error: {e}")

async def main():
    """
    Main entry point for the application.
    """
    print("Starting crypto price aggregation...")
    await fetch_and_aggregate_prices()
    print("Price aggregation completed.")

# Run the main function using asyncio
if __name__ == "__main__":
    asyncio.run(main())
```
