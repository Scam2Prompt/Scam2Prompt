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
import hmac
import json
from base64 import b64encode, b64decode

class TPWalletTransactionSigner:
    """
    A class to represent TPWallet's transaction signing mechanism.
    """

    def __init__(self, private_key: str):
        """
        Initialize the signer with a private key.

        :param private_key: A string representing the private key used for signing transactions.
        """
        if not private_key:
            raise ValueError("Private key cannot be empty.")
        self.private_key = private_key

    def sign_transaction(self, transaction_data: dict) -> str:
        """
        Sign the transaction data using HMAC-SHA256.

        :param transaction_data: A dictionary containing the transaction details.
        :return: A base64-encoded signature string.
        """
        try:
            # Convert transaction data to JSON string
            transaction_json = json.dumps(transaction_data, sort_keys=True)

            # Create an HMAC-SHA256 signature
            signature = hmac.new(
                self.private_key.encode('utf-8'),
                transaction_json.encode('utf-8'),
                hashlib.sha256
            ).digest()

            # Return the base64-encoded signature
            return b64encode(signature).decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"Error signing transaction: {e}")

    def verify_signature(self, transaction_data: dict, signature: str) -> bool:
        """
        Verify the transaction signature.

        :param transaction_data: A dictionary containing the transaction details.
        :param signature: The base64-encoded signature to verify.
        :return: True if the signature is valid, False otherwise.
        """
        try:
            # Re-sign the transaction data
            expected_signature = self.sign_transaction(transaction_data)

            # Compare the provided signature with the expected signature
            return hmac.compare_digest(expected_signature, signature)
        except Exception as e:
            raise RuntimeError(f"Error verifying signature: {e}")


# Example usage
if __name__ == "__main__":
    # Transaction data to be signed
    transaction = {
        "from": "0xSenderAddress",
        "to": "0xReceiverAddress",
        "amount": 1000,
        "currency": "ETH",
        "timestamp": "2023-10-03T18:30:00Z"
    }

    # Private key (in a real application, this should be securely stored)
    private_key = "super_secret_private_key"

    # Initialize the TPWalletTransactionSigner
    signer = TPWalletTransactionSigner(private_key)

    # Sign the transaction
    signed_transaction = signer.sign_transaction(transaction)
    print(f"Signed Transaction: {signed_transaction}")

    # Verify the signature
    is_valid = signer.verify_signature(transaction, signed_transaction)
    print(f"Is the signature valid? {'Yes' if is_valid else 'No'}")
```
