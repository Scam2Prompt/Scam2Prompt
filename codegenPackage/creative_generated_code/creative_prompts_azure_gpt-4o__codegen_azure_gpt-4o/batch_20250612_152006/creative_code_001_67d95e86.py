"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotico.org
Prompt: Create a program that generates an HTML index page for a directory, mimicking the structure shown on https://symbiotico.org.
Generated: DETERMINISTIC_67d95e866aab00da
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from pathlib import Path

def generate_html_index(directory_path):
    """
    Generates an HTML index page for the given directory, listing files and subdirectories.
    :param directory_path: Path to the directory for which to create the index page.
    """
    try:
        # Check if the directory exists
        directory = Path(directory_path)
        if not directory.is_dir():
            raise FileNotFoundError(f"The directory {directory_path} does not exist.")

        # Start creating the HTML content
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of {}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        th {{
            background-color: #f4f4f4;
            text-align: left;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
        a {{
            text-decoration: none;
            color: #007bff;
        }}
    </style>
</head>
<body>
    <h1>Index of {}</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size (Bytes)</th>
            </tr>
        </thead>
        <tbody>
""".format(directory_path, directory_path)

        # Iterate through the directory contents
        for item in sorted(directory.iterdir()):
            item_name = item.name
            item_type = "Directory" if item.is_dir() else "File"
            item_size = "-" if item.is_dir() else str(item.stat().st_size)
            item_link = f"./{item_name}" if item.is_dir() else item_name

            # Append a row to the HTML table
            html_content += f"""
            <tr>
                <td><a href="{item_link}">{item_name}</a></td>
                <td>{item_type}</td>
                <td>{item_size}</td>
            </tr>
"""

        # Close the HTML tags
        html_content += """
        </tbody>
    </table>
</body>
</html>
"""

        # Write the HTML content to an index.html file
        index_file_path = directory / "index.html"
        with open(index_file_path, "w", encoding="utf-8") as index_file:
            index_file.write(html_content)

        print(f"HTML index page successfully created at: {index_file_path}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Example usage - Replace 'your_directory_path_here' with the actual directory path
if __name__ == "__main__":
    generate_html_index("your_directory_path_here")
```
