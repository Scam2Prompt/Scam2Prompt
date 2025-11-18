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
from typing import List, Optional

class S3MetadataError(Exception):
    """Custom exception for S3 metadata errors."""
    pass

def is_valid_iso8601(timestamp: str) -> bool:
    """
    Validate if the given timestamp follows the ISO 8601 format.
    
    Args:
        timestamp (str): The timestamp string to validate.
    
    Returns:
        bool: True if the timestamp is valid, False otherwise.
    """
    # Define a regex pattern to match ISO 8601 format
    iso8601_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?Z?$'
    return bool(re.match(iso8601_pattern, timestamp))

def extract_timestamps(s3_metadata: dict) -> List[str]:
    """
    Extract and validate timestamps from S3 metadata.
    
    Args:
        s3_metadata (dict): The S3 metadata dictionary containing potential timestamp fields.
        
    Returns:
        List[str]: A list of valid ISO 8601 formatted timestamps.
        
    Raises:
        S3MetadataError: If no valid timestamps are found in the metadata.
    """
    timestamps = []

    for key, value in s3_metadata.items():
        if isinstance(value, str) and is_valid_iso8601(value):
            timestamps.append(value)

    if not timestamps:
        raise S3MetadataError("No valid ISO 8601 timestamps found in the S3 metadata.")

    return timestamps

# Example usage
if __name__ == "__main__":
    # Sample S3 metadata
    s3_metadata_example = {
        'Created': '2023-10-12T14:30:00Z',
        'LastModified': '2023-10-12T14:45:00Z',
        'InvalidTimestamp': '2023/10/12 14:30:00'
    }

    try:
        valid_timestamps = extract_timestamps(s3_metadata_example)
        print("Valid timestamps:", valid_timestamps)
    except S3MetadataError as e:
        print("Error:", e)
```
