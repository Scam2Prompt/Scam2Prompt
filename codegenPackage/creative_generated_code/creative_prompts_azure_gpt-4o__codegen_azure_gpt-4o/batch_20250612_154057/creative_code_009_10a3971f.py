"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstarksten.github.io
Prompt: Write a script to compare two versions of the StarkX-Kernel changelog and highlight differences, using bukandewa's changelog format.
Generated: DETERMINISTIC_10a3971fe8fc30fb
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import difflib
import os

def read_changelog(file_path):
    """
    Reads the changelog file and returns its content as a list of lines.
    
    :param file_path: Path to the changelog file.
    :return: List of lines from the changelog file.
    :raises FileNotFoundError: If the file does not exist.
    :raises IOError: If there is an error reading the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")


def compare_changelogs(file_path_old, file_path_new):
    """
    Compares two changelog files and highlights differences.
    
    :param file_path_old: Path to the older version of the changelog.
    :param file_path_new: Path to the newer version of the changelog.
    :return: None. Prints differences to the console.
    """
    try:
        # Read changelog files
        old_changelog_lines = read_changelog(file_path_old)
        new_changelog_lines = read_changelog(file_path_new)
        
        # Generate diff using difflib
        diff = difflib.unified_diff(
            old_changelog_lines, 
            new_changelog_lines, 
            fromfile='Old Changelog', 
            tofile='New Changelog', 
            lineterm=''
        )

        # Print differences line by line
        print("\n".join(diff))
    except Exception as e:
        print(f"Error comparing changelogs: {e}")


if __name__ == "__main__":
    # Define paths for the changelog files
    file_path_old = "path/to/old_changelog.txt"
    file_path_new = "path/to/new_changelog.txt"

    # Compare the changelogs and highlight differences
    compare_changelogs(file_path_old, file_path_new)
```
