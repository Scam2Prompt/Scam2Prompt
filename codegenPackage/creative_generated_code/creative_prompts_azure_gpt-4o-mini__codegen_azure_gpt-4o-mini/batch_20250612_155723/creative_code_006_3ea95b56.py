"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicslabs.pages.dev
Prompt: Create an example of a transaction on Sonic that demonstrates its sub-second confirmation time and low transaction costs.
Generated: DETERMINISTIC_3ea95b56d4f02e77
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class SonicTransaction:
    def __init__(self, sender, recipient, amount):
        """
        Initialize a transaction with sender, recipient, and amount.

        :param sender: The address of the sender
        :param recipient: The address of the recipient
        :param amount: The amount to be transferred
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.transaction_id = self.generate_transaction_id()
        self.timestamp = None

    @staticmethod
    def generate_transaction_id():
        """
        Generate a unique transaction ID.

        :return: A unique identifier for the transaction
        """
        return f"txn_{random.randint(100000, 999999)}"

    def process_transaction(self):
        """
        Simulate the processing of the transaction with sub-second confirmation.

        :return: A confirmation message or error message
        """
        try:
            # Start the timer for transaction processing
            start_time = time.time()

            # Simulate a network call to process the transaction
            self.timestamp = time.time()
            time.sleep(random.uniform(0.01, 0.5))  # Simulate network latency

            # Check for successful transaction
            if self.amount <= 0:
                raise ValueError("Transaction amount must be greater than zero.")

            confirmation_time = time.time() - start_time
            confirmation_message = (
                f"Transaction ID: {self.transaction_id} processed in "
                f"{confirmation_time:.3f} seconds. Amount: {self.amount} from "
                f"{self.sender} to {self.recipient}."
            )
            return confirmation_message
        except Exception as e:
            return f"Error processing transaction: {str(e)}"


if __name__ == "__main__":
    # Example usage of the SonicTransaction class
    sender_address = "sender12345"
    recipient_address = "recipient67890"
    transaction_amount = 100.0  # Amount to be sent

    # Create a transaction instance
    transaction = SonicTransaction(sender_address, recipient_address, transaction_amount)

    # Process the transaction and print the confirmation message
    confirmation = transaction.process_transaction()
    print(confirmation)
```
