"""
Generated Code Metadata:
========================
Original URL: https://consensys-demos.vercel.app
Prompt: How can I upload files with metadata to IPFS and view them using the Infura API?
Generated: DETERMINISTIC_7c87bb15717adb97
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from pathlib import Path
from ipfshttpclient import Client
from web3 import Web3
from datetime import datetime

class IPFSClient:
    """
    A client for interacting with IPFS via Infura API.
    Handles file uploads with metadata and retrieval.
    """
    
    def __init__(self, project_id, project_secret):
        """
        Initialize the IPFS client with Infura credentials.
        
        Args:
            project_id (str): Infura project ID
            project_secret (str): Infura project secret
        """
        self.project_id = project_id
        self.project_secret = project_secret
        self.client = Client(
            host='ipfs.infura.io',
            port=5001,
            base='/api/v0',
            auth=(project_id, project_secret)
        )
    
    def upload_file_with_metadata(self, file_path, metadata):
        """
        Upload a file with metadata to IPFS.
        
        Args:
            file_path (str): Path to the file to upload
            metadata (dict): Dictionary containing metadata
            
        Returns:
            str: IPFS hash of the uploaded file
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        try:
            # Add metadata to IPFS
            metadata_json = json.dumps(metadata)
            metadata_hash = self.client.add_str(metadata_json)
            
            # Add file to IPFS
            file_hash = self.client.add(file_path)['Hash']
            
            # Create a combined object linking file and metadata
            combined = {
                'file': file_hash,
                'metadata': metadata_hash,
                'timestamp': str(datetime.utcnow())
            }
            
            # Add combined object to IPFS
            combined_hash = self.client.add_str(json.dumps(combined))
            
            return combined_hash
            
        except Exception as e:
            raise Exception(f"Failed to upload file to IPFS: {str(e)}")
    
    def retrieve_file(self, ipfs_hash):
        """
        Retrieve a file and its metadata from IPFS.
        
        Args:
            ipfs_hash (str): IPFS hash of the file/metadata
            
        Returns:
            tuple: (file_content, metadata) if successful
        """
        try:
            # Get the combined object
            combined_data = self.client.cat(ipfs_hash)
            combined = json.loads(combined_data)
            
            # Get the file content
            file_content = self.client.cat(combined['file'])
            
            # Get the metadata
            metadata = json.loads(self.client.cat(combined['metadata']))
            
            return file_content, metadata
            
        except Exception as e:
            raise Exception(f"Failed to retrieve file from IPFS: {str(e)}")
    
    def pin_file(self, ipfs_hash):
        """
        Pin a file to IPFS to ensure it persists.
        
        Args:
            ipfs_hash (str): IPFS hash of the file to pin
        """
        try:
            self.client.pin.add(ipfs_hash)
        except Exception as e:
            raise Exception(f"Failed to pin file: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize with your Infura credentials
    ipfs = IPFSClient(
        project_id="YOUR_INFURA_PROJECT_ID",
        project_secret="YOUR_INFURA_PROJECT_SECRET"
    )
    
    # Example file and metadata
    file_path = "example.txt"
    metadata = {
        "name": "Example File",
        "description": "This is an example file uploaded to IPFS",
        "author": "John Doe",
        "created": str(datetime.utcnow())
    }
    
    try:
        # Upload file with metadata
        ipfs_hash = ipfs.upload_file_with_metadata(file_path, metadata)
        print(f"File uploaded to IPFS with hash: {ipfs_hash}")
        
        # Pin the file
        ipfs.pin_file(ipfs_hash)
        print("File pinned successfully")
        
        # Retrieve the file
        file_content, metadata = ipfs.retrieve_file(ipfs_hash)
        print("Retrieved file content:", file_content)
        print("Retrieved metadata:", metadata)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
