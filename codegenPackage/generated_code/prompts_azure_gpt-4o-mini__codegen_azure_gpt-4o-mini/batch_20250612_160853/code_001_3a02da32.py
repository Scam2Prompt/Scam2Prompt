"""
Generated Code Metadata:
========================
Original URL: https://bafybeia7hhfaanym5gb2qaa3v5kkaps2vnowe2tqf5r2pnfax6cxobgow4.ipfs.dweb.link
Prompt: Write a Python script that utilizes the Oasis Network's unique features for building applications as described in the content.
Generated: DETERMINISTIC_3a02da3247d6053b
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.oasis.dev": {
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

class OasisNetworkClient:
    """
    A client for interacting with the Oasis Network.
    This client provides methods to interact with the Oasis blockchain.
    """

    BASE_URL = "https://api.oasis.dev"  # Base URL for the Oasis Network API

    def __init__(self):
        """
        Initializes the OasisNetworkClient.
        """
        self.session = requests.Session()

    def get_account_balance(self, address):
        """
        Retrieves the balance of a given account address.

        :param address: The account address to check the balance for.
        :return: The balance of the account.
        :raises ValueError: If the address is invalid.
        :raises Exception: For any other errors during the API call.
        """
        if not self.is_valid_address(address):
            raise ValueError("Invalid address format.")

        endpoint = f"{self.BASE_URL}/account/{address}/balance"
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('balance', 0)
        except requests.RequestException as e:
            raise Exception(f"Error fetching balance: {e}")

    def is_valid_address(self, address):
        """
        Validates the format of the Oasis account address.

        :param address: The account address to validate.
        :return: True if valid, False otherwise.
        """
        # Basic validation for address format (length and character checks)
        return isinstance(address, str) and len(address) == 42 and address.startswith("oasis1")

    def send_transaction(self, from_address, to_address, amount):
        """
        Sends a transaction from one account to another.

        :param from_address: The sender's account address.
        :param to_address: The recipient's account address.
        :param amount: The amount to send.
        :return: Transaction ID if successful.
        :raises ValueError: If any address is invalid or amount is non-positive.
        :raises Exception: For any other errors during the API call.
        """
        if not self.is_valid_address(from_address) or not self.is_valid_address(to_address):
            raise ValueError("Invalid address format.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        transaction_data = {
            "from": from_address,
            "to": to_address,
            "amount": amount
        }

        endpoint = f"{self.BASE_URL}/transaction/send"
        try:
            response = self.session.post(endpoint, json=transaction_data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('transaction_id')
        except requests.RequestException as e:
            raise Exception(f"Error sending transaction: {e}")

if __name__ == "__main__":
    # Example usage of the OasisNetworkClient
    client = OasisNetworkClient()

    try:
        # Replace with actual addresses and amount
        sender_address = "oasis1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        recipient_address = "oasis1yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
        amount_to_send = 100

        # Get account balance
        balance = client.get_account_balance(sender_address)
        print(f"Balance of {sender_address}: {balance}")

        # Send transaction
        transaction_id = client.send_transaction(sender_address, recipient_address, amount_to_send)
        print(f"Transaction sent successfully. Transaction ID: {transaction_id}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
