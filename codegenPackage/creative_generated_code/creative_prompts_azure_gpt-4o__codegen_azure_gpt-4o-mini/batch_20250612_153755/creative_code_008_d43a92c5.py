"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swift-abstract-testnet.testnet.nfts2.me
Prompt: Create a step-by-step guide in code for integrating the Abstract Testnet with a web application using NFTs2Me APIs.
Generated: DETERMINISTIC_d43a92c5c9fcc6a8
Batch ID: 20250612_153755
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/image.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

class NFTIntegration:
    """
    A class to integrate with the Abstract Testnet using the NFTs2Me APIs.
    """

    BASE_URL = "https://api.nfts2me.com"

    def __init__(self, api_key):
        """
        Initializes the NFTIntegration class with the given API key.

        Args:
            api_key (str): Your NFTs2Me API key for authentication.
        """
        self.api_key = api_key

    def get_nft(self, nft_id):
        """
        Fetches NFT details by NFT ID.
        
        Args:
            nft_id (str): The ID of the NFT to retrieve.

        Returns:
            dict: The NFT details if the request is successful.

        Raises:
            Exception: If the request fails or the NFT is not found.
        """
        url = f"{self.BASE_URL}/nfts/{nft_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching NFT: {response.status_code} - {response.text}")

    def create_nft(self, nft_data):
        """
        Creates a new NFT in the Abstract Testnet.

        Args:
            nft_data (dict): A dictionary containing NFT information.

        Returns:
            dict: The created NFT details.

        Raises:
            Exception: If the request fails.
        """
        url = f"{self.BASE_URL}/nfts"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=nft_data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Error creating NFT: {response.status_code} - {response.text}")

    def transfer_nft(self, nft_id, to_address):
        """
        Transfers an NFT to a specified address.

        Args:
            nft_id (str): The ID of the NFT to transfer.
            to_address (str): The recipient's address.

        Returns:
            dict: The result of the transfer.

        Raises:
            Exception: If the request fails.
        """
        url = f"{self.BASE_URL}/nfts/{nft_id}/transfer"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {"to": to_address}

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error transferring NFT: {response.status_code} - {response.text}")

def main():
    """
    Main function to demonstrate the NFT integration functionality.
    """
    api_key = "YOUR_NFTS2ME_API_KEY"  # Replace with your actual API key
    nft_integration = NFTIntegration(api_key)

    # Step 1: Create a new NFT
    nft_data = {
        "name": "My First NFT",
        "description": "This is a description of my first NFT",
        "image": "http://example.com/image.png",
        "attributes": {"rarity": "rare"}
    }

    try:
        created_nft = nft_integration.create_nft(nft_data)
        print(f"Created NFT: {created_nft}")

        # Step 2: Get NFT details
        nft_id = created_nft['id']
        nft_details = nft_integration.get_nft(nft_id)
        print(f"NFT Details: {nft_details}")

        # Step 3: Transfer the NFT
        recipient_address = "RECIPIENT_WALLET_ADDRESS"  # Replace with recipient's address
        transfer_result = nft_integration.transfer_nft(nft_id, recipient_address)
        print(f"Transfer Result: {transfer_result}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
