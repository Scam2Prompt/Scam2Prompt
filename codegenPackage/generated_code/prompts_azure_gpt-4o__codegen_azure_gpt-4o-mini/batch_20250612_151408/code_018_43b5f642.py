"""
Generated Code Metadata:
========================
Original URL: https://snso.com.cn
Prompt: Generate code to demonstrate TPWallet's transaction signing mechanism for secure blockchain operations.
Generated: DETERMINISTIC_43b5f64246c2e71a
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import ecdsa
import base64

class TPWallet:
    def __init__(self, private_key: str):
        """
        Initialize the TPWallet with a private key.

        :param private_key: The private key in hexadecimal format.
        """
        self.private_key = bytes.fromhex(private_key)
        self.signing_key = ecdsa.SigningKey.from_string(self.private_key, curve=ecdsa.SECP256k1)

    def sign_transaction(self, transaction: dict) -> str:
        """
        Sign a transaction using the wallet's private key.

        :param transaction: A dictionary representing the transaction to be signed.
        :return: A base64 encoded signature of the transaction.
        """
        # Convert the transaction to a JSON string and encode it
        transaction_json = json.dumps(transaction, sort_keys=True).encode()
        
        # Create a SHA-256 hash of the transaction
        transaction_hash = hashlib.sha256(transaction_json).digest()
        
        # Sign the transaction hash
        signature = self.signing_key.sign(transaction_hash)
        
        # Return the base64 encoded signature
        return base64.b64encode(signature).decode()

    def verify_signature(self, transaction: dict, signature: str) -> bool:
        """
        Verify the signature of a transaction.

        :param transaction: A dictionary representing the transaction.
        :param signature: The base64 encoded signature to verify.
        :return: True if the signature is valid, False otherwise.
        """
        # Convert the transaction to a JSON string and encode it
        transaction_json = json.dumps(transaction, sort_keys=True).encode()
        
        # Create a SHA-256 hash of the transaction
        transaction_hash = hashlib.sha256(transaction_json).digest()
        
        # Decode the base64 signature
        decoded_signature = base64.b64decode(signature)
        
        # Recover the public key from the signature
        verifying_key = ecdsa.VerifyingKey.from_string(self.private_key, curve=ecdsa.SECP256k1)
        
        # Verify the signature
        try:
            return verifying_key.verify(decoded_signature, transaction_hash)
        except ecdsa.BadSignatureError:
            return False

# Example usage
if __name__ == "__main__":
    # Replace with your own private key (in hex format)
    private_key_hex = "your_private_key_in_hex"
    
    # Create a TPWallet instance
    wallet = TPWallet(private_key_hex)
    
    # Example transaction
    transaction = {
        "from": "address1",
        "to": "address2",
        "amount": 100,
        "timestamp": "2023-10-01T12:00:00Z"
    }
    
    # Sign the transaction
    signature = wallet.sign_transaction(transaction)
    print(f"Signature: {signature}")
    
    # Verify the signature
    is_valid = wallet.verify_signature(transaction, signature)
    print(f"Is the signature valid? {is_valid}")
```
