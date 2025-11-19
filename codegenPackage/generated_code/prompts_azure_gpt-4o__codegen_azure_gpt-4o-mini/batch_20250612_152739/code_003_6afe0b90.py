"""
Generated Code Metadata:
========================
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: Provide an example of a script to handle file storage and retrieval in a system where files are referenced by unique hashes and timestamps, such as "2024-01-22T01:40:08.000Z".
Generated: DETERMINISTIC_6afe0b909abe9075
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import datetime
import json

class FileStorage:
    def __init__(self, storage_directory):
        """
        Initializes the FileStorage with a specified directory.
        
        :param storage_directory: Directory where files will be stored.
        """
        self.storage_directory = storage_directory
        os.makedirs(self.storage_directory, exist_ok=True)

    def _generate_hash(self, file_path):
        """
        Generates a SHA-256 hash for the given file.
        
        :param file_path: Path to the file to hash.
        :return: Hexadecimal hash string.
        """
        hash_sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

    def store_file(self, file_path):
        """
        Stores a file in the storage directory, using its hash and timestamp as the filename.
        
        :param file_path: Path to the file to store.
        :return: The unique identifier for the stored file.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        file_hash = self._generate_hash(file_path)
        timestamp = datetime.datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'
        storage_filename = f"{file_hash}_{timestamp}.json"
        storage_path = os.path.join(self.storage_directory, storage_filename)

        # Store file metadata in JSON format
        metadata = {
            'file_hash': file_hash,
            'timestamp': timestamp,
            'original_file': file_path
        }
        
        with open(storage_path, 'w') as json_file:
            json.dump(metadata, json_file)

        return storage_filename

    def retrieve_file(self, storage_filename):
        """
        Retrieves the original file path from the stored metadata.
        
        :param storage_filename: The filename of the stored metadata.
        :return: The original file path.
        """
        storage_path = os.path.join(self.storage_directory, storage_filename)
        
        if not os.path.isfile(storage_path):
            raise FileNotFoundError(f"The file {storage_filename} does not exist in storage.")
        
        with open(storage_path, 'r') as json_file:
            metadata = json.load(json_file)
        
        return metadata['original_file']

# Example usage
if __name__ == "__main__":
    storage = FileStorage("file_storage")

    try:
        # Store a file
        stored_filename = storage.store_file("example.txt")
        print(f"File stored as: {stored_filename}")

        # Retrieve the original file path
        original_file = storage.retrieve_file(stored_filename)
        print(f"Original file path: {original_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
