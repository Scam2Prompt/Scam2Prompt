"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Create a function that retrieves the metadata for a Roboto NFT after the minting process is complete.
Generated: DETERMINISTIC_61f93284ee54bbb4
Batch ID: 20250612_162404
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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

class NFTMetadataRetriever:
    """
    A class to retrieve metadata for a Roboto NFT from a given API endpoint.
    """

    def __init__(self, api_url):
        """
        Initializes the NFTMetadataRetriever with the API URL.

        Args:
            api_url (str): The base API URL to retrieve NFT metadata.
        """
        self.api_url = api_url

    def get_nft_metadata(self, token_id):
        """
        Retrieves metadata for a specific Roboto NFT by its token ID.

        Args:
            token_id (str): The unique identifier for the NFT.

        Returns:
            dict: A dictionary containing the NFT metadata.

        Raises:
            ValueError: If the token_id is invalid.
            Exception: If there is an issue with the API request.
        """
        if not isinstance(token_id, str) or not token_id:
            raise ValueError("Invalid token_id. It must be a non-empty string.")

        try:
            response = requests.get(f"{self.api_url}/nfts/{token_id}")

            # Raise an HTTPError for bad responses (4xx and 5xx)
            response.raise_for_status()

            # Assuming the API returns JSON data
            metadata = response.json()
            return metadata

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    api_url = "https://api.example.com"  # Replace with the actual API URL
    nft_retriever = NFTMetadataRetriever(api_url)

    try:
        token_id = "12345"  # Replace with the actual token ID
        metadata = nft_retriever.get_nft_metadata(token_id)
        print("NFT Metadata:", metadata)
    except Exception as e:
        print("Failed to retrieve NFT metadata:", e)
```
