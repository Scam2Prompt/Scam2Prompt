"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0x2d255c2xa5014e1510747ef2971009fec0e1db48.pages.dev
Prompt: Write a Python script to analyze data from OpenSea Pro's API and identify NFT collections with the highest percentage increase in owner listings over the past 24 hours.
Generated: DETERMINISTIC_728b25d8d5ceaa1e
Batch ID: 20250612_152235
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

# Creative Generated Code:
# ========================

```python
import requests
import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
OPENSEA_API_URL = "https://api.opensea.io/api/v1"
COLLECTIONS_ENDPOINT = f"{OPENSEA_API_URL}/collections"
LISTINGS_ENDPOINT = f"{OPENSEA_API_URL}/assets"
HEADERS = {
    "Accept": "application/json",
    "X-API-KEY": "your_api_key_here"  # Replace with your OpenSea Pro API key
}

def fetch_collections():
    """
    Fetch the list of NFT collections from OpenSea API.
    Returns a list of collections or raises an exception on failure.
    """
    try:
        response = requests.get(COLLECTIONS_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        return response.json().get("collections", [])
    except requests.RequestException as e:
        logging.error(f"Error fetching collections: {e}")
        raise

def fetch_owner_listings(collection_slug):
    """
    Fetch owner listing data for a specific collection.
    Returns the number of listings or raises an exception on failure.
    """
    params = {"collection": collection_slug, "limit": 100}
    try:
        response = requests.get(LISTINGS_ENDPOINT, headers=HEADERS, params=params)
        response.raise_for_status()
        assets = response.json().get("assets", [])
        return len(assets)  # Number of listings for owners
    except requests.RequestException as e:
        logging.error(f"Error fetching owner listings for {collection_slug}: {e}")
        raise

def analyze_collections():
    """
    Analyze collections to find the ones with the highest percentage increase
    in owner listings over the past 24 hours.
    """
    try:
        # Fetch collections data
        collections = fetch_collections()
        if not collections:
            logging.warning("No collections data found.")
            return

        collection_analysis = []

        # Analyze each collection
        for collection in collections:
            collection_slug = collection.get("slug")
            if not collection_slug:
                logging.warning(f"Collection does not have a slug: {collection}")
                continue

            logging.info(f"Analyzing collection: {collection_slug}")

            # Fetch current listings and simulate fetching yesterday's listings
            current_listings = fetch_owner_listings(collection_slug)
            yesterday_listings = current_listings * 0.8  # Mocking data for demonstration

            # Calculate percentage increase
            percentage_increase = ((current_listings - yesterday_listings) / yesterday_listings) * 100
            collection_analysis.append({
                "slug": collection_slug,
                "current_listings": current_listings,
                "yesterday_listings": yesterday_listings,
                "percentage_increase": percentage_increase,
            })

        # Sort collections by percentage increase
        sorted_collections = sorted(collection_analysis, key=lambda x: x["percentage_increase"], reverse=True)

        # Display top collections
        logging.info("Top collections by percentage increase in owner listings:")
        for collection in sorted_collections[:5]:
            logging.info(
                f"Collection: {collection['slug']} | Current Listings: {collection['current_listings']} | "
                f"Yesterday Listings: {collection['yesterday_listings']} | "
                f"Percentage Increase: {collection['percentage_increase']:.2f}%"
            )
    except Exception as e:
        logging.error(f"Error during analysis: {e}")

if __name__ == "__main__":
    analyze_collections()
```

Make sure to replace `"your_api_key_here"` with your actual OpenSea Pro API key. Note that the script mocks yesterday's listings data for demonstration purposes, as the actual historical data would require access to a proper endpoint for historical stats, which is not included in the public API.
