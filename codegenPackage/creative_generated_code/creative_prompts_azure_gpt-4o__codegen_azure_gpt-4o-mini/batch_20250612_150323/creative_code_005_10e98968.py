"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.pro
Prompt: Develop a script to automate the discovery of new NFT collections using OpenSea Pro's aggregation tools.
Generated: DETERMINISTIC_10e98968067b5926
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/assets": {
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
from datetime import datetime

# Constants
API_URL = "https://api.opensea.io/api/v1/assets"
HEADERS = {
    "Accept": "application/json",
    "X-API-KEY": "YOUR_API_KEY_HERE"  # Replace with your OpenSea API key
}

# Function to fetch NFT collections
def fetch_nft_collections(offset=0, limit=20):
    """
    Fetch new NFT collections from OpenSea.

    Parameters:
    offset (int): The offset for pagination.
    limit (int): The number of collections to fetch.

    Returns:
    list: A list of NFT collections.
    """
    try:
        params = {
            "order_direction": "desc",
            "offset": offset,
            "limit": limit
        }
        response = requests.get(API_URL, headers=HEADERS, params=params)
        
        # Check if the request was successful
        response.raise_for_status()

        # Parse JSON response
        data = response.json()
        
        # Extract collections from assets
        collections = [asset['asset_contract']['name'] for asset in data['assets']]
        return collections

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return []

# Function to monitor new collections
def monitor_new_collections(check_interval=300):
    """
    Monitor and discover new NFT collections at a specified interval.

    Parameters:
    check_interval (int): The time interval (in seconds) to check for new collections.
    """
    seen_collections = set()  # To track already discovered collections

    while True:
        print(f"Checking for new NFT collections at {datetime.now()}...")
        
        # Fetch collections
        new_collections = fetch_nft_collections()

        # Identify new collections
        for collection in new_collections:
            if collection not in seen_collections:
                print(f"New NFT Collection Discovered: {collection}")
                seen_collections.add(collection)

        # Wait for the specified interval before checking again
        time.sleep(check_interval)

if __name__ == "__main__":
    # Start monitoring new NFT collections
    monitor_new_collections()
```

### Notes:
- Replace `YOUR_API_KEY_HERE` with your actual OpenSea API key.
- The script checks for new NFT collections every 5 minutes (300 seconds) by default, but this can be adjusted by passing a different value to `monitor_new_collections()`.
- The program will print out newly discovered collections in real-time.
