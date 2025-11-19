"""
Generated Code Metadata:
========================
Original URL: https://swift-abstract-testnet.testnet.nfts2.me
Prompt: Create a step-by-step guide in code for integrating the Abstract Testnet with a web application using NFTs2Me APIs.
Generated: DETERMINISTIC_d43a92c5c9fcc6a8
Batch ID: 20250612_153755
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
  "https://api.nfts2me.com": {
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

class AbstractTestnetIntegration:
    """
    A class to integrate with the Abstract Testnet using NFTs2Me APIs.
    """

    BASE_URL = "https://api.nfts2me.com"  # Base URL for NFTs2Me API

    def __init__(self, api_key):
        """
        Initializes the integration with the provided API key.

        :param api_key: str - The API key for authenticating with NFTs2Me API.
        """
        self.api_key = api_key

    def get_nft_metadata(self, nft_id):
        """
        Fetches metadata for a specific NFT.

        :param nft_id: str - The ID of the NFT to retrieve metadata for.
        :return: dict - The metadata of the NFT.
        :raises ValueError: If the NFT ID is invalid.
        :raises Exception: For any other errors during the API call.
        """
        if not nft_id:
            raise ValueError("NFT ID must not be empty.")

        url = f"{self.BASE_URL}/nfts/{nft_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def create_nft(self, nft_data):
        """
        Creates a new NFT on the Abstract Testnet.

        :param nft_data: dict - The data for the NFT to be created.
        :return: dict - The response from the API after creating the NFT.
        :raises ValueError: If the NFT data is invalid.
        :raises Exception: For any other errors during the API call.
        """
        if not isinstance(nft_data, dict) or not nft_data:
            raise ValueError("NFT data must be a non-empty dictionary.")

        url = f"{self.BASE_URL}/nfts"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=nft_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def transfer_nft(self, nft_id, recipient_address):
        """
        Transfers an NFT to a specified recipient.

        :param nft_id: str - The ID of the NFT to transfer.
        :param recipient_address: str - The address of the recipient.
        :return: dict - The response from the API after transferring the NFT.
        :raises ValueError: If the NFT ID or recipient address is invalid.
        :raises Exception: For any other errors during the API call.
        """
        if not nft_id or not recipient_address:
            raise ValueError("NFT ID and recipient address must not be empty.")

        url = f"{self.BASE_URL}/nfts/{nft_id}/transfer"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {"recipient": recipient_address}

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual API key
    api_key = "your_api_key"
    integration = AbstractTestnetIntegration(api_key)

    # Fetch NFT metadata
    try:
        nft_metadata = integration.get_nft_metadata("nft_id_example")
        print("NFT Metadata:", nft_metadata)
    except Exception as e:
        print("Error fetching NFT metadata:", e)

    # Create a new NFT
    try:
        new_nft_data = {
            "name": "My NFT",
            "description": "This is a test NFT.",
            "image": "https://example.com/image.png"
        }
        created_nft = integration.create_nft(new_nft_data)
        print("Created NFT:", created_nft)
    except Exception as e:
        print("Error creating NFT:", e)

    # Transfer an NFT
    try:
        transfer_response = integration.transfer_nft("nft_id_example", "recipient_address_example")
        print("Transfer Response:", transfer_response)
    except Exception as e:
        print("Error transferring NFT:", e)
```
