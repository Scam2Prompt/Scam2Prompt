"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://approvalscan.com
Prompt: Write a Python script that utilizes the Etherscan API to fetch and display the top ERC-20 tokens based on transaction volume.
Generated: DETERMINISTIC_083fd9274c61e08c
Batch ID: 20250612_155436
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
    BASE_URL = "https://api.etherscan.io/api"

    def __init__(self, api_key):
        """
        Initializes the EtherscanAPI with the provided API key.

        :param api_key: str - Your Etherscan API key.
        """
        self.api_key = api_key

    def fetch_top_erc20_tokens(self, limit=10):
        """
        Fetches the top ERC-20 tokens based on transaction volume.

        :param limit: int - The number of tokens to fetch (default is 10).
        :return: list - A list of top ERC-20 tokens and their details.
        """
        params = {
            "module": "token",
            "action": "tokenlist",
            "sort": "transfers",
            "sortorder": "desc",
            "limit": limit,
            "apikey": self.api_key
        }
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if data['status'] != '1':
                raise ValueError("Error fetching data from Etherscan: " + data['message'])

            return data['result']
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the API request: {e}")
            return []
        except ValueError as ve:
            print(ve)
            return []

def display_tokens(tokens):
    """
    Displays the list of tokens in a readable format.

    :param tokens: list - A list of token data to display.
    """
    if not tokens:
        print("No tokens to display.")
        return

    print(f"{'Token Name':<30} {'Symbol':<10} {'Transaction Volume':<20}")
    print("=" * 70)
    for token in tokens:
        print(f"{token['name']:<30} {token['symbol']:<10} {token['transfers']:<20}")

def main():
    """
    Main entry point of the script.
    """
    API_KEY = "YourEtherscanAPIKeyHere"  # Replace with your Etherscan API key
    etherscan_api = EtherscanAPI(API_KEY)

    # Fetch the top ERC-20 tokens
    top_tokens = etherscan_api.fetch_top_erc20_tokens(limit=10)

    # Display the tokens
    display_tokens(top_tokens)

if __name__ == "__main__":
    main()
```
