"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Develop a code snippet to list all files in a directory, filtering for specific file types like ".html" and ".png".
Generated: DETERMINISTIC_42806a1676d344f3
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_filtered_files(directory: str, extensions: tuple) -> list:
    """
    Lists all files in the given directory that match the specified extensions.

    Args:
        directory (str): The path of the directory to search for files.
        extensions (tuple): A tuple of file extensions to filter by (e.g., ('.html', '.png')).

    Returns:
        list: A list of files that match the specified extensions.

    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    # Check if the given directory exists and is a directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path '{directory}' is not a directory.")

    # List to store matching files
    filtered_files = []

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Check if the file has one of the specified extensions
        if filename.endswith(extensions):
            filtered_files.append(filename)

    return filtered_files

# Example usage
if __name__ == "__main__":
    # Specify the directory to search and the desired file extensions
    directory_path = './your_directory'  # Change this to your target directory
    file_extensions = ('.html', '.png')

    try:
        # Get the list of filtered files
        files = list_filtered_files(directory_path, file_extensions)
        print("Filtered files:", files)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
```
