"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0g-zerogravity.testnet.nfts2.me
Prompt: Create a function to handle 404 errors when querying NFT collections from the "NFTs 2 Me" testnet API.
Generated: DETERMINISTIC_38747b4f2cbcf626
Batch ID: 20250612_154057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.api.nfts2me.com/collections": {
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

class NFTCollectionError(Exception):
    """Custom exception for NFT collection errors."""
    pass

def fetch_nft_collection(api_url: str) -> dict:
    """
    Fetches NFT collection data from the specified API endpoint.

    Args:
        api_url (str): The URL of the "NFTs 2 Me" testnet API.

    Returns:
        dict: The JSON response containing NFT collection data.

    Raises:
        NFTCollectionError: If the request to the API fails or returns a 404 error.
    """
    try:
        response = requests.get(api_url)

        # Check if the response indicates a 404 error
        if response.status_code == 404:
            raise NFTCollectionError(f"404 Not Found: The resource at {api_url} was not found.")
        
        # Check for other potential HTTP errors
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)

        # Return the JSON content of the response
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        raise NFTCollectionError(f"HTTP error occurred: {http_err}") from http_err
    except requests.exceptions.RequestException as req_err:
        raise NFTCollectionError(f"Request error occurred: {req_err}") from req_err
    except ValueError as json_err:
        raise NFTCollectionError(f"JSON decoding error: {json_err}") from json_err

# Example usage (uncomment to use in production)

# API_URL = "https://testnet.api.nfts2me.com/collections"
# try:
#     nft_collection = fetch_nft_collection(API_URL)
#     print(nft_collection)
# except NFTCollectionError as e:
#     print(e)
```
