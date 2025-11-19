"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Explain how to use Etherscan's advanced filter options to find specific transactions on the Ethereum blockchain.
Generated: DETERMINISTIC_bcfbfe0693967880
Batch ID: 20250612_135046
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
    """
    A class to interact with the Etherscan API to filter and retrieve Ethereum blockchain transactions.
    """

    BASE_URL = 'https://api.etherscan.io/api'

    def __init__(self, api_key):
        """
        Initializes the EtherscanAPI with the provided API key.

        :param api_key: str - Your Etherscan API key.
        """
        self.api_key = api_key

    def get_transactions(self, address, start_block=0, end_block=99999999, 
                         sort='asc', page=1, offset=10):
        """
        Retrieves transactions for a given address with advanced filter options.

        :param address: str - The Ethereum address to query.
        :param start_block: int - The starting block number (default is 0).
        :param end_block: int - The ending block number (default is the latest block).
        :param sort: str - Sorting order ('asc' or 'desc', default is 'asc').
        :param page: int - The page number for pagination (default is 1).
        :param offset: int - Number of transactions to return per page (default is 10).
        :return: dict - JSON response containing the transaction data.
        """
        # Prepare the parameters for the API request
        params = {
            'module': 'account',
            'action': 'txlist',
            'address': address,
            'startblock': start_block,
            'endblock': end_block,
            'sort': sort,
            'page': page,
            'offset': offset,
            'apikey': self.api_key
        }

        try:
            # Make the API request
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Check for API errors
            if data['status'] != '1':
                raise Exception(f"Error fetching data: {data['message']}")

            return data['result']

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


if __name__ == "__main__":
    # Example usage of EtherscanAPI class

    # Replace 'YOUR_API_KEY' with your actual Etherscan API key
    etherscan_api = EtherscanAPI(api_key='YOUR_API_KEY')

    # Replace 'YOUR_ETHEREUM_ADDRESS' with the address you want to query
    transactions = etherscan_api.get_transactions(address='YOUR_ETHEREUM_ADDRESS')

    if transactions:
        print("Transactions retrieved:")
        for tx in transactions:
            print(f"Hash: {tx['hash']}, Block: {tx['blockNumber']}, Value: {tx['value']}")
    else:
        print("No transactions found or an error occurred.")
```
