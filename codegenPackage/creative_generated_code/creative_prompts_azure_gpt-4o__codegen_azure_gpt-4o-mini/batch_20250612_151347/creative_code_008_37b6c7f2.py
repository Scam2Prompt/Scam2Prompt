"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkscan-sepolia.netlify.app
Prompt: Develop a Python script using the Starkscan API to track and log the status of transactions with a specific hash.
Generated: DETERMINISTIC_37b6c7f298e11ae1
Batch ID: 20250612_151347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://starkscan.co/api": {
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

# Set up logging configuration
logging.basicConfig(
    filename='transaction_status.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class StarkscanAPI:
    BASE_URL = "https://starkscan.co/api"

    def __init__(self):
        """Initialize the Starkscan API client."""
        pass

    def get_transaction_status(self, tx_hash):
        """
        Retrieve the status of a transaction by its hash.

        Args:
            tx_hash (str): The hash of the transaction to check.

        Returns:
            dict: A dictionary containing the transaction status data.

        Raises:
            Exception: If the request to the API fails or the transaction is not found.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/v1/transactions/{tx_hash}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Failed to fetch transaction status: {e}")
            raise Exception("Error fetching transaction status. Please check the transaction hash or try again later.") from e


def track_transaction(tx_hash, interval=30):
    """
    Track the status of a transaction at regular intervals.

    Args:
        tx_hash (str): The hash of the transaction to track.
        interval (int): The time (in seconds) to wait between status checks.
    """
    api = StarkscanAPI()

    while True:
        try:
            status = api.get_transaction_status(tx_hash)
            logging.info(f"Transaction Status for {tx_hash}: {status}")

            # Check for a specific condition to break out of the loop (optional)
            if status['status'] == 'completed':  # Example condition
                logging.info(f"Transaction {tx_hash} completed.")
                break

        except Exception as e:
            logging.error(e)

        time.sleep(interval)  # Wait before checking again


if __name__ == "__main__":
    # Example transaction hash (replace with an actual hash)
    transaction_hash = "0x123456789abcdef" 
    polling_interval = 30  # Check every 30 seconds

    try:
        track_transaction(transaction_hash, polling_interval)
    except KeyboardInterrupt:
        logging.info("Transaction tracking stopped by user.")
```
