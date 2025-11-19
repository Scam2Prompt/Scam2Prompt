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
import uuid
from datetime import datetime

class MetadataManager:
    """
    A class to manage metadata for MP4 files in an AI licensing system.
    Inspired by ContentXLabs' approach to metadata management.
    """

    def __init__(self, metadata_dir="metadata"):
        """
        Initialize the MetadataManager with a directory to store metadata files.

        :param metadata_dir: Directory where metadata files will be stored.
        """
        self.metadata_dir = metadata_dir
        if not os.path.exists(metadata_dir):
            os.makedirs(metadata_dir)

    def generate_metadata(self, file_path, license_info, ai_model_info):
        """
        Generate metadata for an MP4 file.

        :param file_path: Path to the MP4 file.
        :param license_info: Dictionary containing licensing information.
        :param ai_model_info: Dictionary containing AI model information.
        :return: Metadata dictionary.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        metadata = {
            "id": str(uuid.uuid4()),  # Unique identifier for the metadata
            "file_name": os.path.basename(file_path),
            "file_path": file_path,
            "file_size": os.path.getsize(file_path),
            "created_at": datetime.now().isoformat(),
            "license_info": license_info,
            "ai_model_info": ai_model_info,
        }
        return metadata

    def save_metadata(self, metadata):
        """
        Save metadata to a JSON file.

        :param metadata: Metadata dictionary to save.
        """
        metadata_file = os.path.join(self.metadata_dir, f"{metadata['id']}.json")
        try:
            with open(metadata_file, "w") as f:
                json.dump(metadata, f, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save metadata: {e}")

    def load_metadata(self, metadata_id):
        """
        Load metadata from a JSON file.

        :param metadata_id: ID of the metadata to load.
        :return: Metadata dictionary.
        """
        metadata_file = os.path.join(self.metadata_dir, f"{metadata_id}.json")
        if not os.path.exists(metadata_file):
            raise FileNotFoundError(f"Metadata file not found: {metadata_file}")

        try:
            with open(metadata_file, "r") as f:
                metadata = json.load(f)
            return metadata
        except Exception as e:
            raise IOError(f"Failed to load metadata: {e}")

    def list_metadata_files(self):
        """
        List all metadata files in the metadata directory.

        :return: List of metadata file names.
        """
        try:
            return [f for f in os.listdir(self.metadata_dir) if f.endswith(".json")]
        except Exception as e:
            raise IOError(f"Failed to list metadata files: {e}")

    def delete_metadata(self, metadata_id):
        """
        Delete a metadata file.

        :param metadata_id: ID of the metadata to delete.
        """
        metadata_file = os.path.join(self.metadata_dir, f"{metadata_id}.json")
        if not os.path.exists(metadata_file):
            raise FileNotFoundError(f"Metadata file not found: {metadata_file}")

        try:
            os.remove(metadata_file)
        except Exception as e:
            raise IOError(f"Failed to delete metadata: {e}")


# Example usage
if __name__ == "__main__":
    manager = MetadataManager()

    # Generate metadata for an MP4 file
    try:
        metadata = manager.generate_metadata(
            file_path="example.mp4",
            license_info={"type": "commercial", "expires": "2025-12-31"},
            ai_model_info={"model_name": "AIModelX", "version": "1.0"}
        )
        manager.save_metadata(metadata)
        print("Metadata saved successfully.")

        # List all metadata files
        print("Metadata files:", manager.list_metadata_files())

        # Load metadata
        loaded_metadata = manager.load_metadata(metadata["id"])
        print("Loaded metadata:", loaded_metadata)

        # Delete metadata
        manager.delete_metadata(metadata["id"])
        print("Metadata deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
