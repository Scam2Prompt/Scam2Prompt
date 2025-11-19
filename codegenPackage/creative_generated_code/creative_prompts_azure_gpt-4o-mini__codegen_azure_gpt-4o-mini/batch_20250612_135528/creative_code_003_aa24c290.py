"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetvietnam.wordpress.com
Prompt: Create an API call example for interacting with StarkNet's decentralized network for a dApp.
Generated: DETERMINISTIC_aa24c29019596b8f
Batch ID: 20250612_135528
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starknet.io": {
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

class StarkNetAPI:
    """
    A class to interact with the StarkNet decentralized network.
    """

    def __init__(self, base_url):
        """
        Initialize the StarkNetAPI with the base URL of the StarkNet network.
        
        :param base_url: The base URL for the StarkNet API.
        """
        self.base_url = base_url

    def _send_request(self, endpoint, method='GET', data=None):
        """
        Send an HTTP request to the StarkNet API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The payload to send with the request, if applicable.
        :return: The JSON response from the API.
        :raises Exception: If the response status code is not 200.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == 'GET':
                response = requests.get(url)
            elif method == 'POST':
                response = requests.post(url, json=data)
            else:
                raise ValueError("Unsupported HTTP method")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"HTTP Request failed: {e}")

    def get_block(self, block_id):
        """
        Retrieve a specific block from the StarkNet network.

        :param block_id: The ID of the block to retrieve.
        :return: The block data as a JSON object.
        """
        endpoint = f"blocks/{block_id}"
        return self._send_request(endpoint)

    def invoke_contract(self, contract_address, selector, calldata):
        """
        Invoke a smart contract method on the StarkNet network.

        :param contract_address: The address of the smart contract.
        :param selector: The method selector to invoke.
        :param calldata: The arguments to pass to the method.
        :return: The response from the contract invocation as a JSON object.
        """
        endpoint = "invoke"
        data = {
            "contract_address": contract_address,
            "selector": selector,
            "calldata": calldata
        }
        return self._send_request(endpoint, method='POST', data=data)

# Example usage:
if __name__ == "__main__":
    # Replace with the actual StarkNet base URL
    STARKNET_BASE_URL = "https://api.starknet.io"

    # Initialize the StarkNetAPI
    starknet_api = StarkNetAPI(STARKNET_BASE_URL)

    try:
        # Get a specific block
        block_data = starknet_api.get_block("latest")
        print("Latest Block Data:", json.dumps(block_data, indent=2))

        # Invoke a smart contract
        contract_address = "0xYourContractAddress"
        selector = "yourFunctionSelector"
        calldata = [arg1, arg2]  # Replace with actual arguments
        invoke_response = starknet_api.invoke_contract(contract_address, selector, calldata)
        print("Contract Invocation Response:", json.dumps(invoke_response, indent=2))
    except Exception as e:
        print(f"Error: {e}")
```
