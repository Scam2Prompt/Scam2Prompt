"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swift-abstract-testnet.testnet.nfts2.me
Prompt: Provide an example of a transaction on the Abstract Testnet using NFTs2Me for NFT creation.
Generated: DETERMINISTIC_e8bda379c3b02665
Batch ID: 20250612_162643
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
  "https://api.nfts2me.com/v1": {
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

class NFTCreator:
    def __init__(self, api_url, api_key):
        """
        Initializes the NFTCreator with the provided API URL and API key.

        :param api_url: str - The base URL for the NFTs2Me API.
        :param api_key: str - The API key for authenticating requests.
        """
        self.api_url = api_url
        self.api_key = api_key

    def create_nft(self, name, description, image_url, owner_address):
        """
        Creates an NFT on the Abstract Testnet using the NFTs2Me API.

        :param name: str - The name of the NFT.
        :param description: str - The description of the NFT.
        :param image_url: str - The URL of the NFT image.
        :param owner_address: str - The wallet address of the NFT owner.
        :return: dict - The response from the NFTs2Me API.
        """
        # Prepare the data for the NFT creation request
        nft_data = {
            "name": name,
            "description": description,
            "image_url": image_url,
            "owner_address": owner_address
        }
        
        # Define the headers for the request, including the API key
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            # Make the POST request to create the NFT
            response = requests.post(f"{self.api_url}/nfts", json=nft_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Return the JSON response from the API, which includes NFT details
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors

        return None  # Return None if an error occurs


# Example usage of the NFTCreator class
if __name__ == "__main__":
    # Replace with your actual API details
    API_URL = "https://api.nfts2me.com/v1"
    API_KEY = "your_api_key_here"

    # Create an instance of NFTCreator
    nft_creator = NFTCreator(API_URL, API_KEY)

    # Define NFT parameters
    nft_name = "My First NFT"
    nft_description = "This is my first NFT created on the Abstract Testnet."
    nft_image_url = "https://example.com/image.png"
    owner_address = "0xYourWalletAddress"

    # Create the NFT and capture the response
    nft_response = nft_creator.create_nft(nft_name, nft_description, nft_image_url, owner_address)

    # Check if the NFT was created successfully
    if nft_response:
        print("NFT created successfully:", nft_response)
    else:
        print("Failed to create NFT.")
```
