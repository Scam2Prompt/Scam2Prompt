"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: What are the steps to ensure the security and immutability of code stored as blobs in a decentralized Git service?
Generated: DETERMINISTIC_03ba41366fc6bf40
Batch ID: 20250612_162945
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
import json
from cryptography.fernet import Fernet
from typing import Any, Dict

class SecureBlobStorage:
    def __init__(self, storage_path: str, encryption_key: bytes):
        """
        Initialize the SecureBlobStorage with a path to store blobs and an encryption key.

        :param storage_path: Directory where blobs will be stored.
        :param encryption_key: Key used for encrypting and decrypting blobs.
        """
        self.storage_path = storage_path
        self.encryption_key = encryption_key
        self.fernet = Fernet(encryption_key)

        # Ensure the storage directory exists
        os.makedirs(self.storage_path, exist_ok=True)

    def _generate_blob_id(self, data: bytes) -> str:
        """
        Generate a unique ID for the blob using SHA-256 hash.

        :param data: The data to hash.
        :return: A unique blob ID.
        """
        return hashlib.sha256(data).hexdigest()

    def store_blob(self, data: bytes) -> str:
        """
        Store a blob securely by encrypting it and saving it to the file system.

        :param data: The data to store as a blob.
        :return: The unique ID of the stored blob.
        """
        blob_id = self._generate_blob_id(data)
        encrypted_data = self.fernet.encrypt(data)

        blob_file_path = os.path.join(self.storage_path, blob_id)
        try:
            with open(blob_file_path, 'wb') as blob_file:
                blob_file.write(encrypted_data)
        except IOError as e:
            raise RuntimeError(f"Failed to write blob to storage: {e}")

        return blob_id

    def retrieve_blob(self, blob_id: str) -> bytes:
        """
        Retrieve a blob by its unique ID, decrypting it before returning.

        :param blob_id: The unique ID of the blob to retrieve.
        :return: The decrypted blob data.
        """
        blob_file_path = os.path.join(self.storage_path, blob_id)
        try:
            with open(blob_file_path, 'rb') as blob_file:
                encrypted_data = blob_file.read()
                return self.fernet.decrypt(encrypted_data)
        except (IOError, ValueError) as e:
            raise RuntimeError(f"Failed to retrieve blob: {e}")

    def list_blobs(self) -> Dict[str, Any]:
        """
        List all stored blobs with their IDs.

        :return: A dictionary of blob IDs and their file paths.
        """
        blobs = {}
        try:
            for blob_file in os.listdir(self.storage_path):
                blobs[blob_file] = os.path.join(self.storage_path, blob_file)
        except OSError as e:
            raise RuntimeError(f"Failed to list blobs: {e}")

        return blobs

# Example usage
if __name__ == "__main__":
    # Generate a key for encryption (this should be done securely and stored safely)
    key = Fernet.generate_key()
    
    # Initialize the blob storage
    storage = SecureBlobStorage(storage_path='blobs', encryption_key=key)

    # Store a blob
    blob_id = storage.store_blob(b"Hello, secure world!")
    print(f"Stored blob with ID: {blob_id}")

    # Retrieve the blob
    retrieved_data = storage.retrieve_blob(blob_id)
    print(f"Retrieved blob data: {retrieved_data.decode()}")

    # List all blobs
    blobs = storage.list_blobs()
    print(f"All stored blobs: {json.dumps(blobs, indent=2)}")
```
