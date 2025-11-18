"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-dao.web.app
Prompt: Write a Python script using the Solana API to fetch the floor price and 24-hour trading volume of NFTs from specific collections listed on the Tensor platform, such as "Mad Lads" or "Transdimensional Fox Federation."
Generated: DETERMINISTIC_18f7af87300b619a
Batch ID: 20250612_153517
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.market/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.tensor.market/v1`": {
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

# Constants
SOLANA_API_BASE_URL = "https://api.tensor.market/v1"  # Tensor API Base URL
COLLECTIONS = ["Mad Lads", "Transdimensional Fox Federation"]  # List of collections
HEADERS = {"Content-Type": "application/json"}  # HTTP request headers

def fetch_collection_data(collection_name):
    """
    Fetch floor price and 24-hour trading volume for a given NFT collection from Tensor API.

    Args:
        collection_name (str): Name of the NFT collection.

    Returns:
        dict: Dictionary containing floor price and 24-hour trading volume if successful.
        None: If the request fails or data is unavailable.
    """
    try:
        # Prepare URL for API request
        url = f"{SOLANA_API_BASE_URL}/collection-stats"
        
        # Query parameters for filtering by collection name
        params = {
            "collection": collection_name
        }
        
        # Make a GET request to Tensor API
        response = requests.get(url, headers=HEADERS, params=params)
        
        # Raise an exception if the response status is not OK (200)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract required fields
        floor_price = data.get("floor_price", None)
        trading_volume_24h = data.get("volume_24h", None)
        
        if floor_price is not None and trading_volume_24h is not None:
            return {
                "collection_name": collection_name,
                "floor_price": floor_price,
                "trading_volume_24h": trading_volume_24h
            }
        else:
            print(f"Data unavailable for collection: {collection_name}")
            return None
    
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"Error fetching data for collection '{collection_name}': {e}")
        return None

def main():
    """
    Main function to fetch data for multiple collections and display results.
    """
    # Loop through each collection and fetch its data
    for collection in COLLECTIONS:
        result = fetch_collection_data(collection)
        if result:
            print(f"Collection: {result['collection_name']}")
            print(f"Floor Price: {result['floor_price']} SOL")
            print(f"24-hour Trading Volume: {result['trading_volume_24h']} SOL")
            print("-" * 40)

# Entry point for the script
if __name__ == "__main__":
    main()
```

Note: Replace the placeholder URL (`https://api.tensor.market/v1`) with the actual Tensor API endpoint if it differs. Ensure you have the necessary API access credentials or tokens if required by Tensor's API. The code assumes the API response structure provides `floor_price` and `volume_24h` fields directly. If the structure differs, adjust the field extraction accordingly.
