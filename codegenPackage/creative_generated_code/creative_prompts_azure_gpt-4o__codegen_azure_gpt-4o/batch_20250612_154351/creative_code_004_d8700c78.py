"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groupists.com
Prompt: Write a function to generate an HTML index page that mimics the directory listing style seen on https://groupists.com.
Generated: DETERMINISTIC_d8700c7839ba49c3
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def generate_html_index(directory_path):
    """
    Generates an HTML index page listing files and directories in a given folder.

    Args:
        directory_path (str): The path of the directory to list.

    Returns:
        str: A string containing the HTML content for the index page.
    """
    try:
        # Verify the directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        # Start building the HTML content
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of {directory}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ padding: 10px; text-align: left; }}
        th {{ background-color: #f4f4f4; border-bottom: 2px solid #ddd; }}
        tr:hover {{ background-color: #f9f9f9; }}
        a {{ text-decoration: none; color: #007BFF; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Index of {directory}</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size</th>
            </tr>
        </thead>
        <tbody>
""".format(directory=os.path.basename(directory_path))

        # Get the list of files and directories
        entries = os.listdir(directory_path)
        entries.sort()  # Optional: Sort entries alphabetically

        for entry in entries:
            entry_path = os.path.join(directory_path, entry)
            is_directory = os.path.isdir(entry_path)
            
            # Format last modified timestamp and size
            last_modified = datetime.fromtimestamp(os.path.getmtime(entry_path)).strftime('%Y-%m-%d %H:%M:%S')
            size = '-' if is_directory else f"{os.path.getsize(entry_path):,} bytes"

            # Append a row to the HTML table
            html_content += f"""
            <tr>
                <td><a href="{entry}">{entry}/</a></td>
                <td>{last_modified}</td>
                <td>{size}</td>
            </tr>
""" if is_directory else f"""
            <tr>
                <td><a href="{entry}">{entry}</a></td>
                <td>{last_modified}</td>
                <td>{size}</td>
            </tr>
"""

        # Close HTML tags
        html_content += """
        </tbody>
    </table>
</body>
</html>
"""
        return html_content

    except Exception as e:
        # Handle exceptions gracefully
        return f"<html><body><h1>Error: {str(e)}</h1></body></html>"

# Example usage:
# Save the output to an 'index.html' file in the specified directory
directory_to_list = "/path/to/your/directory"  # Replace with your directory path
index_content = generate_html_index(directory_to_list)
output_path = os.path.join(directory_to_list, "index.html")

with open(output_path, "w") as file:
    file.write(index_content)
```
