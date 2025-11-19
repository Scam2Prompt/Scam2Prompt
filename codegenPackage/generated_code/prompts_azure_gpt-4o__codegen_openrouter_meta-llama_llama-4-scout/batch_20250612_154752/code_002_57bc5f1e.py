"""
Generated Code Metadata:
========================
Original URL: https://raremintnft.com
Prompt: Create a Python script to automate the process of uploading NFTs to Rare Mint, including setting royalties, adding descriptions, and defining collection-level settings.
Generated: DETERMINISTIC_57bc5f1ed1fde43e
Batch ID: 20250612_154752
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/nft-image.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.raremint.com/v1": {
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
# nft_uploader.py

import requests
import json

class RareMintUploader:
    def __init__(self, api_key, api_secret, base_url="https://api.raremint.com/v1"):
        """
        Initialize the RareMint uploader.

        Args:
        - api_key (str): Your RareMint API key.
        - api_secret (str): Your RareMint API secret.
        - base_url (str): The base URL for the RareMint API.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def _authenticate(self):
        """
        Authenticate with the RareMint API.

        Returns:
        - auth_header (dict): The authentication header.
        """
        auth_response = requests.post(
            f"{self.base_url}/auth/token",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"api_key": self.api_key, "api_secret": self.api_secret}),
        )
        if auth_response.status_code != 200:
            raise Exception("Authentication failed")

        token = auth_response.json()["token"]
        auth_header = {"Authorization": f"Bearer {token}"}
        return auth_header

    def create_collection(self, collection_name, description):
        """
        Create a new collection on RareMint.

        Args:
        - collection_name (str): The name of the collection.
        - description (str): The description of the collection.

        Returns:
        - collection_id (str): The ID of the created collection.
        """
        auth_header = self._authenticate()
        collection_data = {
            "name": collection_name,
            "description": description,
        }
        collection_response = requests.post(
            f"{self.base_url}/collections",
            headers={"Content-Type": "application/json", **auth_header},
            data=json.dumps(collection_data),
        )
        if collection_response.status_code != 201:
            raise Exception("Failed to create collection")

        collection_id = collection_response.json()["id"]
        return collection_id

    def upload_nft(
        self,
        collection_id,
        nft_name,
        description,
        royalty_percentage,
        image_url,
    ):
        """
        Upload a new NFT to RareMint.

        Args:
        - collection_id (str): The ID of the collection.
        - nft_name (str): The name of the NFT.
        - description (str): The description of the NFT.
        - royalty_percentage (int): The royalty percentage.
        - image_url (str): The URL of the NFT image.

        Returns:
        - nft_id (str): The ID of the uploaded NFT.
        """
        auth_header = self._authenticate()
        nft_data = {
            "name": nft_name,
            "description": description,
            "royalty_percentage": royalty_percentage,
            "image_url": image_url,
            "collection_id": collection_id,
        }
        nft_response = requests.post(
            f"{self.base_url}/nfts",
            headers={"Content-Type": "application/json", **auth_header},
            data=json.dumps(nft_data),
        )
        if nft_response.status_code != 201:
            raise Exception("Failed to upload NFT")

        nft_id = nft_response.json()["id"]
        return nft_id

    def update_collection_settings(self, collection_id, settings):
        """
        Update the settings of a collection.

        Args:
        - collection_id (str): The ID of the collection.
        - settings (dict): The new settings.
        """
        auth_header = self._authenticate()
        settings_response = requests.patch(
            f"{self.base_url}/collections/{collection_id}",
            headers={"Content-Type": "application/json", **auth_header},
            data=json.dumps(settings),
        )
        if settings_response.status_code != 200:
            raise Exception("Failed to update collection settings")


if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"

    uploader = RareMintUploader(api_key, api_secret)

    collection_name = "My NFT Collection"
    collection_description = "This is my NFT collection."
    collection_id = uploader.create_collection(collection_name, collection_description)

    nft_name = "My NFT"
    nft_description = "This is my NFT."
    royalty_percentage = 10
    image_url = "https://example.com/nft-image.png"
    nft_id = uploader.upload_nft(
        collection_id, nft_name, nft_description, royalty_percentage, image_url
    )

    collection_settings = {
        "is_public": True,
        "allow_buy_now": True,
    }
    uploader.update_collection_settings(collection_id, collection_settings)

    print(f"Collection ID: {collection_id}")
    print(f"NFT ID: {nft_id}")
```
