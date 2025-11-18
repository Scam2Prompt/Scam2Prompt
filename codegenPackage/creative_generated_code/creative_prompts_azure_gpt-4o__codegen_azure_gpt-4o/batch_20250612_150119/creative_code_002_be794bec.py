"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Create a program that generates digitally signed letters of guarantee for Bitcoin mixing transactions, following the process described on mixtum.me.
Generated: DETERMINISTIC_be794bec366449dc
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import json
import hashlib
import datetime
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption,
)

# Generate a digitally signed letter of guarantee for Bitcoin mixing transactions.

class LetterOfGuaranteeGenerator:
    def __init__(self, private_key_path, public_key_path):
        """
        Initialize the generator with provided private and public key paths.

        :param private_key_path: Path to the private key file
        :param public_key_path: Path to the public key file
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path
        self.private_key = None
        self.public_key = None
        self._load_keys()

    def _load_keys(self):
        """
        Load private and public keys from the specified file paths.
        """
        try:
            # Load Private Key
            with open(self.private_key_path, 'rb') as private_key_file:
                self.private_key = load_pem_private_key(
                    private_key_file.read(), password=None
                )

            # Load Public Key
            with open(self.public_key_path, 'rb') as public_key_file:
                self.public_key = load_pem_public_key(public_key_file.read())

        except Exception as e:
            print(f"Error loading keys: {e}")
            sys.exit(1)

    def generate_guarantee(self, transaction_id, customer_address, mixing_address):
        """
        Generate a digitally signed letter of guarantee for a Bitcoin mixing transaction.

        :param transaction_id: Unique identifier for the transaction
        :param customer_address: Customer's Bitcoin wallet address
        :param mixing_address: Mixing service's Bitcoin wallet address
        :return: Signed letter of guarantee as a dictionary
        """
        try:
            # Create the letter's content
            letter_content = {
                "transaction_id": transaction_id,
                "customer_address": customer_address,
                "mixing_address": mixing_address,
                "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            }

            # Serialize the content to JSON
            letter_json = json.dumps(letter_content, sort_keys=True).encode('utf-8')

            # Create a digital signature
            signature = self.private_key.sign(
                letter_json,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )

            # Attach the signature to the letter
            letter_content["signature"] = signature.hex()

            return letter_content

        except Exception as e:
            print(f"Error generating letter of guarantee: {e}")
            return None

    def verify_guarantee(self, letter):
        """
        Verify the authenticity of a digitally signed letter of guarantee.

        :param letter: Letter of guarantee dictionary to verify
        :return: True if valid, False otherwise
        """
        try:
            # Extract content and signature
            signature = bytes.fromhex(letter["signature"])
            letter_content = dict(letter)
            del letter_content["signature"]

            # Serialize the content to JSON
            letter_json = json.dumps(letter_content, sort_keys=True).encode('utf-8')

            # Verify the signature
            self.public_key.verify(
                signature,
                letter_json,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )

            return True

        except Exception as e:
            print(f"Verification failed: {e}")
            return False


def main():
    """
    Main function to demonstrate the usage of the LetterOfGuaranteeGenerator class.
    """
    # Paths to the private and public key files
    private_key_path = "private_key.pem"
    public_key_path = "public_key.pem"

    # Ensure keys exist
    if not (os.path.exists(private_key_path) and os.path.exists(public_key_path)):
        print("Error: Key files not found.")
        sys.exit(1)

    # Initialize the generator
    generator = LetterOfGuaranteeGenerator(private_key_path, public_key_path)

    # Example transaction details
    transaction_id = "abc123"
    customer_address = "1BitcoinAddressCustomer"
    mixing_address = "1BitcoinAddressMixer"

    # Generate a letter of guarantee
    letter = generator.generate_guarantee(transaction_id, customer_address, mixing_address)

    if letter:
        print("Letter of Guarantee Generated:")
        print(json.dumps(letter, indent=4))

        # Verify the authenticity of the letter
        is_valid = generator.verify_guarantee(letter)
        print(f"Verification Result: {'Valid' if is_valid else 'Invalid'}")


if __name__ == "__main__":
    main()
```
