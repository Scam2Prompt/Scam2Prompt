"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x1blockdag.pages.dev
Prompt: Develop a command line tool that allows users to connect to the BlockDAG network and perform basic transactions.
Generated: DETERMINISTIC_bf1f791214b849c5
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import requests
import json

class BlockDAGClient:
    """
    A class to interact with the BlockDAG network for performing basic transactions.
    """

    def __init__(self, base_url):
        """
        Initializes the BlockDAGClient with the given base URL.

        :param base_url: The base URL of the BlockDAG network API.
        """
        self.base_url = base_url

    def send_transaction(self, sender, receiver, amount):
        """
        Sends a transaction from the sender to the receiver with the specified amount.

        :param sender: The sender's address.
        :param receiver: The receiver's address.
        :param amount: The amount to send.
        :return: Response from the BlockDAG network.
        """
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }

        try:
            response = requests.post(f"{self.base_url}/transactions", json=transaction)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending transaction: {e}")
            return None

    def get_balance(self, address):
        """
        Retrieves the balance of the given address.

        :param address: The address to check the balance for.
        :return: Balance of the address.
        """
        try:
            response = requests.get(f"{self.base_url}/balance/{address}")
            response.raise_for_status()
            return response.json().get("balance", 0)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching balance: {e}")
            return None

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='BlockDAG Command Line Tool')
    parser.add_argument('--base-url', required=True, help='Base URL of the BlockDAG network API')
    parser.add_argument('--send', nargs=3, metavar=('SENDER', 'RECEIVER', 'AMOUNT'),
                        help='Send a transaction from SENDER to RECEIVER with AMOUNT')
    parser.add_argument('--balance', metavar='ADDRESS', help='Get the balance of ADDRESS')

    args = parser.parse_args()

    client = BlockDAGClient(args.base_url)

    # Handle sending a transaction
    if args.send:
        sender, receiver, amount = args.send
        try:
            amount = float(amount)  # Ensure amount is a float
            transaction_response = client.send_transaction(sender, receiver, amount)
            print("Transaction Response:", transaction_response)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Handle checking balance
    if args.balance:
        balance = client.get_balance(args.balance)
        print(f"Balance for {args.balance}: {balance}")

if __name__ == "__main__":
    main()
```
