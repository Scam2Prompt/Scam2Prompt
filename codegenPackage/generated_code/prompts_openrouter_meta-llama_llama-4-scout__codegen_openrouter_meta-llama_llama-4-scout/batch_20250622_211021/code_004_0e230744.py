"""
Generated Code Metadata:
========================
Original URL: https://npcgrant.online
Prompt: Provide an example of how to programmatically manage files and directories on a web server using a specific library or API.
Generated: DETERMINISTIC_0e23074421adb04c
Batch ID: 20250622_211021
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

class FileManager:
    """
    A class used to manage files and directories on a web server.

    Attributes:
    ----------
    root_dir : str
        The root directory of the file system.

    Methods:
    -------
    create_directory(dir_path)
        Creates a new directory at the specified path.
    delete_directory(dir_path)
        Deletes a directory at the specified path.
    list_files(dir_path)
        Lists all files in the specified directory.
    upload_file(src_path, dest_path)
        Uploads a file from the source path to the destination path.
    download_file(src_path, dest_path)
        Downloads a file from the source path to the destination path.
    delete_file(file_path)
        Deletes a file at the specified path.
    """

    def __init__(self, root_dir):
        """
        Initializes the FileManager with the root directory.

        Parameters:
        ----------
        root_dir : str
            The root directory of the file system.
        """
        self.root_dir = root_dir

    def create_directory(self, dir_path):
        """
        Creates a new directory at the specified path.

        Parameters:
        ----------
        dir_path : str
            The path of the directory to create.

        Raises:
        ------
        FileExistsError
            If the directory already exists.
        OSError
            If an error occurs while creating the directory.
        """
        try:
            dir_path = os.path.join(self.root_dir, dir_path)
            Path(dir_path).mkdir(parents=True, exist_ok=False)
            print(f"Directory '{dir_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{dir_path}' already exists.")
        except OSError as e:
            print(f"Error creating directory '{dir_path}': {e}")

    def delete_directory(self, dir_path):
        """
        Deletes a directory at the specified path.

        Parameters:
        ----------
        dir_path : str
            The path of the directory to delete.

        Raises:
        ------
        FileNotFoundError
            If the directory does not exist.
        OSError
            If an error occurs while deleting the directory.
        """
        try:
            dir_path = os.path.join(self.root_dir, dir_path)
            shutil.rmtree(dir_path)
            print(f"Directory '{dir_path}' deleted successfully.")
        except FileNotFoundError:
            print(f"Directory '{dir_path}' not found.")
        except OSError as e:
            print(f"Error deleting directory '{dir_path}': {e}")

    def list_files(self, dir_path):
        """
        Lists all files in the specified directory.

        Parameters:
        ----------
        dir_path : str
            The path of the directory to list files from.

        Returns:
        -------
        list
            A list of file names in the directory.

        Raises:
        ------
        FileNotFoundError
            If the directory does not exist.
        """
        try:
            dir_path = os.path.join(self.root_dir, dir_path)
            return os.listdir(dir_path)
        except FileNotFoundError:
            print(f"Directory '{dir_path}' not found.")
            return []

    def upload_file(self, src_path, dest_path):
        """
        Uploads a file from the source path to the destination path.

        Parameters:
        ----------
        src_path : str
            The source path of the file.
        dest_path : str
            The destination path of the file.

        Raises:
        ------
        FileNotFoundError
            If the source file does not exist.
        OSError
            If an error occurs while uploading the file.
        """
        try:
            dest_path = os.path.join(self.root_dir, dest_path)
            shutil.copy(src_path, dest_path)
            print(f"File '{src_path}' uploaded to '{dest_path}' successfully.")
        except FileNotFoundError:
            print(f"File '{src_path}' not found.")
        except OSError as e:
            print(f"Error uploading file '{src_path}': {e}")

    def download_file(self, src_path, dest_path):
        """
        Downloads a file from the source path to the destination path.

        Parameters:
        ----------
        src_path : str
            The source path of the file.
        dest_path : str
            The destination path of the file.

        Raises:
        ------
        FileNotFoundError
            If the source file does not exist.
        OSError
            If an error occurs while downloading the file.
        """
        try:
            src_path = os.path.join(self.root_dir, src_path)
            shutil.copy(src_path, dest_path)
            print(f"File '{src_path}' downloaded to '{dest_path}' successfully.")
        except FileNotFoundError:
            print(f"File '{src_path}' not found.")
        except OSError as e:
            print(f"Error downloading file '{src_path}': {e}")

    def delete_file(self, file_path):
        """
        Deletes a file at the specified path.

        Parameters:
        ----------
        file_path : str
            The path of the file to delete.

        Raises:
        ------
        FileNotFoundError
            If the file does not exist.
        OSError
            If an error occurs while deleting the file.
        """
        try:
            file_path = os.path.join(self.root_dir, file_path)
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except OSError as e:
            print(f"Error deleting file '{file_path}': {e}")


if __name__ == "__main__":
    file_manager = FileManager("/path/to/root/dir")

    # Create a new directory
    file_manager.create_directory("new_directory")

    # List files in the root directory
    files = file_manager.list_files("")
    print(files)

    # Upload a file
    file_manager.upload_file("/path/to/local/file.txt", "file.txt")

    # Download a file
    file_manager.download_file("file.txt", "/path/to/local/")

    # Delete a file
    file_manager.delete_file("file.txt")

    # Delete a directory
    file_manager.delete_directory("new_directory")
```
