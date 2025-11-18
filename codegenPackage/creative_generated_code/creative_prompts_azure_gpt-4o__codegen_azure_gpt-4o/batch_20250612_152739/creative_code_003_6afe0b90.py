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
import datetime
from pathlib import Path


class FileStorageSystem:
    """
    A file storage system that stores and retrieves files based on unique hashes
    and timestamps.
    """

    def __init__(self, storage_directory="storage"):
        """
        Initialize the file storage system.

        :param storage_directory: The root directory where files will be stored.
        """
        self.storage_directory = Path(storage_directory)
        self.storage_directory.mkdir(parents=True, exist_ok=True)

    def generate_file_hash(self, file_path):
        """
        Generate a unique hash for the given file using SHA256.

        :param file_path: Path to the file.
        :return: Unique hash as a string.
        """
        try:
            hash_sha256 = hashlib.sha256()
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):  # Read file in chunks for large files
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except FileNotFoundError:
            raise Exception(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error generating file hash: {e}")

    def store_file(self, file_path):
        """
        Store a file in the system with a unique hash and timestamp.

        :param file_path: Path to the file to store.
        :return: The unique hash and timestamp.
        """
        try:
            # Generate unique hash for the file
            file_hash = self.generate_file_hash(file_path)

            # Generate timestamp
            timestamp = datetime.datetime.utcnow().isoformat() + "Z"

            # Create storage subdirectory based on hash
            subdirectory = self.storage_directory / file_hash[:2]
            subdirectory.mkdir(parents=True, exist_ok=True)

            # Create full storage path
            storage_path = subdirectory / f"{file_hash}_{timestamp}"
            os.rename(file_path, storage_path)

            return file_hash, timestamp
        except Exception as e:
            raise Exception(f"Error storing file: {e}")

    def retrieve_file(self, file_hash, timestamp):
        """
        Retrieve a file from the system based on hash and timestamp.

        :param file_hash: The unique hash of the file.
        :param timestamp: The timestamp when the file was stored.
        :return: Path to the retrieved file.
        """
        try:
            # Validate timestamp format
            datetime.datetime.fromisoformat(timestamp.rstrip("Z"))

            # Construct file path
            subdirectory = self.storage_directory / file_hash[:2]
            storage_path = subdirectory / f"{file_hash}_{timestamp}"

            if not storage_path.exists():
                raise FileNotFoundError(f"No file found with hash {file_hash} and timestamp {timestamp}")

            return storage_path
        except ValueError:
            raise Exception("Invalid timestamp format. Expected ISO8601 format.")
        except Exception as e:
            raise Exception(f"Error retrieving file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize storage system
        storage_system = FileStorageSystem()

        # Path to example file (replace with an actual file path)
        example_file_path = "example.txt"

        # Store file
        file_hash, timestamp = storage_system.store_file(example_file_path)
        print(f"File stored with hash: {file_hash}, timestamp: {timestamp}")

        # Retrieve file
        retrieved_file_path = storage_system.retrieve_file(file_hash, timestamp)
        print(f"File retrieved at: {retrieved_file_path}")

    except Exception as err:
        print(f"Error: {err}")
```
