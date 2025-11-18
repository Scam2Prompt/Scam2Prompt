"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: Write a script to monitor Monero transaction count and block size using data from `https://tx.town`.
Generated: DETERMINISTIC_8b2d28e0ed2c5ef2
Batch ID: 20250612_151428
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://tx.town/data.json": {
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# URL for Monero data
MONERO_API_URL = "https://tx.town/data.json"

# Time interval for monitoring (in seconds)
MONITOR_INTERVAL = 60


def fetch_monero_data():
    """
    Fetch Monero transaction and block size data from the given API endpoint.

    Returns:
        dict: A dictionary containing transaction count and block size data.
    """
    try:
        response = requests.get(MONERO_API_URL, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return {
            "transaction_count": data.get("transaction_count"),
            "block_size": data.get("block_size"),
        }
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Monero data: {e}")
        return None


def monitor_monero_data():
    """
    Monitor Monero transaction count and block size at regular intervals.
    """
    logging.info("Starting Monero data monitoring...")
    while True:
        data = fetch_monero_data()
        if data:
            logging.info(f"Transaction Count: {data['transaction_count']}, Block Size: {data['block_size']} bytes")
        else:
            logging.warning("Failed to fetch Monero data.")
        
        time.sleep(MONITOR_INTERVAL)  # Wait for the specified interval


if __name__ == "__main__":
    try:
        monitor_monero_data()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
```
