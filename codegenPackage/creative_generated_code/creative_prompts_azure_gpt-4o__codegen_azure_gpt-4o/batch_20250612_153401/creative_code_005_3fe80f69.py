"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stakes.pages.dev
Prompt: Write a script to query Flashstake analytics data, such as total TVL, strategy TVL, and FLASH token market cap, using the protocol's API.
Generated: DETERMINISTIC_3fe80f6906ce0351
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.flashstake.io/v1": {
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

# Constants for the Flashstake API
BASE_URL = "https://api.flashstake.io/v1"  # Replace with the actual base URL of the Flashstake API
ENDPOINTS = {
    "total_tvl": "/analytics/total-tvl",
    "strategy_tvl": "/analytics/strategy-tvl",
    "flash_market_cap": "/analytics/flash-market-cap"
}

# Function to query the Flashstake API and return analytics data
def fetch_flashstake_data(endpoint: str):
    """
    Fetch data from the Flashstake API for a specified endpoint.

    Args:
        endpoint (str): The API endpoint to query.

    Returns:
        dict: The JSON response from the API.

    Raises:
        Exception: If there is an issue with the API request.
    """
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data from {url}: {e}")

# Main function to retrieve and display analytics data
def main():
    """
    Main function to query and display Flashstake analytics data.
    """
    try:
        # Fetch Total TVL
        total_tvl = fetch_flashstake_data(ENDPOINTS["total_tvl"])
        print("Total TVL:", total_tvl)

        # Fetch Strategy TVL
        strategy_tvl = fetch_flashstake_data(ENDPOINTS["strategy_tvl"])
        print("Strategy TVL:", strategy_tvl)

        # Fetch FLASH Token Market Cap
        flash_market_cap = fetch_flashstake_data(ENDPOINTS["flash_market_cap"])
        print("FLASH Token Market Cap:", flash_market_cap)

    except Exception as e:
        print(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
