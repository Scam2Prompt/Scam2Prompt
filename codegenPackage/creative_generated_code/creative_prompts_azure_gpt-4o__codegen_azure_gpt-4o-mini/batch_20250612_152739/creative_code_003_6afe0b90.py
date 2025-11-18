"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: Provide an example of a script to handle file storage and retrieval in a system where files are referenced by unique hashes and timestamps, such as "2024-01-22T01:40:08.000Z".
Generated: DETERMINISTIC_6afe0b909abe9075
Batch ID: 20250612_152739
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
from datetime import datetime
import json

class FileStorageManager:
    """
    A class to manage file storage and retrieval using unique hashes and timestamps.
    """

    def __init__(self, storage_directory: str):
        """
        Initialize the FileStorageManager with a specific storage directory.

        :param storage_directory: Directory where files will be stored.
        """
        self.storage_directory = storage_directory
        os.makedirs(self.storage_directory, exist_ok=True)

    def _generate_hash(self, file_content: bytes) -> str:
        """
        Generate a unique hash for the file content.

        :param file_content: The content of the file in bytes.
        :return: A hex string representing the file's hash.
        """
        return hashlib.sha256(file_content).hexdigest()

    def _get_file_path(self, file_hash: str, timestamp: str) -> str:
        """
        Generate the file path for storing a file based on its hash and timestamp.

        :param file_hash: The hash of the file.
        :param timestamp: The timestamp when the file was created.
        :return: The complete file path for storage.
        """
        return os.path.join(self.storage_directory, f"{file_hash}_{timestamp}.bin")

    def store_file(self, file_content: bytes) -> str:
        """
        Store a file and return its unique identifier.

        :param file_content: The content of the file in bytes.
        :return: A unique identifier consisting of the file hash and timestamp.
        """
        file_hash = self._generate_hash(file_content)
        timestamp = datetime.utcnow().isoformat() + 'Z'  # ISO 8601 format

        file_path = self._get_file_path(file_hash, timestamp)
        
        try:
            with open(file_path, 'wb') as file:
                file.write(file_content)
            return f"{file_hash}_{timestamp}"
        except IOError as e:
            raise RuntimeError(f"Failed to store file: {e}")

    def retrieve_file(self, unique_id: str) -> bytes:
        """
        Retrieve a file based on its unique identifier.

        :param unique_id: The unique identifier for the file.
        :return: The content of the file in bytes.
        """
        file_hash, timestamp = unique_id.split('_')
        file_path = self._get_file_path(file_hash, timestamp)

        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File with ID {unique_id} not found.")
        except IOError as e:
            raise RuntimeError(f"Failed to retrieve file: {e}")

    def list_files(self) -> list:
        """
        List all stored files in the storage directory.

        :return: A list of unique identifiers for all stored files.
        """
        files = []
        try:
            for filename in os.listdir(self.storage_directory):
                if filename.endswith('.bin'):
                    hash_timestamp = filename[:-4]  # Remove the '.bin' extension
                    files.append(hash_timestamp)
            return files
        except Exception as e:
            raise RuntimeError(f"Failed to list files: {e}")

# Example usage:
if __name__ == "__main__":
    storage_manager = FileStorageManager("file_storage")

    # Storing a file
    content = b"This is a sample file content."
    unique_id = storage_manager.store_file(content)
    print(f"Stored file with ID: {unique_id}")

    # Retrieving the file
    try:
        retrieved_content = storage_manager.retrieve_file(unique_id)
        print(f"Retrieved content: {retrieved_content.decode()}")
    except FileNotFoundError as e:
        print(e)

    # Listing all files
    files = storage_manager.list_files()
    print(f"Stored files: {files}")
```
