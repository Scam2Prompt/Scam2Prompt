"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuel-explorer.vercel.app
Prompt: Provide an example of using the Fuel Labs API to monitor and log changes in the Fuel blockchain's ecosystem.
Generated: DETERMINISTIC_c48ab4b3e7320b2e
Batch ID: 20250612_150816
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fuel-labs-api.example.com": {
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FuelBlockchainMonitor:
    """
    A class to monitor and log changes in the Fuel blockchain's ecosystem using the Fuel Labs API.
    """

    BASE_URL = "https://fuel-labs-api.example.com"  # Replace with the actual Fuel Labs API URL
    POLLING_INTERVAL = 30  # Time in seconds between API requests
    
    def __init__(self):
        """
        Initializes the monitor instance.
        """
        self.last_block_number = None

    def fetch_latest_block(self):
        """
        Fetches the latest block details from the Fuel Labs API.

        Returns:
            dict: The latest block data from the API.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/latest_block")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching latest block: {e}")
            return None

    def log_block_change(self, block):
        """
        Logs the details of the latest block if it has changed.

        Args:
            block (dict): The block data to log.
        """
        if self.last_block_number is None or block['number'] != self.last_block_number:
            logging.info(f"New block detected: {block['number']}")
            logging.info(f"Block details: {block}")
            self.last_block_number = block['number']

    def monitor(self):
        """
        Starts monitoring the Fuel blockchain for changes.
        """
        logging.info("Starting Fuel blockchain monitoring...")
        while True:
            block = self.fetch_latest_block()
            if block:
                self.log_block_change(block)
            time.sleep(self.POLLING_INTERVAL)

if __name__ == "__main__":
    monitor = FuelBlockchainMonitor()
    try:
        monitor.monitor()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
