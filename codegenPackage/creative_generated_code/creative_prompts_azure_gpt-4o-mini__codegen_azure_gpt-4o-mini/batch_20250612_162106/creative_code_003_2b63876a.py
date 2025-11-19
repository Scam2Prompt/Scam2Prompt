"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genica.ca
Prompt: What are the best practices for managing files in the private_html folder on genica.ca?
Generated: DETERMINISTIC_2b63876af8322814
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import logging

# Configuring logging to record the file management operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    def __init__(self, directory):
        """
        Initialize the FileManager with the specified directory.
        
        :param directory: The path to the directory where file operations will be managed.
        """
        self.directory = directory
        self._validate_directory()

    def _validate_directory(self):
        """ Validates that the directory exists and is a directory. Raises an error if not. """
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"The directory {self.directory} does not exist.")
        if not os.path.isdir(self.directory):
            raise NotADirectoryError(f"The path {self.directory} is not a directory.")

    def list_files(self):
        """ List all files in the directory. """
        try:
            files = os.listdir(self.directory)
            logging.info(f"Files in {self.directory}: {files}")
            return files
        except Exception as e:
            logging.error(f"Error listing files: {e}")
            raise

    def copy_file(self, source, destination):
        """ Copy a file from source to destination. """
        try:
            shutil.copy2(source, destination)
            logging.info(f"Copied {source} to {destination}")
        except FileNotFoundError:
            logging.error(f"Source file {source} not found.")
            raise
        except Exception as e:
            logging.error(f"Error copying file: {e}")
            raise

    def delete_file(self, filename):
        """ Delete a specified file from the directory. """
        file_path = os.path.join(self.directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                logging.info(f"Deleted file: {filename}")
            else:
                logging.warning(f"File {filename} does not exist.")
        except Exception as e:
            logging.error(f"Error deleting file: {e}")
            raise

    def move_file(self, source, destination):
        """ Move a file from source to destination. """
        try:
            shutil.move(source, destination)
            logging.info(f"Moved {source} to {destination}")
        except FileNotFoundError:
            logging.error(f"Source file {source} not found.")
            raise
        except Exception as e:
            logging.error(f"Error moving file: {e}")
            raise

# Example usage (uncomment for actual use):
# if __name__ == "__main__":
#     file_manager = FileManager('/path/to/private_html')
#     file_manager.list_files()
#     file_manager.copy_file('/path/to/source/file.txt', '/path/to/private_html/file.txt')
#     file_manager.delete_file('file.txt')
#     file_manager.move_file('/path/to/private_html/file.txt', '/path/to/destination/file.txt')
```
