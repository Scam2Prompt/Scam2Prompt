"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.pages.dev
Prompt: Create a script to query Multichain's Explorer API to fetch transaction details for a specific wallet address across multiple chains.
Generated: DETERMINISTIC_cf68b49efcc694d2
Batch ID: 20250612_151117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multichain.xyz": {
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

class MultichainExplorer:
    """
    A class to interact with the Multichain Explorer API to fetch transaction details for a specific wallet address.

    Attributes:
        base_url (str): The base URL for the Multichain Explorer API.
    """

    def __init__(self, base_url):
        """
        Initializes the MultichainExplorer with the base URL.

        Args:
            base_url (str): The base URL for the Multichain Explorer API.
        """
        self.base_url = base_url

    def fetch_transactions(self, wallet_address, chain):
        """
        Fetches transactions for a specific wallet address on a specified chain.

        Args:
            wallet_address (str): The wallet address to query.
            chain (str): The chain to query.

        Returns:
            dict: A dictionary containing transaction details.

        Raises:
            ValueError: If wallet_address is invalid.
            Exception: For other errors during the API request.
        """
        if not self.is_valid_address(wallet_address):
            raise ValueError("Invalid wallet address format.")

        url = f"{self.base_url}/{chain}/address/{wallet_address}/transactions"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from Multichain API: {e}")

    @staticmethod
    def is_valid_address(address):
        """
        Validates the format of the wallet address.

        Args:
            address (str): The wallet address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Simple placeholder validation (this should be improved based on the specific address format)
        return isinstance(address, str) and len(address) > 0

def main():
    # Define Multichain Explorer API base URL
    BASE_URL = "https://api.multichain.xyz"  # Example URL, replace with actual endpoint
    wallet_address = "your_wallet_address_here"  # Replace with actual wallet address to query
    chains = ["chain1", "chain2", "chain3"]  # Replace with actual chain names to query

    explorer = MultichainExplorer(BASE_URL)

    for chain in chains:
        try:
            transactions = explorer.fetch_transactions(wallet_address, chain)
            print(f"Transactions for {wallet_address} on {chain}:")
            print(json.dumps(transactions, indent=2))
        except Exception as e:
            print(f"Failed to fetch transactions for {wallet_address} on {chain}: {e}")

if __name__ == "__main__":
    main()
```
