"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledqinlv.com
Prompt: Write a script using OpenSea's API to fetch and display statistics for a specific NFT collection, including floor price, volume, and percentage change.
Generated: DETERMINISTIC_a844d96df5ae2372
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/collection/{collection_slug}/stats": {
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

def fetch_nft_collection_stats(collection_slug):
    """
    Fetches statistics for a specific NFT collection using the OpenSea API.

    Args:
        collection_slug (str): The unique identifier (slug) of the NFT collection.

    Returns:
        dict: A dictionary containing floor price, total volume, and 1-day percentage change.
    """
    # OpenSea API endpoint for collection stats
    api_url = f"https://api.opensea.io/api/v1/collection/{collection_slug}/stats"
    
    try:
        # Send GET request to fetch collection stats
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse JSON response
        data = response.json()
        stats = data.get("stats", {})
        
        # Extract relevant statistics
        floor_price = stats.get("floor_price", "N/A")
        total_volume = stats.get("total_volume", "N/A")
        one_day_change = stats.get("one_day_change", "N/A")
        
        # Return the extracted stats
        return {
            "floor_price": floor_price,
            "total_volume": total_volume,
            "one_day_change": one_day_change,
        }
    except requests.exceptions.RequestException as e:
        # Handle HTTP and connection-related errors
        print(f"Error fetching data from OpenSea API: {e}")
        return None
    except KeyError:
        # Handle cases where expected data is missing in the response
        print("Unexpected response structure from OpenSea API.")
        return None

def display_stats(stats, collection_slug):
    """
    Displays the statistics for a given NFT collection in a readable format.

    Args:
        stats (dict): The statistics dictionary containing floor price, total volume, and percentage change.
        collection_slug (str): The NFT collection's unique identifier (slug).
    """
    print(f"\nStatistics for NFT Collection: {collection_slug}")
    if stats:
        print(f"Floor Price: {stats['floor_price']} ETH")
        print(f"Total Volume: {stats['total_volume']} ETH")
        print(f"1-Day % Change: {stats['one_day_change'] * 100 if stats['one_day_change'] != 'N/A' else 'N/A'}%")
    else:
        print("No statistics available.")

if __name__ == "__main__":
    # Prompt user for the collection slug
    collection_slug = input("Enter the NFT collection slug (e.g., boredapeyachtclub): ").strip()

    # Fetch and display the stats for the given collection slug
    stats = fetch_nft_collection_stats(collection_slug)
    display_stats(stats, collection_slug)
```

### Notes:
- The script fetches data from OpenSea's API endpoint for collection statistics.
- Replace `requests.get` with an authenticated request if OpenSea's API requires an API key in the future.
- Ensure you comply with OpenSea's API rate limits and Terms of Service for production use.
- You may need to install the `requests` library if it's not already installed: `pip install requests`.
