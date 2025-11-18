"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-fees.pages.dev
Prompt: Generate code to validate on-chain data using Etherscan's API and display the results in a user-friendly format.
Generated: DETERMINISTIC_0c6b8687659c8ca6
Batch ID: 20250612_150034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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

class EtherscanAPI:
    """Class to interact with Etherscan API for on-chain data validation."""
    
    BASE_URL = "https://api.etherscan.io/api"

    def __init__(self, api_key):
        """
        Initialize the EtherscanAPI with the provided API key.

        :param api_key: str: Your Etherscan API key.
        """
        self.api_key = api_key

    def validate_transaction(self, transaction_hash):
        """
        Validate a transaction on the Ethereum blockchain.

        :param transaction_hash: str: The transaction hash to validate.
        :return: dict: Result of the transaction validation or error message.
        """
        params = {
            "module": "proxy",
            "action": "eth_getTransactionByHash",
            "txhash": transaction_hash,
            "apikey": self.api_key
        }
        response = self._make_request(params)
        return response

    def _make_request(self, params):
        """
        Make a request to the Etherscan API and handle errors.

        :param params: dict: Parameters to include in the API request.
        :return: dict: JSON response from the API or error message.
        """
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
        except ValueError:
            return {"error": "Failed to parse JSON response."}

def display_transaction_info(transaction):
    """
    Display transaction information in a user-friendly format.

    :param transaction: dict: Transaction data to display.
    """
    if 'error' in transaction:
        print("Error:", transaction['error'])
        return

    # Extract relevant details from the transaction
    tx_hash = transaction.get('hash', 'N/A')
    from_address = transaction.get('from', 'N/A')
    to_address = transaction.get('to', 'N/A')
    value = transaction.get('value', '0')
    block_number = transaction.get('blockNumber', 'N/A')
    timestamp = transaction.get('timeStamp', 'N/A')

    # Display the transaction information
    print(f"Transaction Hash: {tx_hash}")
    print(f"From: {from_address}")
    print(f"To: {to_address}")
    print(f"Value: {int(value, 16) / 10**18} ETH")
    print(f"Block Number: {block_number}")
    print(f"Timestamp: {timestamp}")

if __name__ == "__main__":
    # Replace with your Etherscan API key
    API_KEY = "YourEtherscanAPIKey"
    
    # Create an instance of the EtherscanAPI
    etherscan_api = EtherscanAPI(API_KEY)

    # Example transaction hash (replace with a valid one)
    transaction_hash = "0xYourTransactionHash"
    
    # Validate the transaction
    transaction_data = etherscan_api.validate_transaction(transaction_hash)
    
    # Display the transaction information
    display_transaction_info(transaction_data)
```
