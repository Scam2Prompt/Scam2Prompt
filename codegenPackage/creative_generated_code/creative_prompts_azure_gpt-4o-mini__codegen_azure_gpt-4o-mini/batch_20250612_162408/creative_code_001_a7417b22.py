"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portalfridge.com
Prompt: Write a code snippet that connects to the Portal Token Bridge API for transferring tokens between different chains.
Generated: DETERMINISTIC_a7417b220a15f597
Batch ID: 20250612_162408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.portalbridge.com": {
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

class TokenBridgeAPI:
    """
    A class to interact with the Portal Token Bridge API for transferring tokens
    between different chains.
    """

    BASE_URL = "https://api.portalbridge.com"  # Replace with actual API base URL

    def __init__(self, api_key: str):
        """
        Initialize the TokenBridgeAPI with an API key.

        :param api_key: The API key for authenticating requests.
        """
        self.api_key = api_key

    def _request(self, endpoint: str, method: str = 'GET', data: dict = None):
        """
        A private method to handle API requests.

        :param endpoint: The API endpoint for the request.
        :param method: The HTTP method to use ('GET', 'POST', etc.).
        :param data: The data to send with the request (for POST).
        :return: The JSON response from the API.
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            if method.upper() == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return None

    def transfer_tokens(self, from_chain: str, to_chain: str, amount: float, token_address: str):
        """
        Transfer tokens from one chain to another.

        :param from_chain: The chain to transfer tokens from.
        :param to_chain: The chain to transfer tokens to.
        :param amount: The amount of tokens to transfer.
        :param token_address: The address of the token to transfer.
        :return: The response from the API indicating the status of the transfer.
        """
        endpoint = "/transfer"
        data = {
            "from_chain": from_chain,
            "to_chain": to_chain,
            "amount": amount,
            "token_address": token_address
        }

        return self._request(endpoint, method='POST', data=data)


# Example usage:
if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    token_bridge = TokenBridgeAPI(api_key=API_KEY)

    # Transfer tokens
    response = token_bridge.transfer_tokens(
        from_chain="Ethereum",
        to_chain="Binance Smart Chain",
        amount=10.0,
        token_address="0xYourTokenAddressHere"
    )

    if response:
        print("Transfer response:", response)
    else:
        print("Transfer failed.")
```
