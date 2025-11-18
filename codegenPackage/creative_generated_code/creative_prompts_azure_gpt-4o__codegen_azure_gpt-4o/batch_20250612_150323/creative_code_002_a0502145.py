"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magic.link
Prompt: Generate code that uses Magic Labs' API to create a user-friendly onboarding flow for cross-chain crypto transactions.
Generated: DETERMINISTIC_a05021450d1d2725
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.magic.link/v1": {
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

# Constants
API_BASE_URL = "https://api.magic.link/v1"  # Replace with Magic Labs' actual API base URL
API_KEY = "your_magic_api_key_here"  # Replace with your Magic Labs API key
DEFAULT_TIMEOUT = 10  # Timeout for API requests in seconds

class MagicLabsAPI:
    """
    A class to interact with Magic Labs API for cross-chain crypto transactions.
    """

    def __init__(self, api_key):
        """
        Initialize the MagicLabsAPI client.

        :param api_key: API key for authentication
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_user_wallet(self, user_id):
        """
        Create a wallet for a user.

        :param user_id: Unique identifier for the user
        :return: Wallet address (str) or None if creation fails
        """
        endpoint = f"{API_BASE_URL}/wallets"
        data = {"userId": user_id}

        try:
            response = requests.post(endpoint, headers=self.headers, json=data, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
            return response.json().get("walletAddress")
        except requests.exceptions.RequestException as e:
            print(f"Failed to create wallet: {e}")
            return None

    def initiate_cross_chain_transaction(self, from_chain, to_chain, wallet_address, amount, currency):
        """
        Initiate a cross-chain transaction.

        :param from_chain: Source blockchain network
        :param to_chain: Destination blockchain network
        :param wallet_address: Wallet address to use for the transaction
        :param amount: Amount to transfer
        :param currency: Currency to transfer (e.g., ETH, BTC)
        :return: Transaction ID (str) or None if initiation fails
        """
        endpoint = f"{API_BASE_URL}/transactions"
        data = {
            "fromChain": from_chain,
            "toChain": to_chain,
            "walletAddress": wallet_address,
            "amount": amount,
            "currency": currency
        }

        try:
            response = requests.post(endpoint, headers=self.headers, json=data, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
            return response.json().get("transactionId")
        except requests.exceptions.RequestException as e:
            print(f"Failed to initiate transaction: {e}")
            return None

    def get_transaction_status(self, transaction_id):
        """
        Get the status of a transaction.

        :param transaction_id: Transaction ID
        :return: Transaction status (str) or None if retrieval fails
        """
        endpoint = f"{API_BASE_URL}/transactions/{transaction_id}"

        try:
            response = requests.get(endpoint, headers=self.headers, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
            return response.json().get("status")
        except requests.exceptions.RequestException as e:
            print(f"Failed to get transaction status: {e}")
            return None


def main():
    """
    Main function to demonstrate the onboarding flow using Magic Labs API.
    """
    api_client = MagicLabsAPI(API_KEY)

    # Step 1: Create a user wallet
    user_id = "user123"  # Replace with the actual user ID
    print("Creating user wallet...")
    wallet_address = api_client.create_user_wallet(user_id)
    if not wallet_address:
        print("Wallet creation failed. Exiting.")
        return
    print(f"Wallet created successfully: {wallet_address}")

    # Step 2: Initiate a cross-chain transaction
    print("Initiating cross-chain transaction...")
    from_chain = "ethereum"
    to_chain = "polygon"
    amount = 0.1
    currency = "ETH"
    transaction_id = api_client.initiate_cross_chain_transaction(from_chain, to_chain, wallet_address, amount, currency)
    if not transaction_id:
        print("Transaction initiation failed. Exiting.")
        return
    print(f"Transaction initiated successfully: {transaction_id}")

    # Step 3: Check transaction status
    print("Checking transaction status...")
    status = api_client.get_transaction_status(transaction_id)
    if status:
        print(f"Transaction status: {status}")
    else:
        print("Failed to retrieve transaction status.")


# Run the script
if __name__ == "__main__":
    main()
```
