"""
Generated Code Metadata:
========================
Original URL: https://vanillagift.remadet.com
Prompt: Write code to automate the creation of a custom directory index page for LiteSpeed Web Server using Python.
Generated: DETERMINISTIC_0b3eabd744a30d6a
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
Automate the creation of a custom directory index page for LiteSpeed Web Server.

Usage:
    python create_directory_index.py <directory_path> <title> <header> <footer>
"""

import os
import sys
import argparse

def create_directory_index(directory_path, title, header, footer):
    """
    Create a custom directory index page.

    Args:
        directory_path (str): The path to the directory.
        title (str): The title of the page.
        header (str): The header content of the page.
        footer (str): The footer content of the page.

    Returns:
        None
    """

    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Check if the directory is indeed a directory
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    # Get the list of files and directories in the given directory
    try:
        dir_contents = os.listdir(directory_path)
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory_path}'.", file=sys.stderr)
        sys.exit(1)

    # Filter out the index file if it already exists
    dir_contents = [item for item in dir_contents if item not in ['index.html', 'index.htm']]

    # Create the index page content
    index_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{header}</h1>
    <ul>
"""

    # Add directory and file links to the index page content
    for item in dir_contents:
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            index_content += f"        <li><a href='{item}/'>{item}/</a></li>\n"
        else:
            index_content += f"        <li><a href='{item}'>{item}</a></li>\n"

    index_content += f"""
    </ul>
    <p>{footer}</p>
</body>
</html>
"""

    # Write the index page content to a file
    index_path = os.path.join(directory_path, 'index.html')
    try:
        with open(index_path, 'w') as f:
            f.write(index_content)
    except Exception as e:
        print(f"Error: Failed to write to '{index_path}': {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Custom directory index page created at '{index_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a custom directory index page for LiteSpeed Web Server')
    parser.add_argument('directory_path', help='the path to the directory')
    parser.add_argument('title', help='the title of the page')
    parser.add_argument('header', help='the header content of the page')
    parser.add_argument('footer', help='the footer content of the page')
    args = parser.parse_args()

    create_directory_index(args.directory_path, args.title, args.header, args.footer)
```
