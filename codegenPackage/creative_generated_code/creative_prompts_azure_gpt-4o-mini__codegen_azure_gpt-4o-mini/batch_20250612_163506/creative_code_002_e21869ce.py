"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqnetwork.io
Prompt: Write a Python script that bridges IQ tokens across different blockchains as described on the IQ Dashboard.
Generated: DETERMINISTIC_e21869ce15442e32
Batch ID: 20250612_163506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.iqdashboard.com": {
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

class IQTokenBridge:
    """
    A class to facilitate bridging IQ tokens across different blockchains.
    """

    def __init__(self, api_url):
        """
        Initialize the IQTokenBridge with the specified API URL.
        
        :param api_url: The base URL for the IQ Dashboard API.
        """
        self.api_url = api_url

    def fetch_token_info(self, token_id):
        """
        Fetch token information from the IQ Dashboard API.

        :param token_id: The ID of the token to fetch information for.
        :return: A dictionary containing token information.
        :raises Exception: If there is an error during the API request.
        """
        try:
            response = requests.get(f"{self.api_url}/tokens/{token_id}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def bridge_tokens(self, token_id, amount, from_chain, to_chain):
        """
        Initiate the bridging of tokens from one blockchain to another.

        :param token_id: The ID of the token to bridge.
        :param amount: The amount of tokens to bridge.
        :param from_chain: The blockchain to bridge from.
        :param to_chain: The blockchain to bridge to.
        :return: Response from the bridging request.
        :raises Exception: If there is an error during the bridging request.
        """
        payload = {
            "token_id": token_id,
            "amount": amount,
            "from_chain": from_chain,
            "to_chain": to_chain
        }
        
        try:
            response = requests.post(f"{self.api_url}/bridge", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

if __name__ == "__main__":
    # Example usage of the IQTokenBridge class
    API_URL = "https://api.iqdashboard.com"  # Replace with the actual API URL
    bridge = IQTokenBridge(API_URL)

    # Define the parameters for bridging tokens
    token_id = "IQ12345"  # Example token ID
    amount = 100.0        # Amount of tokens to bridge
    from_chain = "Ethereum"  # Source blockchain
    to_chain = "Binance Smart Chain"  # Destination blockchain

    # Fetch token information
    token_info = bridge.fetch_token_info(token_id)
    if token_info:
        print("Token Information:", token_info)

    # Bridge tokens
    response = bridge.bridge_tokens(token_id, amount, from_chain, to_chain)
    if response:
        print("Bridging Response:", response)
```
