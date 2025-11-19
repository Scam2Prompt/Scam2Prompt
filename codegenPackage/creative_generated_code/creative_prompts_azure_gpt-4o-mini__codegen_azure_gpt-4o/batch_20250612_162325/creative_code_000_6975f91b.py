"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://temteamio.web.app
Prompt: How can I trade NFTs on Solana using the features provided by Tensor, including viewing collection floors and 24-hour volume?
Generated: DETERMINISTIC_6975f91b643f2786
Batch ID: 20250612_162325
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tensor.trade/v1": {
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
BASE_URL = "https://api.tensor.trade/v1"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "NFT-Trader-App"
}

def fetch_collection_stats(collection_name):
    """
    Fetches the floor price and 24-hour trading volume of an NFT collection on Solana using Tensor's API.
    
    Args:
        collection_name (str): The name of the NFT collection.
    
    Returns:
        dict: A dictionary containing the floor price and 24-hour volume if successful, None otherwise.
    """
    try:
        endpoint = f"{BASE_URL}/collection-stats/{collection_name}"
        response = requests.get(endpoint, headers=HEADERS)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract required fields
        floor_price = data.get("floor_price", None)
        volume_24h = data.get("volume_24h", None)
        
        return {
            "floor_price": floor_price,
            "volume_24h": volume_24h
        }
    except requests.exceptions.RequestException as e:
        # Log the error and return None
        print(f"Error fetching collection stats: {e}")
        return None


def main():
    """
    Main function to interact with the Tensor API and display collection stats.
    """
    # Example collection name
    collection_name = "degods"
    
    # Fetch collection stats
    stats = fetch_collection_stats(collection_name)
    
    if stats:
        print(f"Collection: {collection_name}")
        print(f"Floor Price: {stats['floor_price']} SOL")
        print(f"24-hour Volume: {stats['volume_24h']} SOL")
    else:
        print("Failed to fetch collection stats. Please try again later.")


if __name__ == "__main__":
    main()
```
