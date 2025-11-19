"""
Generated Code Metadata:
========================
Original URL: https://dalgarno.ie
Prompt: What are the best practices for managing files in a new hosting account using cPanel?
Generated: DETERMINISTIC_c86c7d68e585cf7f
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    def __init__(self, base_directory):
        """
        Initialize the FileManager with a base directory.

        :param base_directory: The root directory for file management.
        """
        self.base_directory = base_directory
        self.ensure_directory_exists(self.base_directory)

    def ensure_directory_exists(self, directory):
        """
        Ensure that the specified directory exists; if not, create it.

        :param directory: The directory to check/create.
        """
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logging.info(f"Created directory: {directory}")
            else:
                logging.info(f"Directory already exists: {directory}")
        except Exception as e:
            logging.error(f"Error creating directory {directory}: {e}")

    def upload_file(self, source_path, destination_filename):
        """
        Upload a file from the local system to the specified directory.

        :param source_path: The path of the file to upload.
        :param destination_filename: The name to save the file as in the destination.
        """
        destination_path = os.path.join(self.base_directory, destination_filename)
        try:
            shutil.copy2(source_path, destination_path)
            logging.info(f"Uploaded file from {source_path} to {destination_path}")
        except FileNotFoundError:
            logging.error(f"Source file not found: {source_path}")
        except Exception as e:
            logging.error(f"Error uploading file: {e}")

    def delete_file(self, filename):
        """
        Delete a file from the specified directory.

        :param filename: The name of the file to delete.
        """
        file_path = os.path.join(self.base_directory, filename)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logging.info(f"Deleted file: {file_path}")
            else:
                logging.warning(f"File not found for deletion: {file_path}")
        except Exception as e:
            logging.error(f"Error deleting file {file_path}: {e}")

    def list_files(self):
        """
        List all files in the specified directory.

        :return: A list of filenames in the directory.
        """
        try:
            files = os.listdir(self.base_directory)
            logging.info(f"Files in {self.base_directory}: {files}")
            return files
        except Exception as e:
            logging.error(f"Error listing files in {self.base_directory}: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Set the base directory for file management
    base_dir = "/path/to/your/cpanel/directory"
    
    # Create a FileManager instance
    file_manager = FileManager(base_dir)

    # Upload a file
    file_manager.upload_file("/path/to/local/file.txt", "uploaded_file.txt")

    # List files
    file_manager.list_files()

    # Delete a file
    file_manager.delete_file("uploaded_file.txt")
```
