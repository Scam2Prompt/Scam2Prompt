"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://substantial-eggplant-fast.on-fleek.app
Prompt: What are the best practices for managing files in IPFS, especially regarding file retrieval and storage efficiency?
Generated: DETERMINISTIC_502550d248a929b1
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ipfshttpclient
import os
from pathlib import Path

class IPFSManager:
    """
    A class to manage files in IPFS (InterPlanetary File System).
    This class provides methods for uploading, retrieving, and managing files efficiently.
    """

    def __init__(self, ipfs_address='/dns/ipfs.infura.io/tcp/5001/https'):
        """
        Initializes the IPFSManager with a connection to the specified IPFS node.
        
        Parameters:
            ipfs_address (str): The address of the IPFS node to connect to.
        """
        self.client = ipfshttpclient.connect(ipfs_address)

    def upload_file(self, file_path):
        """
        Uploads a file to IPFS.

        Parameters:
            file_path (str): The local path of the file to upload.

        Returns:
            str: The IPFS hash of the uploaded file.
        """
        if not Path(file_path).is_file():
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        try:
            res = self.client.add(file_path)
            ipfs_hash = res['Hash']
            print(f"File uploaded successfully. IPFS Hash: {ipfs_hash}")
            return ipfs_hash
        except Exception as e:
            raise RuntimeError(f"An error occurred while uploading the file: {e}")

    def retrieve_file(self, ipfs_hash, save_path):
        """
        Retrieves a file from IPFS and saves it to the specified path.

        Parameters:
            ipfs_hash (str): The IPFS hash of the file to retrieve.
            save_path (str): The local path where the file will be saved.
        """
        try:
            self.client.get(ipfs_hash, target=save_path)
            print(f"File retrieved successfully and saved to {save_path}.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while retrieving the file: {e}")

    def list_files(self):
        """
        Lists the files currently stored in the IPFS node.
        """
        try:
            files = self.client.ls('/ipfs/')
            if files:
                print("Files currently stored in IPFS:")
                for file in files['Objects']:
                    print(f"- {file['Hash']}")
            else:
                print("No files found in IPFS.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while listing files: {e}")

if __name__ == "__main__":
    ipfs_manager = IPFSManager()

    # Example usage
    try:
        # Upload a file
        file_hash = ipfs_manager.upload_file('example.txt')

        # Retrieve the file to a specified location
        ipfs_manager.retrieve_file(file_hash, 'downloaded_example.txt')

        # List files in IPFS
        ipfs_manager.list_files()
    except Exception as e:
        print(f"Error: {e}")
```
