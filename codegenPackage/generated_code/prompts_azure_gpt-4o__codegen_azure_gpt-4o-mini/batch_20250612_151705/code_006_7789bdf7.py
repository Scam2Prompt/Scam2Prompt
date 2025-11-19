"""
Generated Code Metadata:
========================
Original URL: https://debridge.org
Prompt: Provide an example of how to use the deBridge API to implement cross-chain intents for DeFi applications.
Generated: DETERMINISTIC_7789bdf7f041f6f9
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.debridge.finance/v1": {
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
import json

class DeBridgeAPI:
    """
    A class to interact with the deBridge API for cross-chain intents in DeFi applications.
    """

    BASE_URL = "https://api.debridge.finance/v1"

    def __init__(self, api_key):
        """
        Initializes the DeBridgeAPI with the provided API key.

        :param api_key: str - Your API key for authentication.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the deBridge API.

        :param endpoint: str - The API endpoint to call.
        :param params: dict - Optional parameters for the request.
        :return: dict - The JSON response from the API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def get_cross_chain_intents(self, from_chain, to_chain, amount, recipient):
        """
        Retrieves cross-chain intents for a specified transfer.

        :param from_chain: str - The source blockchain (e.g., 'Ethereum').
        :param to_chain: str - The destination blockchain (e.g., 'Binance Smart Chain').
        :param amount: float - The amount to transfer.
        :param recipient: str - The recipient address on the destination chain.
        :return: dict - The response containing cross-chain intent details.
        """
        params = {
            "fromChain": from_chain,
            "toChain": to_chain,
            "amount": amount,
            "recipient": recipient
        }
        return self._make_request("cross-chain/intents", params)

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual deBridge API key
    api_key = "your_api_key"
    debridge_api = DeBridgeAPI(api_key)

    # Define parameters for the cross-chain transfer
    from_chain = "Ethereum"
    to_chain = "Binance Smart Chain"
    amount = 0.1  # Amount to transfer
    recipient = "0xRecipientAddressHere"  # Replace with the actual recipient address

    # Fetch cross-chain intents
    intents = debridge_api.get_cross_chain_intents(from_chain, to_chain, amount, recipient)

    if intents:
        print("Cross-chain intents retrieved successfully:")
        print(json.dumps(intents, indent=4))
    else:
        print("Failed to retrieve cross-chain intents.")
```
