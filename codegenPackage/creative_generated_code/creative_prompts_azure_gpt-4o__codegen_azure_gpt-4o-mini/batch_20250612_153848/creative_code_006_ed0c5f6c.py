"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-explorer.com
Prompt: Create a Python script that uses the Etherscan API to identify and list all transactions involving a specific Ethereum token.
Generated: DETERMINISTIC_ed0c5f6c9b51eddb
Batch ID: 20250612_153848
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
import json

class EtherscanAPI:
    """A class to interact with the Etherscan API for Ethereum transactions."""

    BASE_URL = "https://api.etherscan.io/api"

    def __init__(self, api_key):
        """Initialize the EtherscanAPI with the provided API key.

        Args:
            api_key (str): Your Etherscan API key.
        """
        self.api_key = api_key

    def get_token_transactions(self, contract_address, address, start_block=0, end_block='latest'):
        """Fetch all transactions involving a specific Ethereum token.

        Args:
            contract_address (str): The token's contract address.
            address (str): The Ethereum address to check transactions for.
            start_block (int): The starting block number (default is 0).
            end_block (str): The ending block number (default is 'latest').

        Returns:
            list: A list of transactions involving the specified token, or an empty list if an error occurs.
        """
        try:
            params = {
                "module": "account",
                "action": "tokentx",
                "contractaddress": contract_address,
                "address": address,
                "startblock": start_block,
                "endblock": end_block,
                "sort": "asc",
                "apikey": self.api_key
            }
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if data['status'] == '1':
                return data['result']  # Return the list of transactions
            else:
                print(f"Error fetching transactions: {data['message']}")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Network error occurred: {str(e)}")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON response.")
            return []

def main():
    """Main function to execute the script."""
    ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'  # Replace with your Etherscan API key
    TOKEN_CONTRACT_ADDRESS = 'YOUR_TOKEN_CONTRACT_ADDRESS'  # Replace with the token's contract address
    ADDRESS = 'YOUR_ETHEREUM_ADDRESS'  # Replace with the Ethereum address to check

    # Create an instance of the EtherscanAPI
    etherscan_api = EtherscanAPI(ETHERSCAN_API_KEY)

    # Fetch token transactions
    transactions = etherscan_api.get_token_transactions(TOKEN_CONTRACT_ADDRESS, ADDRESS)

    if transactions:
        print(f"Transactions involving token at {TOKEN_CONTRACT_ADDRESS} for address {ADDRESS}:")
        for tx in transactions:
            print(f"Hash: {tx['hash']}, Block: {tx['blockNumber']}, Time: {tx['timeStamp']}, Value: {tx['value']}")
    else:
        print("No transactions found or an error occurred.")

if __name__ == "__main__":
    main()
```
