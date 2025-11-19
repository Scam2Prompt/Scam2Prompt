"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idsmac-apple.com
Prompt: Create a script that mimics the functionality of a web server's index page by listing files and their attributes.
Generated: DETERMINISTIC_890d55b8cd8bb1b3
Batch ID: 20250612_155428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# HTML template for rendering the file list
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Index</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>File Index</h1>
    <table>
        <tr>
            <th>Filename</th>
            <th>Size (Bytes)</th>
            <th>Last Modified</th>
        </tr>
        {% for file in files %}
        <tr>
            <td>{{ file.name }}</td>
            <td>{{ file.size }}</td>
            <td>{{ file.modified }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

def get_file_attributes(directory):
    """
    Retrieve a list of files in the specified directory with their attributes.

    Args:
        directory (str): The path of the directory to list files from.

    Returns:
        list: A list of dictionaries containing file attributes.
    """
    file_attributes = []
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_info = {
                    'name': filename,
                    'size': os.path.getsize(file_path),
                    'modified': os.path.getmtime(file_path)
                }
                file_attributes.append(file_info)
    except Exception as e:
        app.logger.error(f"Error accessing directory {directory}: {e}")
        raise
    return file_attributes

@app.route('/')
def index():
    """
    Render the index page listing files in the current directory.

    Returns:
        str: Rendered HTML page with file list.
    """
    try:
        files = get_file_attributes(os.getcwd())
        return render_template_string(HTML_TEMPLATE, files=files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask web server
    app.run(host='0.0.0.0', port=5000, debug=False)
```
