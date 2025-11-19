"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwasterdex.com
Prompt: How can I utilize Aster's API to fetch real-time data for advanced trading strategies in Pro Mode?
Generated: DETERMINISTIC_fc8ac0e24419ab6c
Batch ID: 20250612_163133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aster.com/v1": {
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

class AsterAPIClient:
    """
    A client to interact with the Aster API for fetching real-time trading data.
    """

    BASE_URL = "https://api.aster.com/v1"  # Replace with actual Aster API base URL

    def __init__(self, api_key):
        """
        Initialize the Aster API client.

        :param api_key: Your API key for Aster
        """
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        """
        Make a GET request to the Aster API.

        :param endpoint: The API endpoint to call
        :param params: Query parameters for the request
        :return: JSON response from the API
        :raises Exception: For any issues in making the request
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, params=params)

        # Check for HTTP errors
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")

        return response.json()

    def fetch_real_time_data(self, symbol, interval):
        """
        Fetch real-time trading data for a given symbol and interval.

        :param symbol: The stock or asset symbol to fetch data for
        :param interval: The time interval for the data (e.g., '1m', '5m', '1h')
        :return: Real-time data as a JSON object
        """
        endpoint = f"real-time-data/{symbol}"
        params = {"interval": interval}
        return self._make_request(endpoint, params)

def main():
    """
    Main function to demonstrate fetching real-time trading data.
    """
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    client = AsterAPIClient(API_KEY)

    symbol = "AAPL"  # Example symbol
    interval = "1m"  # Example interval

    try:
        # Fetch real-time data in a loop
        while True:
            data = client.fetch_real_time_data(symbol, interval)
            print(json.dumps(data, indent=4))  # Pretty print the JSON response
            time.sleep(60)  # Wait for the next interval

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
