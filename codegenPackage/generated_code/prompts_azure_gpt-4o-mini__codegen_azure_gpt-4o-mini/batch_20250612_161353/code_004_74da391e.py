"""
Generated Code Metadata:
========================
Original URL: https://chainback-en.web.app
Prompt: Describe the process of setting up a decentralized file sharing application using Chainback's ecosystem and $ARCHIVE.
Generated: DETERMINISTIC_74da391ead14c2ca
Batch ID: 20250612_161353
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainback.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import json
import requests

class ChainbackFileSharing:
    def __init__(self, archive_token):
        """
        Initializes the ChainbackFileSharing instance with the provided archive token.
        
        :param archive_token: The token used to authenticate with the Chainback ecosystem.
        """
        self.archive_token = archive_token
        self.base_url = "https://api.chainback.com/v1"

    def upload_file(self, file_path):
        """
        Uploads a file to the Chainback ecosystem.

        :param file_path: The path to the file to be uploaded.
        :return: The response from the Chainback API.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        with open(file_path, 'rb') as file:
            headers = {
                'Authorization': f'Bearer {self.archive_token}',
                'Content-Type': 'application/octet-stream'
            }
            response = requests.post(f"{self.base_url}/upload", headers=headers, data=file)

            # Check for successful upload
            if response.status_code != 200:
                raise Exception(f"Failed to upload file: {response.text}")

            return response.json()

    def download_file(self, file_id, download_path):
        """
        Downloads a file from the Chainback ecosystem.

        :param file_id: The ID of the file to be downloaded.
        :param download_path: The path where the file will be saved.
        :return: None
        """
        headers = {
            'Authorization': f'Bearer {self.archive_token}'
        }
        response = requests.get(f"{self.base_url}/download/{file_id}", headers=headers)

        # Check for successful download
        if response.status_code != 200:
            raise Exception(f"Failed to download file: {response.text}")

        with open(download_path, 'wb') as file:
            file.write(response.content)

    def list_files(self):
        """
        Lists all files in the Chainback ecosystem.

        :return: A list of files.
        """
        headers = {
            'Authorization': f'Bearer {self.archive_token}'
        }
        response = requests.get(f"{self.base_url}/files", headers=headers)

        # Check for successful retrieval
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve files: {response.text}")

        return response.json()

# Example usage
if __name__ == "__main__":
    # Replace 'your_archive_token' with your actual $ARCHIVE token
    archive_token = 'your_archive_token'
    file_sharing = ChainbackFileSharing(archive_token)

    try:
        # Upload a file
        upload_response = file_sharing.upload_file('path/to/your/file.txt')
        print("File uploaded successfully:", upload_response)

        # List files
        files = file_sharing.list_files()
        print("Files in the ecosystem:", files)

        # Download a file (replace 'file_id' with an actual file ID)
        file_id = upload_response['id']  # Assuming the response contains the file ID
        file_sharing.download_file(file_id, 'path/to/download/file.txt')
        print("File downloaded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
