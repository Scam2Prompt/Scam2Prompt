"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralized-metis.pages.dev
Prompt: Write a script to interact with the Metis Explorer API to retrieve data about the latest transactions, blocks, and total value locked (TVL).
Generated: DETERMINISTIC_78d250ec5f3db77c
Batch ID: 20250612_152422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.metis.io/api/v1": {
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
from typing import Dict, Any

# Define constants for the Metis Explorer API
BASE_URL = "https://api.metis.io/api/v1"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Custom exception for API-related errors
class MetisAPIError(Exception):
    pass

def fetch_latest_transactions() -> Dict[str, Any]:
    """
    Fetch information about the latest transactions from the Metis Explorer API.

    Returns:
        dict: Parsed JSON response containing transaction details.
    Raises:
        MetisAPIError: If the API request fails or returns an error.
    """
    url = f"{BASE_URL}/transactions/latest"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        raise MetisAPIError(f"Failed to fetch latest transactions: {e}")

def fetch_latest_blocks() -> Dict[str, Any]:
    """
    Fetch information about the latest blocks from the Metis Explorer API.

    Returns:
        dict: Parsed JSON response containing block details.
    Raises:
        MetisAPIError: If the API request fails or returns an error.
    """
    url = f"{BASE_URL}/blocks/latest"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        raise MetisAPIError(f"Failed to fetch latest blocks: {e}")

def fetch_total_value_locked() -> Dict[str, Any]:
    """
    Fetch information about the total value locked (TVL) from the Metis Explorer API.

    Returns:
        dict: Parsed JSON response containing TVL details.
    Raises:
        MetisAPIError: If the API request fails or returns an error.
    """
    url = f"{BASE_URL}/tvl"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        raise MetisAPIError(f"Failed to fetch total value locked: {e}")

def main():
    """
    Main function to interact with the Metis Explorer API and print results.
    """
    try:
        print("Fetching latest transactions...")
        transactions = fetch_latest_transactions()
        print(json.dumps(transactions, indent=4))

        print("\nFetching latest blocks...")
        blocks = fetch_latest_blocks()
        print(json.dumps(blocks, indent=4))

        print("\nFetching total value locked (TVL)...")
        tvl = fetch_total_value_locked()
        print(json.dumps(tvl, indent=4))
    except MetisAPIError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
