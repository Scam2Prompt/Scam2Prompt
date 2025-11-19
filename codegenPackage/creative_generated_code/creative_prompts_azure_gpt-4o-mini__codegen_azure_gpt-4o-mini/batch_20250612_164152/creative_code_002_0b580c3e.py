"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://substantial-eggplant-fast.on-fleek.app
Prompt: What are the unique features of IPFS that differentiate it from traditional file storage systems?
Generated: DETERMINISTIC_0b580c3e9b4c0cd1
Batch ID: 20250612_164152
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
import json

class IPFSFile:
    """
    A class to represent a file in IPFS.

    Attributes:
        file_path (str): The path of the file to be stored.
        ipfs_hash (str): The unique identifier for the file in IPFS.
    """

    def __init__(self, file_path):
        """
        Initializes the IPFSFile with a file path.

        Args:
            file_path (str): The path of the file to be stored.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        self.file_path = file_path
        self.ipfs_hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the IPFS hash for the file.

        Returns:
            str: The unique IPFS hash of the file.
        """
        hash_sha256 = hashlib.sha256()
        with open(self.file_path, 'rb') as f:
            # Read file in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

    def save_metadata(self):
        """
        Saves the metadata of the file in a JSON format.

        Returns:
            str: The path to the metadata file.
        """
        metadata = {
            "file_name": os.path.basename(self.file_path),
            "ipfs_hash": self.ipfs_hash
        }
        metadata_file_path = f"{self.file_path}.metadata.json"
        with open(metadata_file_path, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)
        return metadata_file_path

def main():
    """
    Main function to demonstrate IPFSFile usage.
    """
    try:
        # Example file path
        example_file_path = "example.txt"
        
        # Initialize IPFSFile object
        ipfs_file = IPFSFile(example_file_path)

        # Save metadata
        metadata_file = ipfs_file.save_metadata()
        print(f"File metadata saved to: {metadata_file}")
        print(f"IPFS hash for the file: {ipfs_file.ipfs_hash}")
    
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
