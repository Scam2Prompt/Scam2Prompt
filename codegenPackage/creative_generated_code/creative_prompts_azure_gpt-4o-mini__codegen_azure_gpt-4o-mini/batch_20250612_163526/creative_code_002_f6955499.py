"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Write a script to manage file indexing on a LiteSpeed web server, similar to the structure seen on perurest.com.
Generated: DETERMINISTIC_f6955499556f288a
Batch ID: 20250612_163526
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
import logging
from pathlib import Path

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileIndexer:
    def __init__(self, root_directory: str, output_file: str):
        """
        Initialize the FileIndexer with the root directory to index and the output file to save the index.

        :param root_directory: Directory to index files from
        :param output_file: File path to save the JSON index
        """
        self.root_directory = Path(root_directory)
        self.output_file = Path(output_file)

        if not self.root_directory.is_dir():
            logging.error(f"Provided root directory '{self.root_directory}' is not valid.")
            raise ValueError(f"Invalid directory: {self.root_directory}")

    def index_files(self):
        """
        Index files in the specified root directory and save the index to the output file.
        """
        logging.info(f"Starting to index files in '{self.root_directory}'")
        
        file_index = {}
        try:
            # Walk through the directory and index files
            for file_path in self.root_directory.rglob('*'):
                if file_path.is_file():
                    relative_path = file_path.relative_to(self.root_directory)
                    file_index[str(relative_path)] = {
                        "size": os.path.getsize(file_path),
                        "modified_time": os.path.getmtime(file_path)
                    }
                    logging.debug(f"Indexed file: {relative_path}")

            # Save the index to the output file
            self.save_index(file_index)
        except Exception as e:
            logging.error(f"Error during file indexing: {e}")
            raise

    def save_index(self, file_index: dict):
        """
        Save the indexed file information to a JSON file.

        :param file_index: Dictionary containing file information
        """
        try:
            with open(self.output_file, 'w', encoding='utf-8') as json_file:
                json.dump(file_index, json_file, indent=4)
            logging.info(f"File index saved to '{self.output_file}'")
        except IOError as e:
            logging.error(f"Failed to save index to '{self.output_file}': {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        indexer = FileIndexer(root_directory='/path/to/your/web/root', output_file='file_index.json')
        indexer.index_files()
    except Exception as e:
        logging.critical(f"Application error: {e}")
```
