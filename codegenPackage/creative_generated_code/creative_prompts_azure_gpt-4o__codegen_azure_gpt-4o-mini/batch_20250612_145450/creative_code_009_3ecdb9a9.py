"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://approvalscan.com
Prompt: Using the Etherscan API, create a program to filter and display transactions involving a specific smart contract address.
Generated: DETERMINISTIC_3ecdb9a91348c727
Batch ID: 20250612_145450
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
    A class to interact with the Etherscan API.
    """

    def __init__(self, api_key: str):
        """
        Initializes the EtherscanAPI with the provided API key.

        :param api_key: Etherscan API key
        """
        self.base_url = "https://api.etherscan.io/api"
        self.api_key = api_key

    def get_transactions_by_contract(self, contract_address: str, start_block: int = 0, end_block: int = 99999999, page: int = 1, offset: int = 100):
        """
        Retrieves transactions involving a specific smart contract address.

        :param contract_address: The smart contract address to filter transactions by
        :param start_block: The starting block number (default is 0)
        :param end_block: The ending block number (default is latest block)
        :param page: The page number for pagination (default is 1)
        :param offset: The number of results per page (default is 100)
        :return: A list of transactions involving the specified contract address
        """
        params = {
            'module': 'account',
            'action': 'txlist',
            'address': contract_address,
            'startblock': start_block,
            'endblock': end_block,
            'sort': 'desc',
            'page': page,
            'offset': offset,
            'apikey': self.api_key
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == '1':
                return data['result']
            else:
                raise ValueError(f"Error fetching data: {data['message']}")
        else:
            response.raise_for_status()


def main():
    # Replace 'YOUR_ETHERSCAN_API_KEY' with your actual Etherscan API key
    api_key = 'YOUR_ETHERSCAN_API_KEY'
    contract_address = '0xYourSmartContractAddressHere'  # Replace with the desired smart contract address

    etherscan = EtherscanAPI(api_key)

    try:
        transactions = etherscan.get_transactions_by_contract(contract_address)
        if transactions:
            print(f"Transactions for contract {contract_address}:")
            for tx in transactions:
                print(f"Tx Hash: {tx['hash']}, Block: {tx['blockNumber']}, From: {tx['from']}, To: {tx['to']}, Value: {tx['value']}")
        else:
            print("No transactions found for this contract.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
