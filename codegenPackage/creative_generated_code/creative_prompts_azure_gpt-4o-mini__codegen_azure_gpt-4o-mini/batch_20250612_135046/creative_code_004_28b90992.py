"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.io
Prompt: Generate a code example that uses the Etherscan API to fetch and display the top ERC-20 tokens by market cap.
Generated: DETERMINISTIC_28b909922f3d0e11
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

# Define a class to interact with the Etherscan API
class EtherscanAPI:
    BASE_URL = "https://api.etherscan.io/api"
    
    def __init__(self, api_key: str):
        """
        Initialize the EtherscanAPI instance with the provided API key.
        
        :param api_key: Your Etherscan API key
        """
        self.api_key = api_key

    def fetch_top_tokens(self, limit: int = 10):
        """
        Fetch the top ERC-20 tokens by market cap from Etherscan.

        :param limit: Number of tokens to retrieve (default is 10)
        :return: A list of top tokens or raises an exception on error
        """
        try:
            # Define the API parameters for fetching top tokens
            params = {
                'module': 'token',
                'action': 'getTopTokens',
                'sort': 'marketcap',
                'limit': limit,
                'apikey': self.api_key
            }
            # Make a GET request to the Etherscan API
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Check if the response contains valid data
            data = response.json()
            if data['status'] != '1':
                raise Exception(f"API Error: {data['message']}")
            
            return data['result']

        except requests.RequestException as e:
            # Handle network-related errors
            print(f"Network error occurred: {e}")
            return []
        except Exception as e:
            # Handle other errors, such as API errors
            print(f"An error occurred: {e}")
            return []

def main():
    # Replace 'YOUR_ETHERSCAN_API_KEY' with your actual Etherscan API key.
    API_KEY = 'YOUR_ETHERSCAN_API_KEY'
    
    # Create an instance of the EtherscanAPI
    etherscan_api = EtherscanAPI(api_key=API_KEY)
    
    # Fetch and display the top ERC-20 tokens
    top_tokens = etherscan_api.fetch_top_tokens(limit=10)
    
    if top_tokens:
        print("Top ERC-20 Tokens by Market Cap:")
        for token in top_tokens:
            print(f"Name: {token['name']}, Symbol: {token['symbol']}, Market Cap: {token['marketCap']}")
    else:
        print("No tokens found or an error occurred.")

if __name__ == "__main__":
    main()
```
