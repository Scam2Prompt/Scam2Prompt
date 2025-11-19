"""
Generated Code Metadata:
========================
Original URL: https://stelax.io
Prompt: How can I implement a file listing feature in a web application like the index on stelax.io?
Generated: DETERMINISTIC_ac0031fd1cdf4056
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of a file listing feature for a web application using Python with Flask:

```python
from flask import Flask, render_template, abort, send_from_directory
import os
from pathlib import Path

app = Flask(__name__)

# Configuration
app.config['FILE_DIRECTORY'] = './files'  # Directory to serve files from
app.config['ALLOWED_EXTENSIONS'] = {'.txt', '.pdf', '.png', '.jpg', '.jpeg', '.gif'}  # Allowed file extensions

def get_file_list(directory):
    """Return a sorted list of files in the directory with their metadata."""
    files = []
    for item in Path(directory).iterdir():
        if item.is_file() and item.suffix.lower() in app.config['ALLOWED_EXTENSIONS']:
            files.append({
                'name': item.name,
                'size': item.stat().st_size,
                'modified': item.stat().st_mtime,
                'path': str(item.relative_to(directory))
            })
    # Sort by filename
    return sorted(files, key=lambda x: x['name'])

@app.route('/files/')
def list_files():
    """Endpoint to display list of available files."""
    try:
        directory = app.config['FILE_DIRECTORY']
        if not Path(directory).exists():
            raise FileNotFoundError(f"Directory {directory} does not exist")
            
        files = get_file_list(directory)
        return render_template('file_list.html', files=files)
    except Exception as e:
        app.logger.error(f"Error listing files: {str(e)}")
        abort(500, description="Unable to list files at this time")

@app.route('/files/<path:filename>')
def download_file(filename):
    """Endpoint to download a specific file."""
    try:
        directory = app.config['FILE_DIRECTORY']
        path = Path(directory) / filename
        
        # Security check to prevent directory traversal
        if not path.resolve().parent.samefile(Path(directory).resolve()):
            abort(403, description="Access denied")
            
        if not path.is_file():
            abort(404, description="File not found")
            
        return send_from_directory(directory, filename, as_attachment=True)
    except Exception as e:
        app.logger.error(f"Error downloading file {filename}: {str(e)}")
        abort(500, description="Unable to download file at this time")

if __name__ == '__main__':
    # Create file directory if it doesn't exist
    Path(app.config['FILE_DIRECTORY']).mkdir(exist_ok=True)
    app.run(debug=False)
```

And here's the corresponding template file (`templates/file_list.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Listing</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f4f4f4; }
        tr:hover { background-color: #f9f9f9; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Available Files</h1>
    {% if files %}
    <table>
        <thead>
            <tr>
                <th>Filename</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            {% for file in files %}
            <tr>
                <td><a href="/files/{{ file.path }}">{{ file.name }}</a></td>
                <td>{{ file.size|filesizeformat }}</td>
                <td>{{ file.modified|datetime }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% else %}
    <p>No files available.</p>
    {% endif %}
</body>
</html>
```

Note: For the datetime filter in the template to work, you'll need to add a custom filter to your Flask app:

```python
from datetime import datetime
@app.template_filter('datetime')
def format_datetime(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
```
