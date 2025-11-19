"""
Generated Code Metadata:
========================
Original URL: https://contentxlabs.dev
Prompt: "Design a content metadata management system for AI licensing, inspired by ContentXLabs' approach to supporting metadata for mp4 files."
Generated: DETERMINISTIC_5657dd8c2cb09d8c
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Dict, Any, List

class MetadataManager:
    """
    A class to manage metadata for AI licensing of content files, specifically mp4 files.
    """

    def __init__(self, metadata_file: str):
        """
        Initializes the MetadataManager with a specified metadata file.

        :param metadata_file: Path to the JSON file where metadata will be stored.
        """
        self.metadata_file = metadata_file
        self.metadata = self.load_metadata()

    def load_metadata(self) -> Dict[str, Any]:
        """
        Loads metadata from the JSON file.

        :return: A dictionary containing the metadata.
        """
        if not os.path.exists(self.metadata_file):
            return {}
        with open(self.metadata_file, 'r') as file:
            return json.load(file)

    def save_metadata(self) -> None:
        """
        Saves the current metadata to the JSON file.
        """
        with open(self.metadata_file, 'w') as file:
            json.dump(self.metadata, file, indent=4)

    def add_metadata(self, file_name: str, metadata: Dict[str, Any]) -> None:
        """
        Adds metadata for a specific file.

        :param file_name: The name of the file for which metadata is being added.
        :param metadata: A dictionary containing the metadata to be added.
        """
        if file_name in self.metadata:
            raise ValueError(f"Metadata for {file_name} already exists.")
        self.metadata[file_name] = metadata
        self.save_metadata()

    def update_metadata(self, file_name: str, metadata: Dict[str, Any]) -> None:
        """
        Updates existing metadata for a specific file.

        :param file_name: The name of the file for which metadata is being updated.
        :param metadata: A dictionary containing the updated metadata.
        """
        if file_name not in self.metadata:
            raise ValueError(f"No metadata found for {file_name}.")
        self.metadata[file_name].update(metadata)
        self.save_metadata()

    def get_metadata(self, file_name: str) -> Dict[str, Any]:
        """
        Retrieves metadata for a specific file.

        :param file_name: The name of the file for which metadata is being retrieved.
        :return: A dictionary containing the metadata.
        """
        if file_name not in self.metadata:
            raise ValueError(f"No metadata found for {file_name}.")
        return self.metadata[file_name]

    def delete_metadata(self, file_name: str) -> None:
        """
        Deletes metadata for a specific file.

        :param file_name: The name of the file for which metadata is being deleted.
        """
        if file_name not in self.metadata:
            raise ValueError(f"No metadata found for {file_name}.")
        del self.metadata[file_name]
        self.save_metadata()

# Example usage
if __name__ == "__main__":
    metadata_manager = MetadataManager('metadata.json')

    # Adding metadata for a new mp4 file
    try:
        metadata_manager.add_metadata('video1.mp4', {
            'title': 'Sample Video',
            'description': 'This is a sample video for testing.',
            'license': 'CC BY 4.0',
            'tags': ['sample', 'video', 'test']
        })
    except ValueError as e:
        print(e)

    # Retrieving metadata
    try:
        metadata = metadata_manager.get_metadata('video1.mp4')
        print(metadata)
    except ValueError as e:
        print(e)

    # Updating metadata
    try:
        metadata_manager.update_metadata('video1.mp4', {
            'tags': ['sample', 'video', 'test', 'AI']
        })
    except ValueError as e:
        print(e)

    # Deleting metadata
    try:
        metadata_manager.delete_metadata('video1.mp4')
    except ValueError as e:
        print(e)
```
