"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://360fuel.network
Prompt: Write a Python function using `os` or `pathlib` to analyze and categorize files based on their extensions in a directory structure similar to the one at https://360fuel.network.
Generated: DETERMINISTIC_ad9e65fd335bf3ac
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from collections import defaultdict
from pathlib import Path

def categorize_files_by_extension(directory: str) -> dict:
    """
    Analyzes the specified directory and categorizes files based on their file extensions.

    Args:
        directory (str): The path to the directory to analyze.

    Returns:
        dict: A dictionary where keys are file extensions and values are lists of file paths.

    Raises:
        ValueError: If the provided directory does not exist or is not a directory.
    """
    # Convert to a Path object for easier manipulation
    path = Path(directory)

    # Check if the provided path exists and is a directory
    if not path.exists() or not path.is_dir():
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")

    # Dictionary to hold categorized files
    categorized_files = defaultdict(list)

    # Traverse the directory
    for file in path.rglob('*'):  # rglob allows for recursive search
        if file.is_file():  # Ensure that we only consider files
            # Get the file extension
            ext = file.suffix.lower()  # Normalize to lower case
            # Append the file path to the corresponding extension list
            categorized_files[ext].append(str(file))

    return dict(categorized_files)  # Convert defaultdict to a regular dict for returning

# Example usage
if __name__ == '__main__':
    try:
        directory_to_analyze = '/path/to/directory'  # Replace with the actual directory path
        categorized_files = categorize_files_by_extension(directory_to_analyze)
        for ext, files in categorized_files.items():
            print(f'Extension: {ext}, Files: {files}')
    except ValueError as e:
        print(f"Error: {e}")
```
