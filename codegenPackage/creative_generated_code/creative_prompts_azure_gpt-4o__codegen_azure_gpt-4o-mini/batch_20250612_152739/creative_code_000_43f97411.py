"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: Write code to parse and extract metadata from files with identifiers like "3088721a2a78a99d26641efc1dc5d1e6fb3790f72cbb172a81dd1d2daf5fd5ba" and timestamps in the format "2024-01-21T23:37:01.000Z".
Generated: DETERMINISTIC_43f97411e0590db8
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime
from typing import Optional, Tuple

class MetadataExtractor:
    """
    A class to extract metadata from files containing identifiers and timestamps.

    Attributes:
        identifier_pattern (str): Regular expression pattern for file identifiers.
        timestamp_pattern (str): Regular expression pattern for timestamps.
    """

    identifier_pattern = r'([a-f0-9]{64})'
    timestamp_pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)'

    def __init__(self, file_content: str):
        """
        Initialize the MetadataExtractor with file content.

        Parameters:
            file_content (str): The content of the file to be parsed.
        """
        self.file_content = file_content

    def extract_metadata(self) -> Optional[Tuple[str, str]]:
        """
        Extract the identifier and timestamp from the file content.

        Returns:
            Optional[Tuple[str, str]]: A tuple containing the identifier and timestamp if found, otherwise None.
        """
        identifier = self._extract_identifier()
        timestamp = self._extract_timestamp()

        if identifier and timestamp:
            return identifier, timestamp
        return None

    def _extract_identifier(self) -> Optional[str]:
        """
        Extract the identifier from the file content.

        Returns:
            Optional[str]: The extracted identifier or None if not found.
        """
        match = re.search(self.identifier_pattern, self.file_content)
        return match.group(1) if match else None

    def _extract_timestamp(self) -> Optional[str]:
        """
        Extract the timestamp from the file content.

        Returns:
            Optional[str]: The extracted timestamp or None if not found.
        """
        match = re.search(self.timestamp_pattern, self.file_content)
        return match.group(1) if match else None

def main():
    """
    Main function to demonstrate the usage of MetadataExtractor.
    """
    # Sample file content for demonstration
    file_content = """
    Some log data...
    Identifier: 3088721a2a78a99d26641efc1dc5d1e6fb3790f72cbb172a81dd1d2daf5fd5ba
    Timestamp: 2024-01-21T23:37:01.000Z
    More log data...
    """

    extractor = MetadataExtractor(file_content)
    metadata = extractor.extract_metadata()

    if metadata:
        identifier, timestamp = metadata
        print(f"Identifier: {identifier}")
        print(f"Timestamp: {timestamp}")
    else:
        print("No valid metadata found.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
