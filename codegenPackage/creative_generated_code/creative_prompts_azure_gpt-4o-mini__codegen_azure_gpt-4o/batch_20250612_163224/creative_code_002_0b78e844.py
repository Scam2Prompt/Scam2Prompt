"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0g-zerogravity.testnet.nfts2.me
Prompt: Can you provide a code snippet for checking the existence of an NFT collection before attempting to access it on NFTs 2 Me?
Generated: DETERMINISTIC_0b78e8444373e8b4
Batch ID: 20250612_163224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nfts2me.com": {
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

def check_nft_collection_exists(api_url, collection_id):
    """
    Check if an NFT collection exists on the NFTs 2 Me platform.
    
    Parameters:
    - api_url (str): Base URL for the NFTs 2 Me API.
    - collection_id (str): ID of the NFT collection to check.
    
    Returns:
    - bool: True if the collection exists, False otherwise.
    """
    try:
        # Construct the API endpoint for checking the collection
        endpoint = f"{api_url}/collections/{collection_id}"
        
        # Send a GET request to the endpoint
        response = requests.get(endpoint)

        # Handle HTTP errors
        response.raise_for_status()
        
        # If the API response is successful, return True
        if response.status_code == 200:
            return True

    except requests.exceptions.HTTPError as http_err:
        # Handle cases when the collection is not found (404 Not Found)
        if response.status_code == 404:
            return False
        # Log other HTTP errors for debugging purposes
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Log network-related errors for debugging purposes
        print(f"Request error occurred: {req_err}")
    
    # Return False in case of any unexpected issues
    return False


# Example usage:
if __name__ == "__main__":
    # Replace with the actual base URL of the NFTs 2 Me API
    API_URL = "https://api.nfts2me.com"
    
    # Replace with the actual collection ID you want to check
    COLLECTION_ID = "example-collection-id"
    
    # Check if the collection exists
    exists = check_nft_collection_exists(API_URL, COLLECTION_ID)
    
    if exists:
        print(f"The NFT collection '{COLLECTION_ID}' exists.")
    else:
        print(f"The NFT collection '{COLLECTION_ID}' does not exist.")
```
