"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythget.com
Prompt: Generate Python code that uses Pythget to monitor asset price changes and triggers an alert if the price exceeds a specified threshold.
Generated: DETERMINISTIC_04b6b5b0130ea5d4
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from pythclient.rpc import PythClient
from pythclient.exceptions import PythError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
ASSET_SYMBOL = "Crypto.BTC/USD"  # Replace with the asset symbol you want to monitor
PRICE_THRESHOLD = 60000.0       # Trigger alert if price exceeds this value
INTERVAL_SECONDS = 10           # Interval to check asset price (in seconds)

# Function to initialize PythClient and connect to the RPC server
def initialize_pyth_client():
    try:
        client = PythClient()
        client.connect_to_cluster("devnet")  # Use appropriate cluster (e.g., 'mainnet' for production)
        return client
    except PythError as e:
        logging.error(f"Failed to initialize PythClient: {e}")
        raise

# Function to monitor asset price
def monitor_asset_price(client):
    try:
        while True:
            # Get all asset prices from Pyth
            client.update_price_data()
            assets = client.get_assets()

            # Find the asset price by symbol
            for asset in assets:
                if asset.symbol == ASSET_SYMBOL:
                    price = asset.price
                    confidence_interval = asset.confidence_interval

                    # Log asset price and confidence interval
                    logging.info(f"Asset: {asset.symbol}, Price: {price}, Confidence Interval: {confidence_interval}")

                    # Trigger alert if price exceeds threshold
                    if price > PRICE_THRESHOLD:
                        logging.warning(f"ALERT: {asset.symbol} price has exceeded the threshold! Current price: {price}")
                    break
            else:
                logging.warning(f"Asset {ASSET_SYMBOL} not found.")
            
            # Wait for the specified interval before checking again
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except PythError as e:
        logging.error(f"Error while monitoring asset price: {e}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")

# Main function
def main():
    try:
        logging.info("Initializing PythClient...")
        client = initialize_pyth_client()
        logging.info("PythClient initialized successfully. Starting asset price monitoring...")
        monitor_asset_price(client)
    except Exception as e:
        logging.exception("Failed to start asset price monitoring.")

# Entry point
if __name__ == "__main__":
    main()
```
