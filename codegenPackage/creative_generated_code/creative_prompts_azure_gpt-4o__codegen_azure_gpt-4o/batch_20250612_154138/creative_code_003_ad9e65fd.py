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
from pathlib import Path
from collections import defaultdict

def categorize_files_by_extension(directory):
    """
    Categorizes files in a given directory and its subdirectories based on their extensions.

    Args:
        directory (str): The path to the directory to analyze.

    Returns:
        dict: A dictionary where keys are file extensions (e.g., '.txt') 
              and values are lists of file paths with that extension.
    """
    # Ensure the directory exists
    if not os.path.exists(directory) or not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")
    
    # Dictionary to store files categorized by extension
    categorized_files = defaultdict(list)
    
    try:
        # Traverse the directory and its subdirectories
        for root, _, files in os.walk(directory):
            for file in files:
                # Use Path to extract file extension
                file_path = Path(root) / file
                file_extension = file_path.suffix.lower()  # Normalize to lowercase
                if file_extension:  # Ensure the file has an extension
                    categorized_files[file_extension].append(str(file_path))
    except Exception as e:
        raise RuntimeError(f"An error occurred while analyzing the directory: {e}")
    
    return dict(categorized_files)


# Example usage:
if __name__ == "__main__":
    try:
        directory_path = "/path/to/your/directory"  # Replace with the target directory path
        categorized = categorize_files_by_extension(directory_path)
        for ext, files in categorized.items():
            print(f"Extension '{ext}' has {len(files)} file(s):")
            for file in files:
                print(f"  - {file}")
    except Exception as error:
        print(f"Error: {error}")
```
