"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.co
Prompt: Provide code examples for connecting to Initia's multichain network and retrieving data from its interwoven infrastructure.
Generated: DETERMINISTIC_6e5b6c4b90bf0eff
Batch ID: 20250612_151759
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.initia.network": {
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

class InitiaMultichainClient:
    """
    A client for connecting to Initia's multichain network and retrieving data.
    """

    def __init__(self, base_url):
        """
        Initialize the client with the base URL for the multichain API.

        :param base_url: str - The base URL for Initia's multichain API.
        """
        self.base_url = base_url

    def get_data(self, endpoint, params=None):
        """
        Retrieve data from a specified endpoint.

        :param endpoint: str - The API endpoint to retrieve data from.
        :param params: dict - Optional parameters for the API request.
        :return: dict - The JSON response from the API.
        :raises ValueError: If the response status code is not 200.
        :raises Exception: For other request-related errors.
        """
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise ValueError(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle other request errors

    def retrieve_block_data(self, block_height):
        """
        Retrieve block data from the multichain network.

        :param block_height: int - The height of the block to retrieve.
        :return: dict - The block data.
        :raises ValueError: If the block data cannot be retrieved.
        """
        endpoint = f"blocks/{block_height}"
        return self.get_data(endpoint)

    def retrieve_transaction_data(self, transaction_id):
        """
        Retrieve transaction data from the multichain network.

        :param transaction_id: str - The ID of the transaction to retrieve.
        :return: dict - The transaction data.
        :raises ValueError: If the transaction data cannot be retrieved.
        """
        endpoint = f"transactions/{transaction_id}"
        return self.get_data(endpoint)


# Example usage:
if __name__ == "__main__":
    base_url = "https://api.initia.network"  # Replace with the actual base URL
    client = InitiaMultichainClient(base_url)

    # Retrieve block data
    try:
        block_data = client.retrieve_block_data(12345)
        print("Block Data:", json.dumps(block_data, indent=2))
    except ValueError as ve:
        print(f"Error retrieving block data: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Retrieve transaction data
    try:
        transaction_data = client.retrieve_transaction_data("tx1234567890")
        print("Transaction Data:", json.dumps(transaction_data, indent=2))
    except ValueError as ve:
        print(f"Error retrieving transaction data: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
