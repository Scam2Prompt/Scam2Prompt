"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nerve-network.web.app
Prompt: Write code to interact with the NerveNetwork API to perform a cross-chain asset swap between two supported blockchains. Include details about how to specify the chains and assets involved.
Generated: DETERMINISTIC_7af6d0ae9750ed8b
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nerve.network/v1": {
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

class NerveNetworkAPI:
    BASE_URL = "https://api.nerve.network/v1"

    def __init__(self, api_key):
        """
        Initializes the NerveNetwork API client with the provided API key.

        :param api_key: Your API key for authentication with the NerveNetwork API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', params=None, data=None):
        """
        Makes a request to the NerveNetwork API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET or POST).
        :param params: Optional query parameters for the request.
        :param data: Optional data for POST requests.
        :return: The response from the API or raises an exception on error.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        url = f"{self.BASE_URL}/{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Unsupported HTTP method provided.")
            
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            raise SystemExit(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise SystemExit(f"An error occurred: {err}")

    def get_supported_chains(self):
        """
        Fetches the list of supported blockchains for asset swaps.

        :return: A list of supported chains.
        """
        return self._make_request("chains")

    def get_asset_info(self, chain, asset):
        """
        Retrieves information about a specific asset on a given chain.

        :param chain: The blockchain chain to query.
        :param asset: The asset symbol to query.
        :return: Asset information.
        """
        params = {
            "chain": chain,
            "asset": asset
        }
        return self._make_request("assets/info", params=params)

    def perform_asset_swap(self, from_chain, from_asset, to_chain, to_asset, amount):
        """
        Performs an asset swap between two supported chains.

        :param from_chain: The source blockchain.
        :param from_asset: The asset to swap from.
        :param to_chain: The destination blockchain.
        :param to_asset: The asset to swap to.
        :param amount: The amount to swap.
        :return: The result of the swap transaction.
        """
        data = {
            "from_chain": from_chain,
            "from_asset": from_asset,
            "to_chain": to_chain,
            "to_asset": to_asset,
            "amount": amount
        }
        return self._make_request("swap", method='POST', data=data)

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    api_client = NerveNetworkAPI(API_KEY)

    try:
        chains = api_client.get_supported_chains()
        print("Supported Chains:", chains)

        # Specify chains and assets for the swap
        from_chain = "Ethereum"
        from_asset = "ETH"
        to_chain = "Binance Smart Chain"
        to_asset = "BNB"
        amount = 0.1  # Amount to swap

        swap_result = api_client.perform_asset_swap(from_chain, from_asset, to_chain, to_asset, amount)
        print("Swap Result:", swap_result)

    except Exception as e:
        print(f"Error during API interaction: {e}")
```
