"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dalgarno.ie
Prompt: What are the best practices for managing files in a new hosting account using cPanel?
Generated: DETERMINISTIC_c86c7d68e585cf7f
Batch ID: 20250612_162753
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

class FileManager:
    """A class to manage files in a cPanel hosting environment."""
    
    def __init__(self, directory):
        """
        Initializes the FileManager with the specified directory.

        :param directory: Path to the directory to manage files.
        """
        self.directory = directory
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """Ensures that the specified directory exists."""
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            print(f"Directory created: {self.directory}")

    def upload_file(self, source_path):
        """
        Uploads a file to the managed directory.

        :param source_path: Path of the file to upload.
        :raises FileNotFoundError: If the source file does not exist.
        """
        if not os.path.isfile(source_path):
            raise FileNotFoundError(f"The file {source_path} does not exist.")

        shutil.copy(source_path, self.directory)
        print(f"File uploaded: {os.path.basename(source_path)} to {self.directory}")

    def list_files(self):
        """
        Lists all files in the managed directory.

        :return: A list of file names.
        """
        try:
            files = os.listdir(self.directory)
            print(f"Files in {self.directory}: {files}")
            return files
        except OSError as e:
            print(f"Error accessing directory: {e}")
            return []

    def delete_file(self, filename):
        """
        Deletes a specified file from the managed directory.

        :param filename: Name of the file to delete.
        :raises FileNotFoundError: If the file does not exist.
        """
        file_path = os.path.join(self.directory, filename)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {filename} does not exist.")

        os.remove(file_path)
        print(f"File deleted: {filename}")

    def move_file(self, filename, new_directory):
        """
        Moves a specified file to a new directory.

        :param filename: Name of the file to move.
        :param new_directory: Destination directory.
        :raises FileNotFoundError: If the file does not exist.
        :raises FileNotFoundError: If the destination directory does not exist.
        """
        if not os.path.isdir(new_directory):
            raise FileNotFoundError(f"The directory {new_directory} does not exist.")

        file_path = os.path.join(self.directory, filename)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {filename} does not exist.")

        shutil.move(file_path, new_directory)
        print(f"File moved: {filename} to {new_directory}")

# Example usage:
if __name__ == "__main__":
    # Replace 'your_directory_path_here' with the actual directory path in your cPanel account
    file_manager = FileManager('your_directory_path_here')
    
    # Example operations:
    try:
        file_manager.upload_file('path_to_local_file.txt')
        file_manager.list_files()
        file_manager.delete_file('path_to_local_file.txt')
        file_manager.move_file('file_to_move.txt', 'new_directory_path_here')
    except Exception as e:
        print(f"An error occurred: {e}")
```
