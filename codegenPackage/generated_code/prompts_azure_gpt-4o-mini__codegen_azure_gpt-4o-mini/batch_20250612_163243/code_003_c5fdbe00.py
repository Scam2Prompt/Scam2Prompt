"""
Generated Code Metadata:
========================
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: What are the steps to integrate Meta Blocks for building immersive NFT applications?
Generated: DETERMINISTIC_c5fdbe00e32f82b1
Batch ID: 20250612_163243
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.metablocks.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image.png": {
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

class MetaBlocksIntegration:
    """
    A class to handle the integration of Meta Blocks for building immersive NFT applications.
    """

    def __init__(self, api_key: str):
        """
        Initializes the MetaBlocksIntegration with the provided API key.

        :param api_key: The API key for authenticating with Meta Blocks.
        """
        self.api_key = api_key
        self.base_url = "https://api.metablocks.com/v1"

    def create_nft(self, nft_data: dict) -> dict:
        """
        Creates a new NFT using the provided data.

        :param nft_data: A dictionary containing NFT details.
        :return: The response from the Meta Blocks API.
        """
        url = f"{self.base_url}/nfts"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=nft_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def get_nft(self, nft_id: str) -> dict:
        """
        Retrieves an NFT by its ID.

        :param nft_id: The ID of the NFT to retrieve.
        :return: The NFT data if found, else None.
        """
        url = f"{self.base_url}/nfts/{nft_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def list_nfts(self) -> list:
        """
        Lists all NFTs created by the user.

        :return: A list of NFTs.
        """
        url = f"{self.base_url}/nfts"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Meta Blocks API key
    api_key = "your_api_key"
    meta_blocks = MetaBlocksIntegration(api_key)

    # Create a new NFT
    nft_data = {
        "name": "My First NFT",
        "description": "This is an example NFT.",
        "image_url": "https://example.com/image.png"
    }
    created_nft = meta_blocks.create_nft(nft_data)
    print("Created NFT:", created_nft)

    # List all NFTs
    nfts = meta_blocks.list_nfts()
    print("List of NFTs:", nfts)

    # Get a specific NFT by ID
    if created_nft and 'id' in created_nft:
        nft_id = created_nft['id']
        nft_details = meta_blocks.get_nft(nft_id)
        print("NFT Details:", nft_details)
```
