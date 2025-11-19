"""
Generated Code Metadata:
========================
Original URL: https://scrollnetwork.ngv.com.ec
Prompt: "Generate a Python script to index files in a directory structure similar to what is shown on the Scroll Network NGV website."
Generated: DETERMINISTIC_0a51a6a2351ffff2
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json

def index_files(directory):
    """
    Indexes all files in the given directory and its subdirectories.

    Args:
        directory (str): The root directory to start indexing.

    Returns:
        dict: A nested dictionary representing the directory structure and files.
    """
    try:
        # Initialize the structure to hold the directory tree
        directory_tree = {}

        # Walk through the directory structure
        for root, dirs, files in os.walk(directory):
            # Get the relative path from the root directory
            relative_path = os.path.relpath(root, directory)
            if relative_path == ".":
                relative_path = ""  # Handle the root directory case

            # Add files and subdirectories to the tree
            directory_tree[relative_path] = {
                "files": files,
                "subdirectories": dirs
            }

        return directory_tree
    except Exception as e:
        # Handle unexpected errors
        print(f"Error while indexing files: {e}")
        return {}

def save_index_to_file(index, output_file):
    """
    Saves the indexed directory structure to a JSON file.

    Args:
        index (dict): The indexed directory structure.
        output_file (str): The path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as file:
            json.dump(index, file, indent=4)
        print(f"Index successfully saved to {output_file}")
    except Exception as e:
        # Handle file writing errors
        print(f"Error while saving index to file: {e}")

def main():
    """
    Main function to index files in a directory and save the result to a JSON file.
    """
    # Define the directory to index and the output file
    directory_to_index = input("Enter the directory to index: ").strip()
    output_file = input("Enter the output JSON file path: ").strip()

    # Validate the directory path
    if not os.path.isdir(directory_to_index):
        print(f"Error: The directory '{directory_to_index}' does not exist or is not accessible.")
        return

    # Index the files
    print("Indexing files...")
    index = index_files(directory_to_index)

    # Save the index to a file
    save_index_to_file(index, output_file)

if __name__ == "__main__":
    main()
```
