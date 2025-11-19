"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: Write a Python script that interacts with the Monero blockchain using the Monero RPC API available at node.xmr.cz.
Generated: DETERMINISTIC_13559590ffe4c127
Batch ID: 20250612_164021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://node.xmr.cz:18081/json_rpc": {
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

class MoneroRPC:
    """
    A class to interact with the Monero RPC API.
    """

    def __init__(self, url='http://node.xmr.cz:18081/json_rpc'):
        """
        Initializes the MoneroRPC client with the specified URL.

        :param url: The URL of the Monero RPC node.
        """
        self.url = url

    def _post_request(self, method, params=None):
        """
        Sends a POST request to the Monero RPC API.

        :param method: The name of the RPC method to call.
        :param params: The parameters to pass to the RPC method.
        :return: The JSON response from the server.
        """
        headers = {'Content-Type': 'application/json'}
        payload = {
            'jsonrpc': '2.0',
            'id': '0',
            'method': method,
            'params': params or {}
        }

        try:
            response = requests.post(self.url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def get_balance(self, address):
        """
        Retrieves the balance of a given Monero address.

        :param address: The Monero address to check the balance for.
        :return: The balance of the address or None if an error occurs.
        """
        result = self._post_request('get_balance', {'address': address})
        if result and 'result' in result:
            return result['result']['balance']
        return None

    def get_height(self):
        """
        Retrieves the current height of the Monero blockchain.

        :return: The height of the blockchain or None if an error occurs.
        """
        result = self._post_request('get_height')
        if result and 'result' in result:
            return result['result']['height']
        return None

if __name__ == '__main__':
    # Example usage of the MoneroRPC class
    rpc_client = MoneroRPC()

    # Check the current blockchain height
    height = rpc_client.get_height()
    if height is not None:
        print(f"Current blockchain height: {height}")

    # Check the balance of a specific address
    address = 'YOUR_MONERO_ADDRESS_HERE'  # Replace with a valid Monero address
    balance = rpc_client.get_balance(address)
    if balance is not None:
        print(f"Balance for address {address}: {balance} XMR")
```

### Note:
- Replace `'YOUR_MONERO_ADDRESS_HERE'` with a valid Monero address to check the balance.
- Ensure to have the `requests` library installed (`pip install requests`) before running the script.
