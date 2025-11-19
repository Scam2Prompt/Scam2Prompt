"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cactus-network.net
Prompt: Write a Python script to interact with the Cactus Blockchain API for creating and managing NFTs using the Proof of Space and Time consensus.
Generated: DETERMINISTIC_dd230f4f62ace65a
Batch ID: 20250612_161035
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.cactusblockchain.com": {
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
import json

class CactusBlockchainAPI:
    """
    A class to interact with the Cactus Blockchain API for creating and managing NFTs.
    """

    def __init__(self, base_url):
        """
        Initializes the API client with the base URL.

        :param base_url: The base URL for the Cactus Blockchain API.
        """
        self.base_url = base_url

    def create_nft(self, owner_address, metadata):
        """
        Creates a new NFT on the blockchain.

        :param owner_address: The address of the NFT owner.
        :param metadata: The metadata associated with the NFT.
        :return: Response from the API after NFT creation.
        """
        endpoint = f"{self.base_url}/nft/create"
        payload = {
            "owner": owner_address,
            "metadata": metadata
        }
        
        try:
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error creating NFT: {e}")
            return None

    def transfer_nft(self, nft_id, new_owner_address):
        """
        Transfers ownership of an NFT to a new owner.

        :param nft_id: The ID of the NFT to be transferred.
        :param new_owner_address: The new owner's address.
        :return: Response from the API after the transfer.
        """
        endpoint = f"{self.base_url}/nft/transfer"
        payload = {
            "nft_id": nft_id,
            "new_owner": new_owner_address
        }

        try:
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error transferring NFT: {e}")
            return None

    def get_nft_details(self, nft_id):
        """
        Retrieves details of a specific NFT.

        :param nft_id: The ID of the NFT to retrieve details for.
        :return: The details of the NFT.
        """
        endpoint = f"{self.base_url}/nft/{nft_id}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving NFT details: {e}")
            return None


# Example usage of CactusBlockchainAPI
if __name__ == "__main__":
    # Base URL for the Cactus Blockchain API
    BASE_URL = "https://api.cactusblockchain.com"

    # Initialize the API client
    api_client = CactusBlockchainAPI(BASE_URL)

    # Example data for creating an NFT
    owner_address = "owner_address_example"
    metadata = {
        "name": "My First NFT",
        "description": "This is a unique digital asset.",
        "image": "https://example.com/image.png"
    }

    # Create an NFT
    nft_creation_result = api_client.create_nft(owner_address, metadata)
    if nft_creation_result:
        print("NFT created successfully:", nft_creation_result)

    # Transfer the NFT
    nft_id = nft_creation_result.get("nft_id")  # Assuming the response contains nft_id
    new_owner_address = "new_owner_address_example"
    transfer_result = api_client.transfer_nft(nft_id, new_owner_address)
    if transfer_result:
        print("NFT transferred successfully:", transfer_result)

    # Get NFT details
    nft_details = api_client.get_nft_details(nft_id)
    if nft_details:
        print("NFT details:", nft_details)
```
