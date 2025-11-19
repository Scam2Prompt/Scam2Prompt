"""
Generated Code Metadata:
========================
Original URL: https://mixbtc.online
Prompt: Generate a script that notifies users if they attempt to mix an amount less than the minimum required transaction size of 20 USD in a Bitcoin mixing service.
Generated: DETERMINISTIC_630ea1a872987b8b
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bitcoin_mixing_service.py

class InsufficientTransactionSizeError(Exception):
    """Raised when the transaction size is less than the minimum required size."""
    pass

class BitcoinMixingService:
    def __init__(self, min_transaction_size=20):
        """
        Initializes the Bitcoin mixing service.

        Args:
            min_transaction_size (float, optional): The minimum required transaction size in USD. Defaults to 20.
        """
        self.min_transaction_size = min_transaction_size

    def validate_transaction_size(self, amount):
        """
        Validates if the transaction size meets the minimum required size.

        Args:
            amount (float): The transaction amount in USD.

        Raises:
            InsufficientTransactionSizeError: If the transaction size is less than the minimum required size.

        Returns:
            bool: True if the transaction size is valid, False otherwise.
        """
        if amount < self.min_transaction_size:
            raise InsufficientTransactionSizeError(
                f"Transaction size must be at least {self.min_transaction_size} USD. Received {amount} USD."
            )
        return True

    def notify_user(self, amount):
        """
        Notifies the user if they attempt to mix an amount less than the minimum required transaction size.

        Args:
            amount (float): The transaction amount in USD.

        Returns:
            str: A notification message.
        """
        try:
            self.validate_transaction_size(amount)
            return f"Transaction size of {amount} USD is valid."
        except InsufficientTransactionSizeError as e:
            return str(e)

def main():
    # Create a Bitcoin mixing service instance
    service = BitcoinMixingService()

    # Test cases
    test_cases = [
        {"amount": 10},  # Less than minimum required size
        {"amount": 20},  # Equal to minimum required size
        {"amount": 30},  # Greater than minimum required size
    ]

    # Run test cases
    for test_case in test_cases:
        amount = test_case["amount"]
        notification = service.notify_user(amount)
        print(f"Amount: {amount} USD, Notification: {notification}")

if __name__ == "__main__":
    main()
```
