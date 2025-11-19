"""
Generated Code Metadata:
========================
Original URL: https://benenergie-dz.com
Prompt: Generate a code snippet to create an index page similar to the one found at benenergie-dz.com, including file size and last modified date.
Generated: DETERMINISTIC_56e59a97304bd225
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python code snippet that generates an index page similar to the one found at benenergie-dz.com, including file size and last modified date. This script uses the `os`, `datetime`, and `mimetypes` modules to gather file information and guesses the MIME type for each file.

```python
import os
import datetime
import mimetypes

def get_file_info(directory):
    """Returns a list of dictionaries containing file information."""
    file_info_list = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Get file size
            file_size = os.path.getsize(filepath)
            file_size_str = f"{file_size / (1024 * 1024):.2f} MB" if file_size > 1024 * 1024 else f"{file_size / 1024:.2f} KB" if file_size > 1024 else f"{file_size} B"

            # Get last modified date
            modified_timestamp = os.path.getmtime(filepath)
            modified_date = datetime.datetime.fromtimestamp(modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')

            # Guess MIME type
            mime_type, _ = mimetypes.guess_type(filepath)

            file_info_list.append({
                'filename': filename,
                'filepath': filepath,
                'file_size': file_size_str,
                'modified_date': modified_date,
                'mime_type': mime_type if mime_type else "Unknown"
            })
    return file_info_list

def generate_index_page(directory):
    """Generates an index page for the given directory."""
    file_info_list = get_file_info(directory)

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Directory Index</title>
        <style>
            body { font-family: monospace; }
            table { border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 5px; text-align: left; }
        </style>
    </head>
    <body>
        <h1>Directory Index</h1>
        <table>
            <tr>
                <th>Filename</th>
                <th>File Size</th>
                <th>Last Modified</th>
                <th>MIME Type</th>
            </tr>
    """

    for file_info in file_info_list:
        html_content += f"""
            <tr>
                <td><a href="{file_info['filename']}">{file_info['filename']}</a></td>
                <td>{file_info['file_size']}</td>
                <td>{file_info['modified_date']}</td>
                <td>{file_info['mime_type']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Generating index for directory: {current_dir}")
    generate_index_page(current_dir)
    print("Index generation complete. Please find 'index.html' in the current directory.")
```
