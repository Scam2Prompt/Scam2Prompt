"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consejodigitalmx.com
Prompt: Recommend a library or tool for analyzing directory structures like the one shown in `Index of /`, and demonstrate its usage in a code snippet.
Generated: DETERMINISTIC_66f52c6ff72109db
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_directory_structure(path):
    """
    Analyzes the directory structure at the given path and returns a summary.

    :param path: str - The file system path to analyze.
    :return: dict - A summary of files and directories.
    """
    if not os.path.exists(path):
        logging.error(f"The path '{path}' does not exist.")
        return None
    if not os.path.isdir(path):
        logging.error(f"The path '{path}' is not a directory.")
        return None

    summary = {
        'directories': [],
        'files': [],
        'total_items': 0
    }

    try:
        # Iterate through the directory
        for entry in os.scandir(path):
            if entry.is_dir():
                summary['directories'].append(entry.name)
            elif entry.is_file():
                summary['files'].append(entry.name)
            summary['total_items'] += 1

        logging.info(f"Directory analysis complete for '{path}'.")
        return summary

    except PermissionError:
        logging.error(f"Permission denied to access the directory '{path}'.")
        return None
    except Exception as e:
        logging.error(f"An error occurred while analyzing the directory: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    directory_path = '/path/to/directory'  # Change this to the directory you want to analyze
    result = analyze_directory_structure(directory_path)
    
    if result:
        print("Directory Analysis Result:")
        print(f"Total Items: {result['total_items']}")
        print(f"Directories: {result['directories']}")
        print(f"Files: {result['files']}")
```
