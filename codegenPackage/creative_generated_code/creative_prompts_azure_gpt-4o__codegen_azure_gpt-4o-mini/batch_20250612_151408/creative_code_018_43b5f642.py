"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: Generate code to demonstrate TPWallet's transaction signing mechanism for secure blockchain operations.
Generated: DETERMINISTIC_43b5f64246c2e71a
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import binascii
import ecdsa
from typing import Any, Dict

class Transaction:
    """
    A class to represent a blockchain transaction.
    """

    def __init__(self, sender: str, recipient: str, amount: float, fee: float):
        """
        Initializes the Transaction object.

        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount to be transferred
        :param fee: Transaction fee
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.fee = fee
        self.signature = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the transaction to a dictionary format.

        :return: Dictionary representation of the transaction
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'fee': self.fee,
            'signature': self.signature
        }

    def sign_transaction(self, private_key: str):
        """
        Signs the transaction using the sender's private key.

        :param private_key: The private key to sign the transaction
        :raises ValueError: If the private key is invalid
        """
        try:
            # Create a string representation of the transaction
            transaction_string = json.dumps(self.to_dict(), sort_keys=True).encode()
            # Hash the transaction
            transaction_hash = hashlib.sha256(transaction_string).digest()
            # Generate a signing key
            sk = ecdsa.SigningKey.from_string(binascii.unhexlify(private_key), curve=ecdsa.SECP256k1)
            # Sign the transaction hash
            self.signature = sk.sign(transaction_hash)
        except Exception as e:
            raise ValueError("Error signing transaction: " + str(e))

    def is_valid(self) -> bool:
        """
        Validates the transaction by checking the signature.

        :return: True if the signature is valid, False otherwise
        """
        if self.signature is None:
            return False
        try:
            # Create a string representation of the transaction
            transaction_string = json.dumps(self.to_dict(), sort_keys=True).encode()
            # Hash the transaction
            transaction_hash = hashlib.sha256(transaction_string).digest()
            # Generate a verifying key
            vk = ecdsa.VerifyingKey.from_string(binascii.unhexlify(self.sender), curve=ecdsa.SECP256k1)
            # Verify the signature
            return vk.verify(self.signature, transaction_hash)
        except Exception as e:
            print("Error during signature verification: " + str(e))
            return False

# Example usage
if __name__ == "__main__":
    # Example addresses (in actual implementation, use real public/private key pairs)
    sender_private_key = "1c3b0f8d1d4f7e5c4f7c2c9f03d2e5b908b7f2a1a8b8f1c5f3a3e021a1f3ef3a"  # Example private key in hex
    sender_public_key = "f3f5a3a3e5e2c9f7c8b8f7c2c4f3b0f8d1d4f5f2a3f3e0c9e5f2a1f3b4f2d5c"  # Example public key in hex
    recipient_address = "b0f3e2c2f9e4c8b7f3c4f2a1e5e2c9f7c8b8f7c9f0f2a1b0f3e4c0b7f9e5c7a"  # Example recipient address

    # Create a transaction
    transaction = Transaction(sender=sender_public_key, recipient=recipient_address, amount=100.0, fee=0.01)
    
    # Sign the transaction
    transaction.sign_transaction(sender_private_key)

    # Check if the transaction is valid
    if transaction.is_valid():
        print("Transaction is valid.")
    else:
        print("Transaction is invalid.")
```
