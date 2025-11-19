"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groupists.com
Prompt: Create a command line tool that mimics the index page of groupists.com, displaying directory contents.
Generated: DETERMINISTIC_8767bdaaca715599
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

import os
import argparse
import sys
from datetime import datetime

def list_directory_contents(directory):
    """
    Lists contents of the specified directory and mimics an index page format.
    """
    try:
        # Get a list of all files and directories in the specified path
        entries = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when accessing '{directory}'.")
        sys.exit(1)

    print(f"Index of {directory}/")
    print("-" * 80)
    print("{:<40} {:<20} {:>15}".format("Name", "Last Modified", "Size (bytes)"))
    print("-" * 80)

    try:
        for entry in entries:
            entry_path = os.path.join(directory, entry)
            last_modified = datetime.fromtimestamp(os.path.getmtime(entry_path)).strftime("%Y-%m-%d %H:%M:%S")
            size = os.path.getsize(entry_path) if os.path.isfile(entry_path) else "-"
            print("{:<40} {:<20} {:>15}".format(entry, last_modified, size))
    except Exception as e:
        print(f"Error: Failed to retrieve directory contents. {e}")
        sys.exit(1)

    print("-" * 80)
    print("End of index.")

def main():
    """
    Entry point for the CLI tool. Parses arguments and invokes directory listing.
    """
    parser = argparse.ArgumentParser(
        description="Command Line Tool: Mimics the index page of groupists.com by displaying directory contents."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Path to the directory to list. Defaults to the current directory.",
    )
    args = parser.parse_args()

    list_directory_contents(args.directory)

if __name__ == "__main__":
    main()
```

To run the script:
1. Save it as `directory_index.py`.
2. Make it executable with `chmod +x directory_index.py`.
3. Run it with `./directory_index.py /path/to/directory`, or for the current directory, simply `./directory_index.py` without arguments.
