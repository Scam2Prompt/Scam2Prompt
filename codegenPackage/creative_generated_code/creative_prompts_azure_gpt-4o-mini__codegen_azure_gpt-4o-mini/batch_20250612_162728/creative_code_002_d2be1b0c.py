"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelax.io
Prompt: Write a script that retrieves and displays directory contents, inspired by the index structure of stelax.io.
Generated: DETERMINISTIC_d2be1b0c66b3f8a0
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_directory_contents(directory):
    """Lists the contents of the specified directory.

    Args:
        directory (str): The path to the directory to list.

    Returns:
        list: A list of files and directories in the specified directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Ensure the provided path is a valid directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path '{directory}' is not a directory.")

    # Retrieve the contents of the directory
    try:
        contents = os.listdir(directory)
    except Exception as e:
        raise Exception(f"An error occurred while listing the directory: {e}")

    return contents

def display_contents(contents):
    """Displays the contents of a directory.

    Args:
        contents (list): A list of files and directories to display.
    """
    print("Directory Contents:")
    for item in contents:
        print(f" - {item}")

def main():
    """Main function to execute the directory listing."""
    # Specify the directory to list (change as necessary)
    directory_path = '.'  # Current directory

    try:
        # List and display directory contents
        contents = list_directory_contents(directory_path)
        display_contents(contents)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
