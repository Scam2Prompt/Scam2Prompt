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

def parse_file_metadata(file_content):
    """
    Parses file content to extract metadata including unique identifiers and timestamps.

    Args:
        file_content (str): The content of the file as a string.

    Returns:
        dict: A dictionary containing extracted metadata. Keys include 'identifiers' and 'timestamps'.
    """
    # Regular expression patterns for identifier and timestamp
    identifier_pattern = re.compile(r'\b[a-f0-9]{64}\b')  # 64-character hex strings
    timestamp_pattern = re.compile(r'\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z\b')  # ISO 8601 format

    # Extract identifiers and timestamps using regex
    identifiers = identifier_pattern.findall(file_content)
    timestamps = timestamp_pattern.findall(file_content)

    # Validate timestamps and ensure they are parsable
    valid_timestamps = []
    for ts in timestamps:
        try:
            # Parse timestamp to check validity
            valid_timestamps.append(datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ"))
        except ValueError:
            # Skip invalid timestamps
            pass

    # Return metadata as a dictionary
    return {
        "identifiers": identifiers,
        "timestamps": [dt.isoformat() for dt in valid_timestamps]  # Convert datetime objects back to ISO format
    }


# Example usage:
if __name__ == "__main__":
    # Example file content
    file_content = """
    Identifier: 3088721a2a78a99d26641efc1dc5d1e6fb3790f72cbb172a81dd1d2daf5fd5ba
    Timestamp: 2024-01-21T23:37:01.000Z
    Invalid Timestamp: 2024-01-21T23:37:01
    Another Identifier: abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234
    Another Timestamp: 2025-12-31T12:00:00.000Z
    """

    # Parse metadata from file content
    metadata = parse_file_metadata(file_content)

    # Print extracted metadata
    print("Extracted Metadata:")
    print(metadata)
```
