"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gicoin.trade
Prompt: Write Python code to integrate a secure digital wallet system using the principles outlined in GIC's tailored financial solutions for global business growth.
Generated: DETERMINISTIC_831489b8ce9718d5
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import uuid
from typing import Optional

class DigitalWallet:
    """
    A class representing a secure digital wallet system. 
    This wallet is designed with security and scalability in mind, 
    adhering to best practices for global business financial solutions.
    """

    def __init__(self, owner_name: str):
        """
        Initialize a new digital wallet for the owner.

        Args:
            owner_name (str): Name of the wallet owner.
        """
        self.owner_name = owner_name
        self.wallet_id = self._generate_wallet_id()
        self.balance = 0.0  # Default balance in the wallet
        self.secret_key = self._generate_secret_key()  # For securing transactions

    def _generate_wallet_id(self) -> str:
        """
        Generate a unique wallet ID using UUID.

        Returns:
            str: Unique wallet ID.
        """
        return str(uuid.uuid4())

    def _generate_secret_key(self) -> str:
        """
        Generate a secure secret key for HMAC operations.

        Returns:
            str: Generated secret key.
        """
        return hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()

    def deposit(self, amount: float) -> None:
        """
        Deposit funds into the wallet.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If the amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw funds from the wallet.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If the amount is invalid or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Retrieve the current wallet balance.

        Returns:
            float: Current wallet balance.
        """
        return self.balance

    def secure_transaction_signature(self, data: str) -> str:
        """
        Generate a secure HMAC-based signature for transaction data.

        Args:
            data (str): Transaction data to secure.

        Returns:
            str: HMAC signature for the data.
        """
        return hmac.new(
            self.secret_key.encode(), data.encode(), hashlib.sha256
        ).hexdigest()

    def validate_transaction_signature(self, data: str, signature: str) -> bool:
        """
        Validate a transaction's HMAC signature.

        Args:
            data (str): Original transaction data.
            signature (str): HMAC signature to validate.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        expected_signature = self.secure_transaction_signature(data)
        return hmac.compare_digest(expected_signature, signature)


# Example Usage:
if __name__ == "__main__":
    try:
        # Create a new digital wallet
        wallet = DigitalWallet(owner_name="John Doe")

        # Deposit some funds
        wallet.deposit(100.0)
        print(f"Balance after deposit: {wallet.get_balance()}")

        # Withdraw some funds
        wallet.withdraw(30.0)
        print(f"Balance after withdrawal: {wallet.get_balance()}")

        # Demonstrate secure transaction
        transaction_data = "Transaction of $70 to Merchant ABC"
        signature = wallet.secure_transaction_signature(transaction_data)

        # Validate the transaction
        is_valid = wallet.validate_transaction_signature(transaction_data, signature)
        print(f"Transaction signature valid: {is_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
