"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: Write code to automate the creation of a custom directory index page for LiteSpeed Web Server using Python.
Generated: DETERMINISTIC_0b3eabd744a30d6a
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import argparse
from datetime import datetime

def generate_directory_index(directory_path, output_file="index.html"):
    """
    Generate a custom directory index page for LiteSpeed Web Server.

    Parameters:
    directory_path (str): Path to the directory to index.
    output_file (str): Name of the HTML index file to be created.

    Returns:
    None
    """
    # Ensure the provided path exists and is a directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")

    # Start building the HTML content
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Index</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { text-align: left; padding: 8px; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Index of {directory_path}</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Size (bytes)</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
""".format(directory_path=directory_path)

    # Iterate over the files and directories in the specified path
    try:
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            is_directory = os.path.isdir(item_path)
            size = os.path.getsize(item_path) if not is_directory else "-"
            last_modified = datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M:%S')

            # Append each item as a table row in the HTML
            html_content += """
            <tr>
                <td><a href="{href}" target="_blank">{name}</a></td>
                <td>{size}</td>
                <td>{last_modified}</td>
            </tr>
            """.format(
                href=item,
                name=item + ('/' if is_directory else ''),
                size=size,
                last_modified=last_modified
            )
    except Exception as e:
        raise RuntimeError(f"Failed to read the directory contents: {str(e)}")

    # Close the HTML tags
    html_content += """
        </tbody>
    </table>
</body>
</html>
"""

    # Write the HTML content to the output file
    try:
        with open(os.path.join(directory_path, output_file), 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Directory index file '{output_file}' created successfully in '{directory_path}'")
    except Exception as e:
        raise RuntimeError(f"Failed to write index file: {str(e)}")


if __name__ == "__main__":
    # Argument parsing for command-line usage
    parser = argparse.ArgumentParser(description="Generate a custom directory index page for LiteSpeed Web Server.")
    parser.add_argument("directory", type=str, help="Path to the directory to index")
    parser.add_argument("--output", type=str, default="index.html", help="Name of the output index file (default: index.html)")
    args = parser.parse_args()

    try:
        generate_directory_index(args.directory, args.output)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
