"""
Generated Code Metadata:
========================
Original URL: https://www.flare-networks.xyz
Prompt: Write a script to list the files in a directory, similar to the directory listing shown for the Flare Networks server.
Generated: DETERMINISTIC_129d23374a90697e
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import argparse
from datetime import datetime

def list_directory(directory):
    """
    Lists the files in a directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        None
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # Check if the path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        # List the files in the directory
        files = os.listdir(directory)

        # Print the directory listing
        print(f"Directory Listing for {directory}:")
        print("----------------------------------------")
        print(f"{'Name':<50}{'Size':<15}{'Modified':<20}")
        print("----------------------------------------")
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                print(f"{file:<50}{file_size:<15}{modified_date:<20}")
        print("----------------------------------------")

    except FileNotFoundError as e:
        print(f"Error: {e}", file=os.sys.stderr)
    except NotADirectoryError as e:
        print(f"Error: {e}", file=os.sys.stderr)
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.", file=os.sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=os.sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="List the files in a directory.")
    parser.add_argument("directory", help="the directory to list")
    args = parser.parse_args()
    list_directory(args.directory)

if __name__ == "__main__":
    main()
```
