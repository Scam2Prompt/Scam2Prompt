"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrett.on-fleek.app
Prompt: Provide a step-by-step guide for using the Base Chain API to query $Brett token data, including its current price and transaction history.
Generated: DETERMINISTIC_46fe59ad96b92c52
Batch ID: 20250612_153954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.basechain.com/v1": {
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

class BrettTokenAPI:
    """
    A class to interact with the Base Chain API to query $Brett token data.
    """

    BASE_URL = "https://api.basechain.com/v1"  # Base URL for the API
    TOKEN_SYMBOL = "Brett"                      # Token symbol for $Brett

    def __init__(self):
        """
        Initializes the BrettTokenAPI instance.
        """
        pass

    def fetch_current_price(self):
        """
        Fetches the current price of the $Brett token.

        Returns:
            float: The current price of the $Brett token.
            None: If the API call fails or returns an error.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/tokens/{self.TOKEN_SYMBOL}/price")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data.get("current_price")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching current price: {e}")
            return None

    def fetch_transaction_history(self, wallet_address):
        """
        Fetches the transaction history for a specific wallet address.

        Args:
            wallet_address (str): The wallet address to query.

        Returns:
            list: A list of transactions for the wallet address.
            None: If the API call fails or returns an error.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/tokens/{self.TOKEN_SYMBOL}/transactions/{wallet_address}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data.get("transactions", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching transaction history: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    api = BrettTokenAPI()

    # Fetch current price of $Brett token
    current_price = api.fetch_current_price()
    if current_price is not None:
        print(f"Current price of $Brett: ${current_price}")

    # Fetch transaction history for a specific wallet address
    wallet_address = "0xYourWalletAddressHere"  # Replace with a valid wallet address
    transaction_history = api.fetch_transaction_history(wallet_address)
    if transaction_history is not None:
        print(f"Transaction history for wallet {wallet_address}:")
        for transaction in transaction_history:
            print(transaction)
```
