"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamak.lagunaproductions.net
Prompt: Can you provide a summary of the directory structure and contents found at Mestamak's index page?
Generated: DETERMINISTIC_ba506b89084a1ff3
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def summarize_directory(path):
    """
    Summarizes the directory structure and contents of the given path.

    Args:
        path (str): The path to the directory to summarize.

    Returns:
        dict: A summary of the directory structure, including directories and files.
    """
    summary = {
        'directories': [],
        'files': []
    }

    try:
        # List all entries in the directory
        with os.scandir(path) as entries:
            for entry in entries:
                # Check if the entry is a directory
                if entry.is_dir():
                    summary['directories'].append(entry.name)
                elif entry.is_file():
                    summary['files'].append(entry.name)

    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return summary

if __name__ == "__main__":
    # Define the path to the directory to be summarized
    directory_path = '/path/to/mestamak/index'  # Change this to the actual path

    # Get and print the summary of the directory
    directory_summary = summarize_directory(directory_path)
    print("Directory Summary:")
    print(f"Directories: {directory_summary['directories']}")
    print(f"Files: {directory_summary['files']}")
```
