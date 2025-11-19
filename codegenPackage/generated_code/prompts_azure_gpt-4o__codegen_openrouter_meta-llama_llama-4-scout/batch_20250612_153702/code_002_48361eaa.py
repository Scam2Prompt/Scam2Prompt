"""
Generated Code Metadata:
========================
Original URL: https://dustbox.netlify.app
Prompt: Generate code to create a file view interface similar to the one described on Dustbox.netlify.app.
Generated: DETERMINISTIC_48361eaae6ce34c4
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# file_view_interface.py

import os
import mimetypes
from datetime import datetime
from pathlib import Path

class FileViewInterface:
    """
    A class representing a file view interface.

    Attributes:
    ----------
    root_dir : str
        The root directory to view files from.

    Methods:
    -------
    list_files()
        Lists all files in the root directory.
    get_file_info(file_path)
        Gets information about a specific file.
    """

    def __init__(self, root_dir):
        """
        Initializes the FileViewInterface.

        Parameters:
        ----------
        root_dir : str
            The root directory to view files from.
        """
        self.root_dir = root_dir

    def list_files(self):
        """
        Lists all files in the root directory.

        Returns:
        -------
        list
            A list of dictionaries containing file information.
        """
        try:
            files = []
            for file_path in Path(self.root_dir).iterdir():
                if file_path.is_file():
                    file_info = self.get_file_info(file_path)
                    files.append(file_info)
            return files
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    def get_file_info(self, file_path):
        """
        Gets information about a specific file.

        Parameters:
        ----------
        file_path : Path
            The path to the file.

        Returns:
        -------
        dict
            A dictionary containing file information.
        """
        try:
            file_info = {
                "name": file_path.name,
                "size": self.format_size(file_path.stat().st_size),
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "type": self.get_mime_type(file_path)
            }
            return file_info
        except Exception as e:
            print(f"Error getting file info: {e}")
            return {}

    @staticmethod
    def format_size(size_bytes):
        """
        Formats a size in bytes to a human-readable format.

        Parameters:
        ----------
        size_bytes : int
            The size in bytes.

        Returns:
        -------
        str
            The formatted size.
        """
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}B"
            size_bytes /= 1024
        return f"{size_bytes:.2f} EB"

    @staticmethod
    def get_mime_type(file_path):
        """
        Gets the MIME type of a file.

        Parameters:
        ----------
        file_path : Path
            The path to the file.

        Returns:
        -------
        str
            The MIME type.
        """
        return mimetypes.guess_type(file_path.as_posix())[0] or "Unknown"


def main():
    root_dir = "."  # current directory
    file_view = FileViewInterface(root_dir)
    files = file_view.list_files()
    for file in files:
        print(file)


if __name__ == "__main__":
    main()
```
