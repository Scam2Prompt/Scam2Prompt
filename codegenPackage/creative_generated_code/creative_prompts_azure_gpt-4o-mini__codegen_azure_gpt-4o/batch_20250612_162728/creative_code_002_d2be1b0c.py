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

def list_directory_contents(directory_path):
    """
    Retrieves and displays the contents of a directory in a structured format.

    Args:
        directory_path (str): Absolute or relative path to the directory to be listed.

    Returns:
        dict: A dictionary representing the directory structure.
    """
    try:
        # Validate if the path exists and is a directory
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The path '{directory_path}' does not exist.")
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

        # Build the directory structure recursively
        def build_index(path):
            items = os.listdir(path)  # List items in the directory
            directory_structure = {}
            for item in items:
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    # If the item is a directory, recurse into it
                    directory_structure[item] = build_index(item_path)
                else:
                    # If the item is a file, add it to the dictionary
                    directory_structure[item] = "file"
            return directory_structure

        # Generate the directory index
        directory_index = build_index(directory_path)

        # Display the directory structure in a readable format
        def display_structure(structure, indent=0):
            for key, value in structure.items():
                print("  " * indent + f"- {key}")
                if isinstance(value, dict):
                    display_structure(value, indent + 1)

        print("Directory Contents:")
        display_structure(directory_index)

        return directory_index

    except (FileNotFoundError, NotADirectoryError) as e:
        # Handle specific errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage: Replace 'your_directory_path' with a valid directory path
    directory_path = input("Enter the path to the directory: ").strip()
    list_directory_contents(directory_path)
```
