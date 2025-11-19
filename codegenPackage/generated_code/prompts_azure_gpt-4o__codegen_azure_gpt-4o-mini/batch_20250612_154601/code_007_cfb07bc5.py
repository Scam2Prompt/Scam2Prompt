"""
Generated Code Metadata:
========================
Original URL: https://jupiterdigitalasset.com
Prompt: Write a tutorial on how to use cryptographic methods to secure Bitcoin ownership, aligning with the "digital property" concept discussed by Jupiter Digital Asset.
Generated: DETERMINISTIC_cfb07bc57c92c1f2
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import binascii
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class BitcoinWallet:
    """
    A class to represent a Bitcoin wallet using cryptographic methods.
    """

    def __init__(self):
        """
        Initializes a new Bitcoin wallet by generating a private key and corresponding public key.
        """
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key(self.private_key)

    @staticmethod
    def generate_private_key():
        """
        Generates a random private key using os.urandom.
        
        Returns:
            str: A hexadecimal representation of the private key.
        """
        private_key = SigningKey.generate(curve=SECP256k1)
        return private_key.to_string().hex()

    @staticmethod
    def generate_public_key(private_key_hex):
        """
        Generates the public key from the given private key.
        
        Args:
            private_key_hex (str): The private key in hexadecimal format.
        
        Returns:
            str: A hexadecimal representation of the public key.
        """
        private_key_bytes = bytes.fromhex(private_key_hex)
        private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        public_key = private_key.get_verifying_key()
        return public_key.to_string().hex()

    @staticmethod
    def sign_transaction(private_key_hex, transaction_data):
        """
        Signs a transaction using the private key.
        
        Args:
            private_key_hex (str): The private key in hexadecimal format.
            transaction_data (str): The transaction data to be signed.
        
        Returns:
            str: The signature of the transaction in hexadecimal format.
        """
        private_key_bytes = bytes.fromhex(private_key_hex)
        private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        signature = private_key.sign(transaction_data.encode())
        return binascii.hexlify(signature).decode()

    @staticmethod
    def verify_signature(public_key_hex, transaction_data, signature_hex):
        """
        Verifies the signature of a transaction using the public key.
        
        Args:
            public_key_hex (str): The public key in hexadecimal format.
            transaction_data (str): The transaction data that was signed.
            signature_hex (str): The signature in hexadecimal format.
        
        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        public_key_bytes = bytes.fromhex(public_key_hex)
        public_key = VerifyingKey.from_string(public_key_bytes, curve=SECP256k1)
        signature_bytes = binascii.unhexlify(signature_hex)
        return public_key.verify(signature_bytes, transaction_data.encode())

# Example usage
if __name__ == "__main__":
    try:
        # Create a new Bitcoin wallet
        wallet = BitcoinWallet()
        print("Private Key:", wallet.private_key)
        print("Public Key:", wallet.public_key)

        # Sample transaction data
        transaction_data = "Send 0.1 BTC to address XYZ"

        # Sign the transaction
        signature = wallet.sign_transaction(wallet.private_key, transaction_data)
        print("Signature:", signature)

        # Verify the signature
        is_valid = wallet.verify_signature(wallet.public_key, transaction_data, signature)
        print("Is the signature valid?", is_valid)

    except Exception as e:
        print("An error occurred:", str(e))
```
