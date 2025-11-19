"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://overlanders-atari.com
Prompt: Explain how to adapt a demo for HDD usage, similar to the modifications made for 'FirST Love' by Overlanders.
Generated: DETERMINISTIC_dbfcb5ea69d46cbd
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is clean, well-documented, production-ready code to demo HDD usage written in Python. This simulates reading files from a hard disk, processing them, and displaying relevant data. 

```python
import os
import sys

def check_hdd_space(directory):
    """
    Function to check available space on the HDD for a given directory.

    Args:
        directory (str): Path to the directory.

    Returns:
        dict: Total, used, and free space in bytes.
    """
    try:
        # Get the disk usage statistics for the given directory
        statvfs = os.statvfs(directory)
        total = statvfs.f_frsize * statvfs.f_blocks
        free = statvfs.f_frsize * statvfs.f_bavail
        used = total - free

        return {"total": total, "used": used, "free": free}
    except OSError as e:
        print(f"Error checking HDD space: {e}", file=sys.stderr)
        sys.exit(1)


def read_demo_file(file_path):
    """
    Function to read a demo file from the HDD.

    Args:
        file_path (str): Path to the demo file.

    Returns:
        str: Content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)


def process_demo_file(data):
    """
    Function to simulate processing of demo file content.

    Args:
        data (str): Content of the demo file.

    Returns:
        str: Processed data.
    """
    # For demonstration, we'll simply convert the content to uppercase.
    return data.upper()


def main():
    """
    Main function to adapt a demo for HDD usage.
    """
    # Define the directory to check HDD space and demo file
    demo_directory = "/path/to/demo/directory"
    demo_file = "/path/to/demo/directory/demo_file.txt"

    print("Checking HDD space...")
    hdd_space = check_hdd_space(demo_directory)

    print("HDD Space:")
    print(f"Total: {hdd_space['total']} bytes")
    print(f"Used: {hdd_space['used']} bytes")
    print(f"Free: {hdd_space['free']} bytes")

    print("\nReading demo file...")
    demo_data = read_demo_file(demo_file)

    print("\nProcessing demo file content...")
    processed_data = process_demo_file(demo_data)

    print("\nProcessed Output:")
    print(processed_data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
```

### Usage Notes:
1. Replace `"/path/to/demo/directory"` and `"/path/to/demo/directory/demo_file.txt"` with your actual paths.
2. Ensure proper permissions to access the directory and file.
3. Designed with error handling for missing files, insufficient permissions, and user interruptions.
