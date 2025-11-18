"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axienftexchange.com
Prompt: Generate code to automate the process of listing NFTs for sale on Axie NFT Exchange using fixed pricing strategies.
Generated: DETERMINISTIC_675fd8fa0d43f6b4
Batch ID: 20250612_154757
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.axieinfinity.com/v1": {
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

class AxieNFTExchange:
    API_URL = "https://api.axieinfinity.com/v1"

    def __init__(self, wallet_address, api_key):
        """
        Initializes the AxieNFTExchange with the user's wallet address and API key.

        :param wallet_address: str - The wallet address of the user
        :param api_key: str - The API key for authentication
        """
        self.wallet_address = wallet_address
        self.api_key = api_key

    def list_nft_for_sale(self, nft_id, price):
        """
        List an NFT for sale on the Axie NFT Exchange with a fixed price.

        :param nft_id: str - The ID of the NFT to be listed
        :param price: float - The price at which to list the NFT
        :return: dict - Response from the API
        """
        # Ensure price is a positive value
        if price <= 0:
            raise ValueError("Price must be a positive value.")

        # Prepare the payload for the API request
        payload = {
            "wallet_address": self.wallet_address,
            "nft_id": nft_id,
            "price": price,
            "action": "list"
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Make a POST request to list the NFT for sale
            response = requests.post(f"{self.API_URL}/nfts", headers=headers, data=json.dumps(payload))

            # Raise an exception if the request was unsuccessful
            response.raise_for_status()

            # Return the response as a dictionary
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Error during requests to {self.API_URL}: {req_err}")

        return None  # Return None in case of an error

# Example usage
if __name__ == "__main__":
    # Replace with actual wallet address and API key
    wallet_address = "YOUR_WALLET_ADDRESS"
    api_key = "YOUR_API_KEY"
    
    axie_exchange = AxieNFTExchange(wallet_address, api_key)
    
    nft_id = "AXIE_ID"  # Replace with the NFT ID you want to sell
    price = 0.05  # Fixed price in ETH or the equivalent currency

    result = axie_exchange.list_nft_for_sale(nft_id, price)

    if result:
        print("NFT listed successfully:", result)
    else:
        print("Failed to list NFT.")
```
