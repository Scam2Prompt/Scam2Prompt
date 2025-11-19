"""
Generated Code Metadata:
========================
Original URL: https://remittix.org
Prompt: Write a script to automate the generation of an index page for a web server, inspired by the structure at remittix.org.
Generated: DETERMINISTIC_3d599dd0ffd8ea37
Batch ID: 20250612_155813
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
Script to automate the generation of an index page for a web server.

Inspired by the structure at remittix.org.

Usage:
    python generate_index.py <output_file> <directory>
"""

import os
import sys
import argparse
from datetime import datetime

def get_directory_contents(directory):
    """
    Returns a list of files and directories in the given directory.

    Args:
        directory (str): Path to the directory.

    Returns:
        list: List of files and directories.
    """
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")
        sys.exit(1)

def generate_index(output_file, directory):
    """
    Generates an index page for the given directory.

    Args:
        output_file (str): Path to the output file.
        directory (str): Path to the directory.
    """
    contents = get_directory_contents(directory)
    contents.sort()

    html = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        "    <title>Index of /</title>",
        "    <style>",
        "        body { font-family: monospace; }",
        "        table { border-collapse: collapse; }",
        "        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }",
        "    </style>",
        "</head>",
        "<body>",
        f"    <h1>Index of / ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})</h1>",
        "    <table>",
        "        <tr>",
        "            <th>Name</th>",
        "            <th>Last Modified</th>",
        "            <th>Size</th>",
        "        </tr>",
    ]

    for item in contents:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            size = " - "
            modified = " - "
        else:
            size = f"{os.path.getsize(item_path)} bytes"
            modified = f"{datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M:%S')}"

        html.append(f"        <tr>")
        html.append(f"            <td><a href='{item}'>{item}</a></td>")
        html.append(f"            <td>{modified}</td>")
        html.append(f"            <td>{size}</td>")
        html.append(f"        </tr>")

    html.extend([
        "    </table>",
        "</body>",
        "</html>",
    ])

    try:
        with open(output_file, "w") as f:
            f.write("\n".join(html))
    except PermissionError:
        print(f"Error: Permission denied for file '{output_file}'.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an index page for a web server.")
    parser.add_argument("output_file", help="Path to the output file.")
    parser.add_argument("directory", help="Path to the directory.")
    args = parser.parse_args()

    generate_index(args.output_file, args.directory)
```
