"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-h5ht7yy42-zapper-fi.vercel.app
Prompt: Generate a script that uses Zapper's Beta API to track and display the trading volume of popular NFT collections.
Generated: DETERMINISTIC_9080bfe24d1acde0
Batch ID: 20250612_145421
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.fi/v1/nfts/collections": {
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
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

# Define constants for API endpoint and headers
API_URL = "https://api.zapper.fi/v1/nfts/collections"
HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY_HERE",  # Replace with your actual API key
    "Content-Type": "application/json"
}

def get_nft_collections():
    """
    Fetches popular NFT collections and their trading volumes from Zapper's Beta API.
    
    Returns:
        list: A list of dictionaries containing NFT collection data.
    """
    try:
        response = requests.get(API_URL, headers=HEADERS)
        response.raise_for_status()  # Raise an error for bad responses
        collections = response.json()  # Parse JSON response
        return collections
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except Exception as err:
        logging.error(f"An error occurred: {err}")  # Log other errors
    return []

def display_trading_volume(collections):
    """
    Displays the trading volume of each NFT collection.

    Args:
        collections (list): A list of NFT collection dictionaries.
    """
    if not collections:
        logging.info("No collections found.")
        return

    logging.info("Trading Volume of Popular NFT Collections:")
    for collection in collections:
        name = collection.get("name")
        volume = collection.get("tradingVolume", 0)  # Default to 0 if not available
        logging.info(f"Collection: {name}, Trading Volume: {volume}")

def main():
    """
    Main function to execute the script.
    """
    logging.info("Fetching NFT collections...")
    collections = get_nft_collections()
    display_trading_volume(collections)

if __name__ == "__main__":
    main()
```

### Note:
- Replace `"YOUR_API_KEY_HERE"` with your actual API key to authenticate requests to Zapper's API.
- Ensure you have the `requests` library installed in your Python environment (`pip install requests`).
