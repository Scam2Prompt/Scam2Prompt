"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infrastructure.bincom.net
Prompt: Suggest tools or libraries for automating the indexing of a server directory, referencing the structure found at https://infrastructure.bincom.net.
Generated: DETERMINISTIC_fc911ef5eb97bac0
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that demonstrates how to automate the indexing of a server directory using `os` and `json` modules. The code is production-ready, adheres to best practices, and includes comments and error handling.

```python
import os
import json
from datetime import datetime

def index_server_directory(directory_path, output_file="directory_index.json"):
    """
    Indexes the contents of a given server directory and writes the structure to a JSON file.

    Args:
        directory_path (str): The path of the directory to index.
        output_file (str): The name of the file where the indexed structure will be stored (default: directory_index.json).

    Returns:
        None
    """
    try:
        # Validate directory path
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"The path '{directory_path}' is not a valid directory.")

        def get_directory_structure(path):
            """
            Recursively retrieves the structure of a directory.
            
            Args:
                path (str): The directory path.

            Returns:
                dict: A nested dictionary representing the directory structure.
            """
            structure = {}
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    # If the item is a directory, recursively index it
                    structure[item] = get_directory_structure(item_path)
                else:
                    # If the item is a file, include its size and modification time
                    structure[item] = {
                        "type": "file",
                        "size": os.path.getsize(item_path),
                        "modified": datetime.fromtimestamp(os.path.getmtime(item_path)).isoformat()
                    }
            return structure

        # Generate directory structure
        indexed_structure = get_directory_structure(directory_path)

        # Save the structure to a JSON file
        with open(output_file, "w") as json_file:
            json.dump(indexed_structure, json_file, indent=4)

        print(f"Directory successfully indexed. Output written to '{output_file}'.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except NotADirectoryError as nd_error:
        print(f"Error: {nd_error}")
    except PermissionError as permission_error:
        print(f"Permission Error: {permission_error}")
    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")


if __name__ == "__main__":
    # Example usage
    directory_to_index = "/path/to/server/directory"  # Replace with the actual directory path
    output_file_name = "server_directory_index.json"
    index_server_directory(directory_to_index, output_file_name)
```

**Usage Instructions:**
1. Replace `/path/to/server/directory` with the path of the directory you want to index.
2. Run the script, and it will generate a `.json` file containing the hierarchical structure of the directory.

**Dependencies:**
No external libraries are required; the script uses Python's standard library.
