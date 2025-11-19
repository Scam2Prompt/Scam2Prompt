"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.direct
Prompt: What are the steps to ensure the security and immutability of code stored as blobs in a decentralized Git service?
Generated: DETERMINISTIC_03ba41366fc6bf40
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
from typing import List

class BlobManager:
    def __init__(self, storage_directory: str):
        """
        Initializes the BlobManager with the specified storage directory.
        Ensures the directory exists.

        :param storage_directory: Directory where blobs will be stored
        """
        self.storage_directory = storage_directory
        os.makedirs(self.storage_directory, exist_ok=True)

    def _hash_blob(self, content: str) -> str:
        """
        Generates a SHA-256 hash of the blob content for immutability.

        :param content: The content of the blob
        :return: Hexadecimal representation of the SHA-256 hash
        """
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def store_blob(self, content: str) -> str:
        """
        Stores the blob content as a file in the storage directory.

        :param content: The content to be stored as a blob
        :return: The hash of the stored blob
        """
        blob_hash = self._hash_blob(content)
        blob_path = os.path.join(self.storage_directory, blob_hash)

        # Check if the blob already exists to maintain immutability
        if os.path.exists(blob_path):
            raise FileExistsError(f"Blob with hash {blob_hash} already exists.")

        # Write the blob content to a file
        with open(blob_path, 'w') as blob_file:
            blob_file.write(content)

        return blob_hash

    def retrieve_blob(self, blob_hash: str) -> str:
        """
        Retrieves the blob content by its hash.

        :param blob_hash: The hash of the blob to retrieve
        :return: The blob content
        :raises FileNotFoundError: If the blob does not exist
        """
        blob_path = os.path.join(self.storage_directory, blob_hash)

        if not os.path.exists(blob_path):
            raise FileNotFoundError(f"Blob with hash {blob_hash} not found.")

        with open(blob_path, 'r') as blob_file:
            return blob_file.read()

    def list_blobs(self) -> List[str]:
        """
        Lists all stored blobs in the storage directory.

        :return: A list of blob hashes
        """
        return [f for f in os.listdir(self.storage_directory) if os.path.isfile(os.path.join(self.storage_directory, f))]

# Example usage
if __name__ == "__main__":
    try:
        blob_manager = BlobManager(storage_directory='./blobs')

        # Store a blob
        blob_hash = blob_manager.store_blob("This is a test blob.")
        print(f"Stored blob with hash: {blob_hash}")

        # Retrieve the blob
        retrieved_content = blob_manager.retrieve_blob(blob_hash)
        print(f"Retrieved blob content: {retrieved_content}")

        # List all blobs
        all_blobs = blob_manager.list_blobs()
        print(f"All stored blobs: {all_blobs}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
