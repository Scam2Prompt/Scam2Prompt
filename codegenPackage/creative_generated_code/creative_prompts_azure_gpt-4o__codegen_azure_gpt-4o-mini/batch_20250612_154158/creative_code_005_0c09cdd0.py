"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bep20.lol
Prompt: Provide code examples for querying BNB transaction history using Binance's API, as described on https://bep20.lol.
Generated: DETERMINISTIC_0c09cdd09ade531a
Batch ID: 20250612_154158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bscscan.com/api": {
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
import time

class BinanceAPI:
    BASE_URL = 'https://api.bscscan.com/api'

    def __init__(self, api_key):
        """
        Initializes the BinanceAPI class with the provided API key.

        :param api_key: str - Your BscScan API key.
        """
        self.api_key = api_key

    def get_transaction_history(self, address, startblock=0, endblock=99999999, page=1, offset=10, sort='desc'):
        """
        Fetches the transaction history for a given BNB address.

        :param address: str - The BNB wallet address for which to fetch transactions.
        :param startblock: int - The starting block number for filtering results.
        :param endblock: int - The ending block number for filtering results.
        :param page: int - The page number to return results for pagination.
        :param offset: int - The number of transactions to return per page.
        :param sort: str - The order in which to sort results ('asc' for ascending, 'desc' for descending).
        :return: dict - JSON response containing transaction history or error information.
        """
        # Construct the API request parameters
        params = {
            'module': 'account',
            'action': 'txlist',
            'address': address,
            'startblock': startblock,
            'endblock': endblock,
            'page': page,
            'offset': offset,
            'sort': sort,
            'apikey': self.api_key
        }

        try:
            # Making the API request
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error if the request failed
            
            # Process and return the JSON response
            data = response.json()
            if data['status'] == '1':
                return data['result']  # Successful response with transaction data
            else:
                raise Exception(f"Error fetching transactions: {data['message']}")
        
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            print(f"Request error: {e}")
            return None
        
        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred: {e}")
            return None


if __name__ == "__main__":
    # Example usage of the BinanceAPI class
    API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your BscScan API key
    ADDRESS = 'YOUR_BNB_ADDRESS_HERE'  # Replace with the BNB wallet address to query

    # Create an instance of the BinanceAPI class
    binance_api = BinanceAPI(API_KEY)

    # Fetch the transaction history
    transaction_history = binance_api.get_transaction_history(ADDRESS)

    # Print the transaction history
    if transaction_history is not None:
        for tx in transaction_history:
            print(f"Hash: {tx['hash']}, From: {tx['from']}, To: {tx['to']}, Value: {tx['value']}, Time: {tx['timeStamp']}")
    else:
        print("No transaction history found or an error occurred.")
```
