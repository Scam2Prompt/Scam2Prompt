"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-presents.blogspot.com
Prompt: Explain how to use the Tron blockchain API to create and manage TRC-20 tokens programmatically.
Generated: DETERMINISTIC_a26e77a276f1a02a
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tronstack.io/v1": {
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

class TronAPI:
    def __init__(self, api_url):
        """
        Initialize the TronAPI class with the base API URL.

        :param api_url: str - The base URL for the Tron API.
        """
        self.api_url = api_url

    def create_trc20_token(self, owner_address, name, symbol, decimals, total_supply):
        """
        Create a TRC-20 token on the Tron blockchain.

        :param owner_address: str - The address of the token owner.
        :param name: str - The name of the token.
        :param symbol: str - The symbol of the token.
        :param decimals: int - The number of decimals for the token.
        :param total_supply: int - The total supply of the token.
        :return: dict - The response from the Tron API containing token details or error information.
        """
        url = f"{self.api_url}/createToken"
        payload = {
            "owner_address": owner_address,
            "name": name,
            "symbol": symbol,
            "decimals": decimals,
            "total_supply": total_supply
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")
            return {"error": str(err)}

    def get_token_info(self, token_id):
        """
        Retrieve information about a TRC-20 token.

        :param token_id: str - The ID of the token to retrieve information for.
        :return: dict - The response from the Tron API containing token information or error information.
        """
        url = f"{self.api_url}/getToken/{token_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")
            return {"error": str(err)}

    def transfer_token(self, owner_address, to_address, token_id, amount):
        """
        Transfer TRC-20 tokens from one address to another.

        :param owner_address: str - The address of the token owner.
        :param to_address: str - The recipient address.
        :param token_id: str - The ID of the token to transfer.
        :param amount: int - The amount of tokens to transfer.
        :return: dict - The response from the Tron API confirming the transfer or error information.
        """
        url = f"{self.api_url}/transferToken"
        payload = {
            "owner_address": owner_address,
            "to_address": to_address,
            "token_id": token_id,
            "amount": amount
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")
            return {"error": str(err)}

# Example usage
if __name__ == "__main__":
    tron_api = TronAPI(api_url="https://api.tronstack.io/v1")  # Replace with actual Tron API Endpoint
    
    # Create a TRC-20 token
    token_creation_response = tron_api.create_trc20_token(
        owner_address="TXYZ1234567890",  # Replace with a valid Tron address
        name="MyToken",
        symbol="MTK",
        decimals=18,
        total_supply=1000000
    )
    
    print("Token Creation Response:", token_creation_response)

    # Get token information
    token_info_response = tron_api.get_token_info(token_id="token_id_here")  # Replace with actual token ID
    print("Token Info Response:", token_info_response)

    # Transfer tokens
    transfer_response = tron_api.transfer_token(
        owner_address="TXYZ1234567890",  # Replace with a valid Tron address
        to_address="TABC1234567890",  # Replace with a valid recipient address
        token_id="token_id_here",  # Replace with actual token ID
        amount=100
    )
    
    print("Transfer Response:", transfer_response)
```

In this code snippet, the class `TronAPI` encapsulates methods for creating TRC-20 tokens, retrieving token information, and transferring tokens on the Tron blockchain. Each method includes appropriate error handling and comments for clarity.
