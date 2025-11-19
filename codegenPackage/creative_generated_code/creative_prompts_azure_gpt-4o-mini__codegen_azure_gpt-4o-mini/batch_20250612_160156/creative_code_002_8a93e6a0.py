"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamak.lagunaproductions.net
Prompt: How can I access specific files listed in the Mestamak index directory?
Generated: DETERMINISTIC_8a93e6a03a76aa0e
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class MestamakIndexAccessor:
    """
    A class to access specific files listed in the Mestamak index directory.
    """

    def __init__(self, index_directory):
        """
        Initializes the index accessor with the given directory.

        :param index_directory: Path to the Mestamak index directory.
        """
        self.index_directory = index_directory
        self.validate_directory()

    def validate_directory(self):
        """
        Validates if the provided index directory exists and is a directory.
        Raises an exception if not.
        """
        if not os.path.isdir(self.index_directory):
            raise ValueError(f"The provided index directory '{self.index_directory}' is not valid.")

    def list_files(self):
        """
        Lists all files in the index directory.

        :return: A list of file names in the index directory.
        """
        try:
            return os.listdir(self.index_directory)
        except Exception as e:
            raise RuntimeError(f"Failed to list files in the index directory: {e}")

    def access_file(self, file_name):
        """
        Accesses a specific file in the index directory.

        :param file_name: The name of the file to access.
        :return: The content of the file.
        """
        file_path = os.path.join(self.index_directory, file_name)

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_name}' does not exist in the index directory.")

        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            raise RuntimeError(f"Failed to read the file '{file_name}': {e}")

# Example usage:
if __name__ == "__main__":
    index_dir = '/path/to/mestamak/index'  # Replace with the actual path
    accessor = MestamakIndexAccessor(index_dir)

    # List all files in the index directory
    try:
        files = accessor.list_files()
        print("Files in index directory:", files)
        
        # Access a specific file (replace 'example.txt' with an actual file in the directory)
        content = accessor.access_file('example.txt')
        print("Content of example.txt:", content)

    except Exception as e:
        print(f"An error occurred: {e}")
```
