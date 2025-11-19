"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://injective.events
Prompt: Write a Python script that integrates with Dropbox API to automatically back up files from a specified directory.
Generated: DETERMINISTIC_db8ffbf3b3519266
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import dropbox
from dropbox.exceptions import AuthError, ApiError


class DropboxBackup:
    """
    A class to handle Dropbox API integration for backing up files from a specified directory.
    """

    def __init__(self, access_token: str, local_directory: str, dropbox_directory: str):
        """
        Initialize the DropboxBackup class.

        :param access_token: Dropbox API access token.
        :param local_directory: Path to the local directory containing files to back up.
        :param dropbox_directory: Dropbox folder path where files will be uploaded.
        """
        self.access_token = access_token
        self.local_directory = local_directory
        self.dropbox_directory = dropbox_directory
        self.dbx = self._connect_to_dropbox()

    def _connect_to_dropbox(self):
        """
        Establish a connection to Dropbox using the API access token.

        :return: Dropbox client instance.
        """
        try:
            dbx = dropbox.Dropbox(self.access_token)
            # Test authentication
            dbx.users_get_current_account()
            return dbx
        except AuthError as e:
            print("Error: Unable to authenticate with Dropbox. Check your access token.")
            raise e

    def upload_file(self, local_file_path: str, dropbox_file_path: str):
        """
        Upload a single file to Dropbox.

        :param local_file_path: Path to the local file to upload.
        :param dropbox_file_path: Path in the Dropbox folder to upload the file to.
        """
        try:
            with open(local_file_path, "rb") as file:
                self.dbx.files_upload(file.read(), dropbox_file_path, mode=dropbox.files.WriteMode("overwrite"))
            print(f"Uploaded: {local_file_path} -> {dropbox_file_path}")
        except FileNotFoundError:
            print(f"Error: File not found - {local_file_path}")
        except ApiError as e:
            print(f"Error: Failed to upload {local_file_path}. {e}")

    def backup_directory(self):
        """
        Back up all files from the specified local directory to the Dropbox folder.
        """
        if not os.path.exists(self.local_directory):
            print(f"Error: Local directory does not exist - {self.local_directory}")
            return

        for root, _, files in os.walk(self.local_directory):
            for file_name in files:
                local_file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_file_path, self.local_directory)
                dropbox_file_path = os.path.join(self.dropbox_directory, relative_path).replace("\\", "/")  # Normalize path
                self.upload_file(local_file_path, dropbox_file_path)


if __name__ == "__main__":
    # Replace these with your actual values
    ACCESS_TOKEN = "your_dropbox_access_token_here"  # Obtain this from Dropbox App Console
    LOCAL_DIRECTORY = "/path/to/your/local/directory"
    DROPBOX_DIRECTORY = "/path/to/your/dropbox/folder"

    try:
        backup = DropboxBackup(ACCESS_TOKEN, LOCAL_DIRECTORY, DROPBOX_DIRECTORY)
        backup.backup_directory()
    except Exception as e:
        print(f"An error occurred: {e}")
```
