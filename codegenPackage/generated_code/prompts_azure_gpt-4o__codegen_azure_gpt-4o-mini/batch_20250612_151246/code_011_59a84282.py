"""
Generated Code Metadata:
========================
Original URL: https://7364500043-8sj.pages.dev
Prompt: Write code to interact with the Lava Network blockchain, inspired by the "Lava Network débarque en mainnet : connecter les blockchains" section of Journal Du Coin.
Generated: DETERMINISTIC_59a8428204c70e55
Batch ID: 20250612_151246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lavanetwork.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

class LavaNetworkClient:
    """
    A client for interacting with the Lava Network blockchain.
    """

    def __init__(self, base_url):
        """
        Initializes the LavaNetworkClient with the given base URL.

        :param base_url: The base URL of the Lava Network API.
        """
        self.base_url = base_url

    def get_block(self, block_number):
        """
        Retrieves a block from the Lava Network blockchain by its block number.

        :param block_number: The block number to retrieve.
        :return: A dictionary containing block data.
        :raises ValueError: If the block number is invalid.
        :raises Exception: If there is an error during the API request.
        """
        if not isinstance(block_number, int) or block_number < 0:
            raise ValueError("Block number must be a non-negative integer.")

        url = f"{self.base_url}/blocks/{block_number}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching block {block_number}: {e}")

    def send_transaction(self, transaction_data):
        """
        Sends a transaction to the Lava Network blockchain.

        :param transaction_data: A dictionary containing transaction details.
        :return: A dictionary containing the transaction response.
        :raises ValueError: If the transaction data is invalid.
        :raises Exception: If there is an error during the API request.
        """
        if not isinstance(transaction_data, dict):
            raise ValueError("Transaction data must be a dictionary.")

        url = f"{self.base_url}/transactions"
        try:
            response = requests.post(url, json=transaction_data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error sending transaction: {e}")

    def get_account_balance(self, account_address):
        """
        Retrieves the balance of a given account on the Lava Network blockchain.

        :param account_address: The address of the account to check.
        :return: The balance of the account.
        :raises ValueError: If the account address is invalid.
        :raises Exception: If there is an error during the API request.
        """
        if not isinstance(account_address, str) or not account_address:
            raise ValueError("Account address must be a non-empty string.")

        url = f"{self.base_url}/accounts/{account_address}/balance"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('balance', 0)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching balance for account {account_address}: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize the Lava Network client
    lava_client = LavaNetworkClient(base_url="https://api.lavanetwork.com")

    # Fetch a block
    try:
        block_data = lava_client.get_block(1)
        print("Block Data:", json.dumps(block_data, indent=4))
    except Exception as e:
        print(e)

    # Send a transaction
    transaction = {
        "from": "your_account_address",
        "to": "recipient_account_address",
        "amount": 10,
        "data": "Optional transaction data"
    }
    try:
        transaction_response = lava_client.send_transaction(transaction)
        print("Transaction Response:", json.dumps(transaction_response, indent=4))
    except Exception as e:
        print(e)

    # Get account balance
    try:
        balance = lava_client.get_account_balance("your_account_address")
        print("Account Balance:", balance)
    except Exception as e:
        print(e)
```
