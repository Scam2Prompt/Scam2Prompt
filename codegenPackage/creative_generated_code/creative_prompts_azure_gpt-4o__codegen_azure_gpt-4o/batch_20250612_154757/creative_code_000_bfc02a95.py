"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artrecast.com
Prompt: Write a Python script using the OpenSea API to list NFTs for sale, including metadata attributes like "BoredApeYachtClub" and price in ETH, similar to the collections featured on ArtRecast.
Generated: DETERMINISTIC_bfc02a95a5ba3bd2
Batch ID: 20250612_154757
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

def get_opensea_nfts(collection_slug, limit=10):
    """
    Fetches NFTs for sale from the OpenSea API for a specific collection.
    
    Args:
        collection_slug (str): The slug of the collection (e.g., 'boredapeyachtclub').
        limit (int): The number of assets to fetch per request (default is 10).
        
    Returns:
        list: A list of NFTs with metadata and price details.
    """
    # OpenSea API endpoint for fetching assets
    url = "https://api.opensea.io/api/v1/assets"
    params = {
        "collection": collection_slug,  # Collection slug (e.g., 'boredapeyachtclub')
        "order_direction": "asc",       # Sort direction (ascending)
        "limit": limit,                 # Number of assets to fetch
    }
    
    try:
        # Make the GET request to the OpenSea API
        response = requests.get(url, params=params)

        # Raise an exception if the request fails
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        nfts = []

        # Extract relevant details from each asset
        for asset in data.get("assets", []):
            nft = {
                "name": asset.get("name"),
                "token_id": asset.get("token_id"),
                "image_url": asset.get("image_url"),
                "price_in_eth": None,  # Default value if no price info is available
                "metadata": asset.get("traits", []),  # Metadata attributes
            }

            # Extract price details if available
            sell_orders = asset.get("sell_orders")
            if sell_orders:
                # Assuming price is in ETH; extract the first sell order
                current_price = int(sell_orders[0].get("current_price", 0))
                nft["price_in_eth"] = current_price / 10 ** 18  # Convert from wei to ETH
            
            nfts.append(nft)

        return nfts

    except requests.exceptions.RequestException as e:
        # Log and re-raise network-related errors
        print(f"Error fetching data from OpenSea API: {e}")
        raise
    except Exception as e:
        # Log and re-raise other errors
        print(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    # Example usage of the script
    collection_slug = "boredapeyachtclub"  # Replace with your desired collection slug
    try:
        # Fetch NFTs for sale
        nfts = get_opensea_nfts(collection_slug, limit=10)
        
        # Display the fetched NFTs
        for nft in nfts:
            print(f"Name: {nft['name']}, Token ID: {nft['token_id']}, "
                  f"Price: {nft['price_in_eth']} ETH, Metadata: {nft['metadata']}")
    except Exception as e:
        print(f"Failed to fetch NFTs: {e}")
```

Make sure to install `requests` if not already installed by running:
```bash
pip install requests
```
