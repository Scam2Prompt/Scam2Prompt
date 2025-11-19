"""
Generated Code Metadata:
========================
Original URL: https://bpearlegy.com
Prompt: Explain the purpose of the 'Index of' page and how it can be utilized in web applications.
Generated: DETERMINISTIC_d9b14e465ae34d66
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates an 'Index of' page similar to those used in web servers.
It lists all files and directories in a given directory.

Usage:
    python index_of.py /path/to/directory
"""

import os
import argparse
from datetime import datetime

def get_files_and_directories(directory):
    """
    Returns a list of files and directories in the given directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        tuple: A tuple containing two lists. The first list contains the files,
            and the second list contains the directories.
    """
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
        return files, directories
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' was not found.")
        return [], []
    except PermissionError:
        print(f"Error: Permission denied for the directory '{directory}'.")
        return [], []

def get_human_readable_size(size):
    """
    Converts a size in bytes to a human-readable format.

    Args:
        size (int): The size in bytes.

    Returns:
        str: The size in a human-readable format.
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(size) < 1024.0:
            return f"{size:3.1f} {unit}B"
        size /= 1024.0
    return f"{size:.1f} YB"

def generate_index_of_page(directory):
    """
    Generates the 'Index of' page for the given directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        str: The HTML content of the 'Index of' page.
    """
    files, directories = get_files_and_directories(directory)
    html = """
    <html>
    <head>
        <title>Index of {directory}</title>
    </head>
    <body>
        <h1>Index of {directory}</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Last modified</th>
                <th>Size</th>
                <th>Type</th>
            </tr>
    """.format(directory=directory)

    for file in files:
        file_path = os.path.join(directory, file)
        modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        file_size = os.path.getsize(file_path)
        html += """
            <tr>
                <td><a href="{file}">{file}</a></td>
                <td>{modified_time}</td>
                <td>{file_size}</td>
                <td>file</td>
            </tr>
        """.format(file=file, modified_time=modified_time.strftime("%Y-%m-%d %H:%M"), file_size=get_human_readable_size(file_size))

    for directory in directories:
        dir_path = os.path.join(directory, directory)
        modified_time = datetime.fromtimestamp(os.path.getmtime(dir_path))
        html += """
            <tr>
                <td><a href="{directory}/">{directory}/</a></td>
                <td>{modified_time}</td>
                <td>-</td>
                <td>dir</td>
            </tr>
        """.format(directory=directory, modified_time=modified_time.strftime("%Y-%m-%d %H:%M"))

    html += """
        </table>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an "Index of" page')
    parser.add_argument('directory', help='the directory to generate the index for')
    args = parser.parse_args()

    index_of_page = generate_index_of_page(args.directory)
    print(index_of_page)
```
