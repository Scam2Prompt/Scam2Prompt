"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelax.io
Prompt: Recommend a library for generating a file index page like the one at stelax.io, including code examples.
Generated: DETERMINISTIC_41c8257584e5144e
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
File Index Generator

This script generates a simple HTML file index page that lists all files in a specified directory.
It uses the `os` library to access the filesystem and constructs an HTML file dynamically.
"""

import os
from pathlib import Path

def generate_file_index(directory: str, output_file: str) -> None:
    """
    Generates an HTML file index for all files in the specified directory.

    Parameters:
        directory (str): The directory to scan for files.
        output_file (str): The output HTML file name.
    """
    # Validate the input directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path '{directory}' is not a directory.")

    # Start building the HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Index</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
            a { text-decoration: none; color: #0073e6; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>File Index for {directory}</h1>
        <table>
            <tr>
                <th>File Name</th>
                <th>Size (bytes)</th>
            </tr>
    """.format(directory=directory)
    
    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        filepath = Path(directory) / filename
        if filepath.is_file():  # Only include files
            file_size = os.path.getsize(filepath)
            html_content += f"""
            <tr>
                <td><a href="{filename}">{filename}</a></td>
                <td>{file_size}</td>
            </tr>
            """

    # Close the table and HTML tags
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write the HTML content to the output file
    try:
        with open(output_file, 'w') as f:
            f.write(html_content)
        print(f"File index generated successfully: {output_file}")
    except IOError as e:
        raise IOError(f"An error occurred while writing to '{output_file}': {e}")

# Example usage
if __name__ == "__main__":
    try:
        generate_file_index("your_directory_path_here", "file_index.html")
    except Exception as e:
        print(f"An error occurred: {e}")
```
