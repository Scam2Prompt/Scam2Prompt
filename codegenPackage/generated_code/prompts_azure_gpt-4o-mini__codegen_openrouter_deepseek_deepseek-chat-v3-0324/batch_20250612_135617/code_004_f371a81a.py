"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Create a function that checks for the presence of documentation files (.DOC, .RTF, .TXT) in a screen saver package, inspired by the content from Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_f371a81a40c0c386
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import List, Optional

def check_documentation_files(directory: str) -> Optional[List[str]]:
    """
    Checks for the presence of documentation files (.DOC, .RTF, .TXT) in a given directory.

    Args:
        directory (str): Path to the directory to search for documentation files.

    Returns:
        Optional[List[str]]: List of found documentation files if any exist, None otherwise.

    Raises:
        ValueError: If the provided directory does not exist or is not a directory.
    """
    # Validate directory exists and is a directory
    if not os.path.exists(directory):
        raise ValueError(f"Directory does not exist: {directory}")
    if not os.path.isdir(directory):
        raise ValueError(f"Path is not a directory: {directory}")

    # Supported documentation file extensions
    doc_extensions = {'.doc', '.rtf', '.txt'}
    found_files = []

    try:
        # Iterate through files in directory
        for filename in os.listdir(directory):
            # Check if file has a supported extension (case-insensitive)
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in doc_extensions:
                found_files.append(filename)
    except Exception as e:
        # Handle potential permission errors or other filesystem issues
        raise RuntimeError(f"Error while scanning directory: {e}")

    return found_files if found_files else None
```
