"""
Generated Code Metadata:
========================
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: Write code to parse and extract metadata from files with identifiers like "3088721a2a78a99d26641efc1dc5d1e6fb3790f72cbb172a81dd1d2daf5fd5ba" and timestamps in the format "2024-01-21T23:37:01.000Z".
Generated: DETERMINISTIC_43f97411e0590db8
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
from typing import Dict, Any, Optional

class MetadataExtractor:
    """
    A class to extract metadata from files based on specific identifiers and timestamps.
    """

    def __init__(self, identifier_pattern: str, timestamp_format: str):
        """
        Initializes the MetadataExtractor with the given identifier pattern and timestamp format.

        :param identifier_pattern: A regex pattern to match file identifiers.
        :param timestamp_format: The format of the timestamp to parse.
        """
        self.identifier_pattern = identifier_pattern
        self.timestamp_format = timestamp_format

    def extract_metadata(self, text: str) -> Optional[Dict[str, Any]]:
        """
        Extracts metadata from the provided text.

        :param text: The input text containing identifiers and timestamps.
        :return: A dictionary containing the extracted identifier and timestamp, or None if not found.
        """
        try:
            identifier = self._extract_identifier(text)
            timestamp = self._extract_timestamp(text)

            if identifier and timestamp:
                return {
                    'identifier': identifier,
                    'timestamp': timestamp
                }
            else:
                return None
        except Exception as e:
            print(f"Error extracting metadata: {e}")
            return None

    def _extract_identifier(self, text: str) -> Optional[str]:
        """
        Extracts the identifier from the text using the defined pattern.

        :param text: The input text.
        :return: The extracted identifier or None if not found.
        """
        match = re.search(self.identifier_pattern, text)
        return match.group(0) if match else None

    def _extract_timestamp(self, text: str) -> Optional[datetime]:
        """
        Extracts and parses the timestamp from the text.

        :param text: The input text.
        :return: The parsed datetime object or None if not found.
        """
        match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z', text)
        if match:
            return datetime.strptime(match.group(0), self.timestamp_format)
        return None

# Example usage
if __name__ == "__main__":
    # Define the identifier pattern and timestamp format
    identifier_pattern = r'[a-f0-9]{64}'  # Example pattern for a 64-character hex identifier
    timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"

    # Create an instance of MetadataExtractor
    extractor = MetadataExtractor(identifier_pattern, timestamp_format)

    # Sample text containing identifier and timestamp
    sample_text = "File ID: 3088721a2a78a99d26641efc1dc5d1e6fb3790f72cbb172a81dd1d2daf5fd5ba created at 2024-01-21T23:37:01.000Z"

    # Extract metadata
    metadata = extractor.extract_metadata(sample_text)

    # Print the extracted metadata
    if metadata:
        print("Extracted Metadata:", metadata)
    else:
        print("No metadata found.")
```
