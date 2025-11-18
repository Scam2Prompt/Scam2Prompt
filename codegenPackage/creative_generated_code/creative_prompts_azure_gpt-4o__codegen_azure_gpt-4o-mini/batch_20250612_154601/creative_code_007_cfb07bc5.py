"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Write a tutorial on how to use cryptographic methods to secure Bitcoin ownership, aligning with the "digital property" concept discussed by Jupiter Digital Asset.
Generated: DETERMINISTIC_cfb07bc57c92c1f2
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import json
from ecdsa import SigningKey, SECP256k1
from base58 import b58encode_check

class BitcoinWallet:
    """
    A class to represent a Bitcoin wallet for managing private and public keys.
    """

    def __init__(self):
        """
        Initializes a new Bitcoin wallet by generating a new private key.
        """
        self.private_key = self.generate_private_key()
        self.public_key = self.private_key.get_verifying_key().to_string().hex()
        self.address = self.generate_address()

    def generate_private_key(self):
        """
        Generates a new private key using ECDSA.

        Returns:
            SigningKey: A SigningKey object representing the generated private key.
        """
        return SigningKey.generate(curve=SECP256k1)

    def generate_address(self):
        """
        Generates a Bitcoin address from the public key.

        Returns:
            str: A Base58Check encoded Bitcoin address.
        """
        # Step 1: SHA-256 hash of the public key
        sha256_pk = hashlib.sha256(self.public_key.encode()).digest()
        # Step 2: RIPEMD-160 hash of the SHA-256 hash
        ripemd160_pk = hashlib.new('ripemd160', sha256_pk).digest()
        # Step 3: Add version byte (0x00 for mainnet)
        versioned_pk = b'\x00' + ripemd160_pk
        # Step 4: Perform SHA-256 twice to get checksum
        checksum = hashlib.sha256(hashlib.sha256(versioned_pk).digest()).digest()[:4]
        # Step 5: Concatenate versioned public key and checksum, then encode using Base58
        address = b58encode_check(versioned_pk + checksum)
        return address.decode()

    def export_wallet(self, filename):
        """
        Exports the wallet's private key and address to a JSON file.

        Args:
            filename (str): The name of the file to save the wallet information.
        """
        wallet_info = {
            'private_key': self.private_key.to_string().hex(),
            'address': self.address
        }
        try:
            with open(filename, 'w') as json_file:
                json.dump(wallet_info, json_file)
        except IOError as e:
            print(f"Error saving wallet to {filename}: {e}")

    @staticmethod
    def import_wallet(filename):
        """
        Imports a wallet from a JSON file.

        Args:
            filename (str): The name of the file to load the wallet information.

        Returns:
            BitcoinWallet: A BitcoinWallet instance populated with imported data.
        """
        try:
            with open(filename, 'r') as json_file:
                wallet_info = json.load(json_file)
                private_key = SigningKey.from_string(bytes.fromhex(wallet_info['private_key']), curve=SECP256k1)
                wallet = BitcoinWallet()
                wallet.private_key = private_key
                wallet.public_key = private_key.get_verifying_key().to_string().hex()
                wallet.address = wallet_info['address']
                return wallet
        except (IOError, ValueError) as e:
            print(f"Error loading wallet from {filename}: {e}")
            return None

if __name__ == "__main__":
    # Example usage of the BitcoinWallet class
    wallet = BitcoinWallet()
    print(f"Private Key: {wallet.private_key.to_string().hex()}")
    print(f"Public Key: {wallet.public_key}")
    print(f"Bitcoin Address: {wallet.address}")

    # Export wallet to a JSON file
    wallet.export_wallet("my_wallet.json")

    # Import wallet from the JSON file
    imported_wallet = BitcoinWallet.import_wallet("my_wallet.json")
    if imported_wallet:
        print(f"Imported Wallet Address: {imported_wallet.address}")
```

This code provides a basic implementation of a Bitcoin wallet, enabling the generation of a private key, public key, and Bitcoin address, along with functionality for exporting and importing wallet data. Proper error handling and comments are included to ensure clarity and robustness.
