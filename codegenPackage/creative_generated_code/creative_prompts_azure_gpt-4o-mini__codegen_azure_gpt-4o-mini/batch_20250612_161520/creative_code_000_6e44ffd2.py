"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synerex-bo.com
Prompt: Generate a Python script to list all files in a directory, similar to the index structure found on synerex-bo.com.
Generated: DETERMINISTIC_6e44ffd2af690028
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

def list_files_in_directory(directory_path):
    """
    Lists all files in the specified directory and its subdirectories.

    Parameters:
        directory_path (str): The path of the directory to list files from.

    Returns:
        list: A list of file paths found in the directory.
    """
    files_list = []  # Initialize an empty list to store file paths

    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path '{directory_path}' is not a valid directory.")
    
    try:
        # Walk through the directory
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Create the full file path and append it to the list
                full_path = os.path.join(root, file)
                files_list.append(full_path)
                
    except Exception as e:
        raise RuntimeError(f"An error occurred while listing files: {e}")

    return files_list


if __name__ == "__main__":
    # Example usage
    directory_to_search = input("Enter the directory path to list files: ")

    try:
        found_files = list_files_in_directory(directory_to_search)
        print(f"\nFiles found in '{directory_to_search}':")
        for file in found_files:
            print(file)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
