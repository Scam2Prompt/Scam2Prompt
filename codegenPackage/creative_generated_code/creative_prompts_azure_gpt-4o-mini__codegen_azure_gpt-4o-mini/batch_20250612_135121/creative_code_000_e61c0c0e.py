"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-feature-vercel-audience-419labs.vercel.app
Prompt: Generate a code snippet to interact with a dApp in the StarkNet ecosystem using its API.
Generated: DETERMINISTIC_e61c0c0ebec3afc2
Batch ID: 20250612_135121
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starknet.io/v1": {
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
    A class to interact with the StarkNet ecosystem API.
    """

    def __init__(self, base_url):
        """
        Initializes the StarkNetAPI with the given base URL.

        Args:
            base_url (str): The base URL of the StarkNet API.
        """
        self.base_url = base_url

    def get_block(self, block_number):
        """
        Retrieves a block by its number.

        Args:
            block_number (int): The number of the block to retrieve.

        Returns:
            dict: The block data if the request is successful.

        Raises:
            ValueError: If the block number is invalid.
            Exception: For other API related errors.
        """
        if block_number < 0:
            raise ValueError("Block number must be a non-negative integer.")
        
        # Construct the URL for the API endpoint
        url = f"{self.base_url}/blocks/{block_number}"
        
        try:
            # Send a GET request to the API
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse and return the JSON response
            return response.json()
        
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other error
            raise

    def send_transaction(self, transaction_data):
        """
        Sends a transaction to the StarkNet network.

        Args:
            transaction_data (dict): The transaction data to send.

        Returns:
            dict: The transaction response if the request is successful.

        Raises:
            ValueError: If the transaction data is invalid.
            Exception: For other API related errors.
        """
        if not isinstance(transaction_data, dict) or not transaction_data:
            raise ValueError("Transaction data must be a non-empty dictionary.")

        # Construct the URL for the API endpoint
        url = f"{self.base_url}/transactions"
        
        try:
            # Send a POST request to the API
            response = requests.post(url, json=transaction_data)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse and return the JSON response
            return response.json()
        
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other error
            raise

# Example usage:
if __name__ == "__main__":
    # Replace with the actual StarkNet API base URL
    BASE_URL = "https://api.starknet.io/v1"
    starknet_api = StarkNetAPI(BASE_URL)

    try:
        # Fetch a block by its number
        block_data = starknet_api.get_block(12345)
        print("Block Data:", json.dumps(block_data, indent=4))

        # Prepare transaction data (example)
        transaction_data = {
            "from": "0xYourFromAddress",
            "to": "0xYourToAddress",
            "amount": 100,
            "nonce": 1
        }

        # Send a transaction
        transaction_response = starknet_api.send_transaction(transaction_data)
        print("Transaction Response:", json.dumps(transaction_response, indent=4))

    except Exception as e:
        print(f"An error occurred in the example usage: {e}")
```
