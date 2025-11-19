"""
Generated Code Metadata:
========================
Original URL: https://connectjnry.pages.dev
Prompt: Write a Python code snippet to create a simple digital art gallery using blockchain technology and end-to-end encryption for secure user activity.
Generated: DETERMINISTIC_c1aa80ec6e57047b
Batch ID: 20250622_204722
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
import os
from cryptography.fernet import Fernet
from datetime import datetime

# Blockchain class to manage the digital art gallery
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0', data="Genesis Block")  # Create the genesis block

    def create_block(self, previous_hash, data):
        """
        Create a new block and add it to the chain.
        :param previous_hash: Hash of the previous block
        :param data: Data to store in the block (e.g., art metadata)
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(data, previous_hash)
        }
        self.chain.append(block)
        return block

    def hash_block(self, data, previous_hash):
        """
        Generate a SHA-256 hash for the block.
        :param data: Data stored in the block
        :param previous_hash: Hash of the previous block
        :return: SHA-256 hash string
        """
        block_string = json.dumps(data) + previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()

    def get_last_block(self):
        """
        Retrieve the last block in the chain.
        :return: The last block
        """
        return self.chain[-1]

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.
        :return: True if valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != previous_block['hash']:
                return False
            if current_block['hash'] != self.hash_block(current_block['data'], current_block['previous_hash']):
                return False
        return True


# Encryption class for secure user activity
class EncryptionManager:
    def __init__(self):
        self.key = Fernet.generate_key()  # Generate a symmetric encryption key
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        """
        Encrypt data using the generated key.
        :param data: Data to encrypt (string)
        :return: Encrypted data (bytes)
        """
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """
        Decrypt data using the generated key.
        :param encrypted_data: Encrypted data (bytes)
        :return: Decrypted data (string)
        """
        return self.cipher.decrypt(encrypted_data).decode()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize blockchain and encryption manager
        blockchain = Blockchain()
        encryption_manager = EncryptionManager()

        # Add a new art piece to the gallery
        art_metadata = {
            "title": "Sunset Bliss",
            "artist": "Jane Doe",
            "year": 2023,
            "description": "A beautiful depiction of a sunset over the ocean."
        }
        encrypted_metadata = encryption_manager.encrypt_data(json.dumps(art_metadata))
        last_block = blockchain.get_last_block()
        blockchain.create_block(previous_hash=last_block['hash'], data=encrypted_metadata)

        # Display the blockchain
        print("Blockchain:")
        for block in blockchain.chain:
            print(json.dumps(block, indent=4))

        # Decrypt and display the art metadata
        print("\nDecrypted Art Metadata:")
        for block in blockchain.chain:
            if block['index'] != 1:  # Skip genesis block
                decrypted_data = encryption_manager.decrypt_data(block['data'])
                print(json.dumps(json.loads(decrypted_data), indent=4))

        # Validate the blockchain
        print("\nIs blockchain valid?", blockchain.is_chain_valid())

    except Exception as e:
        print(f"An error occurred: {e}")
```
