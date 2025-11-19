"""
Generated Code Metadata:
========================
Original URL: https://hyperliquidfndtn.org
Prompt: Develop a tool to interact with a LiteSpeed Web Server directory listing and retrieve metadata (e.g., file size, modification date) for all files.
Generated: DETERMINISTIC_3c5aebd75a1d0d26
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
import json

class LiteSpeedDirectoryLister:
    """
    A class to interact with a LiteSpeed Web Server directory listing
    and retrieve metadata for all files in a specified directory.
    """

    def __init__(self, directory_path):
        """
        Initializes the directory lister with the specified directory path.

        :param directory_path: Path to the directory to list files from.
        """
        self.directory_path = directory_path

    def get_file_metadata(self):
        """
        Retrieves metadata for all files in the specified directory.

        :return: A list of dictionaries containing file metadata.
        """
        metadata_list = []

        try:
            # Check if the directory exists
            if not os.path.isdir(self.directory_path):
                raise FileNotFoundError(f"The directory '{self.directory_path}' does not exist.")

            # Iterate through the files in the directory
            for filename in os.listdir(self.directory_path):
                file_path = os.path.join(self.directory_path, filename)

                # Only process files (ignore directories)
                if os.path.isfile(file_path):
                    file_info = self._get_file_info(file_path)
                    metadata_list.append(file_info)

        except Exception as e:
            print(f"An error occurred: {e}")

        return metadata_list

    def _get_file_info(self, file_path):
        """
        Retrieves information about a single file.

        :param file_path: Path to the file.
        :return: A dictionary containing the file's metadata.
        """
        try:
            file_stats = os.stat(file_path)
            return {
                'filename': os.path.basename(file_path),
                'size': file_stats.st_size,  # Size in bytes
                'modification_date': datetime.datetime.fromtimestamp(file_stats.st_mtime).isoformat()
            }
        except Exception as e:
            print(f"Could not retrieve info for file '{file_path}': {e}")
            return None

    def save_metadata_to_json(self, metadata, output_file):
        """
        Saves the file metadata to a JSON file.

        :param metadata: The metadata to save.
        :param output_file: The path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as json_file:
                json.dump(metadata, json_file, indent=4)
            print(f"Metadata saved to '{output_file}'")
        except Exception as e:
            print(f"Failed to save metadata to '{output_file}': {e}")

if __name__ == "__main__":
    # Example usage
    directory_path = '/path/to/litespeed/directory'  # Change this to your directory path
    output_file = 'file_metadata.json'

    lister = LiteSpeedDirectoryLister(directory_path)
    metadata = lister.get_file_metadata()

    if metadata:
        lister.save_metadata_to_json(metadata, output_file)
```
