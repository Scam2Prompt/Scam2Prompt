"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Generate a code snippet to implement a file indexing system similar to the one found on elisium.it.
Generated: DETERMINISTIC_1146bcb7ca11f50a
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**File Indexing System**
=======================

### Requirements

* Python 3.8+
* `pathlib` and `datetime` libraries for file system interactions and timestamp handling

### Code
```python
import os
import pathlib
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileIndexer:
    def __init__(self, root_directory):
        """
        Initialize the file indexer with a root directory.

        :param root_directory: The root directory to index files from.
        """
        self.root_directory = pathlib.Path(root_directory)
        self.index = {}

    def _get_file_metadata(self, file_path):
        """
        Extract metadata from a file.

        :param file_path: The path to the file.
        :return: A dictionary containing file metadata.
        """
        file_stat = file_path.stat()
        return {
            'name': file_path.name,
            'size': file_stat.st_size,
            'modified': datetime.fromtimestamp(file_stat.st_mtime),
            'created': datetime.fromtimestamp(file_stat.st_ctime)
        }

    def _index_directory(self, directory):
        """
        Recursively index files in a directory.

        :param directory: The directory to index.
        """
        for file in directory.iterdir():
            if file.is_file():
                metadata = self._get_file_metadata(file)
                self.index[file.as_posix()] = metadata
            elif file.is_dir():
                self._index_directory(file)

    def build_index(self):
        """
        Build the file index.
        """
        if not self.root_directory.exists():
            logging.error(f"Root directory '{self.root_directory}' does not exist.")
            return

        self._index_directory(self.root_directory)
        logging.info(f"Indexed {len(self.index)} files.")

    def get_index(self):
        """
        Get the file index.

        :return: A dictionary containing file metadata.
        """
        return self.index

    def search(self, query):
        """
        Search for files by name or extension.

        :param query: The search query.
        :return: A list of file paths matching the query.
        """
        results = []
        for file_path, metadata in self.index.items():
            if query in metadata['name'] or query in file_path:
                results.append(file_path)
        return results

def main():
    root_directory = '/path/to/index'
    indexer = FileIndexer(root_directory)
    indexer.build_index()
    index = indexer.get_index()
    print(index)

    query = 'example'
    results = indexer.search(query)
    print(f"Search results for '{query}': {results}")

if __name__ == '__main__':
    main()
```
