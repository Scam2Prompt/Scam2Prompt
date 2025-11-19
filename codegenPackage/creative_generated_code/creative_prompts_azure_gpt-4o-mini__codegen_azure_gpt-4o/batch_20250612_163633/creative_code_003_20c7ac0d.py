"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecataloguegoodies-pepsico.com
Prompt: How can I implement a file retrieval system that mimics the structure of the eCatalog Goodies PepsiCo index page?
Generated: DETERMINISTIC_20c7ac0db204f904
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class FileRetrievalSystem:
    """
    A class to mimic the structure of an eCatalog index page for file retrieval operations.
    """

    def __init__(self, base_directory):
        """
        Initialize the file retrieval system with a base directory.
        :param base_directory: The root directory where files are stored.
        """
        self.base_directory = base_directory

    def list_files(self, relative_path=""):
        """
        List all files and directories in the given relative path.
        :param relative_path: The relative path within the base directory to list files.
        :return: A dictionary representing file structure.
                 Keys are directory names, values are lists of files or subdirectories.
        """
        try:
            full_path = os.path.join(self.base_directory, relative_path)
            if not os.path.exists(full_path):
                raise FileNotFoundError(f"Path not found: {full_path}")

            structure = {}
            for root, dirs, files in os.walk(full_path):
                relative_root = os.path.relpath(root, self.base_directory)
                structure[relative_root] = {
                    "directories": dirs,
                    "files": files
                }
                # Only process the top-level directory if relative_path is provided
                if relative_path:
                    break
            return structure
        except FileNotFoundError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def retrieve_file(self, relative_file_path):
        """
        Retrieve the contents of a file given its relative path.
        :param relative_file_path: The relative path of the file to retrieve.
        :return: The content of the file as a string or an error message.
        """
        try:
            full_file_path = os.path.join(self.base_directory, relative_file_path)
            if not os.path.exists(full_file_path):
                raise FileNotFoundError(f"File not found: {full_file_path}")

            with open(full_file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

# Example Usage
if __name__ == "__main__":
    # Specify the base directory (change this to a valid path on your system)
    base_dir = "/path/to/ecatalog/goodies/pepsico"

    # Initialize the file retrieval system
    frs = FileRetrievalSystem(base_directory=base_dir)

    # List files and directories at the root level
    root_structure = frs.list_files()
    print("Root Structure:", root_structure)

    # Retrieve a specific file's content
    file_content = frs.retrieve_file("sample.txt")
    print("File Content:", file_content)
```
