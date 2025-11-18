"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasclub.xyz
Prompt: Provide code examples for querying historical data on cryptocurrency liquidations using Binance Smart Chain APIs, inspired by the market crash mentioned.
Generated: DETERMINISTIC_d5e83e967c5dc0ef
Batch ID: 20250612_153314
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bscscan.com/api": {
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
from datetime import datetime, timedelta

# Constants
BINANCE_API_URL = "https://api.bscscan.com/api"
API_KEY = "your_bscscan_api_key"  # Add your API key here
ADDRESS = "0xBinanceLiquidationContractAddress"  # Replace with the actual contract address
START_DATE = "2023-10-01"  # Replace with your starting date (YYYY-MM-DD)
END_DATE = "2023-10-10"  # Replace with your ending date (YYYY-MM-DD)

# Helper function to convert human-readable date to UNIX timestamp
def date_to_timestamp(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return int(date_obj.timestamp())
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

# Function to fetch historical liquidation data
def fetch_liquidation_data(contract_address, start_date, end_date):
    """
    Fetch historical liquidation data from Binance Smart Chain using BSCScan APIs.

    Args:
        contract_address (str): Contract address of the liquidation data source.
        start_date (str): Start date in format YYYY-MM-DD.
        end_date (str): End date in format YYYY-MM-DD.

    Returns:
        list: A list of liquidation events.

    Raises:
        Exception: Raises an exception if the API call fails or returns an error.
    """
    try:
        # Convert start and end dates to UNIX timestamps
        start_timestamp = date_to_timestamp(start_date)
        end_timestamp = date_to_timestamp(end_date)

        # Prepare API request parameters
        params = {
            "module": "account",
            "action": "txlist",
            "address": contract_address,
            "startblock": 0,
            "endblock": 99999999,
            "page": 1,
            "offset": 10000,  # Maximum allowed by BSCScan
            "sort": "asc",
            "apikey": API_KEY,
        }

        # Make the API request
        response = requests.get(BINANCE_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Error handling for API response
        if data.get("status") != "1":
            raise Exception(f"API Error: {data.get('message')}")

        # Filter liquidation events based on timestamp range
        events = []
        for tx in data.get("result", []):
            tx_timestamp = int(tx["timeStamp"])
            if start_timestamp <= tx_timestamp <= end_timestamp:
                events.append(tx)

        return events

    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error: {e}")
    except Exception as e:
        raise Exception(f"Error: {e}")

# Main driver code
if __name__ == "__main__":
    try:
        # Fetch historical liquidations within the specified date range
        liquidations = fetch_liquidation_data(ADDRESS, START_DATE, END_DATE)

        if liquidations:
            print(f"Found {len(liquidations)} liquidation events:")
            for liquidation in liquidations:
                print(f"TxHash: {liquidation['hash']}, Timestamp: {liquidation['timeStamp']}")
        else:
            print("No liquidation events found in the specified date range.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
