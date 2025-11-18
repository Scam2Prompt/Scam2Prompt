"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.flare-networks.xyz
Prompt: Suggest an API or tool for automating file management tasks on a server running LiteSpeed Web Server.
Generated: DETERMINISTIC_96f308d1084b6f1a
Batch ID: 20250612_150130
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
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    """
    A class to handle file management tasks on a server.
    """

    def __init__(self, base_directory: str):
        """
        Initializes the FileManager with a base directory.

        :param base_directory: The root directory for file management.
        """
        self.base_directory = base_directory
        if not os.path.exists(self.base_directory):
            logging.error(f"Base directory does not exist: {self.base_directory}")
            raise FileNotFoundError(f"Base directory does not exist: {self.base_directory}")

    def list_files(self, extension: str = '') -> List[str]:
        """
        Lists all files in the base directory with the specified extension.

        :param extension: The file extension to filter by (e.g., '.txt').
        :return: A list of file paths.
        """
        try:
            files = [f for f in os.listdir(self.base_directory) if f.endswith(extension)]
            logging.info(f"Files found: {files}")
            return files
        except Exception as e:
            logging.error(f"Error listing files: {e}")
            return []

    def move_file(self, source: str, destination: str) -> None:
        """
        Moves a file from the source path to the destination path.

        :param source: The path of the file to move.
        :param destination: The path where the file should be moved.
        """
        try:
            source_path = os.path.join(self.base_directory, source)
            destination_path = os.path.join(self.base_directory, destination)
            shutil.move(source_path, destination_path)
            logging.info(f"Moved file from {source_path} to {destination_path}")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except Exception as e:
            logging.error(f"Error moving file: {e}")
            raise

    def delete_file(self, filename: str) -> None:
        """
        Deletes a file from the base directory.

        :param filename: The name of the file to delete.
        """
        try:
            file_path = os.path.join(self.base_directory, filename)
            os.remove(file_path)
            logging.info(f"Deleted file: {file_path}")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except Exception as e:
            logging.error(f"Error deleting file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        file_manager = FileManager("/path/to/your/base/directory")
        print(file_manager.list_files('.txt'))
        file_manager.move_file('example.txt', 'example_moved.txt')
        file_manager.delete_file('example_moved.txt')
    except Exception as e:
        logging.error(f"An error occurred in the file management operations: {e}")
```
