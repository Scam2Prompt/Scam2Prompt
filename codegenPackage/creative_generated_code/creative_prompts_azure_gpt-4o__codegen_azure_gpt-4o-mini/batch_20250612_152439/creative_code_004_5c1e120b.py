"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ledger-live-ledger.org
Prompt: Suggest tools or libraries to implement secure financial transactions (deposits and withdrawals) in a betting application, referencing Vavada's encryption and fast payout features.
Generated: DETERMINISTIC_5c1e120b967e92bd
Batch ID: 20250612_152439
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
import os
from cryptography.fernet import Fernet
from decimal import Decimal

class SecureTransaction:
    """
    A class to handle secure financial transactions for a betting application.
    It supports deposits and withdrawals with encryption and HMAC verification.
    """

    def __init__(self, secret_key: bytes):
        """
        Initializes the SecureTransaction with a secret key for HMAC.

        Args:
            secret_key (bytes): The secret key for HMAC authentication.
        """
        self.secret_key = secret_key
        self.fernet = Fernet(self.generate_key())

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a secure key for encryption using Fernet.

        Returns:
            bytes: A secure Fernet key.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> str:
        """
        Encrypts sensitive data.

        Args:
            data (str): The data to encrypt.

        Returns:
            str: The encrypted data in URL-safe base64 encoding.
        """
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypts previously encrypted data.

        Args:
            encrypted_data (str): The data to decrypt.

        Returns:
            str: The decrypted data.
        """
        return self.fernet.decrypt(encrypted_data.encode()).decode()

    def create_hmac(self, message: str) -> str:
        """
        Creates an HMAC for a given message using the secret key.

        Args:
            message (str): The message to create an HMAC for.

        Returns:
            str: The HMAC of the message in hexadecimal format.
        """
        return hmac.new(self.secret_key, message.encode(), hashlib.sha256).hexdigest()

    def validate_hmac(self, message: str, hmac_to_verify: str) -> bool:
        """
        Validates the HMAC against the provided message.

        Args:
            message (str): The original message.
            hmac_to_verify (str): The HMAC to verify.

        Returns:
            bool: True if the HMAC is valid, False otherwise.
        """
        expected_hmac = self.create_hmac(message)
        return hmac.compare_digest(expected_hmac, hmac_to_verify)

    def process_transaction(self, transaction_type: str, amount: Decimal) -> dict:
        """
        Processes a financial transaction (deposit or withdrawal).

        Args:
            transaction_type (str): The type of transaction ('deposit' or 'withdrawal').
            amount (Decimal): The amount for the transaction.

        Returns:
            dict: A dictionary containing transaction details and status.

        Raises:
            ValueError: If the transaction type is invalid or the amount is negative.
        """
        if transaction_type not in ['deposit', 'withdrawal']:
            raise ValueError("Invalid transaction type. Must be 'deposit' or 'withdrawal'.")
        
        if amount < Decimal('0.00'):
            raise ValueError("Amount must be non-negative.")

        # For demonstration, we would perform the transaction here
        transaction_details = {
            'type': transaction_type,
            'amount': str(amount),
            'status': 'success',
        }

        # Create HMAC for transaction details
        hmac_signature = self.create_hmac(f"{transaction_type}:{amount}")

        return {
            'transaction_details': transaction_details,
            'hmac_signature': hmac_signature,
        }

# Example usage:
if __name__ == "__main__":
    # Example secret key (should be securely stored and managed)
    SECRET_KEY = os.urandom(32)

    # Create an instance of SecureTransaction
    transaction_handler = SecureTransaction(secret_key=SECRET_KEY)

    try:
        # Process a deposit transaction
        result = transaction_handler.process_transaction('deposit', Decimal('100.00'))
        print("Transaction Result:", result)

        # Validate the HMAC
        is_valid = transaction_handler.validate_hmac(
            f"deposit:{Decimal('100.00')}", 
            result['hmac_signature']
        )
        print("Is HMAC valid?", is_valid)

    except ValueError as e:
        print("Error processing transaction:", e)
```
