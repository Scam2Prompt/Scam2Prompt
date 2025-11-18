"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Write a tutorial-style code snippet demonstrating how to use the Sui JSON-RPC API to query network status and transaction history.
Generated: DETERMINISTIC_ccb0b1558ab0620a
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-sui-rpc-url.com": {
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

class SuiClient:
    """
    A simple client for interacting with the Sui JSON-RPC API.
    """

    def __init__(self, rpc_url):
        """
        Initializes the SuiClient with the given RPC URL.

        :param rpc_url: The URL of the Sui JSON-RPC endpoint.
        """
        self.rpc_url = rpc_url

    def _send_request(self, method, params):
        """
        Sends a JSON-RPC request to the Sui API.

        :param method: The JSON-RPC method name to call.
        :param params: The parameters for the method.
        :return: The JSON response from the API, or raises an error.
        """
        headers = {'Content-Type': 'application/json'}
        payload = {
            'jsonrpc': '2.0',
            'id': 1,
            'method': method,
            'params': params
        }

        try:
            response = requests.post(self.rpc_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for HTTP issues
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to send request: {e}")

    def get_network_status(self):
        """
        Queries the network status from the Sui API.

        :return: Network status information.
        """
        response = self._send_request('sui_getNetworkStatus', [])
        return response.get('result', {})

    def get_transaction_history(self, address):
        """
        Queries the transaction history for a given address.

        :param address: The address for which to retrieve transaction history.
        :return: A list of transactions associated with the address.
        """
        response = self._send_request('sui_getTransactions', [address])
        return response.get('result', [])

# Example usage:
if __name__ == "__main__":
    # Define the Sui RPC URL
    RPC_URL = "https://your-sui-rpc-url.com"  # Replace with actual Sui RPC URL

    # Create an instance of the SuiClient
    sui_client = SuiClient(RPC_URL)

    # Query network status
    try:
        network_status = sui_client.get_network_status()
        print("Network Status:", network_status)
    except RuntimeError as e:
        print(f"Error fetching network status: {e}")

    # Query transaction history for a specific address
    address = "0xYourAddress"  # Replace with actual address
    try:
        transaction_history = sui_client.get_transaction_history(address)
        print("Transaction History:", transaction_history)
    except RuntimeError as e:
        print(f"Error fetching transaction history: {e}")
```
