"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kima-cmn.pages.dev
Prompt: Write a script using Kima's SDK to create a universal wallet that supports transactions across multiple blockchains without relying on oracles or multi-sigs.
Generated: DETERMINISTIC_ddf7c92bab4221f1
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from Kima's SDK
from kima_sdk import Kima

# Define a class for managing a universal wallet
class UniversalWallet:
    def __init__(self, user_id):
        """
        Initialize the Universal Wallet for the given user.

        :param user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.wallet = Kima.create_wallet(user_id)
        self.supported_blockchains = ['Ethereum', 'Bitcoin', 'Binance Smart Chain', 'Polygon']

    def check_blockchain_support(self, blockchain):
        """
        Check if the specified blockchain is supported.

        :param blockchain: The blockchain to check for support
        :return: Boolean indicating support status
        """
        if blockchain in self.supported_blockchains:
            return True
        return False

    def perform_transaction(self, blockchain, recipient_address, amount):
        """
        Execute a transaction on the specified blockchain.

        :param blockchain: The blockchain to perform the transaction on
        :param recipient_address: The recipient's address
        :param amount: The amount to send
        :raises ValueError: If the blockchain is not supported or amount is non-positive
        :return: Transaction receipt
        """
        if not self.check_blockchain_support(blockchain):
            raise ValueError(f"Blockchain '{blockchain}' is not supported.")

        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")

        try:
            # Execute the transaction using Kima's SDK
            transaction_receipt = Kima.send_transaction(
                wallet=self.wallet,
                blockchain=blockchain,
                to=recipient_address,
                value=amount
            )
            return transaction_receipt
        except Exception as e:
            # Log the error and raise it for further handling
            print(f"Error occurred during transaction: {e}")
            raise

    def get_wallet_balance(self, blockchain):
        """
        Retrieve the wallet balance for the specified blockchain.

        :param blockchain: The blockchain to check the balance for
        :raises ValueError: If the blockchain is not supported
        :return: Balance amount
        """
        if not self.check_blockchain_support(blockchain):
            raise ValueError(f"Blockchain '{blockchain}' is not supported.")
        
        try:
            balance = Kima.get_balance(self.wallet, blockchain)
            return balance
        except Exception as e:
            print(f"Error retrieving balance: {e}")
            raise

# Example of usage
if __name__ == "__main__":
    user_id = "user_12345"  # Example user ID
    wallet = UniversalWallet(user_id)

    # Perform a transaction
    try:
        transaction_receipt = wallet.perform_transaction('Ethereum', '0xRecipientAddress', 0.1)
        print(f"Transaction successful: {transaction_receipt}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Get wallet balance
    try:
        balance = wallet.get_wallet_balance('Ethereum')
        print(f"Ethereum Balance: {balance}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
