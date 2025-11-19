"""
Generated Code Metadata:
========================
Original URL: https://substantial-eggplant-fast.on-fleek.app
Prompt: What are the best practices for managing files in IPFS, especially regarding file retrieval and storage efficiency?
Generated: DETERMINISTIC_502550d248a929b1
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Python script demonstrating best practices for managing files in IPFS using the `ipfshttpclient` library, including efficient storage and retrieval:

```python
import ipfshttpclient
import os
from typing import Optional, Union
from pathlib import Path

class IPFSManager:
    """
    A class to handle IPFS file operations with best practices for storage efficiency and retrieval.
    """
    
    def __init__(self, host: str = '/ip4/127.0.0.1/tcp/5001'):
        """
        Initialize IPFS client connection.
        
        Args:
            host: Multiaddr of the IPFS API server (default: localhost)
        """
        try:
            self.client = ipfshttpclient.connect(host)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to IPFS daemon: {str(e)}")

    def add_file(self, file_path: Union[str, Path], pin: bool = True) -> str:
        """
        Add a file to IPFS with optional pinning.
        
        Args:
            file_path: Path to the file to be added
            pin: Whether to pin the file (default: True for persistence)
            
        Returns:
            CID of the added file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            IPFSError: If IPFS operation fails
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        try:
            res = self.client.add(file_path, pin=pin)
            return res['Hash']
        except Exception as e:
            raise RuntimeError(f"Failed to add file to IPFS: {str(e)}")

    def get_file(self, cid: str, output_path: Optional[Union[str, Path]] = None) -> bytes:
        """
        Retrieve a file from IPFS by CID.
        
        Args:
            cid: Content Identifier of the file
            output_path: Optional path to save the file (returns bytes if None)
            
        Returns:
            File content as bytes if output_path is None
            
        Raises:
            ValueError: If CID is invalid
            IPFSError: If retrieval fails
        """
        if not cid or not isinstance(cid, str):
            raise ValueError("Invalid CID provided")
            
        try:
            content = self.client.cat(cid)
            
            if output_path:
                with open(output_path, 'wb') as f:
                    f.write(content)
            return content
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve file from IPFS: {str(e)}")

    def add_directory(self, dir_path: Union[str, Path], pin: bool = True) -> str:
        """
        Add a directory recursively to IPFS.
        
        Args:
            dir_path: Path to the directory
            pin: Whether to pin the directory (default: True)
            
        Returns:
            CID of the root directory
            
        Raises:
            FileNotFoundError: If directory doesn't exist
            IPFSError: If IPFS operation fails
        """
        if not os.path.isdir(dir_path):
            raise FileNotFoundError(f"Directory not found: {dir_path}")
            
        try:
            res = self.client.add(dir_path, recursive=True, pin=pin)
            # The last item in the response is the root directory
            return res[-1]['Hash']
        except Exception as e:
            raise RuntimeError(f"Failed to add directory to IPFS: {str(e)}")

    def unpin(self, cid: str) -> bool:
        """
        Unpin a CID to free up storage space.
        
        Args:
            cid: Content Identifier to unpin
            
        Returns:
            True if successful
            
        Raises:
            IPFSError: If unpinning fails
        """
        try:
            return self.client.pin.rm(cid)
        except Exception as e:
            raise RuntimeError(f"Failed to unpin CID {cid}: {str(e)}")

    def close(self):
        """Close the IPFS client connection."""
        if hasattr(self, 'client'):
            self.client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

# Example usage
if __name__ == "__main__":
    try:
        with IPFSManager() as ipfs:
            # Add and pin a file
            cid = ipfs.add_file("example.txt")
            print(f"File added with CID: {cid}")
            
            # Retrieve file
            content = ipfs.get_file(cid)
            print(f"Retrieved file content length: {len(content)} bytes")
            
            # Add a directory
            dir_cid = ipfs.add_directory("example_dir")
            print(f"Directory added with CID: {dir_cid}")
            
            # Clean up (unpin)
            ipfs.unpin(cid)
            print(f"Unpinned file {cid}")
            
    except Exception as e:
        print(f"IPFS operation failed: {str(e)}")
```
