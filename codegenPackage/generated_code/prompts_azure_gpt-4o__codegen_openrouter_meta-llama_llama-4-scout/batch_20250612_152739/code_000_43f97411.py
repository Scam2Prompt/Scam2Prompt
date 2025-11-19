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
import hashlib
from datetime import datetime

def extract_metadata(file_path):
    """
    Extracts metadata from a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing the extracted metadata.
    """

    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

    # Regular expression pattern to match the identifier
    identifier_pattern = r"[0-9a-f]{40}"

    # Regular expression pattern to match the timestamp
    timestamp_pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z"

    # Search for the identifier in the content
    identifier_match = re.search(identifier_pattern, content)
    if identifier_match:
        identifier = identifier_match.group()
    else:
        print(f"No identifier found in file: {file_path}")
        return None

    # Search for the timestamp in the content
    timestamp_match = re.search(timestamp_pattern, content)
    if timestamp_match:
        timestamp_str = timestamp_match.group()
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            print(f"Invalid timestamp format: {timestamp_str}")
            return None
    else:
        print(f"No timestamp found in file: {file_path}")
        return None

    # Verify the identifier is a valid SHA-1 hash
    try:
        hashlib.sha1(bytes.fromhex(identifier))
    except ValueError:
        print(f"Invalid SHA-1 hash: {identifier}")
        return None

    metadata = {
        "identifier": identifier,
        "timestamp": timestamp
    }

    return metadata


def main():
    file_path = "path_to_your_file.txt"  # replace with your file path
    metadata = extract_metadata(file_path)
    if metadata:
        print("Extracted Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```
