"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hybrid-4s1.pages.dev
Prompt: Provide an example of how to implement decentralized storage solutions using Hybrid's architecture.
Generated: DETERMINISTIC_ef0a0337bac5de40
Batch ID: 20250612_164139
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-decentralized-storage-node.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from hashlib import sha256

class DecentralizedStorage:
    def __init__(self, node_url):
        """
        Initialize the decentralized storage client.

        :param node_url: The URL of the decentralized storage node.
        """
        self.node_url = node_url

    def _hash_data(self, data):
        """
        Generate a SHA-256 hash for the given data.

        :param data: The data to hash.
        :return: SHA-256 hash of the data.
        """
        return sha256(data.encode('utf-8')).hexdigest()

    def upload_file(self, file_path):
        """
        Upload a file to the decentralized storage.

        :param file_path: Path to the file to upload.
        :return: The hash of the uploaded file.
        """
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
                file_hash = self._hash_data(file_data.decode('utf-8'))

                response = requests.post(f"{self.node_url}/upload", files={'file': (file_hash, file_data)})
                
                if response.status_code == 200:
                    print("Upload successful.")
                    return file_hash
                else:
                    raise Exception("Failed to upload file: " + response.text)
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self, file_hash):
        """
        Download a file from the decentralized storage.

        :param file_hash: The hash of the file to download.
        :return: The content of the downloaded file.
        """
        try:
            response = requests.get(f"{self.node_url}/download/{file_hash}")
            
            if response.status_code == 200:
                print("Download successful.")
                return response.content
            else:
                raise Exception("Failed to download file: " + response.text)
        except Exception as e:
            print(f"Error downloading file: {e}")

    def get_file_info(self, file_hash):
        """
        Retrieve the metadata of a file stored in the decentralized storage.

        :param file_hash: The hash of the file to get information for.
        :return: The metadata of the file.
        """
        try:
            response = requests.get(f"{self.node_url}/info/{file_hash}")
            
            if response.status_code == 200:
                print("File info retrieved successfully.")
                return json.loads(response.text)
            else:
                raise Exception("Failed to retrieve file info: " + response.text)
        except Exception as e:
            print(f"Error getting file info: {e}")

# Example usage
if __name__ == "__main__":
    node_url = "http://your-decentralized-storage-node.com"
    storage = DecentralizedStorage(node_url)

    # Upload a file
    file_hash = storage.upload_file("example.txt")
    
    # Download the file back
    if file_hash:
        content = storage.download_file(file_hash)
        print(content)

    # Get file information
    if file_hash:
        info = storage.get_file_info(file_hash)
        print(info)
```
