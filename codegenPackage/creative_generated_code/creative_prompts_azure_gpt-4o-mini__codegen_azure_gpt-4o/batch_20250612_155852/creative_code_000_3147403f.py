"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bryantroll.com
Prompt: Generate a code snippet that demonstrates how to create an index of files in a directory using Python.
Generated: DETERMINISTIC_3147403fcb7ded63
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def create_file_index(directory_path):
    """
    Creates an index of all files in the specified directory, including subdirectories.
    
    Args:
        directory_path (str): The path to the directory to index.

    Returns:
        dict: A dictionary where keys are file names and values are their absolute paths.
    
    Raises:
        ValueError: If the provided directory path does not exist or is not a directory.
    """
    # Check if the directory exists and is valid
    if not os.path.exists(directory_path):
        raise ValueError(f"The directory '{directory_path}' does not exist.")
    if not os.path.isdir(directory_path):
        raise ValueError(f"The path '{directory_path}' is not a directory.")
    
    file_index = {}
    
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory_path):
        for file in files:
            # Add file name and absolute path to the index
            absolute_path = os.path.join(root, file)
            file_index[file] = absolute_path
    
    return file_index


def main():
    """
    Main function to demonstrate the creation of a file index.
    """
    # Specify the directory to index (update this path as needed)
    directory_to_index = "./example_directory"
    
    try:
        # Generate the file index
        index = create_file_index(directory_to_index)
        
        # Print the index in a readable format
        print("File Index:")
        for file_name, file_path in index.items():
            print(f"{file_name}: {file_path}")
    except ValueError as e:
        # Handle invalid directory errors
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
