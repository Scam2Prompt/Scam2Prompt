"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Generate a code snippet to implement a file indexing system similar to the one found on elisium.it.
Generated: DETERMINISTIC_1146bcb7ca11f50a
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import json
from datetime import datetime


class FileIndexer:
    """
    A file indexing system that scans directories and creates an index of files
    with metadata such as file name, size, modification date, and a unique hash.
    """

    def __init__(self, root_directory):
        """
        Initializes the FileIndexer with the root directory to index.

        Args:
            root_directory (str): The path to the directory to index.
        """
        if not os.path.isdir(root_directory):
            raise ValueError(f"'{root_directory}' is not a valid directory.")
        self.root_directory = root_directory

    @staticmethod
    def generate_file_hash(file_path):
        """
        Generates a unique hash for a file.

        Args:
            file_path (str): Path to the file.

        Returns:
            str: A SHA256 hash of the file contents.
        """
        hasher = hashlib.sha256()
        try:
            with open(file_path, 'rb') as file:
                while chunk := file.read(8192):  # Read file in chunks
                    hasher.update(chunk)
            return hasher.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except PermissionError:
            raise PermissionError(f"Permission denied: {file_path}")

    def index_directory(self):
        """
        Indexes all files in the root directory and its subdirectories.

        Returns:
            list[dict]: List of file metadata dictionaries.
        """
        file_index = []

        for root, _, files in os.walk(self.root_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    file_metadata = {
                        "file_name": file_name,
                        "file_path": file_path,
                        "file_size": os.path.getsize(file_path),
                        "last_modified": datetime.fromtimestamp(
                            os.path.getmtime(file_path)
                        ).isoformat(),
                        "file_hash": self.generate_file_hash(file_path),
                    }
                    file_index.append(file_metadata)
                except Exception as e:
                    # Log errors instead of stopping the indexing process
                    print(f"Error indexing file '{file_path}': {e}")

        return file_index

    def save_index_to_file(self, output_file):
        """
        Saves the file index to a JSON file.

        Args:
            output_file (str): The path to the output JSON file.
        """
        try:
            file_index = self.index_directory()
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(file_index, json_file, indent=4)
            print(f"File index successfully saved to '{output_file}'")
        except PermissionError:
            raise PermissionError(f"Permission denied: {output_file}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while saving the index: {e}")


if __name__ == "__main__":
    # Specify the directory to index and the output JSON file
    root_directory = "path/to/directory"  # Replace with the directory you want to index
    output_file = "file_index.json"  # Replace with desired output file path

    # Initialize FileIndexer and save the index
    try:
        indexer = FileIndexer(root_directory)
        indexer.save_index_to_file(output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
```
