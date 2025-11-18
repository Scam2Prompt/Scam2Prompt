"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: Write a Python script to interact with the Polkadot Live desktop client API for retrieving blockchain data on Mac or Windows.
Generated: DETERMINISTIC_956c321fc30fcc91
Batch ID: 20250612_153849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:9933": {
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

class PolkadotAPI:
    """A class to interact with the Polkadot Live desktop client API."""

    def __init__(self, base_url="http://127.0.0.1:9933"):
        """
        Initializes the PolkadotAPI with the given base URL.

        Args:
            base_url (str): The base URL of the Polkadot API. Default is localhost.
        """
        self.base_url = base_url

    def _send_request(self, method, params=None):
        """
        Sends a JSON-RPC request to the Polkadot API.

        Args:
            method (str): The method name to call on the API.
            params (list): The parameters to pass to the method.

        Returns:
            dict: The response from the API.

        Raises:
            Exception: If the request fails or if the response contains an error.
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params or []
        }

        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()  # Raise an error for bad HTTP status codes
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error connecting to Polkadot API: {str(e)}")

        response_data = response.json()

        # Check for errors in the response
        if 'error' in response_data:
            raise Exception(f"API Error: {response_data['error']}")

        return response_data['result']

    def get_chain_info(self):
        """Retrieves information about the current chain."""
        return self._send_request("chain_getHeader")

    def get_block_by_number(self, block_number):
        """
        Retrieves a block by its number.

        Args:
            block_number (int): The block number to retrieve.

        Returns:
            dict: The block data.

        Raises:
            Exception: If the block cannot be retrieved.
        """
        return self._send_request("chain_getBlock", [block_number])

    def get_latest_block(self):
        """Retrieves the latest block in the chain."""
        header = self.get_chain_info()
        return self.get_block_by_number(header['number'])

def main():
    """Main entry point for the script."""
    try:
        api = PolkadotAPI()

        # Retrieve and print the latest block information
        latest_block = api.get_latest_block()
        print("Latest Block:", json.dumps(latest_block, indent=2))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
