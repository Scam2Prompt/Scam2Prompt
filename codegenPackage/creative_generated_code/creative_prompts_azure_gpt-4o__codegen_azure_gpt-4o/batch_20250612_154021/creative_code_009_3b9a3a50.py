"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterde.com
Prompt: Create a tutorial-style code example for building a portfolio tracker using Aster's API, displaying user trading statistics like total trading volume, open interest, and symbols traded.
Generated: DETERMINISTIC_3b9a3a506fa46c43
Batch ID: 20250612_154021
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
"""
Portfolio Tracker using Aster's API
Description:
This script uses Aster's API to fetch and display user trading statistics, including total trading volume,
open interest, and symbols traded. It assumes the user has valid API credentials.
"""

import requests
from typing import Dict, List

# Constants: Replace these with your actual API credentials and endpoint
API_BASE_URL = "https://api.aster.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Function to make API requests
def fetch_data(endpoint: str, params: Dict = None) -> Dict:
    """
    Fetch data from Aster's API.
    Args:
        endpoint (str): API endpoint to query.
        params (Dict): Query parameters for the API request.

    Returns:
        Dict: Parsed JSON response from the API.
    """
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(f"{API_BASE_URL}/{endpoint}", headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request Error: {req_err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    return {}

# Function to fetch trading statistics
def get_trading_statistics() -> Dict:
    """
    Fetch trading statistics from Aster's API.

    Returns:
        Dict: Dictionary containing trading statistics.
    """
    endpoint = "portfolio/trading-statistics"  # Adjust as per Aster's API documentation
    return fetch_data(endpoint)

# Function to display trading statistics
def display_statistics(stats: Dict) -> None:
    """
    Display trading statistics in a user-friendly format.
    Args:
        stats (Dict): Trading statistics fetched from the API.
    """
    if not stats:
        print("No statistics available. Please check your API credentials or network connection.")
        return

    # Extract and display relevant statistics
    total_volume = stats.get("total_trading_volume", "N/A")
    open_interest = stats.get("open_interest", "N/A")
    symbols_traded = stats.get("symbols_traded", [])

    print("\n--- Trading Statistics ---")
    print(f"Total Trading Volume: {total_volume}")
    print(f"Open Interest: {open_interest}")
    print("Symbols Traded:")
    for symbol in symbols_traded:
        print(f"  - {symbol}")

# Main function
def main():
    """
    Main function to execute the portfolio tracker logic.
    """
    print("Fetching trading statistics...")
    trading_stats = get_trading_statistics()
    display_statistics(trading_stats)

# Entry point of the script
if __name__ == "__main__":
    main()
```
