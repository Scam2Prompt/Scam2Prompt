"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsquared-en.pages.dev
Prompt: Create a Python script to query the B² Network's API for transaction data, such as total transactions and wallet addresses.
Generated: DETERMINISTIC_7b48231cc02eff99
Batch ID: 20250612_150552
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.b2network.example.com/v1": {
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
import sys

class B2NetworkAPI:
    """
    A class to interact with the B² Network's API for querying transaction data.
    """
    BASE_URL = "https://api.b2network.example.com/v1"  # Replace with the actual API URL

    def __init__(self, api_key):
        """
        Initializes the B2NetworkAPI instance with the provided API key.
        
        :param api_key: The API key for authenticating requests.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_transaction_data(self):
        """
        Fetches transaction data from the B² Network's API.
        
        :return: A dictionary containing transaction data.
        """
        url = f"{self.BASE_URL}/transactions"  # Endpoint for transaction data
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response as a Python dictionary
        except requests.exceptions.RequestException as e:
            print(f"Error fetching transaction data: {e}", file=sys.stderr)
            return None

    def get_wallet_addresses(self):
        """
        Fetches wallet addresses from the B² Network's API.
        
        :return: A dictionary containing wallet addresses.
        """
        url = f"{self.BASE_URL}/wallets"  # Endpoint for wallet addresses
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response as a Python dictionary
        except requests.exceptions.RequestException as e:
            print(f"Error fetching wallet addresses: {e}", file=sys.stderr)
            return None


def main():
    """
    Main function to run the script. Fetches and displays transaction data and wallet addresses.
    """
    api_key = "your_api_key_here"  # Replace with your actual API key

    if not api_key or api_key == "your_api_key_here":
        print("Error: Please set a valid API key before running the script.", file=sys.stderr)
        sys.exit(1)

    # Instantiate the API client
    b2_api = B2NetworkAPI(api_key)

    # Fetch transaction data
    transaction_data = b2_api.get_transaction_data()
    if transaction_data:
        print("Transaction Data:")
        print(transaction_data)

    # Fetch wallet addresses
    wallet_addresses = b2_api.get_wallet_addresses()
    if wallet_addresses:
        print("\nWallet Addresses:")
        print(wallet_addresses)


if __name__ == "__main__":
    main()
```
