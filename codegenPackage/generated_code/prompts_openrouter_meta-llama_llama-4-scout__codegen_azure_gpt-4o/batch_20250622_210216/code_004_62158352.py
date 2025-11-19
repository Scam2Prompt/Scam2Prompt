"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Develop a Python script to interact with the OpenSea API for managing and retrieving information about an NFT collection, specifically one that is similar to the MetaRebelz collection.
Generated: DETERMINISTIC_6215835248fa93f8
Batch ID: 20250622_210216
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

# Constants
API_BASE_URL = "https://api.opensea.io/api/v1"
COLLECTION_SLUG = "metarebelz"  # Replace with the slug of your desired NFT collection
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Function to fetch collection details
def fetch_collection_details(collection_slug):
    """
    Fetch details of an NFT collection from OpenSea API.

    Args:
        collection_slug (str): The slug of the NFT collection.

    Returns:
        dict: Collection details if successful, None otherwise.
    """
    url = f"{API_BASE_URL}/collection/{collection_slug}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching collection details: {e}")
        return None

# Function to fetch assets in a collection
def fetch_collection_assets(collection_slug, limit=20, offset=0):
    """
    Fetch assets in an NFT collection from OpenSea API.

    Args:
        collection_slug (str): The slug of the NFT collection.
        limit (int): Number of assets to fetch per request (default: 20).
        offset (int): Offset for pagination (default: 0).

    Returns:
        dict: Assets data if successful, None otherwise.
    """
    url = f"{API_BASE_URL}/assets"
    params = {
        "collection": collection_slug,
        "limit": limit,
        "offset": offset
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching collection assets: {e}")
        return None

# Main function
def main():
    """
    Main function to interact with the OpenSea API and retrieve NFT collection data.
    """
    print(f"Fetching details for collection: {COLLECTION_SLUG}")
    collection_details = fetch_collection_details(COLLECTION_SLUG)
    if collection_details:
        print(json.dumps(collection_details, indent=4))  # Pretty print collection details

    print(f"\nFetching assets for collection: {COLLECTION_SLUG}")
    assets_data = fetch_collection_assets(COLLECTION_SLUG, limit=10)  # Fetch first 10 assets
    if assets_data:
        print(json.dumps(assets_data, indent=4))  # Pretty print assets data

# Entry point
if __name__ == "__main__":
    main()
```

### Notes:
- Replace `COLLECTION_SLUG` with the slug of the NFT collection you want to interact with.
- Ensure you have an active internet connection to make API requests.
- If OpenSea requires an API key for certain endpoints, you may need to include it in the `HEADERS` dictionary.
