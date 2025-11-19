"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myetherwallet.com
Prompt: Create a guide for using MyEtherWallet's blockchain explorer to track and analyze Ethereum transactions.
Generated: DETERMINISTIC_be5a20aa5c7435c8
Batch ID: 20250612_135046
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.myetherwallet.com/v2/": {
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

class EthereumExplorer:
    """
    A class to interact with the MyEtherWallet (MEW) blockchain explorer API
    for tracking and analyzing Ethereum transactions.
    """

    BASE_URL = 'https://api.myetherwallet.com/v2/'

    def __init__(self):
        """
        Initializes the EthereumExplorer with the base URL.
        """
        pass

    def get_transaction_details(self, tx_hash):
        """
        Retrieves transaction details based on the transaction hash.

        Parameters:
            tx_hash (str): The hash of the Ethereum transaction.

        Returns:
            dict: A dictionary containing transaction details.

        Raises:
            ValueError: If the transaction hash is invalid.
            Exception: For any other errors during the API call.
        """
        if not self.is_valid_tx_hash(tx_hash):
            raise ValueError("Invalid transaction hash provided.")

        url = f"{self.BASE_URL}transaction/{tx_hash}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching transaction details: {e}")

    @staticmethod
    def is_valid_tx_hash(tx_hash):
        """
        Validates the Ethereum transaction hash format.

        Parameters:
            tx_hash (str): The transaction hash to validate.

        Returns:
            bool: True if valid, otherwise False.
        """
        # Ethereum transaction hashes are 66 characters long (including '0x')
        return isinstance(tx_hash, str) and len(tx_hash) == 66 and tx_hash.startswith('0x')

if __name__ == "__main__":
    explorer = EthereumExplorer()

    # Example usage: Replace with a valid transaction hash
    tx_hash = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
    
    try:
        transaction_details = explorer.get_transaction_details(tx_hash)
        print("Transaction Details:")
        print(transaction_details)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
