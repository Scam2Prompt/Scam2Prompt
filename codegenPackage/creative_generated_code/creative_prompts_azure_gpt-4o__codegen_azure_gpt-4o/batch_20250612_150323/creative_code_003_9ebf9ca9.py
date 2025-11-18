"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-mixer-tron.com
Prompt: Implement a feature in a blockchain application that allows users to set a custom mixing fee to prevent amount-based blockchain analysis, as recommended by the USDT TRON mixer.
Generated: DETERMINISTIC_9ebf9ca94879281c
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import random
import json

class BlockchainMixer:
    """
    A class to represent a blockchain mixing service.
    Allows users to set a custom mixing fee to enhance privacy.
    """

    def __init__(self, base_fee_percentage=0.5):
        """
        Initialize the BlockchainMixer instance with a default base fee.

        :param base_fee_percentage: Default fee percentage (e.g., 0.5%)
        """
        self.base_fee_percentage = base_fee_percentage
        self.transactions = []

    def set_custom_fee(self, percentage):
        """
        Set a custom mixing fee percentage.

        :param percentage: Custom fee percentage (must be between 0.1 and 5.0)
        :raises ValueError: If the percentage is not within the valid range.
        """
        if not (0.1 <= percentage <= 5.0):
            raise ValueError("Fee percentage must be between 0.1 and 5.0")
        self.base_fee_percentage = percentage

    def mix_funds(self, sender, recipient, amount):
        """
        Mix funds between sender and recipient with the applied fee.

        :param sender: Sender's wallet address.
        :param recipient: Recipient's wallet address.
        :param amount: Amount to be mixed.
        :return: A dictionary representing the mixed transaction.
        :raises ValueError: If the amount is less than or equal to 0.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        # Calculate the fee based on the custom or default percentage
        fee = amount * (self.base_fee_percentage / 100)
        mixed_amount = amount - fee

        if mixed_amount <= 0:
            raise ValueError("Amount after fee deduction must be greater than 0")

        # Generate a transaction ID
        transaction_id = hashlib.sha256(f"{sender}{recipient}{amount}{random.randint(1, 1000000)}".encode()).hexdigest()

        transaction = {
            "transaction_id": transaction_id,
            "sender": sender,
            "recipient": recipient,
            "original_amount": amount,
            "fee_percentage": self.base_fee_percentage,
            "fee_amount": fee,
            "mixed_amount": mixed_amount
        }

        # Save the transaction to the history
        self.transactions.append(transaction)
        return transaction

    def get_transaction_history(self):
        """
        Retrieve the list of all transactions processed by the mixer.

        :return: List of transactions.
        """
        return self.transactions

    def save_transaction_history_to_file(self, file_path):
        """
        Save the transaction history to a file in JSON format.

        :param file_path: Path to the file where the history will be saved.
        :raises IOError: If the file cannot be written.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.transactions, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving transaction history to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the mixer
        mixer = BlockchainMixer()

        # Set a custom fee
        mixer.set_custom_fee(1.0)  # 1% fee

        # Perform a mix operation
        transaction = mixer.mix_funds("sender_address_123", "recipient_address_456", 100)
        print("Transaction:", transaction)

        # Retrieve and display transaction history
        history = mixer.get_transaction_history()
        print("Transaction History:", history)

        # Save transaction history to a file
        mixer.save_transaction_history_to_file("transaction_history.json")
        print("Transaction history saved to file.")
    except Exception as e:
        print(f"Error: {e}")
```
