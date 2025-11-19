"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-six.vercel.app
Prompt: Write a Python script that interacts with an OpenSea API to fetch and display the top trending NFTs and their respective volumes.
Generated: DETERMINISTIC_f5abdf4e76f43d8c
Batch ID: 20250612_160503
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

# Constants
OPENSEA_API_URL = "https://api.opensea.io/api/v1/assets"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def fetch_top_trending_nfts(limit=10):
    """
    Fetch the top trending NFTs from the OpenSea API.

    :param limit: The number of NFTs to fetch (default: 10).
    :return: A list of NFTs with their names and trading volumes.
    """
    try:
        # Define query parameters for the API request
        params = {
            "order_direction": "desc",  # Sort by descending order
            "limit": limit,            # Limit the number of results
            "offset": 0                # Start from the first result
        }

        # Make the API request
        response = requests.get(OPENSEA_API_URL, headers=HEADERS, params=params)
        response.raise_for_status()  # Raise an error for HTTP error codes

        # Parse the JSON response
        data = response.json()

        # Extract and format NFT details
        nfts = []
        for asset in data.get("assets", []):
            nfts.append({
                "name": asset.get("name") or "Unnamed NFT",
                "volume": asset.get("last_sale", {}).get("total_price", "N/A"),
                "token_id": asset.get("token_id"),
                "collection_name": asset.get("collection", {}).get("name", "Unknown Collection")
            })

        return nfts
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching data from OpenSea API: {e}")
        return []
    except KeyError as e:
        # Handle unexpected response structure
        print(f"Unexpected data structure: {e}")
        return []

def display_nfts(nfts):
    """
    Display the NFTs in a readable format.

    :param nfts: A list of NFT details to display.
    """
    if not nfts:
        print("No NFTs to display.")
        return

    print("Top Trending NFTs:")
    print("-" * 50)
    for i, nft in enumerate(nfts, start=1):
        print(f"{i}. Name: {nft['name']}")
        print(f"   Collection: {nft['collection_name']}")
        print(f"   Token ID: {nft['token_id']}")
        print(f"   Volume: {nft['volume']}")
        print("-" * 50)

def main():
    """
    Main function to fetch and display top trending NFTs.
    """
    print("Fetching top trending NFTs from OpenSea...")
    nfts = fetch_top_trending_nfts(limit=10)  # Fetch top 10 NFTs
    display_nfts(nfts)

if __name__ == "__main__":
    main()
```
