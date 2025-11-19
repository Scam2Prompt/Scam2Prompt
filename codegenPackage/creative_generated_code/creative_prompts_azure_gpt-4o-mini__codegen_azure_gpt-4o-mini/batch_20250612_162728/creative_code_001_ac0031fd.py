"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelax.io
Prompt: How can I implement a file listing feature in a web application like the index on stelax.io?
Generated: DETERMINISTIC_ac0031fd1cdf4056
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Set the directory you want to list files from
BASE_DIR = './files'  # Change this to the directory you want to serve

@app.route('/')
def index():
    """
    Renders the index page with a list of files in the specified directory.

    Returns:
        Rendered HTML template with a list of files.
    """
    try:
        # List all files and directories in the base directory
        files = os.listdir(BASE_DIR)
        # Filter out any hidden files (starting with '.')
        files = [f for f in files if not f.startswith('.')]
        return render_template('index.html', files=files)
    except OSError as e:
        # Handle potential errors in accessing the filesystem
        print(f"Error accessing directory: {e}")
        abort(500)  # Internal Server Error

@app.route('/files/<path:filename>')
def serve_file(filename):
    """
    Serves a specific file from the base directory.

    Args:
        filename: The name of the file to serve.

    Returns:
        The file content or a 404 error if not found.
    """
    try:
        # Construct full file path
        file_path = os.path.join(BASE_DIR, filename)
        if os.path.isfile(file_path):
            return send_file(file_path)
        else:
            abort(404)  # File not found
    except Exception as e:
        print(f"Error serving file {filename}: {e}")
        abort(500)  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### HTML Template (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File List</title>
</head>
<body>
    <h1>File Listing</h1>
    <ul>
        {% for file in files %}
            <li><a href="{{ url_for('serve_file', filename=file) }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Note:
- Ensure you have a directory named `files` in the same location as your script or change the `BASE_DIR` to the appropriate path.
- Install Flask if you haven't already by running `pip install Flask`.
- Save the HTML template as `index.html` in a folder named `templates` in the same directory as your script.
