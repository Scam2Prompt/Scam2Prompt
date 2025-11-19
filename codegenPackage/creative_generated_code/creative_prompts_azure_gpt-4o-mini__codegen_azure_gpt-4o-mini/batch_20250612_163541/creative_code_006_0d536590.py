"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layeralorg.pages.dev
Prompt: Create a code example that demonstrates how to interact with the Layer Marketplace for trading Data Capsule NFTs.
Generated: DETERMINISTIC_0d536590c099a558
Batch ID: 20250612_163541
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.layer.marketplace/v1": {
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

class LayerMarketplace:
    BASE_URL = 'https://api.layer.marketplace/v1'  # Base URL for the Layer Marketplace API

    def __init__(self, api_key):
        """Initialize LayerMarketplace with an API key."""
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_nfts(self):
        """Retrieve a list of available Data Capsule NFTs."""
        try:
            response = requests.get(f'{self.BASE_URL}/nfts', headers=self.headers)

            # Raise an error if the request was unsuccessful
            response.raise_for_status()

            return response.json()  # Return the JSON response containing NFTs
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Log HTTP errors
        except Exception as err:
            print(f'An error occurred: {err}')  # Log other errors

    def buy_nft(self, nft_id, user_id):
        """Purchase a Data Capsule NFT by its ID for a specific user."""
        try:
            payload = {
                'nft_id': nft_id,
                'user_id': user_id
            }
            response = requests.post(f'{self.BASE_URL}/purchase', json=payload, headers=self.headers)

            # Raise an error if the request was unsuccessful
            response.raise_for_status()

            return response.json()  # Return the JSON response confirming the purchase
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred while purchasing NFT: {http_err}')  # Log HTTP errors
        except Exception as err:
            print(f'An error occurred while purchasing NFT: {err}')  # Log other errors

    def sell_nft(self, nft_id, price):
        """List a Data Capsule NFT for sale."""
        try:
            payload = {
                'nft_id': nft_id,
                'price': price
            }
            response = requests.post(f'{self.BASE_URL}/sell', json=payload, headers=self.headers)

            # Raise an error if the request was unsuccessful
            response.raise_for_status()

            return response.json()  # Return the JSON response confirming the listing
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred while selling NFT: {http_err}')  # Log HTTP errors
        except Exception as err:
            print(f'An error occurred while selling NFT: {err}')  # Log other errors

# Example Usage
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    marketplace = LayerMarketplace(api_key)

    # Fetch available NFTs
    nfts = marketplace.get_nfts()
    print(nfts)

    # Buy an NFT (replace with actual nft_id and user_id)
    purchase_response = marketplace.buy_nft(nft_id='NFT_ID', user_id='USER_ID')
    print(purchase_response)

    # Sell an NFT (replace with actual nft_id and desired price)
    sell_response = marketplace.sell_nft(nft_id='NFT_ID', price=100)
    print(sell_response)
```
