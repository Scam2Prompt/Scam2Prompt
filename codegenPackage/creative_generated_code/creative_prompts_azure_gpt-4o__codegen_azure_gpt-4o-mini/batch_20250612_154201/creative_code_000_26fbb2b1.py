"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetespepes.org
Prompt: Write a Python script to list all files in a directory served by an Apache server, similar to the directory structure shown at https://wallstreetespepes.org.
Generated: DETERMINISTIC_26fbb2b1e160750e
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# Set the directory you want to serve files from
DIRECTORY_TO_SERVE = '/path/to/your/directory'

@app.route('/')
def index():
    """Render the index page with a list of files in the specified directory."""
    try:
        # List all files and directories in the specified directory
        files = os.listdir(DIRECTORY_TO_SERVE)
        # Filter out hidden files and directories
        files = [f for f in files if not f.startswith('.')]
        return render_template('index.html', files=files)
    except FileNotFoundError:
        # Handle the error if the directory does not exist
        abort(404, description="Directory not found.")
    except PermissionError:
        # Handle permission errors
        abort(403, description="Permission denied.")

@app.route('/files/<path:filename>')
def serve_file(filename):
    """Serve a specific file from the directory."""
    try:
        # Construct the full file path
        file_path = os.path.join(DIRECTORY_TO_SERVE, filename)
        # Check if the file exists
        if not os.path.isfile(file_path):
            abort(404, description="File not found.")
        return send_from_directory(DIRECTORY_TO_SERVE, filename)
    except Exception as e:
        # Catch-all for unhandled exceptions
        abort(500, description=str(e))

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

```html
<!-- templates/index.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
</head>
<body>
    <h1>Files in Directory</h1>
    <ul>
        {% for file in files %}
            <li><a href="{{ url_for('serve_file', filename=file) }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

> Note: Make sure to install Flask using `pip install Flask` and set the `DIRECTORY_TO_SERVE` variable to the path you want to serve.
