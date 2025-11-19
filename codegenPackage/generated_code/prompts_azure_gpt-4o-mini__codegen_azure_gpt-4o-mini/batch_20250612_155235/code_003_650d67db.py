"""
Generated Code Metadata:
========================
Original URL: https://inovarerep.com.br
Prompt: What are the best practices for managing files in the public_html directory of a web hosting service?
Generated: DETERMINISTIC_650d67db538b6415
Batch ID: 20250612_155235
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
from pathlib import Path

class PublicHtmlManager:
    """
    A class to manage files in the public_html directory of a web hosting service.
    """

    def __init__(self, public_html_path):
        """
        Initializes the PublicHtmlManager with the path to the public_html directory.

        :param public_html_path: Path to the public_html directory.
        """
        self.public_html_path = Path(public_html_path)

        # Ensure the public_html directory exists
        if not self.public_html_path.is_dir():
            raise FileNotFoundError(f"The directory {self.public_html_path} does not exist.")

    def list_files(self):
        """
        Lists all files in the public_html directory.

        :return: A list of file names in the directory.
        """
        try:
            return [file.name for file in self.public_html_path.iterdir() if file.is_file()]
        except Exception as e:
            raise RuntimeError(f"Error listing files: {e}")

    def upload_file(self, source_path):
        """
        Uploads a file to the public_html directory.

        :param source_path: Path to the file to be uploaded.
        """
        try:
            source = Path(source_path)
            if not source.is_file():
                raise FileNotFoundError(f"The file {source_path} does not exist.")

            shutil.copy(source, self.public_html_path)
            print(f"Uploaded {source.name} to {self.public_html_path}")
        except Exception as e:
            raise RuntimeError(f"Error uploading file: {e}")

    def delete_file(self, filename):
        """
        Deletes a file from the public_html directory.

        :param filename: Name of the file to be deleted.
        """
        try:
            file_to_delete = self.public_html_path / filename
            if not file_to_delete.is_file():
                raise FileNotFoundError(f"The file {filename} does not exist in {self.public_html_path}.")

            file_to_delete.unlink()
            print(f"Deleted {filename} from {self.public_html_path}")
        except Exception as e:
            raise RuntimeError(f"Error deleting file: {e}")

    def move_file(self, filename, target_directory):
        """
        Moves a file from the public_html directory to a target directory.

        :param filename: Name of the file to be moved.
        :param target_directory: Path to the target directory.
        """
        try:
            file_to_move = self.public_html_path / filename
            if not file_to_move.is_file():
                raise FileNotFoundError(f"The file {filename} does not exist in {self.public_html_path}.")

            target_path = Path(target_directory)
            if not target_path.is_dir():
                raise FileNotFoundError(f"The target directory {target_directory} does not exist.")

            shutil.move(file_to_move, target_path)
            print(f"Moved {filename} to {target_directory}")
        except Exception as e:
            raise RuntimeError(f"Error moving file: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        manager = PublicHtmlManager('/path/to/public_html')
        print(manager.list_files())
        manager.upload_file('/path/to/local/file.txt')
        manager.delete_file('file.txt')
        manager.move_file('file_to_move.txt', '/path/to/target_directory')
    except Exception as e:
        print(f"An error occurred: {e}")
```
