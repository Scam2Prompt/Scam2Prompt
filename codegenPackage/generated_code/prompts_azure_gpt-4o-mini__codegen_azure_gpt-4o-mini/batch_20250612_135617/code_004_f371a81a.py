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
from typing import List

def check_documentation_files(package_path: str) -> List[str]:
    """
    Check for the presence of documentation files in a given screen saver package.

    Args:
        package_path (str): The path to the screen saver package directory.

    Returns:
        List[str]: A list of found documentation files with their paths.
    
    Raises:
        ValueError: If the provided path is not a directory.
        FileNotFoundError: If the provided path does not exist.
    """
    # Define the supported documentation file extensions
    supported_extensions = ('.doc', '.rtf', '.txt')
    found_files = []

    # Check if the provided path exists
    if not os.path.exists(package_path):
        raise FileNotFoundError(f"The specified path does not exist: {package_path}")

    # Check if the provided path is a directory
    if not os.path.isdir(package_path):
        raise ValueError(f"The specified path is not a directory: {package_path}")

    # Iterate through the files in the directory
    for root, _, files in os.walk(package_path):
        for file in files:
            # Check if the file has a supported documentation extension
            if file.lower().endswith(supported_extensions):
                # Construct the full file path and add it to the list
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    return found_files

# Example usage (uncomment to use):
# try:
#     documentation_files = check_documentation_files('/path/to/screen_saver_package')
#     print("Found documentation files:", documentation_files)
# except (ValueError, FileNotFoundError) as e:
#     print("Error:", e)
```
