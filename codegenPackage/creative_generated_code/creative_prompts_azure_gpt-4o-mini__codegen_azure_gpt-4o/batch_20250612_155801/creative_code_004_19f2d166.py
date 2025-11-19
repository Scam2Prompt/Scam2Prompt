"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://360fuel.network
Prompt: Provide an example of how to parse the directory listing from the 360Fuel Media site for specific file types.
Generated: DETERMINISTIC_19f2d166828cad5f
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_files_by_extension(directory_path, file_extension):
    """
    Lists files with a specific extension in a given directory.

    Args:
        directory_path (str): The path to the directory to scan.
        file_extension (str): The file extension to filter by (e.g., ".txt").

    Returns:
        list: A list of file names matching the specified extension.
    """
    # Ensure the file extension starts with a dot.
    if not file_extension.startswith('.'):
        raise ValueError("File extension must start with a dot (e.g., '.txt').")
    
    # Validate that the directory exists.
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    # Initialize an empty list to store matching files.
    matching_files = []

    try:
        # Iterate through the directory contents.
        for file_name in os.listdir(directory_path):
            # Check if the file has the desired extension.
            if file_name.endswith(file_extension):
                matching_files.append(file_name)
    except Exception as e:
        # Log or re-raise unexpected exceptions for debugging.
        raise RuntimeError(f"An error occurred while accessing the directory: {e}")

    return matching_files


if __name__ == "__main__":
    # Example usage:
    directory = "/path/to/360Fuel/Media/site/directory"
    extension = ".jpg"  # Change to desired file extension.

    try:
        files = list_files_by_extension(directory, extension)
        print(f"Files with extension '{extension}':")
        for file in files:
            print(file)
    except Exception as error:
        print(f"Error: {error}")
```
