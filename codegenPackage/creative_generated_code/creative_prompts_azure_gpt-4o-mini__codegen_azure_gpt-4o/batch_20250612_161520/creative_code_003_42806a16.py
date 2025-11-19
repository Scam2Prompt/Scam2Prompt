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

def list_files_by_extension(directory_path, extensions):
    """
    Lists all files in a given directory that match specific file extensions.

    Parameters:
        directory_path (str): The path of the directory to search.
        extensions (list): A list of file extensions to filter, e.g., ['.html', '.png'].

    Returns:
        list: A list of file paths that match the specified extensions.
    """
    # Validate input
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")
    if not isinstance(extensions, list) or not extensions:
        raise ValueError("Extensions must be a non-empty list of strings.")

    matching_files = []
    try:
        # Iterate through the files in the directory
        for file_name in os.listdir(directory_path):
            # Check if the file has one of the specified extensions
            if any(file_name.endswith(ext) for ext in extensions):
                matching_files.append(os.path.join(directory_path, file_name))

    except Exception as e:
        # Log and re-raise any unexpected errors
        raise RuntimeError(f"An error occurred while listing files: {e}")

    return matching_files


if __name__ == "__main__":
    # Example usage
    directory = "/path/to/your/directory"
    file_extensions = [".html", ".png"]

    try:
        filtered_files = list_files_by_extension(directory, file_extensions)
        print("Matching files:")
        for file in filtered_files:
            print(file)
    except Exception as error:
        print(f"Error: {error}")
```
