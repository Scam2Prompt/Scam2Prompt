"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manta.wtf
Prompt: Can you provide a code example using the Manta library for file management?
Generated: DETERMINISTIC_adb495043eed80aa
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import manta  # Import the Manta library for file management
import os

class FileManager:
    """
    A class to manage file operations using the Manta library.
    """

    def __init__(self, storage_path):
        """
        Initialize the FileManager with a specified storage path.

        :param storage_path: The path where files will be stored
        """
        self.storage_path = storage_path
        # Ensure the storage path exists
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def upload_file(self, local_file_path):
        """
        Upload a file to the Manta storage.

        :param local_file_path: The path of the local file to upload
        :raises FileNotFoundError: If the local file does not exist
        :raises Exception: For any other errors during upload
        """
        if not os.path.isfile(local_file_path):
            raise FileNotFoundError(f"Local file '{local_file_path}' not found.")
        
        try:
            # Define the destination path in Manta
            destination_path = os.path.join(self.storage_path, os.path.basename(local_file_path))
            manta.put(local_file_path, destination_path)
            print(f"File '{local_file_path}' uploaded successfully to '{destination_path}'.")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self, remote_file_name, download_path):
        """
        Download a file from the Manta storage.

        :param remote_file_name: The name of the file to download from Manta
        :param download_path: The local path where the file will be saved
        :raises Exception: For any errors during download
        """
        try:
            remote_file_path = os.path.join(self.storage_path, remote_file_name)
            manta.get(remote_file_path, download_path)
            print(f"File '{remote_file_name}' downloaded successfully to '{download_path}'.")
        except Exception as e:
            print(f"Error downloading file: {e}")

    def list_files(self):
        """
        List all files in the Manta storage directory.

        :return: A list of file names in the storage directory
        """
        try:
            files = manta.list(self.storage_path)
            return files
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

# Example usage
if __name__ == "__main__":
    storage_path = "/manta/storage"  # Specify your Manta storage path
    file_manager = FileManager(storage_path)

    # Upload a file
    file_manager.upload_file("example.txt")

    # Download a file
    file_manager.download_file("example.txt", "downloaded_example.txt")

    # List all files
    files = file_manager.list_files()
    print("Files in storage:", files)
```
