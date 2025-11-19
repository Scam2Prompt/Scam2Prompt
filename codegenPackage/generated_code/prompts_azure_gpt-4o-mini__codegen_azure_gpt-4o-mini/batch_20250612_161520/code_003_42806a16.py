"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Develop a code snippet to list all files in a directory, filtering for specific file types like ".html" and ".png".
Generated: DETERMINISTIC_42806a1676d344f3
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

def list_files(directory: str, extensions: tuple) -> list:
    """
    List all files in the specified directory that match the given extensions.

    Args:
        directory (str): The path to the directory to search.
        extensions (tuple): A tuple of file extensions to filter by (e.g., ('.html', '.png')).

    Returns:
        list: A list of files that match the specified extensions.

    Raises:
        ValueError: If the provided directory is not valid.
    """
    # Check if the provided directory is valid
    if not os.path.isdir(directory):
        raise ValueError(f"The provided directory '{directory}' is not valid.")

    # List to hold the filtered file names
    filtered_files = []

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Check if the file has one of the specified extensions
        if filename.endswith(extensions):
            filtered_files.append(filename)

    return filtered_files

# Example usage
if __name__ == "__main__":
    try:
        # Specify the directory and the file types to filter
        directory_path = './your_directory'  # Change this to your target directory
        file_types = ('.html', '.png')

        # Get the list of filtered files
        files = list_files(directory_path, file_types)

        # Print the filtered files
        print("Filtered files:", files)

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
