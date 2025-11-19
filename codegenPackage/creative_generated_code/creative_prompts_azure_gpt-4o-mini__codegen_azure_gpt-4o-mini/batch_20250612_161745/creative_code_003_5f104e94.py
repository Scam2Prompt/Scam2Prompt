"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mellotoken.com
Prompt: Create a sample API request to retrieve Mello Token transaction data from BscScan using its contract address.
Generated: DETERMINISTIC_5f104e940c6e0a69
Batch ID: 20250612_161745
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

class BscScanAPI:
    """
    A class to interact with the BscScan API to retrieve token transaction data.
    """
    BASE_URL = 'https://api.bscscan.com/api'

    def __init__(self, api_key):
        """
        Initializes the BscScanAPI with the provided API key.

        :param api_key: BscScan API key for authentication.
        """
        self.api_key = api_key

    def get_token_transactions(self, contract_address, start_block=0, end_block='latest', page=1, offset=10):
        """
        Retrieves the transaction data for a specific token contract.

        :param contract_address: The contract address of the token.
        :param start_block: The starting block number (Default is 0).
        :param end_block: The ending block number (Default is 'latest').
        :param page: Page number for paginated results (Default is 1).
        :param offset: Number of results per page (Default is 10).
        
        :return: JSON response containing transaction data.
        :raises ValueError: If the contract address is invalid.
        :raises Exception: If the API request fails or returns an error.
        """
        if not self._is_valid_address(contract_address):
            raise ValueError(f"Invalid contract address: {contract_address}")

        params = {
            'module': 'account',
            'action': 'tokentx',
            'contractaddress': contract_address,
            'startblock': start_block,
            'endblock': end_block,
            'page': page,
            'offset': offset,
            'apikey': self.api_key
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            raise Exception(f"API request failed with status code: {response.status_code}")

        data = response.json()

        if data['status'] != '1':
            raise Exception(f"API returned an error: {data['message']}")

        return data['result']

    @staticmethod
    def _is_valid_address(address):
        """
        Validates the contract address format.

        :param address: The address to validate.
        :return: True if valid, False otherwise.
        """
        return len(address) == 42 and address.startswith('0x')


# Example usage
if __name__ == "__main__":
    API_KEY = 'Your_BscScan_API_Key'  # Replace with your actual BscScan API key
    CONTRACT_ADDRESS = '0xYourContractAddress'  # Replace with the Mello Token contract address

    # Create an instance of BscScanAPI
    api = BscScanAPI(API_KEY)

    try:
        # Retrieve token transactions
        transactions = api.get_token_transactions(CONTRACT_ADDRESS)
        print(transactions)
    except Exception as e:
        print(f"An error occurred: {e}")
```
