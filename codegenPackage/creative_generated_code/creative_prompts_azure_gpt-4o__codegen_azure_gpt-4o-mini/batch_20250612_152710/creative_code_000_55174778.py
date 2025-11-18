"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: Write a script to interact with the Phi Protocol API to mint a Phi Cred NFT based on specific onchain transaction data. Include functionality for customizing artwork formats such as pixel art or GIFs.
Generated: DETERMINISTIC_551747788156716c
Batch ID: 20250612_152710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.phiprotocol.com": {
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
import os

class PhiProtocolAPI:
    """Class to interact with the Phi Protocol API for minting Phi Cred NFTs."""
    
    def __init__(self, api_key, base_url='https://api.phiprotocol.com'):
        """
        Initialize the API client.
        
        :param api_key: The API key for authenticating requests.
        :param base_url: The base URL for the Phi Protocol API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def mint_phi_cred_nft(self, transaction_data, artwork_path):
        """
        Mint a Phi Cred NFT based on on-chain transaction data and artwork.
        
        :param transaction_data: Dictionary containing transaction details.
        :param artwork_path: File path to the artwork (image or GIF).
        :return: The response from the API as a dictionary.
        """
        # Validate inputs
        if not self._validate_transaction_data(transaction_data):
            raise ValueError("Invalid transaction data provided.")
        
        if not os.path.isfile(artwork_path):
            raise FileNotFoundError(f"Artwork file does not exist: {artwork_path}")

        # Prepare the API endpoint and headers
        endpoint = f"{self.base_url}/nfts/mint"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        # Prepare the payload for the API request
        payload = {
            'transactionData': transaction_data,
            'artwork': self._upload_artwork(artwork_path)
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

    def _validate_transaction_data(self, transaction_data):
        """
        Validate transaction data format.
        
        :param transaction_data: The transaction data to validate.
        :return: True if valid, False otherwise.
        """
        required_keys = ['transaction_id', 'user_id', 'timestamp']
        return all(key in transaction_data for key in required_keys)

    def _upload_artwork(self, artwork_path):
        """
        Upload the artwork to the API and return the uploaded artwork URL.
        
        :param artwork_path: File path to the artwork.
        :return: URL of the uploaded artwork.
        """
        # Prepare the API endpoint for artwork upload
        upload_endpoint = f"{self.base_url}/artwork/upload"
        
        # Upload the artwork file
        with open(artwork_path, 'rb') as artwork_file:
            files = {'file': artwork_file}
            response = requests.post(upload_endpoint, files=files)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('url')  # Extract the URL from the response


# Example usage
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    phi_api = PhiProtocolAPI(api_key=API_KEY)

    # Define transaction data for minting
    transaction_data = {
        'transaction_id': 'abc123',
        'user_id': 'user456',
        'timestamp': '2023-10-01T12:00:00Z'
    }
    
    # Specify the path to the artwork file
    artwork_path = 'path/to/your/artwork.png'  # Replace with the actual file path

    try:
        nft_response = phi_api.mint_phi_cred_nft(transaction_data, artwork_path)
        print("NFT Minted Successfully:", nft_response)
    except Exception as e:
        print("Error minting NFT:", e)
```
