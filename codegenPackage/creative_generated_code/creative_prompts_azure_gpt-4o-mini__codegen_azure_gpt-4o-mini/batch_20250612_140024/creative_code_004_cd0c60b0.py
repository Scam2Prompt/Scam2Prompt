"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: What libraries can I use to automate file management tasks on the e-Kraken server?
Generated: DETERMINISTIC_cd0c60b0cf4b4419
Batch ID: 20250612_140024
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
from pathlib import Path

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    """A class to handle file management tasks on the e-Kraken server."""

    def __init__(self, base_directory: str):
        """
        Initialize the FileManager with a base directory.

        :param base_directory: The base directory where file operations will take place.
        """
        self.base_directory = Path(base_directory)

        # Check if the provided base directory exists
        if not self.base_directory.exists() or not self.base_directory.is_dir():
            logging.error(f"The specified base directory does not exist: {self.base_directory}")
            raise ValueError(f"The specified base directory does not exist: {self.base_directory}")

    def list_files(self) -> list:
        """List all files in the base directory.

        :return: A list of file names in the base directory.
        """
        try:
            files = [f.name for f in self.base_directory.iterdir() if f.is_file()]
            logging.info("Files listed successfully.")
            return files
        except Exception as e:
            logging.error(f"Error listing files: {e}")
            raise

    def move_file(self, src: str, dest: str) -> None:
        """Move a file from source to destination.

        :param src: The source file path.
        :param dest: The destination file path.
        """
        try:
            source_path = self.base_directory / src
            destination_path = self.base_directory / dest

            shutil.move(str(source_path), str(destination_path))
            logging.info(f"File moved from {src} to {dest}.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except Exception as e:
            logging.error(f"Error moving file: {e}")
            raise

    def delete_file(self, filename: str) -> None:
        """Delete a file from the base directory.

        :param filename: The name of the file to delete.
        """
        try:
            file_path = self.base_directory / filename

            if file_path.exists():
                file_path.unlink()
                logging.info(f"File deleted: {filename}.")
            else:
                logging.warning(f"File not found for deletion: {filename}.")
        except Exception as e:
            logging.error(f"Error deleting file: {e}")
            raise

# Example of using the FileManager class (this should be removed or moved to a main guard in production)
if __name__ == "__main__":
    try:
        file_manager = FileManager('/path/to/e-Kraken')  # Replace with actual path
        print(file_manager.list_files())
        file_manager.move_file('test.txt', 'archive/test.txt')
        file_manager.delete_file('old_file.txt')
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
