"""
Generated Code Metadata:
========================
Original URL: https://substantial-eggplant-fast.on-fleek.app
Prompt: Generate a script that automates the process of adding multiple files to IPFS and retrieving their CIDs.
Generated: DETERMINISTIC_1fdfc8020cb564e9
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ipfshttpclient
import os
from typing import List, Dict

class IPFSAutomator:
    """
    A class to automate the process of adding files to IPFS and retrieving their CIDs.
    """

    def __init__(self, host: str = '/ip4/127.0.0.1/tcp/5001'):
        """
        Initialize the IPFS client.

        Args:
            host (str): The host address of the IPFS API. Defaults to localhost.
        """
        try:
            self.client = ipfshttpclient.connect(host)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to IPFS daemon: {e}")

    def add_files(self, file_paths: List[str]) -> Dict[str, str]:
        """
        Add multiple files to IPFS and return their CIDs.

        Args:
            file_paths (List[str]): List of file paths to add to IPFS.

        Returns:
            Dict[str, str]: A dictionary mapping file paths to their respective CIDs.

        Raises:
            FileNotFoundError: If any file in file_paths does not exist.
            ValueError: If file_paths is empty.
        """
        if not file_paths:
            raise ValueError("No file paths provided.")

        cids = {}
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            try:
                res = self.client.add(file_path)
                cids[file_path] = res['Hash']
            except Exception as e:
                raise RuntimeError(f"Failed to add file {file_path} to IPFS: {e}")

        return cids

    def get_file(self, cid: str, output_path: str) -> None:
        """
        Retrieve a file from IPFS using its CID and save it to the specified path.

        Args:
            cid (str): The CID of the file to retrieve.
            output_path (str): The path where the file will be saved.

        Raises:
            ValueError: If CID or output_path is empty.
            RuntimeError: If the file retrieval fails.
        """
        if not cid or not output_path:
            raise ValueError("CID and output_path must not be empty.")

        try:
            self.client.get(cid, output_path)
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve file with CID {cid}: {e}")

    def close(self) -> None:
        """Close the IPFS client connection."""
        if hasattr(self, 'client'):
            self.client.close()

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Automate adding files to IPFS and retrieving their CIDs.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Parser for adding files
    add_parser = subparsers.add_parser('add', help='Add files to IPFS')
    add_parser.add_argument('files', nargs='+', help='List of file paths to add to IPFS')

    # Parser for retrieving files
    get_parser = subparsers.add_parser('get', help='Retrieve a file from IPFS using its CID')
    get_parser.add_argument('cid', help='CID of the file to retrieve')
    get_parser.add_argument('output_path', help='Path to save the retrieved file')

    args = parser.parse_args()

    ipfs = IPFSAutomator()

    try:
        if args.command == 'add':
            cids = ipfs.add_files(args.files)
            print("Files added successfully. CIDs:")
            for file_path, cid in cids.items():
                print(f"{file_path}: {cid}")
        elif args.command == 'get':
            ipfs.get_file(args.cid, args.output_path)
            print(f"File retrieved successfully and saved to {args.output_path}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ipfs.close()

if __name__ == "__main__":
    main()
```
