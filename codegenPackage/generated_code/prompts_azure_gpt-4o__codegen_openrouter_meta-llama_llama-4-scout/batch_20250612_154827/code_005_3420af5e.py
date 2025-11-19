"""
Generated Code Metadata:
========================
Original URL: https://vanillagift.remadet.com
Prompt: Create a script to analyze the "Last Modified" timestamps of files in a directory served by LiteSpeed Web Server.
Generated: DETERMINISTIC_3420af5e58c4768a
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Analyze the 'Last Modified' timestamps of files in a directory.

This script iterates over all files in a specified directory, retrieves their
'Last Modified' timestamps, and prints the results.

Usage:
    python analyze_last_modified.py /path/to/directory
"""

import os
import sys
import argparse
from datetime import datetime

def get_last_modified_timestamps(directory):
    """
    Retrieve 'Last Modified' timestamps for all files in the directory.

    Args:
        directory (str): Path to the directory.

    Returns:
        dict: A dictionary with file names as keys and 'Last Modified' timestamps as values.
    """
    try:
        # Check if the provided directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # Check if the provided path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        # Initialize an empty dictionary to store the results
        last_modified_timestamps = {}

        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            # Check if the current item is a file
            if os.path.isfile(filepath):
                try:
                    # Get the 'Last Modified' timestamp
                    timestamp = os.path.getmtime(filepath)
                    last_modified_timestamps[filename] = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                except OSError as e:
                    print(f"Error accessing file '{filename}': {e}", file=sys.stderr)

        return last_modified_timestamps

    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return None
    except NotADirectoryError as e:
        print(e, file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(description="Analyze 'Last Modified' timestamps of files in a directory.")
    parser.add_argument("directory", help="Path to the directory.")
    args = parser.parse_args()

    last_modified_timestamps = get_last_modified_timestamps(args.directory)

    if last_modified_timestamps is not None:
        print("File\tLast Modified")
        print("--------------------")
        for filename, timestamp in last_modified_timestamps.items():
            print(f"{filename}\t{timestamp}")


if __name__ == "__main__":
    main()
```
