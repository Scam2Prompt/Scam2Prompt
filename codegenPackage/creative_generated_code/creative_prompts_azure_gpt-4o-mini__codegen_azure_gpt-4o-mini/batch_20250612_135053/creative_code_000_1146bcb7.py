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
import json
from typing import List, Dict

class FileIndexer:
    def __init__(self, directory: str):
        """
        Initializes the FileIndexer with the specified directory.

        :param directory: The directory to index files from.
        """
        self.directory = directory
        self.index = {}

    def index_files(self) -> None:
        """
        Indexes files in the specified directory and stores file metadata.
        """
        try:
            # Ensure the directory exists
            if not os.path.isdir(self.directory):
                raise FileNotFoundError(f"Directory not found: {self.directory}")

            # Walk through the directory
            for root, _, files in os.walk(self.directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    self.index[file] = self.get_file_metadata(file_path)

            print(f"Indexed {len(self.index)} files.")

        except Exception as e:
            print(f"Error indexing files: {e}")

    def get_file_metadata(self, file_path: str) -> Dict[str, str]:
        """
        Retrieves metadata for a file.

        :param file_path: The path of the file to retrieve metadata for.
        :return: A dictionary containing file metadata.
        """
        try:
            file_stats = os.stat(file_path)
            return {
                "size": file_stats.st_size,
                "created": file_stats.st_ctime,
                "modified": file_stats.st_mtime,
                "path": file_path
            }
        except Exception as e:
            print(f"Error retrieving metadata for {file_path}: {e}")
            return {}

    def save_index(self, output_file: str) -> None:
        """
        Saves the indexed files to a JSON file.

        :param output_file: The path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(self.index, f, indent=4)
            print(f"Index saved to {output_file}.")
        except Exception as e:
            print(f"Error saving index to file: {e}")

    def load_index(self, input_file: str) -> None:
        """
        Loads an index from a JSON file.

        :param input_file: The path to the input JSON file.
        """
        try:
            with open(input_file, 'r') as f:
                self.index = json.load(f)
            print(f"Index loaded from {input_file}.")
        except Exception as e:
            print(f"Error loading index from file: {e}")

# Example usage
if __name__ == "__main__":
    directory_to_index = "/path/to/directory"  # Specify the directory to index
    index_file = "file_index.json"              # Specify the output index file name

    file_indexer = FileIndexer(directory_to_index)
    file_indexer.index_files()
    file_indexer.save_index(index_file)

    # To load the index
    # file_indexer.load_index(index_file)
```
