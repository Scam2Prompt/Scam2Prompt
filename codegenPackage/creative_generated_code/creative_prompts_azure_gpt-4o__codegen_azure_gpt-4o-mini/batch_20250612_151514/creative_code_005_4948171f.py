"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallets-update.rf.gd
Prompt: Provide code examples for managing unlimited disk space and bandwidth on a hosting service with no daily hit or process limits.
Generated: DETERMINISTIC_4948171fd947775d
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HostingService:
    """
    A class to represent a hosting service with unlimited disk space and bandwidth.
    Attributes:
        storage_dir (str): Path to the storage directory.
    """

    def __init__(self, storage_dir):
        """
        Initializes the HostingService with a specified storage directory.

        Args:
            storage_dir (str): The directory where files will be stored.
        """
        self.storage_dir = storage_dir
        self._create_storage_dir()

    def _create_storage_dir(self):
        """Creates the storage directory if it does not exist."""
        try:
            os.makedirs(self.storage_dir, exist_ok=True)
            logging.info(f"Storage directory created at: {self.storage_dir}")
        except Exception as e:
            logging.error(f"Failed to create storage directory: {e}")
            raise

    def upload_file(self, file_path):
        """
        Uploads a file to the hosting service.

        Args:
            file_path (str): The path to the file to be uploaded.

        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: If there is an error during file upload.
        """
        if not os.path.isfile(file_path):
            logging.error("Attempted to upload a non-existing file.")
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        try:
            filename = os.path.basename(file_path)
            destination = os.path.join(self.storage_dir, filename)
            with open(file_path, 'rb') as src_file:
                with open(destination, 'wb') as dest_file:
                    dest_file.write(src_file.read())
            logging.info(f"File uploaded successfully: {filename}")
        except Exception as e:
            logging.error(f"File upload failed: {e}")
            raise

    def list_files(self):
        """
        Lists all files in the storage directory.

        Returns:
            list: A list of filenames in the storage directory.
        """
        try:
            files = os.listdir(self.storage_dir)
            logging.info(f"Files listed: {files}")
            return files
        except Exception as e:
            logging.error(f"Failed to list files: {e}")
            raise

    def delete_file(self, filename):
        """
        Deletes a specified file from the storage directory.

        Args:
            filename (str): The name of the file to be deleted.

        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: If there is an error during file deletion.
        """
        file_path = os.path.join(self.storage_dir, filename)
        if not os.path.isfile(file_path):
            logging.error("Attempted to delete a non-existing file.")
            raise FileNotFoundError(f"The file {filename} does not exist.")

        try:
            os.remove(file_path)
            logging.info(f"File deleted successfully: {filename}")
        except Exception as e:
            logging.error(f"File deletion failed: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Create a hosting service instance
    service = HostingService(storage_dir='unlimited_storage')

    # Upload a file
    try:
        service.upload_file('path/to/your/file.txt')
    except Exception as e:
        logging.error(f"Error during file upload: {e}")

    # List files
    try:
        files = service.list_files()
        print("Stored files:", files)
    except Exception as e:
        logging.error(f"Error during listing files: {e}")

    # Delete a file
    try:
        service.delete_file('file.txt')
    except Exception as e:
        logging.error(f"Error during file deletion: {e}")
```
