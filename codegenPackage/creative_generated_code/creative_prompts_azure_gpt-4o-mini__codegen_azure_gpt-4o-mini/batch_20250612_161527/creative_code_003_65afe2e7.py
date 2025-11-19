"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-pool-orca-news-4816.pouch.guru
Prompt: Provide an example of using the Orca API for monitoring price changes in DeFi pools.
Generated: DETERMINISTIC_65afe2e7fabe6617
Batch ID: 20250612_161527
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.orca.so": {
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
import json

class OrcaAPI:
    """
    A class to interact with the Orca API for monitoring price changes in DeFi pools.
    """

    BASE_URL = "https://api.orca.so"  # Base URL for the Orca API
    POLLING_INTERVAL = 10  # Time in seconds between price checks

    def __init__(self, pool_id):
        """
        Initializes the OrcaAPI with a specific pool ID.

        :param pool_id: Unique identifier for the DeFi pool to monitor.
        """
        self.pool_id = pool_id
        self.previous_price = None

    def fetch_pool_data(self):
        """
        Fetches the current data for the specified pool.

        :return: JSON response containing pool data.
        :raises Exception: If the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}/pool/{self.pool_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching pool data: {e}")

    def monitor_price_changes(self):
        """
        Monitors price changes in the specified DeFi pool. 
        Logs changes when they occur.
        """
        print(f"Monitoring price changes for pool: {self.pool_id}")
        while True:
            try:
                pool_data = self.fetch_pool_data()
                current_price = pool_data['price']  # Adjust according to actual JSON structure

                if self.previous_price is None:
                    self.previous_price = current_price
                elif current_price != self.previous_price:
                    print(f"Price change detected! Previous: {self.previous_price}, Current: {current_price}")
                    self.previous_price = current_price

                time.sleep(self.POLLING_INTERVAL)

            except Exception as e:
                print(e)  # Log the error but continue monitoring

if __name__ == "__main__":
    # Example usage
    try:
        pool_id = "example_pool_id"  # Replace with the actual pool ID
        orca_api = OrcaAPI(pool_id)
        orca_api.monitor_price_changes()
    except Exception as e:
        print(f"Failed to start monitoring: {e}")
```
