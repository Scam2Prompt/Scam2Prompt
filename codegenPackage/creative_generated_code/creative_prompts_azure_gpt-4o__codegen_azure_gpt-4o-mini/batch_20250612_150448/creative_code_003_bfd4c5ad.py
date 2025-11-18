"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redirectdevs.on.fleek.co
Prompt: Create a script to handle token bridge transfers between chains using the blockchain cloud infrastructure powered by Chain Cloud and Sequence, as described on the webpage.
Generated: DETERMINISTIC_bfd4c5ad90d439bd
Batch ID: 20250612_150448
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chaincloud.com": {
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

class TokenBridge:
    def __init__(self, api_url, api_key):
        """
        Initializes the TokenBridge with the API URL and API key.
        
        :param api_url: The base URL for the blockchain cloud API.
        :param api_key: The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes an HTTP request to the specified endpoint.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET or POST).
        :param data: The data to send with the request (for POST).
        :return: The response from the API as a JSON object.
        """
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        url = f"{self.api_url}/{endpoint}"

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=headers)

            # Raise an exception for HTTP errors
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def transfer_tokens(self, from_chain, to_chain, amount, token_id, recipient_address):
        """
        Transfers tokens from one chain to another using the token bridge.

        :param from_chain: The chain from which tokens are being sent.
        :param to_chain: The chain to which tokens are being sent.
        :param amount: The amount of tokens to transfer.
        :param token_id: The identifier of the token being transferred.
        :param recipient_address: The address of the recipient on the target chain.
        :return: The transaction details if successful.
        """
        endpoint = 'token/bridge/transfer'
        data = {
            'fromChain': from_chain,
            'toChain': to_chain,
            'amount': amount,
            'tokenId': token_id,
            'recipientAddress': recipient_address
        }

        response = self._make_request(endpoint, method='POST', data=data)
        return response

# Example usage
if __name__ == "__main__":
    API_URL = "https://api.chaincloud.com"  # Replace with actual API URL
    API_KEY = "your_api_key_here"           # Replace with actual API key

    bridge = TokenBridge(API_URL, API_KEY)
    
    try:
        # Transfer tokens example
        transaction_details = bridge.transfer_tokens(
            from_chain="Ethereum",
            to_chain="BinanceSmartChain",
            amount=100,
            token_id="0x123456789abcdef",  # Replace with actual token ID
            recipient_address="0xabcdef123456789"  # Replace with actual recipient address
        )
        print("Transfer successful:", transaction_details)
    except Exception as e:
        print("Error during token transfer:", e)
```
