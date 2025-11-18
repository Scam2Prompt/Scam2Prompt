"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.cjjzqkc.cn
Prompt: Develop a program to monitor and alert for price changes of NFTs listed on the OKX marketplace using the API.
Generated: DETERMINISTIC_cfdbbee60451c4a1
Batch ID: 20250612_154757
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com/api/v5/market/nft-ticker": {
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
import time
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
API_URL = "https://www.okx.com/api/v5/market/nft-ticker"
NFT_COLLECTION_ID = "your_collection_id_here"  # Specify the NFT collection ID to monitor
PRICE_THRESHOLD_PERCENT = 5  # Alert if price changes exceed this percentage
CHECK_INTERVAL_SECONDS = 60  # Time interval to check for updates in seconds

# Function to fetch NFT price data from OKX API
def fetch_nft_data(collection_id):
    """
    Fetch the latest NFT data for the given collection ID from OKX Marketplace API.

    Args:
        collection_id (str): The ID of the NFT collection to monitor.

    Returns:
        dict: The NFT data returned from the API, or None if the request fails.
    """
    try:
        response = requests.get(API_URL, params={"collectionId": collection_id})
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.RequestException as e:
        logging.error(f"Failed to fetch NFT data: {e}")
        return None

# Function to monitor price changes
def monitor_price_changes():
    """
    Monitor for significant price changes in the specified NFT collection.
    Alerts if the price change exceeds the defined threshold percentage.
    """
    last_prices = {}  # Stores the last known price of each NFT

    while True:
        logging.info("Fetching latest NFT data...")
        nft_data = fetch_nft_data(NFT_COLLECTION_ID)

        if not nft_data or "data" not in nft_data:
            logging.error("Invalid or empty response from API.")
            time.sleep(CHECK_INTERVAL_SECONDS)
            continue

        for nft in nft_data["data"]:
            nft_id = nft.get("id")
            current_price = float(nft.get("price", 0))

            if nft_id is None or current_price == 0:
                logging.warning(f"Invalid NFT data: {nft}")
                continue

            # Compare with the last known price
            if nft_id in last_prices:
                last_price = last_prices[nft_id]
                price_change = ((current_price - last_price) / last_price) * 100

                if abs(price_change) >= PRICE_THRESHOLD_PERCENT:
                    logging.info(
                        f"Price change alert for NFT {nft_id}: "
                        f"Price changed by {price_change:.2f}% "
                        f"(Old Price: {last_price}, New Price: {current_price})"
                    )

            # Update the last known price
            last_prices[nft_id] = current_price

        # Wait for the defined interval before checking again
        time.sleep(CHECK_INTERVAL_SECONDS)

# Main entry point of the program
if __name__ == "__main__":
    logging.info("Starting NFT price monitoring...")
    try:
        monitor_price_changes()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
```

**Note:** Replace `your_collection_id_here` with the actual NFT collection ID you want to monitor. This script assumes that the OKX API (NFT ticker endpoint) is available and supports the provided arguments (`collectionId`). Ensure proper API access credentials or headers if required.
