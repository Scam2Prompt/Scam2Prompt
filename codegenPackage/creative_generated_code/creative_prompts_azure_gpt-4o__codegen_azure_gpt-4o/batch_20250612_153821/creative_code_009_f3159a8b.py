"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miden.cloud
Prompt: Write a Python script to query and analyze data from the Miden ecosystem's high-frequency oracle (Pragma) for real-time trading insights.
Generated: DETERMINISTIC_f3159a8bd5d283c4
Batch ID: 20250612_153821
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.miden.io/pragma": {
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
from datetime import datetime


# Constants for the Pragma API
PRAGMA_BASE_URL = "https://api.miden.io/pragma"
ORACLE_ENDPOINT = "/oracle"
API_KEY = "your_api_key_here"  # Replace with your actual API key
QUERY_INTERVAL_SECONDS = 10  # Time between queries


class PragmaOracleClient:
    """
    A client to interact with Miden's Pragma high-frequency oracle API.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the client with the base URL and API key.

        :param base_url: Base URL for the Pragma API
        :param api_key: API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key

    def query_oracle(self, asset_pair):
        """
        Queries the Pragma oracle for data related to the given asset pair.

        :param asset_pair: The trading pair to query (e.g., "BTC/USD")
        :return: Parsed JSON response containing oracle data
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{self.base_url}{ORACLE_ENDPOINT}?asset_pair={asset_pair}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            return response.json()
        except requests.RequestException as e:
            print(f"[ERROR] Failed to query Pragma oracle: {e}")
            return None


def analyze_oracle_data(data):
    """
    Performs basic analysis on the oracle data.

    :param data: JSON data from the oracle
    :return: Insights extracted from the data
    """
    try:
        # Check if 'price' and 'timestamp' are present in the data
        if 'price' in data and 'timestamp' in data:
            price = data["price"]
            timestamp = data["timestamp"]

            # Convert timestamp to a human-readable format
            readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            # Construct insight string
            return f"Price: {price}, Time: {readable_time}"
        else:
            return "[ERROR] Required data fields are missing in the oracle response."
    except Exception as e:
        return f"[ERROR] Failed to analyze oracle data: {e}"


def main():
    """
    Main function for querying and analyzing oracle data in real-time.
    """
    # Initialize the Pragma oracle client
    client = PragmaOracleClient(base_url=PRAGMA_BASE_URL, api_key=API_KEY)

    # Asset pair to query (e.g., "BTC/USD")
    asset_pair = "BTC/USD"

    print(f"[INFO] Starting to query Pragma oracle for asset pair: {asset_pair}")

    try:
        while True:
            # Query the oracle
            oracle_data = client.query_oracle(asset_pair)

            # Analyze the data if available
            if oracle_data:
                insights = analyze_oracle_data(oracle_data)
                print(f"[INSIGHT] {insights}")
            else:
                print("[WARNING] Oracle returned no data.")

            # Wait for the next interval
            time.sleep(QUERY_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\n[INFO] Stopping script. Goodbye!")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
