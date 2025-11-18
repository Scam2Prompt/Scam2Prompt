"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerobeings.app
Prompt: Write code to query metadata for an NFT collection hosted on OpenSea, referencing the structure used by "Zero Beings."
Generated: DETERMINISTIC_09d41cc36084dfb1
Batch ID: 20250612_151644
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

def fetch_nft_metadata(collection_slug):
    """
    Fetch metadata for an NFT collection from OpenSea.
    
    Args:
        collection_slug (str): The slug identifier for the NFT collection on OpenSea.
        
    Returns:
        dict: A dictionary containing the metadata of the NFT collection.
        
    Raises:
        ValueError: If the collection slug is invalid or metadata cannot be retrieved.
        Exception: For any other HTTP or network-related errors.
    """

    # Base URL for OpenSea API
    OPENSEA_API_URL = "https://api.opensea.io/api/v1/assets"

    # Parameters for the API request
    params = {
        "collection": collection_slug,  # Slug for the NFT collection
        "limit": 50,  # Limit number of results per request, adjust as needed
        "offset": 0   # Offset for pagination, can be used for larger collections
    }

    try:
        # Perform the GET request to the OpenSea API
        response = requests.get(OPENSEA_API_URL, params=params)

        # Raise an HTTPError if the response status is not OK (200)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if assets are available in the response
        if "assets" not in data or not data["assets"]:
            raise ValueError("No assets found for the given collection slug.")

        return data["assets"]

    except requests.exceptions.HTTPError as http_err:
        # Handle specific HTTP errors
        raise Exception(f"HTTP error occurred: {http_err}")

    except requests.exceptions.RequestException as req_err:
        # Handle non-HTTP network-related errors
        raise Exception(f"Request error occurred: {req_err}")

    except ValueError as val_err:
        # Handle issues with invalid data in response
        raise ValueError(f"Value error: {val_err}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace 'zero-beings' with the slug for the desired collection
        collection_slug = "zero-beings"
        metadata = fetch_nft_metadata(collection_slug)

        # Print metadata for the NFT collection
        for asset in metadata:
            print(f"Name: {asset.get('name')}, Token ID: {asset.get('token_id')}, Image URL: {asset.get('image_url')}")
    
    except Exception as e:
        # Print error if fetching metadata fails
        print(f"An error occurred: {e}")
```
