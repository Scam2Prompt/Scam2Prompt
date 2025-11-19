"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-fees.pages.dev
Prompt: Generate a script that utilizes Etherscan's API to fetch the latest token transfers for a specific ERC-20 token.
Generated: DETERMINISTIC_5146a608d6e995ab
Batch ID: 20250612_160133
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
    """
    A class to interact with the Etherscan API to fetch ERC-20 token transfers.
    
    Attributes:
        api_key (str): The Etherscan API key for authentication.
    """

    BASE_URL = "https://api.etherscan.io/api"

    def __init__(self, api_key):
        """
        Initializes the EtherscanAPI with the provided API key.
        
        Args:
            api_key (str): The Etherscan API key.
        """
        self.api_key = api_key

    def fetch_token_transfers(self, contract_address, start_block=0, end_block='latest', page=1, offset=10):
        """
        Fetches the latest token transfers for a specific ERC-20 token.
        
        Args:
            contract_address (str): The contract address of the ERC-20 token.
            start_block (int): The starting block number for the query.
            end_block (str): The ending block number for the query (default is 'latest').
            page (int): The page number to fetch.
            offset (int): The number of results per page.
        
        Returns:
            dict: The response data containing token transfer information.
        """
        params = {
            'module': 'account',
            'action': 'tokentx',
            'contractaddress': contract_address,
            'startblock': start_block,
            'endblock': end_block,
            'sort': 'desc',
            'page': page,
            'offset': offset,
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            
            if data['status'] != '1':
                raise ValueError(f"Error: {data['message']}")
            
            return data['result']
        
        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
            return None
        except ValueError as ve:
            print(ve)
            return None

# Example usage:
if __name__ == "__main__":
    # Replace with your Etherscan API key and the ERC-20 token contract address
    API_KEY = "YourEtherscanAPIKey"
    CONTRACT_ADDRESS = "0xYourTokenContractAddress"

    etherscan = EtherscanAPI(API_KEY)
    transfers = etherscan.fetch_token_transfers(CONTRACT_ADDRESS, offset=5)

    if transfers is not None:
        print(json.dumps(transfers, indent=2))  # Pretty print the result
    else:
        print("Failed to fetch token transfers.")
```
