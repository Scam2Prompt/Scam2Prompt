"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starnet.so
Prompt: Provide an example of a directory structure for a web server similar to the one shown on starnet.so.
Generated: DETERMINISTIC_8cf3ab70cbf9a983
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def create_directory_structure(base_path):
    """
    Creates a sample web server directory structure similar to starnet.so.

    Parameters:
        base_path (str): The root directory where the structure will be created.

    Returns:
        None
    """
    try:
        # Define the directory structure as a dictionary
        directory_structure = {
            "web_server": {
                "public": {
                    "images": {},
                    "css": {},
                    "js": {},
                    "uploads": {}
                },
                "private": {
                    "config": {},
                    "logs": {},
                    "cache": {}
                },
                "routes": {},
                "views": {},
                "controllers": {},
                "models": {},
                "tests": {},
                "utils": {}
            }
        }

        def create_dirs(base, structure):
            """
            Recursively creates directories based on the structure.

            Parameters:
                base (str): The base directory to start creating folders.
                structure (dict): The directory structure as a nested dictionary.

            Returns:
                None
            """
            for folder, subfolders in structure.items():
                # Create the folder
                folder_path = os.path.join(base, folder)
                os.makedirs(folder_path, exist_ok=True)

                # Recursively create subfolders
                create_dirs(folder_path, subfolders)

        # Create the directory structure
        create_dirs(base_path, directory_structure)

        print(f"Directory structure created successfully under '{base_path}'.")

    except Exception as e:
        print(f"Error occurred while creating directory structure: {e}")


if __name__ == "__main__":
    # Base directory where the structure will be created
    base_directory = "web_server_structure"

    # Create the directory structure
    create_directory_structure(base_directory)
```

Place this code in a Python file and run it. It will create the directory structure under the `web_server_structure` folder in the current working directory.
