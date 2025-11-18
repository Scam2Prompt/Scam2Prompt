"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdx.com
Prompt: Develop a script to retrieve real-time trading data and open interest statistics from Aster's API for use in a trader's portfolio dashboard.
Generated: DETERMINISTIC_b62f813a657f9a8f
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.astertrading.com/v1": {
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

# Constants
BASE_URL = "https://api.astertrading.com/v1"  # Replace with the actual base URL of Aster's API
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Endpoints
TRADING_DATA_ENDPOINT = "/trading-data"  # Replace with the actual endpoint for trading data
OPEN_INTEREST_ENDPOINT = "/open-interest"  # Replace with the actual endpoint for open interest

def fetch_data(endpoint, params=None):
    """
    Fetches data from Aster's API for the given endpoint and parameters.

    Args:
        endpoint (str): The API endpoint.
        params (dict): Optional query parameters.

    Returns:
        dict: The API response data as a dictionary.

    Raises:
        Exception: If the API request fails or an error occurs.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(BASE_URL + endpoint, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data from {endpoint}: {str(e)}")

def get_trading_data():
    """
    Retrieves real-time trading data from Aster's API.

    Returns:
        dict: Trading data as a dictionary.
    """
    return fetch_data(TRADING_DATA_ENDPOINT)

def get_open_interest():
    """
    Retrieves open interest statistics from Aster's API.

    Returns:
        dict: Open interest data as a dictionary.
    """
    return fetch_data(OPEN_INTEREST_ENDPOINT)

def main():
    """
    Main entry point for the script. Retrieves trading data and open interest statistics,
    and prints them for use in a trader's portfolio dashboard.
    """
    try:
        print("Fetching real-time trading data...")
        trading_data = get_trading_data()
        print("Trading Data:")
        print(json.dumps(trading_data, indent=4))  # Pretty-print the data

        print("\nFetching open interest statistics...")
        open_interest_data = get_open_interest()
        print("Open Interest Data:")
        print(json.dumps(open_interest_data, indent=4))  # Pretty-print the data
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace the `BASE_URL`, `API_KEY`, and endpoint constants with the actual values provided by Aster's API documentation.
- This script uses the `requests` library for HTTP interactions. If not installed, you can install it via `pip install requests`.
- Add further enhancements like logging or specific filtering of data as needed for production usage.
