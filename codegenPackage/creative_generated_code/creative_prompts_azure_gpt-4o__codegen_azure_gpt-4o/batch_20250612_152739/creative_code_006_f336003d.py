"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write a function to extract and validate timestamps from S3 metadata, ensuring they follow the ISO 8601 format as shown on the webpage.
Generated: DETERMINISTIC_f336003dce140209
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

def extract_and_validate_timestamps(s3_metadata):
    """
    Extract and validate timestamps from S3 metadata, ensuring they follow the ISO 8601 format.

    Args:
        s3_metadata (dict): A dictionary containing S3 metadata key-value pairs.

    Returns:
        list: A list of valid ISO 8601 timestamps found in the metadata.
    
    Raises:
        ValueError: If an invalid ISO 8601 timestamp is encountered in the metadata.
    """
    
    # Regular expression for matching ISO 8601 timestamps
    iso_8601_regex = re.compile(
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[\+\-]\d{2}:\d{2})$"
    )

    valid_timestamps = []

    for key, value in s3_metadata.items():
        # Check if the metadata value matches the ISO 8601 format
        if isinstance(value, str) and iso_8601_regex.match(value):
            try:
                # Attempt to parse the timestamp to ensure it is valid
                datetime.fromisoformat(value.rstrip('Z').replace('Z', '+00:00'))
                valid_timestamps.append(value)
            except ValueError as e:
                raise ValueError(f"Invalid timestamp found in metadata: {value}") from e

    return valid_timestamps


# Example usage:
if __name__ == "__main__":
    # Sample S3 metadata dictionary
    s3_metadata_example = {
        "timestamp1": "2023-10-15T12:34:56Z",
        "timestamp2": "invalid-timestamp",
        "timestamp3": "2023-10-15T12:34:56+02:00"
    }

    try:
        valid_timestamps = extract_and_validate_timestamps(s3_metadata_example)
        print("Valid timestamps:", valid_timestamps)
    except ValueError as error:
        print("Error:", error)
```
