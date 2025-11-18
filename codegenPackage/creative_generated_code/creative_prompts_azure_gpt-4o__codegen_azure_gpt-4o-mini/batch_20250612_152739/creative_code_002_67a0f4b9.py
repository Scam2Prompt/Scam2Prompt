"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: Generate Python code to validate and process file metadata, including fields like "140" and "v77p9yy8.html", ensuring compatibility with a system using identifiers like "4e1f55e2ae2b75fef7617866c92ee48b".
Generated: DETERMINISTIC_67a0f4b9a7bebd9f
Batch ID: 20250612_152739
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
import re
from typing import Dict, Any

class MetadataValidator:
    """A class to validate and process file metadata."""

    def __init__(self, metadata: Dict[str, Any]):
        """
        Initializes the MetadataValidator with the given metadata.

        Args:
            metadata (Dict[str, Any]): A dictionary containing metadata fields.
        """
        self.metadata = metadata

    @staticmethod
    def validate_id(identifier: str) -> bool:
        """
        Validates the identifier against a predefined pattern.

        Args:
            identifier (str): The identifier to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        pattern = r'^[a-f0-9]{32}$'  # 32 hex characters
        return bool(re.match(pattern, identifier))

    @staticmethod
    def validate_field(field: str) -> bool:
        """
        Validates the field against a predefined pattern.

        Args:
            field (str): The field to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return bool(re.match(r'^[0-9]+$|^[a-zA-Z0-9_.-]+\.html$', field))

    def process_metadata(self) -> Dict[str, Any]:
        """
        Processes the metadata after validation.

        Returns:
            Dict[str, Any]: A dictionary containing processed metadata.

        Raises:
            ValueError: If any field is invalid.
        """
        if not self.validate_id(self.metadata.get('identifier', '')):
            raise ValueError("Invalid identifier format.")

        for field in ['140', 'v77p9yy8.html']:
            if field not in self.metadata or not self.validate_field(self.metadata[field]):
                raise ValueError(f"Invalid field: {field}")

        # Process metadata (placeholder for actual processing logic)
        processed_metadata = {k: v for k, v in self.metadata.items() if self.validate_field(k) or k == 'identifier'}
        
        return processed_metadata


def read_metadata_file(file_path: str) -> Dict[str, Any]:
    """
    Reads metadata from a specified JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Dict[str, Any]: A dictionary containing the metadata.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, 'r') as file:
        return json.load(file)


def main(file_path: str) -> None:
    """
    Main function to read and process metadata from a file.

    Args:
        file_path (str): The path to the metadata file.
    """
    try:
        metadata = read_metadata_file(file_path)
        validator = MetadataValidator(metadata)
        processed_metadata = validator.process_metadata()
        print("Processed Metadata:", processed_metadata)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage:
    # Replace 'metadata.json' with your actual metadata file path
    main('metadata.json')
```
