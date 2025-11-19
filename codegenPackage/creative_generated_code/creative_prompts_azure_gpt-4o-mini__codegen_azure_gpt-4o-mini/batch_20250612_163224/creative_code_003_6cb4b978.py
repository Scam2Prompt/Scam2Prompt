"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0g-zerogravity.testnet.nfts2.me
Prompt: How do I implement error handling for missing NFT collections in my application using the NFTs 2 Me API?
Generated: DETERMINISTIC_6cb4b978bf9d8974
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

class NFTCollectionError(Exception):
    """Custom exception for NFT collection errors."""
    pass

class NFTAPI:
    """Class to interact with the NFTs 2 Me API."""

    BASE_URL = "https://api.nfts2me.com"

    def __init__(self):
        """Initialize the NFTAPI instance."""
        self.session = requests.Session()

    def get_collection(self, collection_id):
        """
        Fetch an NFT collection by its ID.

        Args:
            collection_id (str): The ID of the NFT collection to retrieve.

        Returns:
            dict: The NFT collection data if found.

        Raises:
            NFTCollectionError: If the collection is not found or an error occurs.
        """
        url = f"{self.BASE_URL}/collections/{collection_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            collection_data = response.json()
            if not collection_data:
                raise NFTCollectionError(f"Collection with ID '{collection_id}' not found.")

            return collection_data

        except requests.HTTPError as http_err:
            raise NFTCollectionError(f"HTTP error occurred: {http_err}") from http_err
        except requests.RequestException as req_err:
            raise NFTCollectionError(f"Request error occurred: {req_err}") from req_err
        except Exception as err:
            raise NFTCollectionError(f"An unexpected error occurred: {err}") from err

# Example usage
if __name__ == "__main__":
    nft_api = NFTAPI()
    collection_id = "example-collection-id"

    try:
        collection = nft_api.get_collection(collection_id)
        print("NFT Collection Data:", collection)
    except NFTCollectionError as e:
        print("Error:", e)
```
